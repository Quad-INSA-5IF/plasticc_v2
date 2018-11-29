import colors
import models.metadata as metadata
import models.record as record
from utils import underscore as _
from utils.chart import Chart
from utils.csv_reader import read_csv

data = 'data'
light_curves_filename = f'{data}/training_set.csv'
metadata_filename = f'{data}/training_set_metadata.csv'

if __name__ == '__main__':
    meta = read_csv(metadata_filename, has_header=True, transform=metadata.from_line)
    light_curves = read_csv(light_curves_filename, has_header=True, transform=record.from_line)

    p99_flux_err = _.percentile_by(light_curves, 99.9, lambda it: it.flux_err).flux_err
    good_points, bad_points = _.partition(light_curves, lambda it: it.flux_err <= p99_flux_err)

    print(f'good values: {len(good_points)}')
    print(f'bad values {len(bad_points)}')

    chart = Chart(
        title='Good and bad measures',
        x_label='MJD',
        y_label='Brightness'
    )
    chart.scatter_data(
        good_points,
        lambda it: it.mjd,
        lambda it: it.flux,
        label='good measures',
        color=colors.blue,
        alpha=.5
    )
    chart.scatter_data(
        bad_points,
        lambda it: it.mjd,
        lambda it: it.flux,
        label='bad measures',
        color=colors.pink,
        alpha=.2
    )
    chart.show()
