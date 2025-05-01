from typing import Any, Final

from pymogris.pipeline.pipeline import Pipeline
from pymogris.pipeline.config import BankchurnPipelineConfig
from pymogris.extractor.bankchurn_extractor import BankchurnExtractor
from pymogris.transformer.bankchurn_preprocess_transformer import (
    BankchurnPreprocessTransformer)


class BankchurnPipeline(Pipeline):

    def __init__(self, config: BankchurnPipelineConfig):
        self._config: Final[BankchurnPipelineConfig] = config

    def run(self) -> Any:
        data = BankchurnExtractor().extract()
        BankchurnPreprocessTransformer().transform(data=data)
