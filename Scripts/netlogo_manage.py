import argparse
import configparser
import sys
sys.path.append('../Python-Netlogo')
from NetlogoUtils import Python_Netlogo_Connection

def process(run_experiment):
    if run_experiment is not None:
        config = configparser.ConfigParser()
        config.read('Experiments\\' + 'Experiment1.ini')
        print(run_experiment)
    Python_Netlogo_Connection.run_experiment(config['EXPERIMENT'])


def get_parameters():
    parser = argparse.ArgumentParser(description="Config and run netlogo experiments")
    parser.add_argument('--run_experiment', nargs='?', const='Experiment1.ini', help='Run experiment')
    args = parser.parse_args()
    return vars(args)

if __name__ == "__main__":
    params = get_parameters()
    process(**params)