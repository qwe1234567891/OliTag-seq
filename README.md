# OliTag-seq：The OliTag-seq Analysis Package
The OliTag-seq software package acts as our pipeline for the pretreatment and analysis of OliTag-seq data. The input files are the original sequencing read and manifest files, and the visual svg file is used as the output.
# The original paper describing OliTag-seq:
*******************************************
## Olitag-seq main function:


## Dependencies:
* Ubuntu20.04 or WSL2
* Python2.7 
* Dependency packages such as bwa, bedtools, numpy, matplotlib (in environment.yml)
* Reference genome fasta file(We have uploaded the reference genome fasta to Baidu web disk. human:   mouce:)
## Installation:
    # We recommend doing the following in a conda. A new conda environment will be created with Environment.yml
    # Assume that you already own conda and have a conda base environment open
    wget https://github.com/qwe1234567891/OliTag-seq/archive/refs/heads/main.zip
    unzip main.zip
    cd OliTag-seq-main
    conda env create -f environment.yml
    source activate olitag
## yaml文件举例，说明

## 运行
