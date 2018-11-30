from typing import Dict

from utils.csv_reader import read_csv

data = 'data'
test_light_curves_filename = f'{data}/test_set.csv'
test_metadata_filename = f'{data}/test_set_metadata.csv'
split_folder = f'{data}/parts'

NB_PARTS = 10

if __name__ == '__main__':

    def create_part_file(index: int, prefix: str, header: str):
        output_csv_file = open(f'{split_folder}/{prefix}_{index}.csv', 'w+')
        output_csv_file.write(header)
        return output_csv_file

    def reader(file):
        return open(file.name)

    def get_id(line: str, sep: str = ',') -> int:
        return int(line[0:line.index(sep)])

    def split_meta():
        nb_lines = sum(1 for _line in open(test_metadata_filename)) - 1  # remove header
        part_size = nb_lines / NB_PARTS

        meta_file = open(test_metadata_filename)
        meta_header = meta_file.readline()

        split_dict = {}

        def write_line(line: str, batch_id, file_writer):
            if len(line) != 0:
                star_id = get_id(line)
                split_dict[star_id] = batch_id
                file_writer.write(line)

        for i in range(NB_PARTS - 1):
            part_file = create_part_file(i, 'meta', meta_header)
            j = 0
            while j < part_size:
                write_line(meta_file.readline(), i, part_file)
                j += 1

        last_part_file = create_part_file(NB_PARTS - 1, 'meta', meta_header)
        for line in meta_file:
            write_line(line, NB_PARTS - 1, last_part_file)
        return split_dict

    def split_light_curves(split_dict: Dict[int, int]):
        light_curves_file = open(test_light_curves_filename)
        header = light_curves_file.readline()

        parts_file = [create_part_file(i, 'light_curves', header) for i in range(NB_PARTS)]
        nb_line = 0
        for line in light_curves_file:
            start_id = get_id(line)
            batch_id = split_dict[start_id]
            parts_file[batch_id].write(line)
            if nb_line % 10000000 == 9999999:
                print(f'{(nb_line + 1) / 1000000}M / ~460M')
            nb_line += 1

    split_dict = split_meta()
    split_light_curves(split_dict)
