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


@click.group()
@pass_context
def cli(ctx):
    """delete modify list create """

@cli.command('delete', short_help="""DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups). If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible). """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""An array of IDs of initiators to delete. """)
@pass_context
def delete(ctx,
           initiators):
    """DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups)."""
    """If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _DeleteInitiatorsResult = ctx.element.delete_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators. If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """)
@click.option('--modifyinitiator_initiatorid',
              type=int,
              required=True,
              help="""(Required) The numeric ID of the initiator to modify. (Integer) """)
@click.option('--modifyinitiator_alias',
              type=str,
              required=False,
              help="""(Optional) A new friendly name to assign to the initiator. (String) """)
@click.option('--modifyinitiator_volumeaccessgroupid',
              type=int,
              required=False,
              help="""(Optional) The ID of the volume access group into to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) """)
@click.option('--modifyinitiator_attributes',
              type=dict,
              required=False,
              help="""(Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) """)
@pass_context
def modify(ctx,
           modifyinitiator_initiatorid,
           modifyinitiator_alias = None,
           modifyinitiator_volumeaccessgroupid = None,
           modifyinitiator_attributes = None):
    """ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators."""
    """If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = None
    if(initiators is not None or False):
        kwargsDict = dict()
        kwargsDict["initiatorid"] = modifyinitiator_initiatorid
        kwargsDict["alias"] = modifyinitiator_alias
        kwargsDict["volumeaccessgroupid"] = modifyinitiator_volumeaccessgroupid
        kwargsDict["attributes"] = modifyinitiator_attributes

        initiators = ModifyInitiator(**kwargsDict)

    initiators = parser.parse_array(initiators)

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _ModifyInitiatorsResult = ctx.element.modify_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs). """)
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
              help="""A list of initiator IDs to retrieve. You can supply this parameter or the "startInitiatorID" parameter, but not both. """)
@pass_context
def list(ctx,
           startinitiatorid = None,
           limit = None,
           initiators = None):
    """ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    ctx.logger.info("""startinitiatorid = """+str(startinitiatorid)+""";"""+"""limit = """+str(limit)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        _ListInitiatorsResult = ctx.element.list_initiators(start_initiator_id=startinitiatorid, limit=limit, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups. If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """)
@click.option('--createinitiator_name',
              type=str,
              required=True,
              help="""(Required) The name of the initiator (IQN or WWPN) to create. (String) """)
@click.option('--createinitiator_alias',
              type=str,
              required=False,
              help="""(Optional) The friendly name to assign to this initiator. (String) """)
@click.option('--createinitiator_volumeaccessgroupid',
              type=int,
              required=False,
              help="""(Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) """)
@click.option('--createinitiator_attributes',
              type=dict,
              required=False,
              help="""(Optional) A set of JSON attributes assigned to this initiator. (JSON Object) """)
@pass_context
def create(ctx,
           createinitiator_name,
           createinitiator_alias = None,
           createinitiator_volumeaccessgroupid = None,
           createinitiator_attributes = None):
    """CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups."""
    """If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = None
    if(initiators is not None or False):
        kwargsDict = dict()
        kwargsDict["name"] = createinitiator_name
        kwargsDict["alias"] = createinitiator_alias
        kwargsDict["volumeaccessgroupid"] = createinitiator_volumeaccessgroupid
        kwargsDict["attributes"] = createinitiator_attributes

        initiators = CreateInitiator(**kwargsDict)

    initiators = parser.parse_array(initiators)

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _CreateInitiatorsResult = ctx.element.create_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
