from typing import Any, Final

import pandas as pd

from pymogris.transformer.transformer import Transformer
from pymogris.transformer.config import SklearnModelGridSearchTransformerConfig


class SklearnModelGridSearchTransformer(Transformer):

    def __init__(self, config: SklearnModelGridSearchTransformerConfig):
        self._config: Final[SklearnModelGridSearchTransformerConfig] = config

    def transform(
            self,
            data: tuple[pd.DataFrame, pd.DataFrame]
    ) -> Any:
        X, y = data

        return None
