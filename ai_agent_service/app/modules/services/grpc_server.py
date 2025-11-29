from concurrent import futures  # it let gRPC server run on multiple request in parallel
import grpc

from app.proto import summarizer_pb2, summarizer_pb2_grpc
from app.modules.services.summarizer_service import (
    generate_summary,
)


class SummarizerServicer(summarizer_pb2_grpc.SummarizerServiceServicer):
    def Summarize(self, request, context):
        summary = generate_summary(request.text)
        return summarizer_pb2.SummarizeResponse(summary=summary)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    summarizer_pb2_grpc.add_SummarizerServiceServicer_to_server(
        SummarizerServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    print("gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
