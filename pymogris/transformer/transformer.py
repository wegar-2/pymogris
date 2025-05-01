from typing import Protocol, Any


class Transformer(Protocol):

    def transform(self, data: Any) -> Any:
        pass
