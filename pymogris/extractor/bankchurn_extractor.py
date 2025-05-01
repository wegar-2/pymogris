import pandas as pd
from moddata import load_data

from pymogris.extractor.extractor import Extractor


class BankchurnExtractor(Extractor):

    def extract(self) -> pd.DataFrame:
        return load_data(dataset="bankchurn")
