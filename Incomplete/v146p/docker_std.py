# coding=utf-8
# --------------------------------------------------------------------
# Copyright (C) 1991 - 2019 - EDF R&D - www.code-aster.org
# This file is part of code_aster.
#
# code_aster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# code_aster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with code_aster.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
Configuration for Scibian 9

. $HOME/dev/codeaster/devtools/etc/env_unstable.sh

waf configure --use-config=scibian9_std --prefix=../install/std
waf install -p
"""

import os
ASTER_ROOT = '/opt/aster'
YAMMROOT = ''

import official_programs


def configure(self):
    opts = self.options

    #official_programs.configure(self)
    #official_programs.check_prerequisites_package(self, YAMMROOT, '20190513')

    self.env.append_value('CXXFLAGS', ['-D_GLIBCXX_USE_CXX11_ABI=0'])
    self.env['ADDMEM'] = 350

    TFELHOME = '/opt/aster/public/tfel-3.2.1'
    TFELVERS = '3.2.1'
    self.env.TFELHOME = TFELHOME
    self.env.TFELVERS = TFELVERS

    self.env.append_value('LIBPATH', [
        '/opt/aster/public/hdf5-1.10.3/lib',
        '/opt/aster/public/med-4.0.0/lib',
        '/opt/aster/public/metis-5.1.0/lib',
        '/opt/aster/public/mumps-5.1.2/lib',
        '/opt/aster/public/scotch-6.0.4/lib',
        #'/opt/aster/public/tfel-3.2.1/lib',
    ])

    self.env.append_value('INCLUDES', [
        '/opt/aster/public/hdf5-1.10.3/include',
        '/opt/aster/public/med-4.0.0/include',
        '/opt/aster/public/metis-5.1.0/include',
        '/opt/aster/public/mumps-5.1.2/include',
        '/opt/aster/public/scotch-6.0.4/include',
        #'/opt/aster/public/tfel-3.2.1/include',
    ])

    self.env.append_value('LIB', ('pthread', 'util'))
    self.env.append_value('LIB_SCOTCH', ('scotcherrexit'))
    # to fail if not found
    
    opts.maths_libs = 'openblas superlu'
    
    opts.enable_hdf5 = True
    opts.enable_homard = True
    opts.enable_med = True
    opts.enable_metis = False
    opts.enable_mfront = False    
    opts.enable_mumps = False
    opts.enable_scotch = True

    os.environ['HOMARD_ASTER_ROOT_DIR'] = '/opt/aster/public/homard-11.12'

    opts.with_prog_gmsh = False
    opts.with_prog_metis = True
    opts.with_prog_miss3d = False
    opts.with_prog_homard = True
    opts.with_prog_ecrevisse = False
    opts.with_prog_xmgrace = True
