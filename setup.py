from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("Tree", ["Tree.pyx"]),
    Extension("ForestGrid", ["ForestGrid.pyx"])
]

setup(
    name='GameOfLife',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)

# setup(
#   name = 'MyProject',
#   ext_modules = cythonize(["*.pyx"]),
# )
