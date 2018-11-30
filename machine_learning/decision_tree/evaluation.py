from typing import TypeVar, Generic, List

import utils.underscore as _
from machine_learning.decision_tree.decision_tree import ComputedDecisionTree
from machine_learning.decision_tree.properties import Property
# from utils import colors
# from utils.chart import Chart

T = TypeVar('T')
Type = TypeVar('Type')
Label = TypeVar('Label')


class PredictedVsExpectedScore(Generic[T]):
    def __init__(self, predicted: T, expected: T):
        self.predicted = predicted
        self.expected = expected

    def is_valid(self) -> bool:
        return self.predicted == self.expected

    def __eq__(self, other):
        if type(other) is not PredictedVsExpectedScore:
            return False
        else:
            return self.predicted == other.predicted and self.expected == other.expected

    def __hash__(self):
        return hash((self.predicted, self.expected))


def evaluate(
        model: ComputedDecisionTree[Type, Label],
        test_set: List[Type],
        label: Property[Type, Label],
        show_chart: bool = True
):

    def is_well_classified(element: Type) -> bool:
        return model.classify(element) == label.of(element)

    def get_label(element: Type) -> Label:
        return label.of(element)

    def get_prediction_and_expected(element: Type) -> PredictedVsExpectedScore[Type]:
        return PredictedVsExpectedScore(model.classify(element), label.of(element))

    accuracy = _.count(test_set, is_well_classified) / float(len(test_set))
    print(f'Accuracy: {accuracy}')

    """
    if show_chart:
        count_by_label = _.count_by(test_set, get_label)
        data = _.count_by(
            _.map(
                test_set,
                get_prediction_and_expected
            )
        ).items()

        chart = Chart(
            title="Predicted vs Target",
            x_label="Target",
            y_label="Predicted",
            width=1080,
            height=1080
        )
        chart.scatter_data(
            data=data,
            x=lambda it: it[0].expected,
            y=lambda it: it[0].predicted,
            size=lambda it: 5000.0 * it[1] / float(count_by_label[it[0].expected]),
            color=lambda it: colors.blue if it[0].is_valid() else colors.pink,
            marker='.'
        )
        chart.show()
    """