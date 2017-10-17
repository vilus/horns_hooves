from django.utils.deprecation import MiddlewareMixin
from django.http import Http404, HttpResponse


class ProcessRequest(MiddlewareMixin):
    def process_request(self, request):
        request._from_process_req = 'from middleware'
        return None


class ProcessResponse(MiddlewareMixin):
    def process_response(self, request, response):
        response.set_cookie('from_middleware', request._from_process_req)
        return response


class ProcessException(MiddlewareMixin):
    def process_exception(self, _, exception):
        if isinstance(exception, Http404):
            return HttpResponse('^_^', status=500)
        return None
