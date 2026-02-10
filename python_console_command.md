python -m : 
the M here stands for module.
it takes any module given to it, and runs it as if , it were a script , using the python which the current terminal is pointing towards.
ex -
python -m venv <my_venv>
python -m pip install numpy

What Python itself does
python → starts the Python interpreter executable you’re pointing at

-m pip → tells Python:
“Find the pip module, load it, and execute it as if it were run as a script (__main__).”

Inside pip, this is effectively equivalent to:
pip.main(["install", "numpy"])

install and numpy are nothing but command line arguments to the program called "pip"


python -c :
the -c flag is used to run , inline python
ex - 
python -c "import numpy as np; print(np.sqrt(4))"