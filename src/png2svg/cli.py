# src/fizzbuzz_kata/cli.py
"""Command-line interface for png2svg."""
import argparse
from png2svg.core import png2svg

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="png2svg",
        description="Transform a pixel image in a scalable svg made of hexagons of the picture",
    )
    parser.add_argument("source_image", type=str, nargs="?",
        help="Image to convert",
    )
    parser.add_argument("output_file", type=str, nargs="?",
            help="name of wanted file",
        )
    parser.add_argument("size", type=int, nargs="?",
            help="size of hexagons in the svg",
        )
    parser.add_argument("flattop", type=bool, nargs="?",
            help="wether the hexagons are flattop or not",
        )
    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    png2svg(args.source_image,args.output_file,args.size,args.flattop)

if __name__=="main":
    main()
