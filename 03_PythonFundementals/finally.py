import os
import sys

def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)

def main():
    try:
        print('Current directory is {0}'.format(os.getcwd()))
        make_at(os.getcwd(), 'Frogs')
        print('Ends on directory {0}'.format(os.getcwd()))
    except OSError:
        print('Error has been raised')
        print('Still at directory {0}'.format(os.getcwd()))

if __name__ == '__main__':
    main()
