from ...modules.services import CalculatorServices
from ...proto import calculator_pb2_grpc, calculator_pb2


class CalculatorServicer(calculator_pb2_grpc.CalculationServicer):
    async def Calculate(self, request, context):
        result = await CalculatorServices().calculate(
            request.a, request.b, request.operation
        )
        return calculator_pb2.CalculationResponse(c=result)
