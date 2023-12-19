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

folder=$(dirname "${0}")
SESSION_TOKEN=$(cat "$folder"/session-token.txt)

# On copie le script
CMD="cp ${folder}/code-starter.py ${folder}/solutions/code.day${DAY}.py"
echo "${CMD}"
eval "${CMD}"

CMD_INPUT_START="touch $folder/puzzles/input.day$DAY.start.txt"
echo "${CMD_INPUT_START}"
eval "${CMD_INPUT_START}"

CMD_INPUT="curl 'https://adventofcode.com/2023/day/$DAY/input' -H 'cookie: session=$SESSION_TOKEN' --compressed -o ./$folder/puzzles/input.day$DAY.txt"
echo "${CMD_INPUT}"
eval "${CMD_INPUT}"
