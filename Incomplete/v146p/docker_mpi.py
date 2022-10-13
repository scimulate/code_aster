# encoding: utf-8

"""
Fichier de configuration WAF pour version parallèle sur Ubuntu 13.6 :
- Compilateur : GNU
- MPI         : système (OpenMPI, Ubuntu 13.6)
- BLAS        : OpenBLAS
- Scalapack   : système (Ubuntu 13.6)
- PETSc       : 
"""

import docker_std

def configure(self):
    opts = self.options
    docker_std.configure(self)

    self.env.prepend_value('LIBPATH', [
        '/usr/lib/petsc/lib',
        '/opt/parmetis-4.0.3/lib',
        '/opt/mumps-5.1.2_mob/lib',])

    self.env.prepend_value('INCLUDES', [
        '/opt/petsc-3.9.4/linux-metis-mumps/include',
        '/opt/petsc-3.9.4/include',
        '/usr/include/superlu',
        '/opt/parmetis-4.0.3/include',
        '/opt/mumps-5.1.2_mob/include',])

    self.env.append_value('LIB', ('X11',))

    opts.parallel = True

    opts.enable_mumps  = True
    opts.mumps_version = '5.1.2'
    opts.mumps_libs = 'dmumps zmumps smumps cmumps mumps_common pord metis scalapack openblas esmumps scotch scotcherr'
#    opts.embed_mumps = True

    opts.enable_petsc = True
    opts.petsc_libs='petsc HYPRE ml'
#    opts.petsc_libs='petsc'
#    opts.embed_petsc = True

#    opts.enable_parmetis  = True
    self.env.append_value('LIB_METIS', ('parmetis'))
    self.env.append_value('LIB_SCOTCH', ('ptscotch','ptscotcherr','ptscotcherrexit','ptesmumps'))
