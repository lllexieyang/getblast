# Inc_result
# collect Inc type and node information from blast file

#!/usr/bin/env python

import re

def Inc_result(isolate, gene):
    f = open(isolate, "r")
    line = f.readline()
    node_num = 'apple' #or whatever
    while line:
        find_gene = line.find(gene)
        if find_gene >= 0:
            r = open("node_info.txt", "a")
            node_num = 'NODE_' + re.findall(r"NODE_(.+?)_", line)[0]
            length = re.findall(r"length_(.+?)_", line)[0]
            r.write(isolate + "\t" + node_num + "\t" + length + "\n")
            r.close()  
        c1 = line.find(node_num)
        c2 = line.find('Inc')
        if c1 >= 0 and c2 >= 0:
            r2 = open("Inc_result.txt", "a")
            Inc_type = 'Inc' + re.findall(r"Inc(.+?)\t", line)[0]
            r2.write(isolate + "\t" + Inc_type + "\n")
            r2.close()
        line = f.readline()
    f.close()
    return 0

gene = 
isolates = 
for isolate in isolates:
    Inc_result(isolate, gene)

