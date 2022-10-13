# encoding: utf-8

"""
Fichier de configuration WAF pour version séquentielle sur Ubuntu 13.6 :
- Compilateur : GNU
- BLAS        : OpenBLAS
"""
import os

def configure(self):
    opts = self.options

    # mfront path
#    self.env.TFELHOME = '/opt/tfel-3.2.0'

    self.env.append_value('LIBPATH', ['/opt/aster/public/hdf5-1.10.3/lib',
                                      '/opt/aster/public/med-4.0.0/lib',
                                      '/opt/aster/public/metis-5.1.0/lib',
                                      '/opt/aster/public/scotch-6.0.4/lib',
                                      '/usr/lib/x86_64-linux-gnu'])

    self.env.append_value('INCLUDES', [
        '/opt/aster/public/hdf5-1.10.3/include',
        '/opt/aster/public/med-4.0.0/include',
        '/opt/aster/public/metis-5.1.0/include',
        '/opt/aster/public/scotch-6.0.4/include',
        '/usr/include'])
#        '/opt/tfel-3.2.0/include',

    opts.maths_libs = 'openblas superlu'
#    opts.embed_math = True

    opts.enable_hdf5 = True
    opts.hdf5_libs  = 'hdf5 z'
#    opts.embed_hdf5 = True

    opts.enable_med = True
    opts.med_libs  = 'med stdc++'
#    opts.embed_med  = True

    opts.enable_mfront = False

    opts.enable_scotch = True
#    opts.embed_scotch  = True

    opts.enable_homard = True
#    opts.embed_aster    = True
#    opts.embed_fermetur = True

    # add paths for external programs
#    os.environ['METISDIR'] = '/opt/aster/public/metis-5.1.0'
#    os.environ['GMSH_BIN_DIR'] = '/opt/aster/public/gmsh-3.0.6-Linux/bin'
    os.environ['HOMARD_ASTER_ROOT_DIR'] = '/opt/aster/public/homard-11.12'

    opts.with_prog_metis = True
#    opts.with_prog_gmsh = True
    # salome: only required by few testcases
    # europlexus: not available on all platforms
#    opts.with_prog_miss3d = True
    opts.with_prog_homard = True
#    opts.with_prog_ecrevisse = True
    opts.with_prog_xmgrace = True
