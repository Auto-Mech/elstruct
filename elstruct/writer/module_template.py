""" empty functions defining the function signatures for each program module
"""


def energy(geom, charge, mult, method, basis,
           # molecule options
           mol_options=(),
           # machine options
           memory=1, comment='', machine_options=(),
           # theory options
           orb_restricted=None, scf_options=(), corr_options=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        corr_options, scf_options,
    )


def gradient(geom, charge, mult, method, basis,
             # molecule options
             mol_options=(),
             # machine options
             memory=1, comment='', machine_options=(),
             # theory options
             orb_restricted=None, scf_options=(), corr_options=(),
             # job options
             job_options=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        corr_options, scf_options,
        job_options,
    )


def hessian(geom, charge, mult, method, basis,
            # molecule options
            mol_options=(),
            # machine options
            memory=1, comment='', machine_options=(),
            # theory options
            orb_restricted=None, scf_options=(), corr_options=(),
            # job options
            job_options=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        corr_options, scf_options,
        job_options,
    )


def optimization(geom, charge, mult, method, basis,
                 # molecule options
                 mol_options=(),
                 # machine options
                 memory=1, comment='', machine_options=(),
                 # theory options
                 orb_restricted=None, scf_options=(), corr_options=(),
                 # job options
                 job_options=(), frozen_coordinates=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        corr_options, scf_options,
        job_options, frozen_coordinates,
    )
