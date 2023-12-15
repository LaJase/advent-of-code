#! /bin/bash

if [ $# -ne 1 ]; then
	echo
	echo "Il faut entrer le numéro du jour"
	echo
	echo "  $0 <day_num>"
	echo "      day_num: num of the day (ex: 10)"
	exit 1
fi

DAY=$1

# On copie le script
folder=$(dirname "${0}")
CMD="cp ${folder}/code-starter.py ${folder}/code.day${DAY}.py"
echo "${CMD}"
eval "${CMD}"
