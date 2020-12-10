import os
import sys

if len(sys.argv) > 3:
    print("Too many arguments")
elif len(sys.argv) < 2:
    print("Not enough arguments")

base = sys.argv[1]
deploy = sys.argv[2]

def loadConfig(file):
    dict = {}
    with open(file) as fin:
        for l in fin.readlines():
            line = l.split('=')
            if len(line) == 2:
                dict[line[0]] = line[1].strip('\n')
    return dict


if 'default' not in os.listdir(os.getcwd()):
    exit(1)

os.chdir('default')


for d in os.listdir():
    ## base config
    base_config = loadConfig( os.getcwd() + '/' + d + '/environments/' + base + '/config.env')
    ## deploy config
    deploy_config = loadConfig(os.getcwd() + '/' + d + '/environments/' + deploy + '/config.env')

    delta = set(base_config.keys()) - set(deploy_config.keys())

    if delta == set():
        continue
    else:
        print(f"{d} is missing the following config values:")
        for k in delta:
            print(k)
