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

@click.group()
@pass_context
def cli(ctx):
    """invoke """

@cli.command('invoke', short_help="""This will invoke any API method supported by the SolidFire API for the version and port the connection is using. Returns a nested hashtable of key/value pairs that contain the result of the invoked method. """, cls=SolidFireCommand)
@click.option('--method',
              type=str,
              required=True,
              help="""The name of the method to invoke. This is case sensitive. """)
@click.option('--parameters',
              type=str,
              required=False,
              help="""An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. """)
@pass_context
def invoke(ctx,
           # Mandatory main parameter
           method,
           # Optional main parameter
           parameters = None):
    """This will invoke any API method supported by the SolidFire API for the version and port the connection is using."""
    """Returns a nested hashtable of key/value pairs that contain the result of the invoked method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""method = """+str(method)+""";"""+"""parameters = """+str(parameters)+""";"""+"")
    try:
        _dict = ctx.element.invoke_sfapi(method=method, parameters=parameters)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_dict), indent=4))
        return
    else:
        cli_utils.print_result(_dict, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

