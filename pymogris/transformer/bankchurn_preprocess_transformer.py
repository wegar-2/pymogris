from typing import Final, Optional, TypeAlias

import pandas as pd

from pymogris.transformer.transformer import Transformer
from sklearn.preprocessing import (
    OneHotEncoder, OrdinalEncoder,
    StandardScaler, MinMaxScaler
)
from sklearn.compose import ColumnTransformer

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
    def _X_y_split(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        return data.loc[:, data.columns != "churn"], data[["churn"]]

    def _apply_categ_encodings(
            self,
            X: pd.DataFrame # noqa
    ) -> pd.DataFrame:
        ohe_country = OneHotEncoder(
            categories=[['France', 'Spain', 'Germany']]
        )
        orde_gender = OrdinalEncoder(
            categories=[["Male", "Female"]]
        )
        ct = ColumnTransformer(
            transformers=[
                ("ohe_country", ohe_country, ["country"]),
                ("orde_gender", orde_gender, ["gender"])
            ],
            remainder="passthrough"
        )
        return ct.transform(X=X)

    def _apply_scaling(
            self,
            X: pd.DataFrame # noqa
    ) -> pd.DataFrame:
        for col in self._float_scaler:
            if col in X:
                scaler = self._float_scaler[col]
                X[col] = scaler.transform(X=X[col])
        return X

    def transform(self, data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        data = self._drop_redundant_cols(data=data)
        X, y = self._X_y_split(data=data)
        X = self._apply_categ_encodings(X=X)
        X = self._apply_scaling(X=X)
        return X, y
