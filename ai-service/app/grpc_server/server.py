import grpc
from concurrent import futures
import asyncio

from .calculator.calculator_servicer import CalculatorServicer
from .summarizer.summarizer_servicer import SummarizerServicer
from ..proto import calculator_pb2_grpc, ai_agent_pb2_grpc


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))

    calculator_pb2_grpc.add_CalculationServicer_to_server(CalculatorServicer(), server)
    ai_agent_pb2_grpc.add_SummarizerServicer_to_server(SummarizerServicer(), server)

    server.add_insecure_port("[::]:50051")
    print("Central gRPC server running on port 50051")

    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
