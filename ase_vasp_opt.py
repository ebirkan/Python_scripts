# Import required modules
import os, sys
import ase
from ase.calculators.vasp import Vasp
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter

#read atoms from POSCAR file
atoms = ase.io.read("POSCAR")

# set environments
os.environ["VASP_PP_PATH"] = "/---/---/vasp/potentials/potpaw_PBE.54/"

# set calculator
dft = Vasp(kpts=[18,18,1],
           gamma=True,
           encut=400,
           ismear = 0,
           sigma = 0.1,
           xc = 'pbe',
           ivdw=202,
           ediff=1E-6,
           pp=os.getenv("VASP_PP_PATH"),
           setups='recommended',
)
atoms.set_calculator(dft)

#Optimizer
opt = BFGS(ExpCellFilter(atoms, mask=[1, 1, 0, 0, 0, 0]), logfile="ase_vasp_opt.log")
opt.run(fmax=0.001)
