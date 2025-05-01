from typing import Any, Final

from pymogris.pipeline.pipeline import Pipeline
from pymogris.pipeline.config import BankchurnPipelineConfig
from pymogris.extractor.bankchurn_extractor import BankchurnExtractor
from pymogris.transformer.bankchurn_preprocess_transformer import (
    BankchurnPreprocessTransformer)
from pymogris.transformer.hyperparam_opt.sklearn_model_grid_search_transformer import (
    SklearnModelGridSearchTransformer)
from pymogris.transformer.config import SklearnModelGridSearchTransformerConfig


class BankchurnPipeline(Pipeline):

    def __init__(self, config: BankchurnPipelineConfig):
        self._config: Final[BankchurnPipelineConfig] = config

    def run(self) -> Any:
        data = BankchurnExtractor().extract()
        X, y = BankchurnPreprocessTransformer().transform(data=data)
        SklearnModelGridSearchTransformer(
            config=SklearnModelGridSearchTransformerConfig(
                hyperparams=self._config.hyperparams,
                model_type=self._config.model_type
            )
        )

        return None
