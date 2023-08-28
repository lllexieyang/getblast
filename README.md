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
 （still good to use)  
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


# blastfilter3.py 
 Python3  
### Changes:
#### 1. Multiple subtypes of a gene in the same sequence are listed and specially labeled.  
  主要针对以下这类结果设置，如：  
| Contig Name                       | Gene Name          | Identity (%) | Length | Mismatches | Gap Opens | Query Start | Query End | Subject Start | Subject End | E-Value | Bit Score |
|----------------------------------|--------------------|--------------|--------|------------|-----------|-------------|-----------|---------------|-------------|---------|-----------|
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_1_V00359 | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_10_EU855787 | 99.717     | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_4_AF498082 | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_3_EF015636 | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_8_Y00452 | 99.433       | 353    | 2          | 0         | 1           | 353       | 772           | 420         | 0.0     | 641       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_7_X62115 | 99.433       | 353    | 2          | 0         | 1           | 353       | 772           | 420         | 0.0     | 641       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_9_EU722351 | 99.150     | 353    | 3          | 0         | 1           | 353       | 772           | 420         | 0.0     | 636       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_6_L05392 | 99.150       | 353    | 3          | 0         | 1           | 353       | 772           | 420         | 0.0     | 636       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_5_AP004237 | 98.300     | 353    | 6          | 0         | 1           | 353       | 772           | 420         | 2.58e-178| 619       |
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_2_EU287476 | 98.300     | 353    | 6          | 0         | 1           | 353       | 772           | 420         | 2.58e-178| 619       |

  在上一版本中筛选结果为：
| Contig Name                       | Gene Name          | Identity (%) | Length | Mismatches | Gap Opens | Query Start | Query End | Subject Start | Subject End | E-Value | Bit Score |
|----------------------------------|--------------------|--------------|--------|------------|-----------|-------------|-----------|---------------|-------------|---------|-----------|
| NODE_931_length_353_cov_1.858696  | aph(3')-Ia_1_V00359 | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       |

  在此版本中结果为：
| Contig Name                         | Gene Name             | Identity (%) | Length | Mismatches | Gap Opens | Query Start | Query End | Subject Start | Subject End | E-Value | Bit Score | Comment          |
|------------------------------------|-----------------------|--------------|--------|------------|-----------|-------------|-----------|---------------|-------------|---------|-----------|------------------|
| NODE_931_length_353_cov_1.858696    | aph(3')-Ia_1_V00359  | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       |                  |
| NODE_931_length_353_cov_1.858696    | aph(3')-Ia_10_EU855787| 99.717     | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       | SameRegion       |
| NODE_931_length_353_cov_1.858696    | aph(3')-Ia_4_AF498082 | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       | SameRegion       |
| NODE_931_length_353_cov_1.858696    | aph(3')-Ia_3_EF015636 | 99.717       | 353    | 1          | 0         | 1           | 353       | 772           | 420         | 0.0     | 647       | SameRegion       |

  可根据情况选择要保留的亚型。

#### 2. Genes with overlap between 50%-80% to last ones are listed and noted.  
  上一版本仅删除与已有结果重合度>80%的比对结果，此版本保留50-80%重合度的比对结果，但在行末标注重合度，以供参考。
