import rich

from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument('file', type=str)
args = parser.parse_args()

print(args.file)




