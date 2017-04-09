import yaml
import sys
import io
import subprocess

with io.open(sys.argv[1], 'r') as f:
    buildspec = yaml.load(f)
    for command in buildspec['phases']['build']['commands']:
        process = subprocess.Popen(command, shell=True)
        process.wait()
        if process.returncode != 0:
            print "Command {0} failed with code {1}".format(command, process.returncode)
