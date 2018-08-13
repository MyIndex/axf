import logging

from django.utils.deprecation import MiddlewareMixin


class LoggerMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        loger = logging.getLogger('django')

        loger.info(request.path)