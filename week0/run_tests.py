import glob
from subprocess import call


def run_tests():
    for dir_ in glob.glob("*[!.]??"):
        print("\ntests for %s"%dir_)
        for folder in glob.glob("./%s/*[!.]??"%dir_):
            call("python3 ./%s/tests.py"%folder, shell = True)


def main():
    run_tests()

if __name__ == '__main__':
    main()
