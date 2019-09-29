# !/usr/bin/env python


# Collect blast result of contigs containing specific gene and coexist with other genes.
# Inc_result.py -b [blast path] -g [gene]


import os
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gene", required=True, help="name of query gene, REQUIRED")
    parser.add_argument("-p", "--path", default=os.getcwd(), help="the path to blast results, default is current path")
    parser.add_argument("-f", "--find", required=False, type=str,
                        help="to find other coexist sequence, like Inc, IS, et al. optional")
    return parser.parse_args()


def find_contig(file, gene):
    contigs = []
    f = open(file, "r")
    for line in f.readlines():
        contig_name = line.split('\t')[0]
        if 0 <= line.find(gene) and contig_name not in contigs:
            contigs.append(contig_name)
    print '\nfile'
    print file
    print '\ncontigs'
    print contigs
    return contigs


def blast_result(file, gene, contig_name, *addition):
    f = open(file, "r")
    find_gene = 0
    for line in f.readlines():
        if line.find(contig_name) >= 0:
            r = open("blast_results.txt", "a")
            t = open("tmp.txt", "a")
            r.write(file + '\t' + line)
            t.write(file + '\t' + line)
            if line.find(gene) >= 0 and find_gene == 0:
                find_gene = line.split('\t')[1]
            r.close()
            t.close()
    print '\ncontig:'
    print contig_name
    print 'gene:'
    print find_gene
    find = addition[0]
    if find is not None:
        t = open("tmp.txt", "r")
        for line in t.readlines():
            if line.find(find) >= 0:
                find_loc = line.split('\t')[1]
                find_name = line.split('\t')[2]
                find_cover = line.split('\t')[3]
                find_identity = line.split('\t')[4]
                o = open("%s+%s.txt" % (gene, find), "a")
                o.write(file + '\t' + find_gene + '\t' + find_loc + '\t' + find_name + '\t' + find_cover + '\t' + find_identity + '\n')
                o.close()
        t.close()
    f.close()
    os.remove("tmp.txt")
    return 0


def main():
    args = get_arguments()
    gene = args.gene
    os.chdir(args.path)
    if os.path.exists("blast_results.txt"):
        button = raw_input("Result file already exist.\nDo you want to run again?[y/n]")
        if button == 'n':
            exit()
        elif button == 'y':
            os.remove("blast_results.txt")
            print 'The old output file will be replaced by the new one.'
    files = os.listdir('./')
    for file in files:
        if file.split('.')[-1] == 'blast':
            for contig_name in find_contig(file, gene):
                blast_result(file, gene, contig_name, args.find)
    print '\nBlast results of contigs containing %s are saved as \033[1;31mblast_results.txt\033[0m' % gene
    if args.find is not None:
        print 'Coexist results are saved as \033[1;31m%s+%s.txt\033[0m' % (gene, args.find)


if __name__ == '__main__':
    main()
