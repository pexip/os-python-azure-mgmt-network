# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExpressRouteCircuitStats(Model):
    """
    Contains Stats associated with the peering

    :param int bytes_in: Gets BytesIn of the peering.
    :param int bytes_out: Gets BytesOut of the peering.
    """ 

    _attribute_map = {
        'bytes_in': {'key': 'bytesIn', 'type': 'int'},
        'bytes_out': {'key': 'bytesOut', 'type': 'int'},
    }

    def __init__(self, bytes_in=None, bytes_out=None, **kwargs):
        self.bytes_in = bytes_in
        self.bytes_out = bytes_out
