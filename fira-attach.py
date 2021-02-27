#!/usr/bin/python3

# dependencies:
# - fontforge

import sys
import os
from subprocess import Popen
from pathlib import Path

cwd = Path.cwd()

FIRA_CODE_FILE_NAME = "Fira Code Light Nerd Font Complete Mono.ttf"
FIRA_PATH = cwd / "font" / FIRA_CODE_FILE_NAME

OUTPUT_FOLDER_NAME = "output"
OUTPUT_FOLDER = cwd / OUTPUT_FOLDER_NAME


def do_the_thing():
    if len(sys.argv) == 1:
        attach_fira_on_folder(cwd)
    else:
        path = Path(sys.argv[1])
        if path.is_dir():
            attach_fira_on_folder(path)
        elif path.is_file():
            attach_fira(path)
        else:
            sys.stderr.write(f"Not supported font type ({str(path)}). \n")


def attach_fira_on_folder(folder: Path):
    for file in list(folder.glob("*.ttf")) + list(folder.glob("*.otf")):
        attach_fira(file)


def check_output_folder():
    if not os.path.exists("output"):
        os.mkdir("output")


def attach_fira(font: Path):
    final_name = f"{removesuffix(font.name, font.suffix)} - FiraAttached.ttf"
    run(["./mergefonts.sh", font, FIRA_PATH, final_name])
    print(f"Attached Fira Code glyphs to {font.name}")


def run(cmd: list):
    return Popen(cmd).wait()


def removesuffix(string: str, suffix: str):
    if string.endswith(suffix):
        return string[: -len(suffix)]


def cleanup():
    if os.path.exists("1.ttf"):
        os.remove("1.ttf")
        os.remove("2.ttf")


if __name__ == "__main__":
    check_output_folder()
    do_the_thing()
    cleanup()
