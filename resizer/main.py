from ast import arg
from email import parser
from email.policy import default
from inspect import ArgSpec
#from nis import maps
import os
import pathlib
#import cv2 as cv
#import numpy as np
#import matplotlib.pyplot as plt
import argparse
import imghdr
from tqdm import tqdm
import PIL
from math import ceil
from PIL import Image


def arguments():
    parser = argparse.ArgumentParser(description="Bulk Image resizer",
    formatter_class=argparse.MetavarTypeHelpFormatter,
    )
    parser._positionals.title = 'Positional arguments'
    parser._optionals.title = 'Optional arguments'
    parser.add_argument('-v', '--version', action='version',version='%(prog)s 1.0', help="Show program's version number and exit.")
    parser.add_argument('-h','--help')
    parser.add_argument(
        "folder",
        matavar="folder",
        type=str,
        nargs="?",
        help="dir of Images that will be resized",
    )
    parser.add_argument(
        "-d",
        type=str,
        nargs="?",
        help="dimention in Width:height",
    )
    parser.add_argument(
        "-o",
        type=str,
        nargs="?",
        default="Resized Images",
        help="directory output ",
    )
    parser.add_argument(
        "-q",
        type=int,
        nargs="?",
        default=50,
        help="Max number of Files Resized , Default = 50",
    )
    parser.add_argument(
        "-p",
        type=int,
        nargs="?",
        default=None,
        help="Percentage of Img Resize",
    )
    parser.add_argument(
        "-k",
        type=int,
        nargs="?",
        help="",
    )

    return parser.parse_args()


def main():
    args = arguments()

    if not args.p and not args.d:
        raise Exception(
            "Dimention ?"
            "Must be provided 'w:h' or 'Percentage'"
        )
        temp_outputs =""
    
        default_save ="Resized/"
        saving_dir = args.o
        # dir of bulk images to be resized
    current_dir =(
        str(pathlib.Path(__file__).parent.absolute())+ "\\%s\\"%arg.folder
    ).replace("\\,""/")

    #check if the path is full directory
    temp = (r"%" % args.folder).replace("\\","/")
    if os.path.isdir(temp):
        current_dir = "%s/" %temp
    
    if args.o != default_save:
        maps = (r"%s" % args.o).split("\\")
        temp_output ="/".join(maps[:-1])
        save = maps[-1]

   #list all items in the current directory
    list_directory = os.listdir(current_dir)
    list_directory = list(
        filter(lambda e: e.endswith(("jpg", "png", "jpeg")), list_directory)
    )
    len_ldirectory = len(list_directory)
    print(
        f"""
    Target Directory  : {args.folder}
    Target Output     : {args.o}
    Target Dimension  : {args.d}
    Target Percentage : {args.p}%
    Target Quality    : {args.q}/100 pixels
    """
    )

    for index in tqdm(range(len_ldirectory)):
        images = current_dir + list_directory[index]
        fl, ex = os.path.splitext(current_dir + list_directory[index])
        splits = (r"%s" % fl).split("/")

        img = Image.open(images)
        original_size = img.size

        if args.p:
            size = (
                ceil(original_size[0] * args.p / 100),
                ceil(original_size[1] * args.p / 100),
            )
        else:
            size = tuple(map(int, args.d.split(":")))

        file = savings_dir + splits[-1] + ex
        imgs = img.resize(size, PIL.Image.ANTIALIAS)
        imgs.save(file, quality=args.q)
        imgs.close()

if __name__=="__main__":
    main()
     

