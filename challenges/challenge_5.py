# python packages
import sys
# internal projects
from graph import Graph


def main(Object):
	print(Object.eulerian_cycle())


if __name__ == '__main__':
	# no filepath -- ask for a string
	if len(sys.argv) == 1:
		output = main(Graph())

	# have a filepath
	elif len(sys.argv) == 2:
		file = sys.argv[1]
		output = main(Graph(file))

	# there was a problem D:
	else:
		raise
