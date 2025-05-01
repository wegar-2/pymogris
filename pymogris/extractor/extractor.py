from typing import Protocol

import pandas as pd


class Extractor(Protocol):

    def extract(self) -> pd.DataFrame:
        pass
    