# getblast
  Collect information from blast results


# findgene.py
  Python2
  Collect blast result of contigs containing specific gene and coexist with other genes.
  
  EXAMPLE:
  findgene.py -b [blast path] -g [gene]


# blastfilter.py
  Python3
  Filter for redundant results, only the best match would be retained.
  Extract blast results of contigs containing specific gene.
  
  EXAMPLES:
  1. filter with default set (length 100, cov 80.00, score 100)
    python blastfilter.py -f [blast file name]
  2. extract results that exactly matched "mcr-1"
    python blastfilter.py -f [blast file name] -g mcr-1 -e
  3. extract results with gene names contains "mcr"
    python blastfilter.py -f [blast file name] -g mcr
    NOTE: "|" is not allowed in the gene name
