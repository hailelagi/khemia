import cantera as ct

#####################################################################
# Anode-side phases
#####################################################################

TPB_length_per_area = 1.0e7  # TPB length per unit area [1/m]

# import the anode-side bulk phases
gas_a, anode_bulk, oxide_a = ct.import_phases('sofc.cti',
                                              ['gas', 'metal', 'oxide_bulk',])

# import the surfaces on the anode side
anode_surf = ct.Interface('sofc.cti', 'metal_surface', [gas_a])
oxide_surf_a = ct.Interface('sofc.cti', 'oxide_surface', [gas_a, oxide_a])

# import the anode-side triple phase boundary
tpb_a = ct.Interface('sofc.cti', 'tpb', [anode_bulk, anode_surf, oxide_surf_a])

anode_surf.name = 'anode surface'
oxide_surf_a.name = 'anode-side oxide surface'


# this function is defined to use with NewtonSolver to invert the current-
# voltage function. NewtonSolver requires a function of one variable, so the
# other objects are accessed through the global namespace.
def anode_curr(E):
    """
    Current from the anode as a function of anode potential relative to
    electrolyte.
    """

    # the anode-side electrolyte potential is kept at zero. Therefore, the
    # anode potential is just equal to E.
    anode_bulk.electric_potential = E

    # get the species net production rates due to the anode-side TPB reaction
    # mechanism. The production rate array has the values for the neighbor
    # species in the order listed in the .cti file, followed by the tpb phase.
    # Since the first neighbor phase is the bulk metal, species 0 is the
    # electron.
    w = tpb_a.net_production_rates

    # the sign convention is that the current is positive when
    # electrons are being delivered to the anode - i.e. it is positive
    # for fuel cell operation.
    return ct.faraday * w[0] * TPB_length_per_area
