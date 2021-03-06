# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class VpnClientRevokedCertificate(SubResource):
    """VPN client revoked certificate of virtual network gateway.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Id
    :type id: str
    :param thumbprint: Gets or sets the revoked Vpn client certificate
     thumbprint
    :type thumbprint: str
    :ivar provisioning_state: Gets provisioning state of the VPN client
     revoked certificate resource Updating/Deleting/Failed
    :vartype provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, thumbprint=None, name=None, etag=None):
        super(VpnClientRevokedCertificate, self).__init__(id=id)
        self.thumbprint = thumbprint
        self.provisioning_state = None
        self.name = name
        self.etag = etag
