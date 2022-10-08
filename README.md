gRPC + CloudEvents Python Server
--------------

How to regenerate protos:

```bash
pip install -r requirements.txt

python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/io/cloudevents/example/service.proto
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/io/cloudevents/v1/cloudevents.proto
```

When the protos are created, please move them manually out of the `io` folder while this
messes up a lot with Python standard `io` library.
