#  Copyright 2022 Yurii Serhiichuk
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import logging
from concurrent import futures

import grpc

from cloudevents.example import service_pb2_grpc, server


def serve():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreeterServicer_to_server(server.Greeter(), grpc_server)
    grpc_server.add_insecure_port('127.0.0.1:52051')
    grpc_server.start()
    grpc_server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
