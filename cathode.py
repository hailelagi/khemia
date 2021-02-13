import cantera as ct

#####################################################################
# Cathode-side phases
#####################################################################

# Here for simplicity we are using the same phase and interface models for the
# cathode as we used for the anode. In a more realistic simulation, separate
# models would be used for the cathode, with a different reaction mechanism.

TPB_length_per_area = 1.0e7  # TPB length per unit area [1/m]

# import the cathode-side bulk phases
gas_c, cathode_bulk, oxide_c = ct.import_phases('sofc.cti',
                                                ['gas', 'metal', 'oxide_bulk'])

# import the surfaces on the cathode side
cathode_surf = ct.Interface('sofc.cti', 'metal_surface', [gas_c])
oxide_surf_c = ct.Interface('sofc.cti', 'oxide_surface', [gas_c, oxide_c])

# import the cathode-side triple phase boundary
tpb_c = ct.Interface('sofc.cti', 'tpb', [cathode_bulk, cathode_surf,
                                         oxide_surf_c])

cathode_surf.name = 'cathode surface'
oxide_surf_c.name = 'cathode-side oxide surface'


def cathode_curr(E):
    """Current to the cathode as a function of cathode
    potential relative to electrolyte"""

    # due to ohmic losses, the cathode-side electrolyte potential is non-zero.
    # Therefore, we need to add this potential to E to get the cathode
    # potential.
    cathode_bulk.electric_potential = E + oxide_c.electric_potential

    # get the species net production rates due to the cathode-side TPB
    # reaction mechanism. The production rate array has the values for the
    # neighbor species in the order listed in the .cti file, followed by the
    # tpb phase. Since the first neighbor phase is the bulk metal, species 0
    # is the electron.
    w = tpb_c.net_production_rates

    # the sign convention is that the current is positive when electrons are
    # being drawn from the cathode (i.e, negative production rate).
    return -ct.faraday * w[0] * TPB_length_per_area
