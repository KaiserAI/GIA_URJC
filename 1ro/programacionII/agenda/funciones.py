import ctypes
import pathlib

# path of the shared library
libfile = pathlib.Path(__file__).parent / "libctest.dll"
ctestlib = ctypes.cdll.LoadLibrary(str(libfile))

# python function wrappers around the c functions
# specify variable types for hello function
ctestlib.muestraDatos.argtypes = []
ctestlib.muestraDatos.restype = None

# specify variable types for sum function
ctestlib.csum.argtypes = [ctypes.c_double, ctypes.c_double]
ctestlib.csum.restype = ctypes.c_double


def muestraDatos():
    # Es normal que este print no sea inmediato, cuidado con el tema de los buffers de salida
    ctestlib.muestraDatos()

def insertarPersona():
    ctestlib.insertarPersona()

def csum(a, b):
    # Podriamos validar, transformar datos o hacer cualquier cosa antes o despues de llamar a la funcion de C
    return ctestlib.csum(a, b)
