from collections import defaultdict
import re

data = open("DA.txt", encoding="utf8").read()

lines = data.split("\n")

reg_pattern = re.compile(r"\w+")

word_count = defaultdict(int)

for line in lines:
    for i in re.findall(reg_pattern, line):
        word_count[i.lower()] += 1

sorted_output = sorted([(x[1], x[0]) for x in word_count.items() if len(x[0]) == 2], key=lambda x: int(x[0]), reverse=True)
for i in sorted_output:
    if int(i[0]) > 1:
        print(i)