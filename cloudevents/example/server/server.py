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
"""The Python implementation of the GRPC helloworld.Greeter server."""

import uuid

from cloudevents.example import service_pb2_grpc
from cloudevents.v1 import cloudevents_pb2


class Greeter(service_pb2_grpc.GreeterServicer):

    def hello(self, request, context):
        event_id = str(uuid.uuid4())
        return cloudevents_pb2.CloudEvent(
            id=event_id,
            source="io.cloudevents.example.server",
            type="io.cloudevents.example.server.ResponseGenerated",
            spec_version="1.0.0",
            text_data="pong",
        )

