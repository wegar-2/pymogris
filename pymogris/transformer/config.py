from typing import Type, TypeAlias

from pydantic import BaseModel, ConfigDict
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    HistGradientBoostingClassifier, GradientBoostingRegressor
)

ModelType: TypeAlias = (
        Type[DecisionTreeRegressor] |
        Type[HistGradientBoostingClassifier] |
        Type[GradientBoostingRegressor]
)

class SklearnModelGridSearchTransformerConfig(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    model_type: ModelType
    hyperparams: dict
