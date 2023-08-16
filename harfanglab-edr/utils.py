from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('harfanglab-edr')

#Utils
def prep_action_parameters(config,params):
    '''
    parse config and params
    '''
    try:        
        cfg = {key.split('@')[1].lower(): value for key, value in config.items() if "config@" in key}
        prm = {key.split('@')[1].lower(): value for key, value in params.items() if "param@" in key}
        return cfg, prm

    except Exception as Err:
        logger.error('Could not parse config and/or params [{0}] '.format(Err))
        raise ConnectorError(Err)