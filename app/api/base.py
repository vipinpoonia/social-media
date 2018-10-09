from flask import request, jsonify
from flask.views import MethodView

from app.api.error import HTTPBadRequest


class BaseAPIMethodView(MethodView):
    def validate_required_keys(self):
        method = request.method.lower()
        keys = getattr(self, 'required_keys_%s' % request.method.lower(), [])
        for key in keys:
            is_present = (
                request.args.get(key) if method == 'get' else
                request.json.get(key)
            )
            if is_present is None:
                raise HTTPBadRequest(key + ' key is missing')
        return True

    def dispatch_request(self, *args, **kwargs):
        self.validate_required_keys()
        test_func = getattr(self, 'test_%s' % request.method.lower(), None)
        if test_func and not test_func(*args, **kwargs):
            raise HTTPBadRequest(message=(getattr(self, 'error', '')))
        data = super(BaseAPIMethodView, self).dispatch_request(*args, **kwargs)
        return jsonify(data)

