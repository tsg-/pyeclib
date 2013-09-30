from distutils.core import setup, Extension
import sys
import os

module = Extension('pyeclib',
                   define_macros = [('MAJOR VERSION', '1'),
                                    ('MINOR VERSION', '0')],
                   include_dirs = ['/usr/include/python2.7',
                                   'src/c/pyeclib',
                                   'src/c/include',
                                   'src/c/xor_codes',
                                   '/usr/local/include/jerasure'],
                   library_dirs = ['/usr/lib', '/usr/local/lib'],
                   libraries = ['python2.7', 'Jerasure'],
                   # The extra arguments are for debugging
                   #extra_compile_args = ['-g', '-O0', '-msse3'],
                   extra_compile_args = ['-msse3'],
                   extra_link_args=['-static'],
                   sources = ['src/c/pyeclib/pyeclib.c', 'src/c/xor_codes/xor_code.c', 'src/c/xor_codes/xor_hd_code.c'])

setup (name = 'PyECLib',
       version = '0.1',
       ext_modules = [module],
       packages=['ec_iface'],
        package_dir={'ec_iface': 'src/python/ec_iface'},
        py_modules = ['ec_iface.ec', 'ec_iface.ec_null', 'ec_iface.ec_stripe', 'ec_iface.ec_pyeclib'])

