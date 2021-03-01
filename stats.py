

import json
import sys

json_file = sys.argv[-1]

with open(json_file, 'r') as fp:
    telegram = json.load(fp)

messages = telegram["messages"]
stats = dict()


for message in messages:
    if message.get('from') is None:
        continue
    if message['from'] not in stats:
        stats[message['from']] = 1
    else:
        stats[message['from']] += 1
print(stats)


import matplotlib.pyplot as plt
from  matplotlib import rcParams

rcParams['font.sans-serif'] = ['Noto Sans']
fig, ax = plt.subplots()
ax.set_xlabel("People")
ax.set_ylabel("Number of messages")
ax.set_title(telegram['name'])
ax.set_frame_on(True)

people = [x[:10] for x in stats.keys()]
messages = stats.values()
ax.bar(people, messages)

for i, v in enumerate(stats.values()):
    ax.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')

ax.legend()
plt.show()

