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
        # Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地
        # 创建StreamHandler之后，可以设置日志级别，设置格式化器Formatter，增加或删除过滤器Filter
        'handlers': {
            'default': {
                'level': logging.DEBUG,
                'formatter': 'verbose',
                'class': 'logging.StreamHandler',
            },
        },
        # Formatter 格式化器，指明了最终输出中日志记录的布局
        'formatters': {
            'verbose': {
                'format': '%(asctime)s  %(name)s  %(levelname)s: %(message)s',
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
