from abc import abstractmethod, ABCMeta
from math import log2, sqrt
from typing import TypeVar, Generic, List, Dict

from utils import underscore as _

from machine_learning.decision_tree.properties import Property

Type = TypeVar('Type')
Label = TypeVar('Label')


class DecisionTreeMetric(Generic[Type, Label]):
    __metaclass__ = ABCMeta # Indicates that the class is abstract Oye Oye python!

    @abstractmethod
    def invoke(
            self,
            full_data: List[Type],
            split_data: List[Type],
            label: Property[Type, Label]
    ) -> float:
        return 0.0

    def empirical_probability(
            self,
            split_data: List[Type],
            label: Property[Type, Label],
            positive_label: Label,
            negative_label: Label
    ) -> float:
        return _.count(split_data, lambda data: label.of(data) == positive_label) / float(len(split_data))

    def get_labels(
            self,
            split_data: List[Type],
            label: Property[Type, Label]
    ) -> List[Label]:
        return _.distinct(_.map(split_data, lambda it: label.of(it)))


class Gini(DecisionTreeMetric):
    def invoke(
            self,
            full_data: List[Type],
            split_data: List[Type],
            label: Property[Type, Label]
    ) -> float:
        labels = self.get_labels(split_data, label)
        if len(labels) == 1:
            return 0.0
        else:
            p = self.empirical_probability(split_data, label, labels[0], labels[1])
            return 2.0 * p * (1 - p)


class Entropy(DecisionTreeMetric):
    def invoke(
            self,
            full_data: List[Type],
            split_data: List[Type],
            label: Property[Type, Label]
    ) -> float:
        labels = self.get_labels(split_data, label)
        if len(labels) == 1:
            return 0.0
        else:
            p = self.empirical_probability(split_data, label, labels[0], labels[1])
            return -1.0 * p * log2(p) - ((1.0 - p) * log2(1.0 - p))


class SubsetDistinctness(DecisionTreeMetric):
    def invoke(
            self,
            full_data: List[Type],
            split_data: List[Type],
            label: Property[Type, Label]
    ) -> float:
        left_labels = _.count_by(full_data, lambda it: label.of(it))
        right_labels = _.count_by(full_data, lambda it: not label.of(it))
        return self.cos(left_labels, right_labels)

    def cos(self, sparse_vec_a: Dict[Type, int], sparse_vec_b: Dict[Type, int]) -> float:
        keys = sparse_vec_a.keys() if len(sparse_vec_a) < len(sparse_vec_b) else sparse_vec_b.keys()

        sum = 0.0
        norm_a = _.sum_double_by(sparse_vec_a.values(), lambda x: x * x)
        norm_b = _.sum_double_by(sparse_vec_b.values(), lambda x: x * x)
        for key in keys:
            a = sparse_vec_a[key] if key in sparse_vec_a else 0
            b = sparse_vec_b[key] if key in sparse_vec_b else 0
            sum += a * b

        return sum / (sqrt(norm_a) * sqrt(norm_b))