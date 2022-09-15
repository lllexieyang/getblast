# getblast
  Collect information from blast results


# findgene.py
  Python2 （ancient unmaintained code)  
  Collect blast result of contigs containing specific gene and coexist with other genes.  

### EXAMPLE:
  1. Find the results contains specific gene  
    ```
    findgene.py -b /path/to/results/ -g mcr-1
    ```
  2. Find other genes coexist in the same contig with target one, like Inc, IS, et al.  
    ``` 
    findgene.py -b /path/to/results/ -g mcr-1 -f Inc
    ```

# blastfilter.py
  Python3  
  Filter for redundant results, only the best match would be retained.  
  Extract blast results of contigs containing specific gene.
  
### EXAMPLES:
  1. filter with default set (length 100, coverage 80.00, score 100)  
    ```
    python blastfilter.py -f [blast file name]
    ```
  2. filter with customized set  
    ```
    python blastfilter.py -f [blast file name] -l 500 -c 60 -s 0
    ```  
  3. extract results that exactly matched "mcr-1"  
    ```
    python blastfilter.py -f [blast file name] -g mcr-1 -e
    ```
  4. extract results with gene names contains "mcr"  
    ```
    python blastfilter.py -f [blast file name] -g mcr
    ```  
    NOTE: "|" is not allowed in the gene name
