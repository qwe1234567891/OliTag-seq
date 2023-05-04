# -*- coding:utf-8 -*-
# @Time    :2023/4/26 14:37
# @Author  :ZZK
# @ File   :data.py
# Description:
import gzip
import os

def ds34fuu_length_insertion(file):
    file_34cor = open("A849-34cor.fq", "w")
    file_34ins = open("A849-34ins.fq", "w")
    file_txt = open("A849-34.txt", "w")
    f = gzip.open(file, 'rb')
    s1_1 = f.readline().decode('utf-8')
    s1_2 = f.readline().decode('utf-8').replace("\n", "")
    s1_3 = f.readline().decode('utf-8')
    s1_4 = f.readline().decode('utf-8').replace("\n", "")
    s1_2_re = s1_2.replace("A", "B").replace("G", "D").replace("T", "A").replace("C", "G").replace("B", "T").replace(
        "D", "C")[::-1]
    seq1 = "AATGGGGGTGTGTCACCAGA"
    ds34g15 = ""
    ds34gFR = ""
    file_numbers = 0
    file_34cor_numbers = 0
    file_34ins_numbers = 0
    file_ds34gFR_numbers = 0
    len230_250_34ins_numbers = 0
    len265_285_34ins_numbers = 0
    while s1_1:
        file_numbers += 1
        if seq1 in s1_2[20:61]:
            file_34cor_numbers += 1
            file_34cor.write(s1_1 + s1_2 + "\n" + s1_3 + s1_4 + "\n")
            if ds34g15 in s1_2:
                file_34ins_numbers += 1
                file_34ins.write(s1_1 + s1_2 + "\n" + s1_3 + s1_4 + "\n")
                if 230 <= len(s1_2) <= 250:
                    len230_250_34ins_numbers += 1
                if 265 <= len(s1_2) <= 285:
                    len265_285_34ins_numbers += 1

            elif ds34g15 in s1_2_re:
                file_34ins_numbers += 1
                file_34ins.write(s1_1 + s1_2_re + "\n" + s1_3 + s1_4[::-1] + "\n")
                if 230 <= len(s1_2_re) <= 250:
                    len230_250_34ins_numbers += 1
                if 265 <= len(s1_2_re) <= 285:
                    len265_285_34ins_numbers += 1
            if ds34gFR in s1_2 or s1_2_re:
                file_ds34gFR_numbers += 1
        s1_1 = f.readline().decode('utf-8')
        s1_2 = f.readline().decode('utf-8').replace("\n", "")
        s1_3 = f.readline().decode('utf-8')
        s1_4 = f.readline().decode('utf-8').replace("\n", "")
        s1_2_re = s1_2.replace("A", "B").replace("G", "D").replace("T", "A").replace("C", "G").replace("B",
                                                                                                       "T").replace("D",
                                                                                                                    "C")[
                  ::-1]
    cmd1 = "gzip A849-34cor.fq"
    cmd2 = "gzip A849-34ins.fq"
    os.system(cmd1)
    os.system(cmd2)
    file_txt.write("{} Total numbers: {} reads\n".format(file,file_numbers))
    file_txt.write("A849-34cor.fq.gz correct amplicon numbers: {} reads\n".format(file_34cor_numbers))
    file_txt.write("A849-34cor.fq.gz with ds inserts: {} reads\n".format(file_34ins_numbers))
    cmd = "Seqkit watch -f ReadLen A849-34ins.fq.gz –O A849-34ins-len.pdf"
    os.system(cmd)
    file_txt.write("with 1 ds34 insert 230-250: {} reads\n".format(len230_250_34ins_numbers))
    file_txt.write("with 1 ds34 insert 265-285: {} reads\n".format(len265_285_34ins_numbers))
    file_txt.write("insertion A849-34cor.fq.gz with FR full length: {} reads\n".format(file_ds34gFR_numbers))

def ds39fuu_length_insertion(file):
    file_39cor = open("A849-39cor.fq", "w")
    file_39ins = open("A849-39ins.fq", "w")
    file_txt = open("A849-39.txt", "w")
    f = gzip.open(file, 'rb')
    s1_1 = f.readline().decode('utf-8')
    s1_2 = f.readline().decode('utf-8').replace("\n", "")
    s1_3 = f.readline().decode('utf-8')
    s1_4 = f.readline().decode('utf-8').replace("\n", "")
    s1_2_re = s1_2.replace("A", "B").replace("G", "D").replace("T", "A").replace("C", "G").replace("B", "T").replace(
        "D", "C")[::-1]
    seq1 = "AATGGGGGTGTGTCACCAGA"
    ds39g15 = ""
    ds39gFR = ""
    file_numbers = 0
    file_39cor_numbers = 0
    file_39ins_numbers = 0
    file_ds39gFR_numbers = 0
    len235_255_39ins_numbers = 0
    len270_290_39ins_numbers = 0
    while s1_1:
        file_numbers += 1
        if seq1 in s1_2[20:61]:
            file_39cor_numbers += 1
            file_39cor.write(s1_1 + s1_2 + "\n" + s1_3 + s1_4 + "\n")
            if ds39g15 in s1_2:
                file_39ins_numbers += 1
                file_39ins.write(s1_1 + s1_2 + "\n" + s1_3 + s1_4 + "\n")
                if 235 <= len(s1_2) <= 255:
                    len235_255_39ins_numbers += 1
                if 270 <= len(s1_2) <= 290:
                    len270_290_39ins_numbers += 1

            elif ds39g15 in s1_2_re:
                file_39ins_numbers += 1
                file_39ins.write(s1_1 + s1_2_re + "\n" + s1_3 + s1_4[::-1] + "\n")
                if 235 <= len(s1_2_re) <= 255:
                    len235_255_39ins_numbers += 1
                if 275 <= len(s1_2_re) <= 290:
                    len270_290_39ins_numbers += 1
            if ds39gFR in s1_2 or s1_2_re:
                file_ds39gFR_numbers += 1
        s1_1 = f.readline().decode('utf-8')
        s1_2 = f.readline().decode('utf-8').replace("\n", "")
        s1_3 = f.readline().decode('utf-8')
        s1_4 = f.readline().decode('utf-8').replace("\n", "")
        s1_2_re = s1_2.replace("A", "B").replace("G", "D").replace("T", "A").replace("C", "G").replace("B",
                                                                                                       "T").replace("D",
                                                                                                                    "C")[
                  ::-1]
    file_txt.write("{} Total numbers: {} reads\n".format(file,file_numbers))
    file_txt.write("A849-39cor.fq.gz correct amplicon numbers: {} reads\n".format(file_39cor_numbers))
    file_txt.write("A849-39cor.fq.gz with ds inserts: {} reads\n".format(file_39ins_numbers))
    cmd = "Seqkit watch -f ReadLen A849-39ins.fq.gz –O A849-39ins-len.pdf"
    os.system(cmd)
    file_txt.write("with 1 ds39 insert 235-255: {} reads\n".format(len235_255_39ins_numbers))
    file_txt.write("with 1 ds39 insert 270-290: {} reads\n".format(len270_290_39ins_numbers))
    file_txt.write("insertion A849-39cor.fq.gz with FR full length: {} reads\n".format(file_ds39gFR_numbers))