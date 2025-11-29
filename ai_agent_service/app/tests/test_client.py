import grpc
from app.proto import summarizer_pb2, summarizer_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = summarizer_pb2_grpc.SummarizerServiceStub(channel)

    request = summarizer_pb2.SummarizerRequest(
        text="Hello world! This is a test for gRPC."
    )

    response = stub.Summarize(request)
    print("Summary:", response.summary)


if __name__ == "__main__":
    run()
