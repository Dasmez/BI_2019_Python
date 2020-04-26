import argparse


def gc_content(self):
    count = 0
    for i in self.sequence:
        if i == 'G' or i == 'C':
            count = count + 1
    return (count * 100 / len(self.sequence))


parser = argparse.ArgumentParser(description="I'll parse your fastq")

parser.add_argument('--min_length', type=int, default=1,
                    help='non zero length')
parser.add_argument('--keep_filtered', action='store_true',
                    help='stores failed reads')
parser.add_argument('--gc_bounds', nargs='*', type=int,
                    help='no more than 2 values')
parser.add_argument('fastq')
parser.add_argument('--output_base_name', type=str,
                    help='prefix for naming files')

args = parser.parse_args()

if args.output_base_name:
    name_passed = args.output_base_name + '__passed.fastq'
    name_failed = args.output_base_name + '__failed.fastq'
else:
    name = args.fastq[:-6]
    name_passed = name + '__passed.fastq'
    name_failed = name + '__failed.fastq'

file_fastq = args.fastq
with open(file_fastq, 'r') as file:
    with open(name_passed, 'w') as ouf_passed:
        if args.keep_filtered:
            with open(name_failed, 'w') as ouf_failed:
                for line in file:
                    id = line
                    if id[0] != '@':
                        raise Exception("Something went wrong, deal with it")
                    s = file.readline()
                    sense = file.readline()
                    quality = file.readline()

                    if len(s) < args.min_length:
                        if args.keep_filtered:
                            ouf_failed.write(id)
                            ouf_failed.write(line)
                            ouf_failed.write(sense)
                            ouf_failed.write(quality)
                        continue

                    if args.gc_bounds:
                        values_list = args.gc_bounds
                        if len(values_list) == 2:
                            gc_min = values_list[0]
                            gc_max = values_list[1]
                        elif len(values_list) == 1:
                            gc_min = values_list[0]
                            gc_max = 100
                        elif len(values_list) == 0:
                            gc_min = 0
                            gc_max = 100
                        else:
                            raise Exception("Read 'help' for help")

                        if gc_content(s) < gc_min or gc_content(s) > gc_max:
                            if args.keep_filtered:
                                ouf_failed.write(id)
                                ouf_failed.write(line)
                                ouf_failed.write(sense)
                                ouf_failed.write(quality)
                            continue

                        ouf_passed.write(id)
                        ouf_passed.write(line)
                        ouf_passed.write(sense)
                        ouf_passed.write(quality)
