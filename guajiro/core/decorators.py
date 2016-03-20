
import types
import functools

from guajiro.core.inspect import get_view_name
from guajiro.core.exceptions import HTTPBadRequest


def route(rule=None, methods=["GET"]):
    def wrapper(view):
        if rule:
            view.name = rule.strip("/")
        view.methods = methods
        return view
    return wrapper


def handle_arguments_and_annotations(view: types.FunctionType) -> types.FunctionType:
    @functools.wraps(view)
    def wrapper(request, **kwargs):
        arguments = []
        attributes = view.__attributes__
        if attributes.get("arguments"):
            for name in attributes.get("arguments"):
                value = request.match_info.get(name)
                if name in attributes.get("annotations"):
                    converter = attributes.get("annotations").get(name)
                    try:
                        value = converter(value)
                    except ValueError:
                        raise HTTPBadRequest
                arguments.append(value)
        return view(request, *arguments)
    return wrapper
