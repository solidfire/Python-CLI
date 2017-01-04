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
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from solidfire.models import Config
from solidfire.models import Network
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """AddNodes GetBootstrapConfig GetConfig GetNetworkConfig GetNodeStats GetOrigin GetPendingOperation ListActiveNodes ListAllNodes ListNodeStats ListPendingActiveNodes ListPendingNodes RemoveNodes SetConfig SetNetworkConfig """

@cli.command('AddNodes', short_help="AddNodes")
@click.option('--pending_nodes',
              type=str,
              required=True,
              help="""List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method. """)
@pass_context
def AddNodes(ctx,
           pending_nodes):
    """AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: It may take several seconds after adding a new Node for it to start up and register the drives as being available."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    pending_nodes = parser.parse_array(pending_nodes)

    AddNodesResult = ctx.element.add_nodes(pending_nodes=pending_nodes)
    cli_utils.print_result(AddNodesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetBootstrapConfig', short_help="GetBootstrapConfig")
@pass_context
def GetBootstrapConfig(ctx):
    """GetBootstrapConfig returns the cluster name and node name from the bootstrap configuration file. This API method should be performed on an individual node before it has been configured into a cluster. The resulting information from this method is used in the Cluster Configuration UI when the cluster is eventually created."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetBootstrapConfigResult = ctx.element.get_bootstrap_config()
    cli_utils.print_result(GetBootstrapConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetConfig', short_help="GetConfig")
@pass_context
def GetConfig(ctx):
    """The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both &quot;GetClusterConfig&quot; and &quot;GetNetworkConfig&quot; methods."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetConfigResult = ctx.element.get_config()
    cli_utils.print_result(GetConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetNetworkConfig', short_help="GetNetworkConfig")
@pass_context
def GetNetworkConfig(ctx):
    """The GetNetworkConfig API method is used to display the network configuration information for a node."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetNetworkConfigResult = ctx.element.get_network_config()
    cli_utils.print_result(GetNetworkConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetNodeStats', short_help="GetNodeStats")
@click.option('--node_id',
              type=int,
              required=True,
              help="""Specifies the node for which statistics are gathered. """)
@pass_context
def GetNodeStats(ctx,
           node_id):
    """GetNodeStats is used to return the high-level activity measurements for a single node."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetNodeStatsResult = ctx.element.get_node_stats(node_id=node_id)
    cli_utils.print_result(GetNodeStatsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetOrigin', short_help="GetOrigin")
@click.option('--force',
              type=bool,
              required=True,
              help="""""")
@pass_context
def GetOrigin(ctx,
           force):
    """GetOrigin enables you to retrieve the origination certificate for where the node was built.NOTE: The GetOrigin method may return &quot;null&quot; if there is no origination certification."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetOriginResult = ctx.element.get_origin(force=force)
    cli_utils.print_result(GetOriginResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetPendingOperation', short_help="GetPendingOperation")
@pass_context
def GetPendingOperation(ctx):
    """GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.&lt;br/&gt;"""
    """&lt;br/&gt;"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetPendingOperationResult = ctx.element.get_pending_operation()
    cli_utils.print_result(GetPendingOperationResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListActiveNodes', short_help="ListActiveNodes")
@pass_context
def ListActiveNodes(ctx):
    """ListActiveNodes returns the list of currently active nodes that are in the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListActiveNodesResult = ctx.element.list_active_nodes()
    cli_utils.print_result(ListActiveNodesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListAllNodes', short_help="ListAllNodes")
@pass_context
def ListAllNodes(ctx):
    """ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListAllNodesResult = ctx.element.list_all_nodes()
    cli_utils.print_result(ListAllNodesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListNodeStats', short_help="ListNodeStats")
@pass_context
def ListNodeStats(ctx):
    """ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListNodeStatsResult = ctx.element.list_node_stats()
    cli_utils.print_result(ListNodeStatsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListPendingActiveNodes', short_help="ListPendingActiveNodes")
@pass_context
def ListPendingActiveNodes(ctx):
    """ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListPendingActiveNodesResult = ctx.element.list_pending_active_nodes()
    cli_utils.print_result(ListPendingActiveNodesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListPendingNodes', short_help="ListPendingNodes")
@pass_context
def ListPendingNodes(ctx):
    """Gets the list of pending nodes."""
    """Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListPendingNodesResult = ctx.element.list_pending_nodes()
    cli_utils.print_result(ListPendingNodesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveNodes', short_help="RemoveNodes")
@click.option('--nodes',
              type=str,
              required=True,
              help="""List of NodeIDs for the nodes to be removed. """)
@pass_context
def RemoveNodes(ctx,
           nodes):
    """RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with &quot;RemoveDrives&quot; method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the &quot;Pending Node&quot; list."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    nodes = parser.parse_array(nodes)

    RemoveNodesResult = ctx.element.remove_nodes(nodes=nodes)
    cli_utils.print_result(RemoveNodesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetConfig', short_help="SetConfig")
@click.option('--config',
              type=str,
              required=True,
              help="""Provide in json format: Objects that you want changed for the cluster interface settings. """)
@pass_context
def SetConfig(ctx,
           config):
    """The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Warning!&lt;/b&gt; Changing the 'bond-mode' on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")

    kwargsDict = simplejson.loads(config)
    config = Config(**kwargsDict)

    SetConfigResult = ctx.element.set_config(config=config)
    cli_utils.print_result(SetConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetNetworkConfig', short_help="SetNetworkConfig")
@click.option('--network',
              type=str,
              required=True,
              help="""Provide in json format: Objects that will be changed for the node network settings. """)
@pass_context
def SetNetworkConfig(ctx,
           network):
    """The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")

    kwargsDict = simplejson.loads(network)
    network = Network(**kwargsDict)

    SetNetworkConfigResult = ctx.element.set_network_config(network=network)
    cli_utils.print_result(SetNetworkConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

