from distutils.core import setup
import py2exe

setup(
    console = [{'main.py','colors.py','algorithms.bubbleSort.py','algorithms.mergeSort.py'}]
)