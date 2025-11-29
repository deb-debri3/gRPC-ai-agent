class CalculatorServices:
    """
    Service class for demo calculation
    """

    async def calculate(self, a: int, b: int, operation: str = "add") -> float:
        """
        a helper method to calculate numbers
        # NOTE: made specially to test protobuf config arguments

        - performs a simple mathematical operation
        """
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case _:
                raise ValueError(f"Unknown operation: {operation}")


def get_calculater_service() -> CalculatorServices:
    """
    Returns a new instance of CalculatorServices.
    """
    return CalculatorServices()
