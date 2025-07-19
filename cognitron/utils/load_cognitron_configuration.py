import yaml
import sys
import argparse

def parseArgs(arguments):
    """ Parse script inputs"""

    parser = argparse.ArgumentParser(description='Script for parsing the Cognitron configurations')
    parser.add_argument(
        '-y',
        '--yaml',
        help='Add YAML file path',
        default='./cognitron.yaml'
    )

    args = parser.parse_args(arguments)

    return args
def convert_yaml_to_dict(yaml_fp):
    # Open the yaml file to read it
    with open(yaml_fp, 'r') as f:
        data = yaml.safe_load(f)

    return data

def convert_yaml_to_env(args):
    args = parseArgs(args)
    yaml_fp = args.yaml

    data = convert_yaml_to_dict(yaml_fp)
    for key, value in data.items():
        # Handle different data types - ensure they are properly quoted if needed
        if isinstance(value, str):
            print(f'export {key}="{value}"')
        else:
            print(f'export {key}={value}')

if __name__ == "__main__":
    # Parse the input arguments from command line
    cli_args = sys.argv[1:]
    convert_yaml_to_env(cli_args)
