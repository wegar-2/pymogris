from pydantic import BaseModel, ConfigDict
from pymogris.transformer.config import ModelType


class BankchurnPipelineConfig(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    model_type: ModelType
    hyperparams: dict
