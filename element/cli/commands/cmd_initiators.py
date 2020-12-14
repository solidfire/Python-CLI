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
    """list modify create delete addtovolumeaccessgroup removefromvolumeaccessgroup """

@cli.command('list', short_help="""ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs). """, cls=SolidFireCommand)
@click.option('--startinitiatorid',
              type=int,
              required=False,
              help="""The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of initiator objects to return. """)
@click.option('--initiators',
              type=str,
              required=False,
              help="""A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. """)
@pass_context
def list(ctx,
           # Optional main parameter
           startinitiatorid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           initiators = None):
    """ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs)."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    initiators = parser.parse_array(initiators)
    

    

    ctx.logger.info(""": """"""startinitiatorid = """+str(startinitiatorid)+";" + """limit = """+str(limit)+";" + """initiators = """+str(initiators)+""";"""+"")
    try:
        _ListInitiatorsResult = ctx.element.list_initiators(start_initiator_id=startinitiatorid, limit=limit, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with CreateInitiators. If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify any initiators (no partial completion is possible). """, cls=SolidFireCommand)
@click.option('--initiators',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["initiatorid", "alias", "volumeaccessgroupid", "attributes", "requirechap", "chapusername", "initiatorsecret", "targetsecret", "virtualnetworkids", ],
              required=True,
              help="""A list of objects containing characteristics of each initiator to modify.  Has the following subparameters: --initiatorid --alias --volumeaccessgroupid --attributes --requirechap --chapusername --initiatorsecret --targetsecret --virtualnetworkids """)
@click.option('--initiatorid',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The numeric ID of the initiator to modify. """,
              cls=SolidFireOption)
@click.option('--alias',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A new friendly name to assign to the initiator. """,
              cls=SolidFireOption)
@click.option('--volumeaccessgroupid',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The ID of the volume access group to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group but not placed in any new volume access group. """,
              cls=SolidFireOption)
@click.option('--attributes',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A new set of JSON attributes assigned to this initiator. """,
              cls=SolidFireOption)
@click.option('--requirechap',
              required=False,
              multiple=True,
              type=bool,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] "requireChap" determines if the initiator is required to use CHAP during session login. CHAP is optional if "requireChap" is false. """,
              cls=SolidFireOption)
@click.option('--chapusername',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The CHAP username for this initiator. Defaults to the initiator name (IQN) if not specified during creation and "requireChap" is true. """,
              cls=SolidFireOption)
@click.option('--initiatorsecret',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The CHAP secret used for authentication of the initiator. Defaults to a randomly generated secret if not specified during creation and "requireChap" is true. """,
              cls=SolidFireOption)
@click.option('--targetsecret',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The CHAP secret used for authentication of the target. Defaults to a randomly generated secret if not specified during creation and "requireChap" is true. """,
              cls=SolidFireOption)
@click.option('--virtualnetworkids',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The list of virtual network identifiers associated with this initiator. If one or more are defined, this initiator will only be able to login to the specified virtual networks. If no virtual networks are defined this initiator can login to all networks. """,
              cls=SolidFireOption)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           initiators,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           initiatorid,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           alias = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           volumeaccessgroupid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           attributes = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           requirechap = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           chapusername = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           initiatorsecret = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           targetsecret = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           virtualnetworkids = None):
    """ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing"""
    """initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with"""
    """CreateInitiators."""
    """If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify"""
    """any initiators (no partial completion is possible)."""

    

    cli_utils.establish_connection(ctx)

    # Converting the virtualnetworkids to list of lists.
    if virtualnetworkids[0] is not None:
        len_virtualnetworkids = len(virtualnetworkids)
        modified_virtualnetworkids = []
        for virtualnetworkid in range(0,len_virtualnetworkids):
            modified_virtualnetworkids.append(virtualnetworkids[virtualnetworkid].split(','))
        virtualnetworkids = modified_virtualnetworkids

    # If we have a submember that's an attributes array, we need to handle it.
    attributes_json = [simplejson.loads(v) if v is not None else None for v in attributes]
    

    initiatorsArray = None
    if len(initiators) == 1 and initiatorid[0] is None and alias[0] is None and volumeaccessgroupid[0] is None and attributes_json[0] is None and requirechap[0] is None and chapusername[0] is None and initiatorsecret[0] is None and targetsecret[0] is None and virtualnetworkids[0] is None:
        initiatorsArray = []
    elif(initiators is not None and initiators != ()):
        initiatorsArray = []
        try:
            for i, _initiators in enumerate(initiators):
                attributes_json = None
                if attributes[i] != None:
                    attributes_json = simplejson.loads(attributes[i])
                initiatorsArray.append(ModifyInitiator(initiator_id=initiatorid[i], alias=alias[i], volume_access_group_id=volumeaccessgroupid[i], attributes=attributes_json, require_chap=requirechap[i], chap_username=chapusername[i], initiator_secret=initiatorsecret[i], target_secret=targetsecret[i], virtual_network_ids=virtualnetworkids[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    

    ctx.logger.info(""": """"""initiators = """ + str(initiatorsArray)+""";"""+"")
    try:
        _ModifyInitiatorsResult = ctx.element.modify_initiators(initiators=initiatorsArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups. If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """, cls=SolidFireCommand)
@click.option('--initiators',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["name", "alias", "volumeaccessgroupid", "attributes", "requirechap", "chapusername", "initiatorsecret", "targetsecret", "virtualnetworkids", ],
              required=True,
              help="""A list of objects containing characteristics of each new initiator.  Has the following subparameters: --name --alias --volumeaccessgroupid --attributes --requirechap --chapusername --initiatorsecret --targetsecret --virtualnetworkids """)
@click.option('--name',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The name of the initiator (IQN or WWPN) to create. """,
              cls=SolidFireOption)
@click.option('--alias',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The friendly name to assign to this initiator. """,
              cls=SolidFireOption)
@click.option('--volumeaccessgroupid',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The ID of the volume access group to which this newly created initiator will be added. """,
              cls=SolidFireOption)
@click.option('--attributes',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A set of JSON attributes assigned to this initiator. (JSON Object) """,
              cls=SolidFireOption)
@click.option('--requirechap',
              required=False,
              multiple=True,
              type=bool,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] "requireChap" determines if the initiator is required to use CHAP during session login. CHAP is optional if "requireChap" is false. """,
              cls=SolidFireOption)
@click.option('--chapusername',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The CHAP username for this initiator. Defaults to the initiator name (IQN) if not specified during creation and "requireChap" is true. """,
              cls=SolidFireOption)
@click.option('--initiatorsecret',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The CHAP secret used for authentication of the initiator. Defaults to a randomly generated secret if not specified during creation and "requireChap" is true. """,
              cls=SolidFireOption)
@click.option('--targetsecret',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The CHAP secret used for authentication of the target. Defaults to a randomly generated secret if not specified during creation and "requireChap" is true. """,
              cls=SolidFireOption)
@click.option('--virtualnetworkids',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The list of virtual network identifiers associated with this initiator. If one or more are defined, this initiator will only be able to login to the specified virtual networks. If no virtual networks are defined this initiator can login to all networks. """,
              cls=SolidFireOption)
@pass_context
def create(ctx,
           # Mandatory main parameter
           initiators,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           alias = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           volumeaccessgroupid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           attributes = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           requirechap = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           chapusername = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           initiatorsecret = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           targetsecret = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           virtualnetworkids = None):
    """CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them"""
    """aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups."""
    """If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create"""
    """any initiators (no partial completion is possible)."""
    
    cli_utils.establish_connection(ctx)

    # Converting the virtualnetworkids to list of lists.
    if virtualnetworkids[0] is not None:
        len_virtualnetworkids = len(virtualnetworkids)
        modified_virtualnetworkids = []
        for virtualnetworkid in range(0,len_virtualnetworkids):
            modified_virtualnetworkids.append(virtualnetworkids[virtualnetworkid].split(','))
        virtualnetworkids = modified_virtualnetworkids
    
    # If we have a submember that's an attributes array, we need to handle it.
    attributes_json = [simplejson.loads(v) if v is not None else None for v in attributes]
    
    initiatorsArray = None
    if len(initiators) == 1 and name[0] is None and alias[0] is None and volumeaccessgroupid[0] is None and attributes_json[0] is None and requirechap[0] is None and chapusername[0] is None and initiatorsecret[0] is None and targetsecret[0] is None and virtualnetworkids[0] is None:
        initiatorsArray = []
    elif(initiators is not None and initiators != ()):
        initiatorsArray = []
        try:
            for i, _initiators in enumerate(initiators):
                attributes_json = None
                if attributes[i] != None:
                    attributes_json = simplejson.loads(attributes[i])
                initiatorsArray.append(CreateInitiator(name=name[i], alias=alias[i], volume_access_group_id=volumeaccessgroupid[i], attributes=attributes_json, require_chap=requirechap[i], chap_username=chapusername[i], initiator_secret=initiatorsecret[i], target_secret=targetsecret[i], virtual_network_ids=virtualnetworkids[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    ctx.logger.info(""": """"""initiators = """ + str(initiatorsArray)+""";"""+"")
    try:
        _CreateInitiatorsResult = ctx.element.create_initiators(initiators=initiatorsArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups). If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible). """, cls=SolidFireCommand)
@click.option('--initiators',
              type=str,
              required=True,
              prompt=True,
              help="""An array of IDs of initiators to delete. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           initiators):
    """DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access"""
    """groups)."""
    """If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any"""
    """initiators (no partial completion is possible)."""

    

    cli_utils.establish_connection(ctx)
    

    initiators = parser.parse_array(initiators)
    

    

    ctx.logger.info(""": """"""initiators = """ + str(initiators)+""";"""+"")
    try:
        _DeleteInitiatorsResult = ctx.element.delete_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addtovolumeaccessgroup', short_help="""AddInitiatorsToVolumeAccessGroup enables you to add initiators to a specified volume access group. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--initiators',
              type=str,
              required=True,
              prompt=True,
              help="""The list of initiators to add to the volume access group. """)
@pass_context
def addtovolumeaccessgroup(ctx,
           # Mandatory main parameter
           volumeaccessgroupid,
           # Mandatory main parameter
           initiators):
    """AddInitiatorsToVolumeAccessGroup enables you"""
    """to add initiators to a specified volume access group."""

    

    cli_utils.establish_connection(ctx)
    
    

    initiators = parser.parse_array(initiators)
    

    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+";"+"""initiators = """ + str(initiators)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.add_initiators_to_volume_access_group(volume_access_group_id=volumeaccessgroupid, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyVolumeAccessGroupResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removefromvolumeaccessgroup', short_help="""RemoveInitiatorsFromVolumeAccessGroup enables you to remove initiators from a specified volume access group. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume access group from which the initiators are removed. """)
@click.option('--initiators',
              type=str,
              required=True,
              prompt=True,
              help="""The list of initiators to remove from the volume access group. """)
@click.option('--deleteorphaninitiators',
              type=bool,
              required=False,
              help="""true: Default. Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. """)
@pass_context
def removefromvolumeaccessgroup(ctx,
           # Mandatory main parameter
           volumeaccessgroupid,
           # Mandatory main parameter
           initiators,
           # Optional main parameter
           deleteorphaninitiators = None):
    """RemoveInitiatorsFromVolumeAccessGroup enables"""
    """you to remove initiators from a specified volume access"""
    """group."""

    

    cli_utils.establish_connection(ctx)
    
    

    initiators = parser.parse_array(initiators)
    
    

    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+";"+"""initiators = """ + str(initiators)+";" + """deleteorphaninitiators = """+str(deleteorphaninitiators)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.remove_initiators_from_volume_access_group(volume_access_group_id=volumeaccessgroupid, initiators=initiators, delete_orphan_initiators=deleteorphaninitiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyVolumeAccessGroupResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


