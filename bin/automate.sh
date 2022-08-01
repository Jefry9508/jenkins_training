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

# while :; do
#     case $1 in
#         -h|--help)
#             python3 main.py -h
#             exit
#             ;;
#         -v|--version)       
#             python3 main.py -v
# 			exit
#             ;;
#         -a|--args)
#             arguments=$2
# 			shift
#             ;;
#         -n|--projname)
#             projName=$2
# 			shift
#             ;;
#         -m|--appname)
#             appName=$2
# 			shift
#             ;;
# 		-p|--properties)
#             properties=$2
# 			shift
#             ;;
# 		-r|--path)
#             jmeterPath="$2"
# 			shift
#             ;;
# 		-V|--versionapp)
#             versionApp=$2
# 			shift
#             ;;
#         *)               # Default case: No more options, so break out of the loop.
#             break
#     esac

#     shift
# done

python main.py -a $ENV_ARGS -p $ENV_PARAMS -n "$ENV_PROJNAME" -m "$ENV_APPNAME" -V $ENV_VERSION