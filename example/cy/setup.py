from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='cy',
    ext_modules=cythonize("cy.pyx")
)
