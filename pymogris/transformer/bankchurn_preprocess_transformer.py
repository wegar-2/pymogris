from typing import Any

import pandas as pd

from pymogris.transformer.transformer import Transformer


class BankchurnPreprocessTransformer(Transformer):

    def transform(self, data: pd.DataFrame) -> Any:
        pass
