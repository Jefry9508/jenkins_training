#! /bin/bash

# POSIX

# Initialize all the option variables.
# This ensures we are not contaminated by variables from the environment.
arguments=
projName=
appName=
properties=
jmeterPath=
versionApp=
path=
workingPath=


cd "$(dirname "$0")"

python main.py -a $ENV_ARGS -p $ENV_PARAMS -n "$ENV_PROJNAME" -m "$ENV_APPNAME" -V $ENV_VERSION