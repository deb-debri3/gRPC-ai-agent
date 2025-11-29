for grpc i have installed (to generate python gRPC stubs)
pip install grpcio grpcio-tools


python -m grpc_tools.protoc \
    -I app/proto \
    --python_out=app/proto \
    --grpc_python_out=app/proto \
    app/proto/summarizer.proto


how they fit together
// summarizer.proto
//        |
//        v
// protoc compiler
//        |
//        |—> summarizer_pb2.py          (messages)
//        └—> summarizer_pb2_grpc.py     (services)
