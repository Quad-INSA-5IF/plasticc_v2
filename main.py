import warnings

import models.metadata as metadata
import models.record as record
from machine_learning.decision_tree.decision_tree import DecisionTree
from machine_learning.decision_tree.decision_tree_metrics import SubsetDistinctness
from machine_learning.decision_tree.evaluation import evaluate
from machine_learning.utils import train_and_test
from models.metadata import Metadata
from utils import underscore as _
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
    LIGHT_CURVES = _.filter(
        read_csv(light_curves_filename, has_header=True, transform=record.from_line),
        lambda it: it.flux_err < P99_9_FLUX_ERR
    )

    features = [
        intra_galactic,
        deep_survey,
        low_specz,
        med_specz,
        high_specz,
        low_mwebv
    ]

    train, test = train_and_test(META, by=lambda it: Metadata.LABEL.of(it), shuffle=False)
    d_tree = DecisionTree(metric=SubsetDistinctness())
    model = d_tree.train(train, features, Metadata.LABEL)
    evaluate(model, test, Metadata.LABEL)
