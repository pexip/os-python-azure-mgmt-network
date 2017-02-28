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


class VirtualNetworkGatewayIPConfiguration(SubResource):
    """IpConfiguration for Virtual network gateway.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Id
    :type id: str
    :param private_ip_allocation_method: Gets or sets PrivateIP allocation
     method. Possible values include: 'Static', 'Dynamic'
    :type private_ip_allocation_method: str or :class:`IPAllocationMethod
     <azure.mgmt.network.models.IPAllocationMethod>`
    :param subnet: Gets or sets the reference of the subnet resource
    :type subnet: :class:`SubResource <azure.mgmt.network.models.SubResource>`
    :param public_ip_address: Gets or sets the reference of the PublicIP
     resource
    :type public_ip_address: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :ivar provisioning_state: Gets provisioning state of the PublicIP
     resource Updating/Deleting/Failed
    :vartype provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _validation = {
        'subnet': {'required': True},
        'public_ip_address': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'SubResource'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, subnet, public_ip_address, id=None, private_ip_allocation_method=None, name=None, etag=None):
        super(VirtualNetworkGatewayIPConfiguration, self).__init__(id=id)
        self.private_ip_allocation_method = private_ip_allocation_method
        self.subnet = subnet
        self.public_ip_address = public_ip_address
        self.provisioning_state = None
        self.name = name
        self.etag = etag
