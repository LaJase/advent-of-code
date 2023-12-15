#! /bin/bash

if [ $# -ne 1 ]; then
	echo
	echo "Enter day's number please"
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

CMD_INPUT="touch $folder/puzzles/input.day$DAY.txt"
echo "${CMD_INPUT}"
eval "${CMD_INPUT}"

CMD_INPUT_START="touch $folder/puzzles/input.day$DAY.start.txt"
echo "${CMD_INPUT_START}"
eval "${CMD_INPUT_START}"
