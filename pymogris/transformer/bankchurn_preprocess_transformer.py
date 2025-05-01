from typing import Final, Optional, TypeAlias

import pandas as pd

from pymogris.transformer.transformer import Transformer
from sklearn.preprocessing import (
    OneHotEncoder, LabelEncoder,
    StandardScaler, MinMaxScaler
)

FloatScaler: TypeAlias = StandardScaler | MinMaxScaler
FloatScalerDict: TypeAlias = dict[str, FloatScaler]


class BankchurnPreprocessTransformer(Transformer):

    def __init__(
            self,
            float_scaler_dict: Optional[FloatScalerDict] = None
    ):
        self._float_scaler: Final[FloatScalerDict] = float_scaler_dict

    @staticmethod
    def _drop_redundant_cols(data: pd.DataFrame) -> pd.DataFrame:
        return data.loc[:, data.columns != "customer_id"]

    @staticmethod
    def _X_y_split(data) -> tuple[pd.DataFrame, pd.DataFrame]:
        return data.loc[:, data.columns != "churn"], data[["churn"]]

    def _apply_categ_encodings(self, X: pd.DataFrame) -> pd.DataFrame:
        ohe_country = OneHotEncoder(
            categories=[['France', 'Spain', 'Germany']])
        le_gender = LabelEncoder()

    def _apply_scaling(self):
        pass

    def transform(self, data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        data = self._drop_redundant_cols(data=data)
        X, y = self._X_y_split(data=data)

        return X, y
