gRPC + CloudEvents Python Server
--------------

How to regenerate protos:

```bash
pip install -r requirements.txt

python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/io/cloudevents/example/service.proto
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/io/cloudevents/v1/cloudevents.proto
```
