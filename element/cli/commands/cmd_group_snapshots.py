#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import json

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListGroupSnapshots")
@click.option('--volume_id',
              type=int,
              required=False,
              help="An array of unique volume IDs to query. If this parameter is not specified, all group snapshots on the cluster will be included. ")
@pass_context
def list(ctx, volume_id = None):
    """ListGroupSnapshots is used to return information about all group snapshots that have been created."""
    ListGroupSnapshotsResult = ctx.element.list_group_snapshots(volume_id=volume_id)
    print(json.dumps(json.loads(jsonpickle.encode(ListGroupSnapshotsResult)),indent=4))

