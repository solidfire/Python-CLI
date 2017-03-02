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
    """getremotelogginghosts setremotelogginghosts setinfo getinfo """

@cli.command('getremotelogginghosts', short_help="""GetRemoteLoggingHosts is used to retrieve the current list of log servers. """, cls=SolidFireCommand)
@pass_context
def getremotelogginghosts(ctx):
    """GetRemoteLoggingHosts is used to retrieve the current list of log servers."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetRemoteLoggingHostsResult = ctx.element.get_remote_logging_hosts()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetRemoteLoggingHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setremotelogginghosts', short_help="""RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts. """, cls=SolidFireCommand)
@click.option('--remotehosts',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["host", "port", ],
              required=True,
              help="""List of hosts to send log messages to.  Has the following subparameters: --host --port """)
@click.option('--host',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Hostname or IP address of the log server. """,
              cls=SolidFireOption)
@click.option('--port',
              required=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Port number that the log server is listening on. """,
              cls=SolidFireOption)
@pass_context
def setremotelogginghosts(ctx,
           # Mandatory main parameter
           remotehosts,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           host,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           port):
    """RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    remotehostsArray = []
    if(remotehosts is not None):
        try:
            for i, _remotehosts in enumerate(remotehosts):
                remotehostsArray.append(LoggingServer(host=host[i], port=port[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""remotehosts = """+str(remotehosts)+""";"""+"")
    try:
        _SetRemoteLoggingHostsResult = ctx.element.set_remote_logging_hosts(remote_hosts=remotehostsArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetRemoteLoggingHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setinfo', short_help="""SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed. """, cls=SolidFireCommand)
@click.option('--timeout',
              type=str,
              required=True,
              help="""Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes. """)
@pass_context
def setinfo(ctx,
           # Mandatory main parameter
           timeout):
    """SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""timeout = """+str(timeout)+""";"""+"")
    try:
        _SetLoginSessionInfoResult = ctx.element.set_login_session_info(timeout=timeout)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetLoginSessionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getinfo', short_help="""GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI. """, cls=SolidFireCommand)
@pass_context
def getinfo(ctx):
    """GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetLoginSessionInfoResult = ctx.element.get_login_session_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetLoginSessionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

