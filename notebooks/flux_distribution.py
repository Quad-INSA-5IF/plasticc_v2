import colors
import models.metadata as metadata
import models.record as record
from utils import underscore as _
from utils.chart import Chart
from utils.csv_reader import read_csv

data = 'data'
light_curves_filename = f'{data}/training_set.csv'
metadata_filename = f'{data}/training_set_metadata.csv'
test_light_curves_filename = f'{data}/test_set.csv'
test_metadata_filename = f'{data}/test_set_metadata.csv'


class Statistics:
    def __init__(self, min: float, p01: float, p10: float, median: float, p90: float, p99: float, max: float):
        self.min = min
        self.p01 = p01
        self.p10 = p10
        self.median = median
        self.p90 = p90
        self.p99 = p99
        self.max = max

    def __repr__(self):
        return f'(min: {self.min}, p1: {self.p01}, p10: {self.p10}, median: {self.median}, p90: {self.p90}, p99: {self.p99}, max: {self.max})'


if __name__ == '__main__':
    meta = read_csv(metadata_filename, has_header=True, transform=metadata.from_line)
    light_curves = read_csv(light_curves_filename, has_header=True, transform=record.from_line)

    target_of = _.index_by(meta, lambda it: it.object_id)

    p99_9_flux_err = _.percentile_by(light_curves, 99.9, lambda it: it.flux_err).flux_err
    good_points, bad_points = _.partition(light_curves, lambda it: it.flux_err <= p99_9_flux_err)

    light_curves_by_class = _.group_by(good_points, lambda it: target_of[it.object_id].target)

    statistics = {}
    for target, target_records in light_curves_by_class.items():
        light_curves_by_passband = _.group_by(target_records, lambda it: it.passband)

        statistics[target] = [None for _ in range(6)]
        for passband, records in light_curves_by_passband.items():
            sorted_records = _.map(_.sort_by(records, lambda it: it.flux), lambda it: it.flux)
            min = sorted_records[0]
            max = sorted_records[len(sorted_records) - 1]
            p1 = _.percentile_by(sorted_records, 1.0, by=lambda it: it, is_sorted=True)
            p10 = _.percentile_by(sorted_records, 10.0, by=lambda it: it, is_sorted=True)
            median = _.percentile_by(sorted_records, 50.0, by=lambda it: it, is_sorted=True)
            p90 = _.percentile_by(sorted_records, 90.0, by=lambda it: it, is_sorted=True)
            p99 = _.percentile_by(sorted_records, 99.0, by=lambda it: it, is_sorted=True)

            statistics[target][passband] = Statistics(min, p1, p10, median, p90, p99, max)

    chart = Chart()
    passband_axis = [i for i in range(6)]
    for target, stats in statistics.items():
        chart.line(
            x=passband_axis,
            y=_.map(stats, lambda it: it.min),
            color=colors.category_15[target],
            label=f'class_{target}: min or max',
            style='--'
        )

        chart.line(
            x=passband_axis,
            y=_.map(stats, lambda it: it.p01),
            color=colors.category_15[target],
            label=f'class_{target}: p01 - p99',
            style='-.'
        )

        chart.line(
            x=passband_axis,
            y=_.map(stats, lambda it: it.p10),
            color=colors.category_15[target],
            label=f'class_{target}: p10 - p90'
        )


        chart.line(
            x=passband_axis,
            y=_.map(stats, lambda it: it.p90),
            color=colors.category_15[target]
        )

        chart.line(
            x=passband_axis,
            y=_.map(stats, lambda it: it.p99),
            color=colors.category_15[target],
            style='-.'
        )

        chart.line(
            x=passband_axis,
            y=_.map(stats, lambda it: it.max),
            color=colors.category_15[target],
            style='--'
        )

    chart.save('graphics/light_curves_distribution_train.png')