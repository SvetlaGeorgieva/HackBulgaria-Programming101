import sys


def main():
	filename = []
	filename = sys.argv[1:]
	for i in filename:
		file = open(i, "r")
		content = file.read().split("\n")
		print("\n".join(content))
		file.close()
		print("\n")

if __name__ == '__main__':
    main()