# -*- coding: utf-8 -*-
import os
import sys
import yaml
import argparse
import traceback
import subprocess

import log

logger = log.createCustomLogger('root')

from alignReads import alignReads
from visualization import visualizeOfftargets
import identifyOfftargetSites
import tagged


class OliTagSeq:

    def __init__(self):
        pass

    def parseManifest(self, manifest_path):
        logger.info('Loading manifest...')
        self.manifest_data = yaml.safe_load(open(manifest_path, 'r'))
        try:
            self.BWA_path = self.manifest_data['bwa']
            self.bedtools = self.manifest_data['bedtools']
            self.reference_genome = self.manifest_data['reference_genome']
            self.output_folder = self.manifest_data['output_folder']
            self.samples = self.manifest_data['samples']
            self.data1 = self.manifest_data['data1']
            self.data2 = self.manifest_data['data2']

        except Exception as e:
            logger.error(
                'Incorrect or malformed manifest file. Please ensure your manifest contains all required fields.')
            sys.exit()

        # Make sure the user has a sample
        if len(self.samples) < 1:
            raise AssertionError('Your manifest must have at least one sample.')

        logger.info('Successfully loaded manifest.')

    def dataTagged(self):
        logger.info('Tagged reads...')
        try:
            tagged.main(self.manifest_data)
            logger.info('Finished tagging reads.')

        except Exception as e:
            logger.error('Error aligning')
            logger.error(traceback.format_exc())
            quit()

    def alignReads(self):
        logger.info('Aligning reads...')

        try:
            self.aligned = {}
            for sample in self.samples:
                sample_alignment_path = os.path.join(self.output_folder, 'aligned', sample + '.sam')

                consolidated1 = os.path.join(self.output_folder, 'consolidated',
                                             sample + '.r1.consolidated.fastq')
                consolidated2 = os.path.join(self.output_folder, 'consolidated',
                                             sample + '.r2.consolidated.fastq')
                alignReads(self.BWA_path,
                           self.reference_genome,
                           consolidated1,
                           consolidated2,
                           sample_alignment_path)
                self.aligned[sample] = sample_alignment_path
                logger.info('Finished aligning reads to genome.')

        except Exception as e:
            logger.error('Error aligning')
            logger.error(traceback.format_exc())
            quit()

    def identifyOfftargetSites(self):
        logger.info('Identifying offtarget sites...')

        try:
            self.identified = {}
            for sample in self.samples:
                sample_data = self.samples[sample]
                annotations = {}
                annotations['Description'] = sample_data['description']
                annotations['Targetsite'] = sample

                annotations['Sequence'] = sample_data['target']

                samfile = self.aligned[sample]

                self.identified[sample] = os.path.join(self.output_folder, 'identified',
                                                       sample + '_identifiedOfftargets.txt')

                identifyOfftargetSites.analyze(samfile, self.reference_genome, self.identified[sample], annotations)

            logger.info('Finished identifying offtarget sites.')

        except Exception as e:
            logger.error('Error identifying offtarget sites.')
            logger.error(traceback.format_exc())
            quit()


    def visualize(self):
        logger.info('Visualizing off-target sites')
        try:
            for sample in self.samples:
                if sample != 'control':
                    infile = self.identified[sample]
                    outfile = os.path.join(self.output_folder, 'visualization', sample + '_offtargets')
                    visualizeOfftargets(infile, outfile, title=sample)

            logger.info('Finished visualizing off-target sites')

        except Exception as e:
            logger.error('Error visualizing off-target sites.')
            logger.error(traceback.format_exc())


def parse_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(description='Individual Step Commands',
                                       help='Use this to run individual steps of the pipeline',
                                       dest='command')

    all_parser = subparsers.add_parser('all', help='Run all steps of the pipeline')
    all_parser.add_argument('--manifest', '-m', help='Specify the manifest Path', required=True)
    all_parser.add_argument('--identifyAndFilter', action='store_true', default=False)

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == 'all':
        g = OliTagSeq()
        g.parseManifest(args.manifest)
        g.dataTagged()
        g.alignReads()
        g.identifyOfftargetSites()
        g.visualize()
    else:
        logger.error('Program parameter error.')


if __name__ == '__main__':
    main()
