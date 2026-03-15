import sys
import os

# Añade la raíz del proyecto al path para que pytest encuentre src/
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))