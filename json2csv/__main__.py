import sys
import argparse
import json2csv.api
import logging


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description='JSON TO CSV Converter',
        epilog="Example: json2csv input_file.json output_file.csv")
    parser.add_argument("input", help="Path of the json file that you want to convert")
    parser.add_argument("output", help="Path of the output csv file")
    parser.add_argument("-l", "--log", help="Log file's path")
    args = parser.parse_args()

    if args.log:
        logger = logging.getLogger('json2csv')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(args.log)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)

    json2csv.api.json_to_csv(args.input, args.output)

if __name__ == "__main__":
    main()
