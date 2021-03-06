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


class VirtualNetworkPeering(SubResource):
    """Peerings in a VirtualNework resource.

    :param id: Resource Id
    :type id: str
    :param allow_virtual_network_access: Gets or sets whether the VMs in the
     linked virtual network space would be able to access all the VMs in
     local Virtual network space
    :type allow_virtual_network_access: bool
    :param allow_forwarded_traffic: Gets or sets whether the forwarded
     traffic from the VMs in the remote virtual network will be
     allowed/disallowed
    :type allow_forwarded_traffic: bool
    :param allow_gateway_transit: Gets or sets if gatewayLinks can be used in
     remote virtual network’s link to this virtual network
    :type allow_gateway_transit: bool
    :param use_remote_gateways: Gets or sets if remote gateways can be used
     on this virtual network. If the flag is set to true, and
     allowGatewayTransit on remote peering is also true, virtual network will
     use gateways of remote virtual network for transit. Only 1 peering can
     have this flag set to true. This flag cannot be set if virtual network
     already has a gateway.
    :type use_remote_gateways: bool
    :param remote_virtual_network: Gets or sets the reference of the remote
     virtual network
    :type remote_virtual_network: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param peering_state: Gets the status of the virtual network peering.
     Possible values include: 'Initiated', 'Connected', 'Disconnected'
    :type peering_state: str or :class:`VirtualNetworkPeeringState
     <azure.mgmt.network.models.VirtualNetworkPeeringState>`
    :param provisioning_state: Gets provisioning state of the resource
    :type provisioning_state: str
    :param name: Gets or sets the name of the resource that is unique within
     a resource group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'allow_virtual_network_access': {'key': 'properties.allowVirtualNetworkAccess', 'type': 'bool'},
        'allow_forwarded_traffic': {'key': 'properties.allowForwardedTraffic', 'type': 'bool'},
        'allow_gateway_transit': {'key': 'properties.allowGatewayTransit', 'type': 'bool'},
        'use_remote_gateways': {'key': 'properties.useRemoteGateways', 'type': 'bool'},
        'remote_virtual_network': {'key': 'properties.remoteVirtualNetwork', 'type': 'SubResource'},
        'peering_state': {'key': 'properties.peeringState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, allow_virtual_network_access=None, allow_forwarded_traffic=None, allow_gateway_transit=None, use_remote_gateways=None, remote_virtual_network=None, peering_state=None, provisioning_state=None, name=None, etag=None):
        super(VirtualNetworkPeering, self).__init__(id=id)
        self.allow_virtual_network_access = allow_virtual_network_access
        self.allow_forwarded_traffic = allow_forwarded_traffic
        self.allow_gateway_transit = allow_gateway_transit
        self.use_remote_gateways = use_remote_gateways
        self.remote_virtual_network = remote_virtual_network
        self.peering_state = peering_state
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
