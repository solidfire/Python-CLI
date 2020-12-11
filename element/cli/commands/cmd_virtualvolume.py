#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from solidfire.custom.models import *
from uuid import UUID
from element import exceptions
from solidfire import common
from element.cli.cli import SolidFireOption, SolidFireCommand

class ProtectionSchemeVisibility(data_model.DataObject):
    """ProtectionSchemeVisibility  
    The public visibility of the protection scheme.

    """
    enum_values = ("customer", "testOnly", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class RemoteClusterSnapshotStatus(data_model.DataObject):
    """RemoteClusterSnapshotStatus  
    Status of the remote snapshot on the target cluster as seen on the source cluster

    """
    enum_values = ("Present", "Not Present", "Syncing", "Deleted", "Unknown", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProtectionSchemeCategory(data_model.DataObject):
    """ProtectionSchemeCategory  
    The category of the protection scheme.

    """
    enum_values = ("helix", "erasureCoded", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProtectionScheme(data_model.DataObject):
    """ProtectionScheme  
    The method of protecting data on the cluster

    """
    enum_values = ("singleHelix", "doubleHelix", "tripleHelix", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class AuthConfigType(data_model.DataObject):
    """AuthConfigType  
    This type indicates the configuration data which will be accessed or modified by the element auth container.

    """
    enum_values = ("mNode", "element", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class DriveEncryptionCapabilityType(data_model.DataObject):
    """DriveEncryptionCapabilityType  
    This specifies a drive's encryption capability.

    """
    enum_values = ("none", "sed", "fips", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class FipsDrivesStatusType(data_model.DataObject):
    """FipsDrivesStatusType  
    This specifies a node's FIPS 140-2 compliance status.

    """
    enum_values = ("None", "Partial", "Ready", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class AuthMethod(data_model.DataObject):
    """AuthMethod  
    This type qualifies a ClusterAdmin with its authentication method.

    """
    enum_values = ("Cluster", "Ldap", "Idp", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class MaintenanceMode(data_model.DataObject):
    """MaintenanceMode  
    Which mode a node is in when it is having maintenenace peformed.

    """
    enum_values = ("Disabled", "FailedToRecover", "Unexpected", "RecoveringFromMaintenance", "PreparingForMaintenance", "ReadyForMaintenance", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProposedNodeErrorCode(data_model.DataObject):
    """ProposedNodeErrorCode  
    This specifies error code for a proposed node addition.

    """
    enum_values = ("nodesNoCapacity", "nodesTooLarge", "nodesConnectFailed", "nodesQueryFailed", "nodesClusterMember", "nonFipsNodeCapable", "nonFipsDrivesCapable", "nodeTypeUnsupported", "nodeTypesHeterogeneous", "nodeTypeInvalid", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class VolumeAccess(data_model.DataObject):
    """VolumeAccess  
    Describes host access for a volume.

    """
    enum_values = ("locked", "readOnly", "readWrite", "replicationTarget", "snapMirrorTarget", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProtectionDomainType(data_model.DataObject):
    """ProtectionDomainType  
    A Protection Domain is a set of one or more components whose simultaneous failure is protected
    from causing data unavailability or loss. This specifies one of the types of Protection Domains
    recognized by this cluster.

    """
    enum_values = ("node", "chassis", "custom", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

@click.group()
@pass_context
def cli(ctx):
    """listvolumestatsby enablefeature listtasks list listbindings getfeaturestatus getcount listhosts listprotocolendpoints """

@cli.command('listvolumestatsby', short_help="""ListVolumeStatsByVirtualVolume enables you to list volume statistics for any volumes in the system that are associated with virtual volumes. Statistics are cumulative from the creation of the volume. """, cls=SolidFireCommand)
@click.option('--virtualvolumeids',
              type=str,
              required=False,
              help="""A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def listvolumestatsby(ctx,
           # Optional main parameter
           virtualvolumeids = None):
    """ListVolumeStatsByVirtualVolume enables you to list volume statistics for any volumes in the system that are associated with virtual volumes. Statistics are cumulative from the creation of the volume."""

    

    cli_utils.establish_connection(ctx)
    

    virtualvolumeids = parser.parse_array(virtualvolumeids)
    

    

    ctx.logger.info(""": """"""virtualvolumeids = """+str(virtualvolumeids)+""";"""+"")
    try:
        _ListVolumeStatsByVirtualVolumeResult = ctx.element.list_volume_stats_by_virtual_volume(virtual_volume_ids=virtualvolumeids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVolumeStatsByVirtualVolumeResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVolumeStatsByVirtualVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablefeature', short_help="""You can use EnableFeature to enable cluster features that are disabled by default. """, cls=SolidFireCommand)
@click.option('--feature',
              type=str,
              required=True,
              prompt=True,
              help="""Indicates which feature to enable. Valid values are: vvols: Enable the NetApp SolidFire VVols cluster feature. FipsDrives: Enable the NetApp SolidFire cluster FIPS 140-2 drive support. Fips: Enable FIPS 140-2 certified encryption for HTTPS communications. SnapMirror: Enable the SnapMirror replication cluster feature. """)
@pass_context
def enablefeature(ctx,
           # Mandatory main parameter
           feature):
    """You can use EnableFeature to enable cluster features that are disabled by default."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""feature = """ + str(feature)+""";"""+"")
    try:
        _EnableFeatureResult = ctx.element.enable_feature(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableFeatureResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableFeatureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listtasks', short_help="""ListVirtualVolumeTasks returns a list of virtual volume tasks in the system. """, cls=SolidFireCommand)
@click.option('--virtualvolumetaskids',
              type=str,
              required=False,
              help="""A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. """)
@pass_context
def listtasks(ctx,
           # Optional main parameter
           virtualvolumetaskids = None):
    """ListVirtualVolumeTasks returns a list of virtual volume tasks in the system."""

    

    cli_utils.establish_connection(ctx)
    

    virtualvolumetaskids = parser.parse_array(virtualvolumetaskids)
    

    

    ctx.logger.info(""": """"""virtualvolumetaskids = """+str(virtualvolumetaskids)+""";"""+"")
    try:
        _ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtualvolumetaskids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVirtualVolumeTasksResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """, cls=SolidFireCommand)
@click.option('--details',
              type=bool,
              required=False,
              help="""Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of virtual volumes to list. """)
@click.option('--recursive',
              type=bool,
              required=False,
              help="""Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. """)
@click.option('--startvirtualvolumeid',
              type=str,
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtualvolumeids',
              type=str,
              required=False,
              help="""A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def list(ctx,
           # Optional main parameter
           details = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           recursive = None,
           # Optional main parameter
           startvirtualvolumeid = None,
           # Optional main parameter
           virtualvolumeids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes,"""
    """or only list a subset."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    virtualvolumeids = parser.parse_array(virtualvolumeids)
    

    

    ctx.logger.info(""": """"""details = """+str(details)+";" + """limit = """+str(limit)+";" + """recursive = """+str(recursive)+";" + """startvirtualvolumeid = """+str(startvirtualvolumeid)+";" + """virtualvolumeids = """+str(virtualvolumeids)+""";"""+"")
    try:
        _ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=startvirtualvolumeid, virtual_volume_ids=virtualvolumeids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVirtualVolumesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listbindings', short_help="""ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints. """, cls=SolidFireCommand)
@click.option('--virtualvolumebindingids',
              type=str,
              required=False,
              help="""A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. """)
@pass_context
def listbindings(ctx,
           # Optional main parameter
           virtualvolumebindingids = None):
    """ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints."""

    

    cli_utils.establish_connection(ctx)
    

    virtualvolumebindingids = parser.parse_array(virtualvolumebindingids)
    

    

    ctx.logger.info(""": """"""virtualvolumebindingids = """+str(virtualvolumebindingids)+""";"""+"")
    try:
        _ListVirtualVolumeBindingsResult = ctx.element.list_virtual_volume_bindings(virtual_volume_binding_ids=virtualvolumebindingids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVirtualVolumeBindingsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVirtualVolumeBindingsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfeaturestatus', short_help="""GetFeatureStatus enables you to retrieve the status of a cluster feature. """, cls=SolidFireCommand)
@click.option('--feature',
              type=str,
              required=False,
              help="""Specifies the feature for which the status is returned. Valid values are: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. FipsDrives: Retrieve status for the FIPS 140-2 drive encryption feature. Fips: Retrieve status for the FIPS 140-2 encryption for HTTPS communication feature. SnapMirror: Retrieve status for the SnapMirror replication cluster feature. """)
@pass_context
def getfeaturestatus(ctx,
           # Optional main parameter
           feature = None):
    """GetFeatureStatus enables you to retrieve the status of a cluster feature."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""feature = """+str(feature)+""";"""+"")
    try:
        _GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetFeatureStatusResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetFeatureStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcount', short_help="""Enables retrieval of the number of virtual volumes currently in the system. """, cls=SolidFireCommand)
@pass_context
def getcount(ctx):
    """Enables retrieval of the number of virtual volumes currently in the system."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetVirtualVolumeCountResult = ctx.element.get_virtual_volume_count()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetVirtualVolumeCountResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetVirtualVolumeCountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listhosts', short_help="""ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host that has initiated a session with the VASA API provider. """, cls=SolidFireCommand)
@click.option('--virtualvolumehostids',
              type=str,
              required=False,
              help="""A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. """)
@pass_context
def listhosts(ctx,
           # Optional main parameter
           virtualvolumehostids = None):
    """ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host"""
    """that has initiated a session with the VASA API provider."""

    

    cli_utils.establish_connection(ctx)
    

    virtualvolumehostids = parser.parse_array(virtualvolumehostids)
    

    

    ctx.logger.info(""": """"""virtualvolumehostids = """+str(virtualvolumehostids)+""";"""+"")
    try:
        _ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtualvolumehostids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVirtualVolumeHostsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listprotocolendpoints', short_help="""ListProtocolEndpoints enables you to retrieve information about all protocol endpoints in the cluster. Protocol endpoints govern access to their associated virtual volume storage containers. """, cls=SolidFireCommand)
@click.option('--protocolendpointids',
              type=str,
              required=False,
              help="""A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints. """)
@pass_context
def listprotocolendpoints(ctx,
           # Optional main parameter
           protocolendpointids = None):
    """ListProtocolEndpoints enables you to retrieve information about all protocol endpoints in the cluster. Protocol endpoints govern"""
    """access to their associated virtual volume storage containers."""

    

    cli_utils.establish_connection(ctx)
    

    protocolendpointids = parser.parse_array(protocolendpointids)
    

    

    ctx.logger.info(""": """"""protocolendpointids = """+str(protocolendpointids)+""";"""+"")
    try:
        _ListProtocolEndpointsResult = ctx.element.list_protocol_endpoints(protocol_endpoint_ids=protocolendpointids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListProtocolEndpointsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListProtocolEndpointsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


