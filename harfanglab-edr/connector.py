""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import logging
from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from .operations import check_health, _run_action

logger = get_logger('harfanglab-edr')
#logger.setLevel(logging.DEBUG) # Uncomment to enable local debug

class HarfangLab(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            logger.debug("Running operation: {}".format(operation))
            params.update({'operation':operation})

            return _run_action(config, params, **kwargs)

        except Exception as Err:
            raise ConnectorError(Err)

    def check_health(self, config):
        try:
            return check_health(config)
        except Exception as e:
            raise ConnectorError(e)
