import os
import sys
import pathlib as PL
import subprocess as SP
import translate as T


def install(package):
    SP.check_call([sys.executable, "-m", "pip", "install", package])


def first_run():
    fp = PL.Path(__file__)
    fr = fp.parent / 'fr'
    if not fr.exists():
        install('pyperclip')
        install('googletrans')
        fr.touch()


def main():
    first_run()
    T.Translate()


if __name__ == "__main__":
    main()
