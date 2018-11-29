from typing import TypeVar, Generic, Union, List

from machine_learning.decision_tree.decision_tree_metrics import DecisionTreeMetric, Gini
from machine_learning.decision_tree.properties import Feature, Property

from utils import underscore as _

Type = TypeVar('Type')
Label = TypeVar('Label')


class NodeOrLeaf(Generic[Type, Label]): pass


class Node(NodeOrLeaf[Type, Label]):
    def __init__(self, feature: Feature[Type], left_child, right_child):
        self.feature = feature
        self.left_child = left_child
        self.right_child = right_child


def new_node(
        feature: Feature[Type],
        left_child: NodeOrLeaf[Type, Label],
        right_child: NodeOrLeaf[Type, Label]
) -> NodeOrLeaf[Type, Label]:
    return Node(feature, left_child, right_child)


class Leaf(NodeOrLeaf[Type, Label]):
    def __init__(self, label):
        self.label = label


def new_leaf(
        label: Label
) -> NodeOrLeaf[Type, Label]:
    return Leaf(label)


class ComputedDecisionTree(Generic[Type, Label]):
    def __init__(self, root):
        self.root = root

    def classify(self, sample):
        node = self.root
        while type(node) is Node:
            if node.feature.accept(sample):
                node = node.left_child
            else:
                node = node.right_child
        assert type(node) is Leaf
        return node.label


class DecisionTree(Generic[Type, Label]):
    def __init__(
            self,
            metric: DecisionTreeMetric[Type, Label] = Gini(),
            homogeneity_percentage: float = 0.9,
            max_depth: Union[int, None] = 15
    ):
        self.metric = metric
        self.homogeneity_percentage = homogeneity_percentage
        self.max_depth = max_depth

    def train(
            self,
            training_data: List[Type],
            features: List[Feature[Type]],
            label: Property[Type, Label]
    ) -> ComputedDecisionTree[Type, Label]:
        return ComputedDecisionTree(self._build_tree(training_data, features, label, 1))

    def _build_tree(
            self,
            training_data: List[Type],
            features: List[Feature[Type]],
            label: Property[Type, Label],
            current_depth: int
    ) -> NodeOrLeaf[Type, Label]:
        current_node_label = self._get_label(training_data, label)
        if current_node_label is not None:
            return new_leaf(current_node_label)

        stopping_criteria_reached = len(features) == 0 or (self.max_depth is not None and current_depth >= self.max_depth)
        majority_label = self._get_majority_label(training_data, label)
        if stopping_criteria_reached:
            return new_leaf(majority_label)

        best_split = self._find_best_split_feature(training_data, features, label)
        left_subset, right_subset = best_split.split(training_data)
        new_features = _.reject(features, lambda feature: feature is best_split)

        if len(left_subset) == 0:
            left_child = new_leaf(majority_label)
        else:
            left_child = self._build_tree(left_subset, new_features, label, current_depth + 1)

        if len(right_subset) == 0:
            right_child = new_leaf(majority_label)
        else:
            right_child = self._build_tree(right_subset, new_features, label, current_depth + 1)

        return new_node(best_split, left_child, right_child)

    def _get_label(
            self,
            data: List[Type],
            label: Property[Type, Label]
    ) -> Union[Label, None]:
        label_count = _.count_by(data, lambda it: label.of(it))
        total_count = float(len(data))

        for label_value, count in label_count.items():
            if count / total_count >= self.homogeneity_percentage:
                return label_value
        return None

    def _get_majority_label(
            self,
            data: List[Type],
            label: Property[Type, Label]
    ) -> Label:
        label_count = _.count_by(data, lambda it: label.of(it))
        return _.max_by(label_count.items(), lambda it: it[1])[0]

    def _find_best_split_feature(
            self,
            data: List[Type],
            features: List[Feature[Type]],
            label: Property[Type, Label]
    ) -> Feature[Type]:
        best_feature = None
        best_impurity = None

        for feature in features:
            current_impurity = self._get_impurity(data, feature, label)
            if best_impurity is None or current_impurity < best_impurity:
                best_impurity = current_impurity
                best_feature = feature
        assert best_feature is not None
        return best_feature

    def _get_impurity(
            self,
            data: List[Type],
            feature: Feature[Type],
            label: Property[Type, Label]
    ) -> float:
        left, right = feature.split(data)
        left_score = 0.0 if len(left) == 0 else self.metric.invoke(data, left, label)
        right_score = 0.0 if len(right) == 0 else self.metric.invoke(data, right, label)
        return (left_score + right_score) / 2