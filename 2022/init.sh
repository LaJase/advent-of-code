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
CMD="cp ${folder}/code-starter.py ${folder}/solutions/code.day0${DAY}.py"
echo "${CMD}"
eval "${CMD}"

CMD_INPUT_START="touch $folder/puzzles/input.day0$DAY.start.txt"
echo "${CMD_INPUT_START}"
eval "${CMD_INPUT_START}"

if [ "$SESSION_TOKEN" != "" ]; then
	CMD_INPUT="curl 'https://adventofcode.com/2022/day/$DAY/input' -H 'cookie: session=$SESSION_TOKEN' --compressed --insecure -o ./$folder/puzzles/input.day0$DAY.txt"
else
	CMD_INPUT="touch $folder/puzzles/input.day0$DAY.txt"
fi
eval "${CMD_INPUT}"
echo "${CMD_INPUT}"
