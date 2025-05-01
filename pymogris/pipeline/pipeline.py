from typing import Protocol, Any


class Pipeline(Protocol):

    def run(self) -> Any:
        pass
    