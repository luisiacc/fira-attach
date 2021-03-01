#!/usr/bin/python3

# dependencies:
# - fontforge

import sys
import os
import shutil
from subprocess import Popen
from pathlib import Path

cwd = Path.cwd()

FIRA_CODE_FILE_NAME = "Fira Code Light Nerd Font Complete Mono.ttf"
FIRA_PATH = cwd / "font" / FIRA_CODE_FILE_NAME

OUTPUT_FOLDER_NAME = "output"
OUTPUT_PATH = cwd / OUTPUT_FOLDER_NAME

ACCEPTED_FONT_EXTENSIONS = ("*.ttf", "*.otf")


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
            sys.stderr.write(f"Not supported file ({str(path)}). \n")


def attach_fira_on_folder(folder: Path):
    for extension in ACCEPTED_FONT_EXTENSIONS:
        for file in folder.glob(extension):
            attach_fira(file)


def check_output_folder():
    if not os.path.exists(OUTPUT_FOLDER_NAME):
        os.mkdir(OUTPUT_FOLDER_NAME)


def attach_fira(font: Path):
    final_name = f"{removesuffix(font.name, font.suffix)} - FiraAttached.ttf"
    run(["./mergefonts.sh", font, FIRA_PATH, final_name])
    shutil.move(final_name, OUTPUT_PATH / final_name)
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
