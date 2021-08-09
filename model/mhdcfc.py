"""
A simple model of a molten hydroxide direct carbon fuel cell using
elementary, reversible reactions obeying mass-action kinetics for all reactions
including charge transfer.
"""

import math
import csv
from anode import *
from cathode import *
from utils import NewtonSolver

ct.add_module_directory()

# parameters
# molten hydroxide fuel cell was heated to 500 degrees Celsius
T = 1073.15  # T in K 500 + 273.15 at stp
P = ct.one_atm # Pressure 1 bar at stp

# Guiding reaction within fuel cell
########################
# Anode:
# C + 202 -> C02 + 4e-
# Cathode:
# O2 + 4e- = 202-
# Overall:
# C+ 02 -> CO2
########################

# gas compositions
anode_gas_X = 'CO2:1, E:4'
cathode_gas_X = 'O2:2'

# time to integrate coverage eqs. to steady state in
# 'advanceCoverages'. This should be more than enough time.
tss = 50.0

sigma = 2.0  # electrolyte conductivity [Siemens / m]
# ethick = 5.0e-5  # electrolyte thickness [m]
# TPB_length_per_area = 1.0e7  # TPB length per unit area [1/m]


def show_coverages(s):
    """Print the coverages for surface s."""
    print('\n{0}\n'.format(s.name))
    cov = s.coverages
    names = s.species_names
    for n in range(s.n_species):
        print('{0:16s}  {1:13.4g}'.format(names[n], cov[n]))


def equil_OCV(gas1, gas2):
    # Tweak this
    return (-ct.gas_constant * gas1.T *
        math.log(gas1['O2'].X / gas2['O2'].X) / (4.0*ct.faraday))



# initialization

# set the gas compositions, and temperatures of all phases

gas_a.TPX = T, P, anode_gas_X
gas_a.equilibrate('TP')  # needed to use equil_OCV

gas_c.TPX = T, P, cathode_gas_X
gas_c.equilibrate('TP')  # needed to use equil_OCV

phases = [anode_bulk, anode_surf, oxide_surf_a, oxide_a, cathode_bulk,
          cathode_surf, oxide_surf_c, oxide_c, tpb_a, tpb_c]

for p in phases:
    p.TP = T, P

# now bring the surface coverages into steady state with these gas
# compositions. Note that the coverages are held fixed at these values - we do
# NOT consider the change in coverages due to TPB reactions. For that, a more
# complex model is required. But as long as the thermal chemistry is fast
# relative to charge transfer, this should be an OK approximation.
for s in [anode_surf, oxide_surf_a, cathode_surf, oxide_surf_c]:
    s.advance_coverages(tss)
    show_coverages(s)


# find open circuit potentials by solving for the E values that give
# zero current.
Ea0 = NewtonSolver(anode_curr, xstart=-0.51)
Ec0 = NewtonSolver(cathode_curr, xstart=0.51)

print('\nocv from zero current is: ', Ec0 - Ea0)
print('OCV from thermo equil is: ', equil_OCV(gas_a, gas_c))

print('Ea0 = ', Ea0)
print('Ec0 = ', Ec0)
print()

# do polarization curve for anode overpotentials from -250 mV
# (cathodic) to +250 mV (anodic)
Ea_min = Ea0 - 0.25
Ea_max = Ea0 + 0.25

csvfile = open('mhdcfc.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(['i (mA/cm2)', 'eta_a', 'eta_c', 'eta_ohmic', 'Eload'])

# vary the anode overpotential, from cathodic to anodic polarization
for n in range(100):
    Ea = Ea_min + 0.005*n

    # set the electrode potential. Note that the anode-side electrolyte is
    # held fixed at 0 V.
    anode_bulk.electric_potential = Ea

    # compute the anode current
    curr = anode_curr(Ea)

    # set potential of the oxide on the cathode side to reflect the ohmic drop
    # through the electrolyte
    delta_V = curr * ethick / sigma

    # if the current is positive, negatively-charged ions are flowing from the
    # cathode to the anode. Therefore, the cathode side must be more negative
    # than the anode side.
    phi_oxide_c = -delta_V

    # note that both the bulk and the surface potentials must be set
    oxide_c.electric_potential = phi_oxide_c
    oxide_surf_c.electric_potential = phi_oxide_c

    # Find the value of the cathode potential relative to the cathode-side
    # electrolyte that yields the same current density as the anode current
    # density
    Ec = NewtonSolver(cathode_curr, xstart=Ec0+0.1, C=curr)

    cathode_bulk.electric_potential = phi_oxide_c + Ec

    # write the current density, anode and cathode overpotentials, ohmic
    # overpotential, and load potential
    writer.writerow([0.1*curr, Ea - Ea0, Ec - Ec0, delta_V,
                     cathode_bulk.electric_potential -
                     anode_bulk.electric_potential])

print('polarization curve data written to file mhdcfc.csv')

csvfile.close()
