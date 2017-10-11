# encoding: utf-8

import functools
import time
import logging
import json

from flask import request

logger = logging.getLogger(__name__)


def api_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rv = func(*args, **kwargs)
        except:
            raise
        else:
            resp = json.dumps({"message": "success"}) if rv is None else rv
            return resp
    return wrapper


def log_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        http_method = request.environ.get('REQUEST_METHOD')
        url = request.environ.get('PATH_INFO')

        def do_log(is_succeed, rv=None):
            kwargs.update(request.json or request.values.to_dict())
            normal_meta = \
                '<{http_method} {url}> {args}, {kwargs}'.format(
                    http_method=http_method, url=url,
                    func_name=func.func_name, args=args, kwargs=kwargs
                )
            time_meta = 'time: {time}ms'.format(
                time=time.time() - start
            )
            if is_succeed:
                normal_meta = '%s, return %r' % (normal_meta, rv)
                logger.info('Call Ok: %s, %s' % (normal_meta, time_meta))
            else:
                logger.warning(
                    'Call Failed: %s, %s' % (normal_meta, time_meta),
                    exc_info=True
                )

        try:
            rv = func(*args, **kwargs)
        except:
            do_log(is_succeed=False)
            raise
        else:
            do_log(is_succeed=True, rv=rv)
        return rv
    return wrapper
