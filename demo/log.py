# encoding: utf-8

import logging
import logging.config


def setup(env='dev'):
    if env == "dev":
        conf = _gen_console_logging_config()
    else:
        conf = _gen_syslog_logging_config()
    logging.config.dictConfig(conf)


def _gen_console_logging_config():
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'handlers': ['default'],
            'level': logging.DEBUG,
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': logging.DEBUG,
                'propagate': True
            },
        },
        'handlers': {
            'default': {
                'level': logging.DEBUG,
                'formatter': 'verbose',
                'class': 'logging.StreamHandler',
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(name)s[%(process)d]: %(message)s',
            },
        },
    }


def _gen_syslog_logging_config():
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'handlers': ['syslog'],
            'level': logging.INFO,
        },
        'loggers': {
            '': {
                "handlers": ['syslog'],
                'level': logging.INFO,
                'propagate': True,
            }
        },
        'handlers': {
            'syslog': {
                'level': logging.INFO,
                'class': 'logging.handlers.SysLogHandler',
                'address': '/dev/log',
                'facility': 'local6',
                'formatter': 'verbose',
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(name)s[%(process)d]: %(message)s',
            },
        }
    }
