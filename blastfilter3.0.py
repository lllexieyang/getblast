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
# Last change:  Aug 8 2023
# Version 3.0
# 3.0 changes:
#   1.Multiple subtypes of a gene in the same sequence are listed and specially labeled.
#   2.Genes with overlap between 50%-80% to last oneswere listed and noted. 


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

coverage_threshold = float(args.coverage)
length_threshold = int(args.length)
score_threshold = float(args.score)

def is_valid_entry(node):
    return float(node[2]) >= coverage_threshold and \
           int(node[3]) >= length_threshold and \
           float(node[11]) >= score_threshold


def overlaps(region0, region):
    f0 = min(int(region0[6]), int(region0[7]))
    t0 = max(int(region0[6]), int(region0[7]))
    len = int(region0[3])
    f = min(int(region[6]), int(region[7]))
    t = max(int(region[6]), int(region[7]))
    overlap = (min(t0, t) - max(f0, f) + 1)/len
    return overlap


def filter_and_modify(file):
    contig_records = {}
    with open(file, "r") as input_file, open("filter3_" + file, "w") as output_file:
        for line in input_file:
            node = line.strip().split('\t')
            current_contig = node[0]
            if is_valid_entry(node):
                if current_contig in contig_records:
                    n = 0
                    keep = True
                    someoverlap = False
                    for existing in contig_records[current_contig]:
                        if node[2] == existing[2] and node[3] == existing[3] and node[11] == existing[11]:
                            keep = False
                            contig_records[current_contig].append(node)
                            output_file.write(line.strip() + '\tSameRegion\n')
                            break
                        else:
                            overlap = overlaps(existing, node)
                            if overlap > 0.8:
                                keep = False
                                break
                            elif 0.5 < overlap < 0.8:
                                someoverlap = True
                                break
                        n += 1
                    if keep:
                        if someoverlap:
                            contig_records[current_contig].append(node)
                            output_file.write(line.strip() + '\toverlap=' + f"{overlap:.2%}" + '\n')
                        else:
                            contig_records[current_contig].append(node)
                            output_file.write(line)
                else:
                    contig_records[current_contig] = [node]
                    output_file.write(line)


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
        filter_and_modify(args.file)


if __name__ == '__main__':
    main()
