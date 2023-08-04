""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

  
import requests, json, os, re
from integrations.crudhub import make_request
from requests_toolbelt.multipart.encoder import MultipartEncoder
from connectors.cyops_utilities.builtins import download_file_from_cyops
from connectors.core.connector import get_logger, ConnectorError
from .lib.harfanglab_sdk import *
from .utils import *

logger = get_logger('harfanglab-edr')


def _run_action(config,params,**kwargs):
    '''
    Runs the actions dynamically based on the operation name and the attributes as defined in info.json
    '''
    try:        
        operation = params['operation']
        cfg, prm = prep_action_parameters(config,params)
        conn = HarfangLabConnector(logger=logger, **cfg)
        command = getattr(HarfangLabConnector,operation)
        results = command(conn, **prm)
        if isinstance(results,tuple):
            return json.loads(json.dumps(results))
        else:
            return results

    except Exception as Err:
        logger.error('Action: [{0}] Failed : Error: [{1}] '.format(operation, Err))
        raise ConnectorError(Err)


def check_health(config):
    try:
        params = {
        "param@limit": 1,
        "operation": "search_endpoint"
        }
        _run_action(config,params)

    except Exception as Err:
        logger.exception('Error occurred while connecting to server: {}'.format(str(Err)))
        raise ConnectorError('Error occurred while connecting to server: {}'.format(Err))
