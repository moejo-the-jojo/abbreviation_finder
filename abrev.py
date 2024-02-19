from collections import defaultdict
import re

data = open("DA.txt", encoding="utf8").read()


lines = data.split("\n")

reg_pattern = re.compile(r"\w+")

word_count = defaultdict(int)

# print(word_count)

for line in lines:
    for i in re.findall(reg_pattern, line):
        word_count[i.lower()] += 1

count_first = [(x[1], x[0]) for x in word_count.items() if len(x[0]) > 2]

ordered_finished_list = sorted(count_first, key=lambda x: int(x[0]), reverse=True)
for i in ordered_finished_list:
    print(i)