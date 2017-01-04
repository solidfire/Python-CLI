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
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """CreateVirtualVolumeHost EnableFeature GetFeatureStatus GetVirtualVolumeCount GetVirtualVolumeTaskUpdate GetVirtualVolumeUnsharedChunks ListVirtualVolumeBindings ListVirtualVolumeHosts ListVirtualVolumes ListVirtualVolumeTasks PrepareVirtualSnapshot """

@cli.command('CreateVirtualVolumeHost', short_help="CreateVirtualVolumeHost")
@click.option('--virtual_volume_host_id',
              type=UUID,
              required=True,
              help="""The GUID of the ESX host. """)
@click.option('--cluster_id',
              type=UUID,
              required=True,
              help="""The GUID of the ESX Cluster. """)
@click.option('--initiator_names',
              type=str,
              required=False,
              help="""""")
@click.option('--visible_protocol_endpoint_ids',
              type=str,
              required=False,
              help="""A list of PEs the host is aware of. """)
@click.option('--host_address',
              type=str,
              required=False,
              help="""IP or DNS name for the host. """)
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="""""")
@pass_context
def CreateVirtualVolumeHost(ctx,
           virtual_volume_host_id,
           cluster_id,
           initiator_names = None,
           visible_protocol_endpoint_ids = None,
           host_address = None,
           calling_virtual_volume_host_id = None):
    """CreateVirtualVolumeHost creates a new ESX host."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    initiator_names = parser.parse_array(initiator_names)

    visible_protocol_endpoint_ids = parser.parse_array(visible_protocol_endpoint_ids)

    VirtualVolumeNullResult = ctx.element.create_virtual_volume_host(virtual_volume_host_id=virtual_volume_host_id, cluster_id=cluster_id, initiator_names=initiator_names, visible_protocol_endpoint_ids=visible_protocol_endpoint_ids, host_address=host_address, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    cli_utils.print_result(VirtualVolumeNullResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('EnableFeature', short_help="EnableFeature")
@click.option('--feature',
              type=str,
              required=True,
              help="""Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def EnableFeature(ctx,
           feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    EnableFeatureResult = ctx.element.enable_feature(feature=feature)
    cli_utils.print_result(EnableFeatureResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetFeatureStatus', short_help="GetFeatureStatus")
@click.option('--feature',
              type=str,
              required=False,
              help="""Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def GetFeatureStatus(ctx,
           feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
    cli_utils.print_result(GetFeatureStatusResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetVirtualVolumeCount', short_help="GetVirtualVolumeCount")
@pass_context
def GetVirtualVolumeCount(ctx):
    """Enables retrieval of the number of virtual volumes currently in the system."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetVirtualVolumeCountResult = ctx.element.get_virtual_volume_count()
    cli_utils.print_result(GetVirtualVolumeCountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetVirtualVolumeTaskUpdate', short_help="GetVirtualVolumeTaskUpdate")
@click.option('--virtual_volume_task_id',
              type=UUID,
              required=True,
              help="""The UUID of the VVol Task. """)
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="""""")
@pass_context
def GetVirtualVolumeTaskUpdate(ctx,
           virtual_volume_task_id,
           calling_virtual_volume_host_id = None):
    """GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    VirtualVolumeTaskResult = ctx.element.get_virtual_volume_task_update(virtual_volume_task_id=virtual_volume_task_id, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    cli_utils.print_result(VirtualVolumeTaskResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetVirtualVolumeUnsharedChunks', short_help="GetVirtualVolumeUnsharedChunks")
@click.option('--virtual_volume_id',
              type=UUID,
              required=True,
              help="""The ID of the Virtual Volume. """)
@click.option('--base_virtual_volume_id',
              type=UUID,
              required=True,
              help="""The ID of the Virtual Volume to compare against. """)
@click.option('--segment_start',
              type=int,
              required=True,
              help="""Start Byte offset. """)
@click.option('--segment_length',
              type=int,
              required=True,
              help="""Length of the scan segment in bytes. """)
@click.option('--chunk_size',
              type=int,
              required=True,
              help="""Number of bytes represented by one bit in the bitmap. """)
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="""""")
@pass_context
def GetVirtualVolumeUnsharedChunks(ctx,
           virtual_volume_id,
           base_virtual_volume_id,
           segment_start,
           segment_length,
           chunk_size,
           calling_virtual_volume_host_id = None):
    """GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of """
    """chunks not shared between two volumes. This call will return results in less """
    """than 30 seconds. If the specified VVol and the base VVil are not related, an """
    """error is thrown. If the offset/length combination is invalid or out fo range """
    """an error is thrown."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    VirtualVolumeUnsharedChunkResult = ctx.element.get_virtual_volume_unshared_chunks(virtual_volume_id=virtual_volume_id, base_virtual_volume_id=base_virtual_volume_id, segment_start=segment_start, segment_length=segment_length, chunk_size=chunk_size, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    cli_utils.print_result(VirtualVolumeUnsharedChunkResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVirtualVolumeBindings', short_help="ListVirtualVolumeBindings")
@click.option('--virtual_volume_binding_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListVirtualVolumeBindings(ctx,
           virtual_volume_binding_ids = None):
    """ListVirtualVolumeBindings returns a list of VVol bindings."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    virtual_volume_binding_ids = parser.parse_array(virtual_volume_binding_ids)

    ListVirtualVolumeBindingsResult = ctx.element.list_virtual_volume_bindings(virtual_volume_binding_ids=virtual_volume_binding_ids)
    cli_utils.print_result(ListVirtualVolumeBindingsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVirtualVolumeHosts', short_help="ListVirtualVolumeHosts")
@click.option('--virtual_volume_host_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListVirtualVolumeHosts(ctx,
           virtual_volume_host_ids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    virtual_volume_host_ids = parser.parse_array(virtual_volume_host_ids)

    ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtual_volume_host_ids)
    cli_utils.print_result(ListVirtualVolumeHostsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVirtualVolumes', short_help="ListVirtualVolumes")
@click.option('--details',
              type=bool,
              required=False,
              help="""Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of virtual volumes to list. """)
@click.option('--recursive',
              type=bool,
              required=False,
              help="""Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response. """)
@click.option('--start_virtual_volume_id',
              type=UUID,
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtual_volume_ids',
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def ListVirtualVolumes(ctx,
           details = None,
           limit = None,
           recursive = None,
           start_virtual_volume_id = None,
           virtual_volume_ids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    virtual_volume_ids = parser.parse_array(virtual_volume_ids)

    ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=start_virtual_volume_id, virtual_volume_ids=virtual_volume_ids)
    cli_utils.print_result(ListVirtualVolumesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVirtualVolumeTasks', short_help="ListVirtualVolumeTasks")
@click.option('--virtual_volume_task_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListVirtualVolumeTasks(ctx,
           virtual_volume_task_ids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    virtual_volume_task_ids = parser.parse_array(virtual_volume_task_ids)

    ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtual_volume_task_ids)
    cli_utils.print_result(ListVirtualVolumeTasksResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('PrepareVirtualSnapshot', short_help="PrepareVirtualSnapshot")
@click.option('--virtual_volume_id',
              type=UUID,
              required=True,
              help="""The ID of the Virtual Volume to clone. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The name for the newly-created volume. """)
@click.option('--writable_snapshot',
              type=bool,
              required=False,
              help="""Will the snapshot be writable? """)
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="""""")
@pass_context
def PrepareVirtualSnapshot(ctx,
           virtual_volume_id,
           name = None,
           writable_snapshot = None,
           calling_virtual_volume_host_id = None):
    """PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    PrepareVirtualSnapshotResult = ctx.element.prepare_virtual_snapshot(virtual_volume_id=virtual_volume_id, name=name, writable_snapshot=writable_snapshot, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    cli_utils.print_result(PrepareVirtualSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

