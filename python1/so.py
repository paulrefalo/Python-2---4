#!/usr/local/bin/python3

d = {}
d['one'] = {"tag":"A"}
d['two'] = {"tag":"B"}
d['three'] = {"tag":"C"}
new_list = []
for k in ('one', 'two', 'three'):
    new_list += [x for x in d[k]["tag"]]

print(new_list)