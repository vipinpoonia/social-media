from flask import jsonify, request
from app import app


class BaseAPIException(Exception):
    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.status = "error"

    def to_dict(self):
        rv = dict(self.payload or ())
        message = self.message if self.message else ''
        if not message and hasattr(self, 'default_message'):
            message = self.default_message()
        rv['message'] = message
        rv['status'] = self.status
        return rv


class HTTPNotFound(BaseAPIException):
    status_code = 404

    def default_message(self):
        return "Not Found: %s" % request.url


class HTTPMethodNotAllowed(BaseAPIException):
    status_code = 405


class HTTPForbidden(BaseAPIException):
    status_code = 403


class HTTPBadRequest(BaseAPIException):
    status_code = 400


class HTTPInternalServerError(BaseAPIException):
    status_code = 500


@app.errorhandler(BaseAPIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(e):
    return handle_invalid_usage(HTTPNotFound())
