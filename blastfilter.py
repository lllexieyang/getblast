# !/usr/bin/env python

# Extract information from blast result.
# Python3
# EXAMPLES:
# 1. filter with default set (length 100, cov 80.00, score 100)
# python blastfilter.py -f [blast file name]
# 2. extract results that exactly matched "mcr-1"
# python blastfilter.py -f [blast file name] -g mcr-1 -e
# 3. extract results with gene names contains "mcr"
# python blastfilter.py -f [blast file name] -g mcr
# NOTE: "|" is not allowed in the gene name


# Copy right reserved : Lu Yang (yanglu2016@cau.edu.cn)
# Last change: Sep 8 2022
# Version 2.0


import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the name blast result file")
    parser.add_argument("-c", "--coverage", default="80.00", help="minimum coverage, default 80.00")
    parser.add_argument("-l", "--length", default="100", help="minimum length, default 100")
    parser.add_argument("-s", "--score", default="100", help="minimum score, default 100")
    parser.add_argument("-g", "--gene", default=False, help="extract results of specific gene")
    parser.add_argument("-e", "--exact", default=False, action="store_true", help="exact name of specific gene")
    return parser.parse_args()
args = get_arguments()


def filter(file):
    file_out = "filter_" + file
    i = open(file, "r")
    o = open(file_out, "w")
    coverage = float(args.coverage)
    length = int(args.length)
    score = float(args.score)
    nodes = []
    for line in i.readlines():
        flag = True
        node = line.split('\t')
        if float(node[2]) >= coverage and int(node[3]) >= length and float(node[11]) >= score:
            if nodes == [] or node[0] != nodes[0][0]:
                nodes = []
                nodes.append(node)
                o.write(line)
            else:
                f0 = int(node[6])
                t0 = int(node[7])
                len = int(node[3])
                for i in nodes:
                    f = int(i[6])
                    t = int(i[7])
                    overlap = min(t0, t) - max(f0, f) + 1
                    if overlap > 0.8 * len:
                        flag = False
                        break
                if flag:
                    nodes.append(node)
                    o.write(line)
    return 0


def extract(file):
    file_out = args.gene + "_" + file
    i = open(file, "r")
    o = open(file_out, "w")
    for line in i.readlines():
        gene = line.split('\t')[1]
        if args.exact:
            if gene == args.gene:
                o.write(line)
        elif args.gene in gene:
            o.write(line)
    return 0


def main():
    args = get_arguments()
    if args.gene:
        extract(args.file)
    else:
        filter(args.file)


if __name__ == '__main__':
    main()
