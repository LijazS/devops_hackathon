from collections import Counter
import os
from pathlib import Path

fl = Path.cwd()
fl2 = os.path.join(fl,"qn3","log.txt")


with open(fl2,"r") as f:
    content = f.read()

words = content.split()
freq = Counter(words)


sum_vals = sum(freq.values())
one_pct = sum_vals * 0.01


anoms = []
for key,value in freq.items():
    if value <= one_pct:
        anoms.append(key)


with open(fl2,"r") as f:
    lines = f.readlines()

flag_line = []
for line in lines:
    wo = line.split()
    for wor in wo:
        if wor in anoms:
            flag_line.append(line.strip())
            break

print("flagged lines: ",flag_line)
