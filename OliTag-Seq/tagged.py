# -*- coding:utf-8 -*-
# @Time    :2023/3/23 18:14
# @Author  :ZZK
# @ File   :NewGS_GS2.py
# Description:
import os
import gzip
import yaml
import datetime
import subprocess


def dep(file1, file2, config):
    outfiles_r1 = {}
    outfiles_r2 = {}

    samples_name = {}
    out_dir = config['output_folder']
    for sample, value in config["samples"].items():
        samples_name["{}".format(config["samples"]["{}".format(sample)]["barcode1"])] = sample
        outfiles_r1[sample] = open(os.path.join(out_dir, '%s.r1.tempumitagged.fastq' % sample), 'a')
        outfiles_r2[sample] = open(os.path.join(out_dir, '%s.r2.tempumitagged.fastq' % sample), 'a')

    linker = "CTCCCTCGCC"
    for file31, file32 in zip(file1, file2):
        f31 = gzip.open(file31, 'rb')
        f32 = gzip.open(file32, 'rb')
        s1_1 = f31.readline().decode('utf-8')
        s1_2 = f31.readline().decode('utf-8')
        s1_3 = f31.readline().decode('utf-8')
        s1_4 = f31.readline().decode('utf-8')

        s2_1 = f32.readline().decode('utf-8')
        s2_2 = f32.readline().decode('utf-8')
        s2_3 = f32.readline().decode('utf-8')
        s2_4 = f32.readline().decode('utf-8')

        while s1_1:
            if linker in s1_2[34:49] and s1_2[:8] in samples_name.keys():
                outfiles_r1['{}'.format(samples_name["{}".format(s1_2[:8])])].write(
                    s1_1.replace("\n", " ") + s1_2[26:34] + "_" + s1_2[46:52] + "_" + s2_2[:6] + "\n" + s1_2[
                                                                                                        46:] + s1_3 + s1_4[
                                                                                                                      46:])
                outfiles_r2['{}'.format(samples_name["{}".format(s1_2[:8])])].write(
                    s2_1.replace("\n", " ") + s1_2[26:34] + "_" + s1_2[46:52] + "_" + s2_2[
                                                                                      :6] + "\n" + s2_2 + s2_3 + s2_4)
            elif linker not in s1_2[34:49] and linker in s2_2[34:49] and s2_2[:8] in samples_name.keys():

                outfiles_r1['{}'.format(samples_name["{}".format(s2_2[:8])])].write(
                    s2_1.replace("\n", " ") + s2_2[26:34] + "_" + s2_2[46:52] + "_" + s1_2[:6] + "\n" + s2_2[
                                                                                                        46:] + s2_3 + s2_4[
                                                                                                                      46:])
                outfiles_r2['{}'.format(samples_name["{}".format(s2_2[:8])])].write(
                    s1_1.replace("\n", " ") + s2_2[26:34] + "_" + s2_2[46:52] + "_" + s1_2[
                                                                                      :6] + "\n" + s1_2 + s1_3 + s1_4)
            s1_1 = f31.readline().decode('utf-8')
            s1_2 = f31.readline().decode('utf-8')
            s1_3 = f31.readline().decode('utf-8')
            s1_4 = f31.readline().decode('utf-8')

            s2_1 = f32.readline().decode('utf-8')
            s2_2 = f32.readline().decode('utf-8')
            s2_3 = f32.readline().decode('utf-8')
            s2_4 = f32.readline().decode('utf-8')

        f31.close()
        f32.close()
    for sample, value in config["samples"].items():
        samples_name["{}".format(config["samples"]["{}".format(sample)]["barcode1"])] = sample
        outfiles_r1[sample].close()
        outfiles_r2[sample].close()

    for sample, value in config["samples"].items():
        r1_umitagged_unsorted_file = os.path.join(out_dir, '%s.r1.tempumitagged.fastq' % sample)
        r2_umitagged_unsorted_file = os.path.join(out_dir, '%s.r2.tempumitagged.fastq' % sample)
        read1_out = os.path.join(out_dir, '%s.r1.umitagged.fastq' % sample)
        read2_out = os.path.join(out_dir, '%s.r2.umitagged.fastq' % sample)
        cmd = 'cat ' + r1_umitagged_unsorted_file + ' | paste - - - - | sort -k3,3 -k1,1 | tr "\t" "\n" >' + read1_out
        subprocess.check_call(cmd, shell=True, env=os.environ.copy())
        cmd = 'cat ' + r2_umitagged_unsorted_file + ' | paste - - - - | sort -k3,3 -k1,1 | tr "\t" "\n" >' + read2_out
        subprocess.check_call(cmd, shell=True, env=os.environ.copy())
        os.remove(r1_umitagged_unsorted_file)
        os.remove(r2_umitagged_unsorted_file)


def main(config):  # manifest_data
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    file_1 = config['data1']
    file_2 = config['data2']
    dep(file_1, file_2, config)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
