import sys
import argparse
import json
import pandas

def main(argv):

    parser = argparse.ArgumentParser(description='Given either a json or csv inputfile, pact-util will run the command specified and write the results to outputfile')
    parser.add_argument('command', help="options are to_csv or to_json")
    parser.add_argument('-i', '--inputfile',
                    help="input file to be acted on")
    parser.add_argument('-o', '--outputfile',
                    help="file output will be written to")
    args = parser.parse_args()

    # open input file
    try:
        with open(args.inputfile, 'r') as f:
            input_pact_string = f.read()
    except:
        print("Error: Could not open input file.")
        sys.exit()

    # jsonify it
    try:
        pact_json = json.loads(input_pact_string)
    except:
        print("Error: could not parse json.")
        sys.exit()

    # flatten it
    try:
        df = pandas.json_normalize(pact_json)
    except:
        print("Error: could not normalize json.")
        sys.exit()

    # output as csv
    try:
        df.to_csv(args.outputfile, encoding='utf-8', index=False)
        print("Saved csv as " + args.outputfile + ".")
    except:
        print("Error: could not write csv.")
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
