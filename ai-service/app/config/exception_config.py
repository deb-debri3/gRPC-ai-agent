from starlette.status import HTTP_400_BAD_REQUEST


class DomainException(Exception):
    """
    Base domain exception for services
    """

    def __init__(self, detail: str, status_code: int = HTTP_400_BAD_REQUEST):
        super().__init__(detail)
        if status_code:
            self.status_code = status_code
        if detail:
            self.detail = detail
