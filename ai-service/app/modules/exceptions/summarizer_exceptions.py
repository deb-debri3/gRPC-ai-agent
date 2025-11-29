from ...config.exception_config import DomainException
from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
)


class ErrorSummarizing(DomainException):
    """
    Raised when some error occur while summarzing
    """

    def __init__(
        self,
        status_code: int = HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str = "Error while summarzing the contents",
    ):
        super().__init__(status_code=status_code, detail=detail)
