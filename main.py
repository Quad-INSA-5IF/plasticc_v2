import warnings

import colors
import models.metadata as metadata
import models.record as record
from models.metadata import Metadata
from utils import underscore as _
from utils.chart import Chart
from utils.csv_reader import read_csv

warnings.simplefilter('ignore')

data = 'data'
light_curves_filename = f'{data}/training_set.csv'
metadata_filename = f'{data}/training_set_metadata.csv'
test_light_curves_filename = f'{data}/test_set.csv'
test_metadata_filename = f'{data}/test_set_metadata.csv'

P99_9_FLUX_ERR = 552.98291

PASSBAND_NAMES = ['u', 'g', 'r', 'i', 'z', 'Y']

MIN_DATE = 59580
MAX_DATE = 60674

intra_galactic = Metadata.PHOTOZ == 0.0
deep_survey = Metadata.DDF == True
low_specz = Metadata.SPECZ <= .3
med_specz = .3 < Metadata.SPECZ < 1
high_specz = Metadata.SPECZ >= 1
low_mwebv = Metadata.MWEBV < 0.7

if __name__ == '__main__':
    META = read_csv(metadata_filename, has_header=True, transform=metadata.from_line)
    LIGHT_CURVES = read_csv(light_curves_filename, has_header=True, transform=record.from_line)

    target_of = _.index_by(META, lambda it: it.object_id)

    for current_class, records_of_current_class in _.group_by(LIGHT_CURVES, lambda it: target_of[it.object_id].target).items():
        objects_of_current_class = _.group_by(
            records_of_current_class,
            lambda it: it.object_id
        )

        element_id = 0
        TAKE = 5
        for object_id, light_curves in objects_of_current_class.items():
            star = target_of[object_id]
            chart = Chart(
                title=f'object {object_id} - class[{star.kaggle_target} -> {star.target}]',
                width=1115,
                height=600,
                x_label='Date',
                y_label='Brightness'
            )

            for passband, records in _.group_by(light_curves, lambda it: it.passband).items():
                chart.scatter_data(
                    data=records,
                    x=lambda it: it.mjd,
                    y=lambda it: it.flux,
                    color=lambda it: colors.passband_colors[passband],
                    label=PASSBAND_NAMES[passband]
                )

            chart.save(f'graphics/light_curves_cls{target_of[object_id].target}_object{element_id}.png')

            if element_id >= TAKE:
                break
            else:
                element_id += 1



