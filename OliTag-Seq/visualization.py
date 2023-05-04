# -*- coding:utf-8 -*-
# @Time    :2023/3/24 09:50
# @Author  :ZZK
# @ File   :
# Description:

import svgwrite
import sys
import os

boxWidth = 10
box_size = 15
v_spacing = 3

colors = {'G': '#F5F500', 'A': '#FF5454', 'T': '#00D118', 'C': '#26A8FF', 'N': '#B3B3B3', 'R': '#B3B3B3'}


def parseSitesFile(infile):
    offtargets = []
    with open(infile, 'r') as f:
        f.readline()
        for line in f:
            line_items = line.split('\t')
            offtarget_sequence = line_items[21]
            offtarget_reads = line_items[11]
            ref_seq_ = line_items[32]
            if offtarget_sequence != '':
                offtargets.append({'seq': offtarget_sequence.strip(),
                                   'reads': int(offtarget_reads.strip())})
    offtargets = sorted(offtargets, key=lambda x: x['reads'], reverse=True)
    return offtargets, ref_seq_


def visualizeOfftargets(infile, outfile, title=None):
    '''
    :param infile:  identified.txt
    :param outfile:
    :param title:
    :return:
    '''

    output_folder = os.path.dirname(outfile)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get offtargets array from file
    offtargets, ref_seq = parseSitesFile(infile)



    # Initiate canvas
    dwg = svgwrite.Drawing(outfile + '.svg', profile='full')

    if title is not None:
        # Define top and left margins
        x_offset = 20
        y_offset = 50
        #dwg.add(dwg.text(title.strip('_identifiedOfftargets'), insert=(x_offset, 30), style="font-size:20px; font-family:Arial"))
        dwg.add(dwg.text(title, insert=(x_offset, 30), style="font-size:20px; font-family:Arial"))
    else:
        # Define top and left margins
        x_offset = 20
        y_offset = 20

    # Draw ticks
    tick_locations = [1, len(ref_seq)]
    tick_locations += range(len(ref_seq) + 1)[::10][1:]
    for x in tick_locations:
        dwg.add(dwg.text(str(x), insert=(x_offset + (x - 1) * box_size + 2, y_offset - 2), style="font-size:10px; font-family:Arial"))

    # Draw reference sequence row
    for i, c in enumerate(ref_seq):
        y = y_offset
        x = x_offset + i * box_size
        dwg.add(dwg.rect((x, y), (box_size, box_size), fill=colors[c]))
        dwg.add(dwg.text(c, insert=(x + 3, y + box_size - 3), fill='black', style="font-size:15px; font-family:Arial"))

    dwg.add(dwg.text('Reads', insert=(x_offset + box_size * len(ref_seq) + 16, y_offset + box_size - 3), style="font-size:15px; font-family:Arial"))

    # Draw aligned sequence rows
    y_offset += 10  # leave some extra space after the reference row
    for j, seq in enumerate(offtargets):
        y = y_offset + j * box_size
        for i, c in enumerate(seq['seq']):
            x = x_offset + i * box_size
            if c == ref_seq[i]: #or ref_seq[i] == 'N':
                dwg.add(dwg.text(u"\u2022", insert=(x + 4.5, 2 * box_size + y - 4), fill='black', style="font-size:10px; font-family:Arial"))
            else:
                dwg.add(dwg.rect((x, box_size + y), (box_size, box_size), fill=colors[c]))
                dwg.add(dwg.text(c, insert=(x + 3, 2 * box_size + y - 3), fill='black', style="font-size:15px; font-family:Arial"))

        reads_text = dwg.text(str(seq['reads']), insert=(box_size * (len(ref_seq) + 1) + 20, y_offset + box_size * (j + 2) - 2), fill='black', style="font-size:15px; font-family:Arial")
        dwg.add(reads_text)

    dwg.save()

    f = open(outfile + '.txt', 'wb')
    f.write(ref_seq)
    f.write('\t')
    f.write('reads')
    f.write('\n')
    for value in offtargets:
        f.write(value['seq'])
        f.write('\t')
        f.write(str(value['reads']))
        f.write('\n')
    f.close()


def main():
    if len(sys.argv) >= 3:
        if len(sys.argv) == 4:
            title = sys.argv[3]
        else:
            title = None
        visualizeOfftargets(sys.argv[1], sys.argv[2], title=title)
    else:
        print 'Usage: python visualization.py INFILE OUTFILE [TITLE]'


if __name__ == '__main__':
    main()
