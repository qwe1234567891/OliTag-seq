# OliTag-seq：The OliTag-seq Analysis Package
The OliTag-seq software package acts as our pipeline for the pretreatment and analysis of OliTag-seq data. The input files are the original sequencing read and manifest files, and the visual svg file is used as the output.
# The original paper describing OliTag-seq:
*******************************************


## Olitag-seq main function:
The package implements a pipeline composed of data screening and labeling, PCR product filtering and off-target identification modules. Using Illumina sequencing data and manifest file as input, the miss sequence information is obtained through a series of processing, and the results are visualized in the form of svg diagram.

![image](https://user-images.githubusercontent.com/76864588/236216435-b9f82902-10f4-4fb9-812a-787c9f250656.png)

The functions of each submodule are as follows：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.&nbsp;&nbsp;**Data filtering and labeling：** The reads to be mixed were first screened for data according to linker and barcodes. The data that meets the conditions will be extracted according to the location of UMI. And take 6 bases after linker as small fragment 1. Six bases were taken from the other end of the two-ended sequencing reads as the small slice end. Finally, all three are combined and written into an id for marking. UMI is used as the sorting basis to sort in ascending alphabetical order.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.&nbsp;&nbsp;**PCR Duplicate Consolidation：** Reads with the same UMI and two small sequences of the same genome were considered to be from the same pre-PCR molecule, and the reads with the highest average Q value were represented to improve the quantitative interpretation of the count of GUIDE-Seq Reads.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.&nbsp;&nbsp;**Align to genome：** The demultiplexed, consolidated paired end reads are aligned to a reference genome using the BWA-MEM algorithm with default parameters (Li. H, 2009).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.&nbsp;&nbsp;**Identify ckeavage sites：** The start mapping positions of the read amplified with the tag-specific primer (second of pair) are tabulated on a genome-wide basis. Start mapping positions are consolidated using a 10-bp sliding window. Windows with reads mapping to both + and - strands, or to the same strand but amplified with both forward and reverse tag-specific primers, are flagged as sites of potential DSBs. 25 bp of reference sequence is retrieved on either side of the most frequently occuring start-mapping position in each flagged window. The retrieved sequence is aligned to the intended target sequence using a Smith-Waterman local-alignment algorithm.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.&nbsp;&nbsp;**Annotation and visualization：** Alignment of detected off-target sites is visualized via a color-coded sequence grid.
Notes: ds34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ds39
## Dependencies:
* Ubuntu 20.04 or WSL2
* Python 2.7 
* Dependency packages such as bwa, bedtools, numpy, matplotlib (in environment.yml)
* Reference genome fasta file(We have uploaded the reference genome fasta to Baidu web disk. human:   mouce:)
## Installation:
    # We recommend doing the following in a conda. A new conda environment will be created with Environment.yml.
    # Assume that you already own conda and have a conda base environment open...
    wget https://github.com/qwe1234567891/OliTag-seq/archive/refs/heads/main.zip
    unzip main.zip  # Download the olitag code package and unzip it...
    cd OliTag-seq-main
    
    conda env create -f environment.yml  # Create a new conda environment for olitag...
    source activate olitag
## Example and description of the Manifest File(\*.yaml)
We added the input parameters required by olitag, the reference genome path, and some tool information to manifest.yaml so that we could manage and adjust the input parameters manifest.yaml can be opened and edited using most text editing tools. Here is an example:

    reference_genome: ../reference_genome/human.fa
    output_folder: ./

    bwa: bwa
    bedtools: bedtools

    data1: ["test_1.fq.gz"]
    data2: ["test_2.fq.gz"]


    samples:
      EXM1:
        target: GTGGGGAAGAAGGTGTCTTCNGG
        barcode1: AACCTCTT
        barcode2: CCAATCTG
        description: EXM1

      EXM2:
        target: GTGGGGAAGAAGGTGTCTTCNGG
        barcode1: AATACCGC
        barcode2: CCAATCTG
        description: EXM2
Meaning of each field:
* _reference_genome:_ Reference to the genomic fasta path can be human or mouse.
* _output_folder:_ Olitage-seq Specifies the path for storing generated files.
* _bwa、bedtools:_ The sequence alignment tool used in the code.
* _data1、data2:_ The input data(\*_1.fq.gz、\*_2.fq.gz)
* _samples:_ A nested field containing the details of each sample. The required parameters are targetsites, forward barcode reverse barcode and a descroption of the sample.

## Running:
After downloading our code package and installing it successfully, you can run our test data using the following commands:

    python OliTag-seq/OliTag.py all -m manifest.yaml

Please note that we don't have a running pipeline for each step, you can test our submodules by code comments, provided you have the output from the previous step.
