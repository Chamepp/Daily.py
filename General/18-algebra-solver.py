from sympy import *
import sys

# Defining Solver
def solver(x):
	sympy_eq = sympify("Eq(" + x.replace("=", ",") + ")")
	result = solve(sympy_eq)
	return result[0]

# Output Results
def main(x):
	X = solver(x)
	print("X = " + str(X))

if __name__ == "__main__":
	main(sys.argv[1])