import types
import inspect


def get_members(cls) -> types.GeneratorType:
    _, parent, *_ = inspect.getmro(cls.__class__)
    base_members = inspect.getmembers(parent, predicate=inspect.isfunction)
    base_members = [member[0] for member in base_members]
    self_members = inspect.getmembers(cls, predicate=inspect.ismethod)
    return (member for member in self_members if not member[0] in base_members)


def get_view_name(view: types.MethodType):
    return view.__name__.lower()


def get_view_annotations(view: types.MethodType):
    return view.__annotations__


def get_view_arguments(view: types.MethodType):
    arguments, *_ = inspect.getfullargspec(view)
    self, request, *arguments = arguments
    return arguments


def get_view_attributes(cls: object, view: types.MethodType) -> dict:
    name = getattr(view, "name", get_view_name(view))
    methods = getattr(view, "methods", ["GET"])
    arguments = get_view_arguments(view)
    annotations = get_view_annotations(view)
    returns = annotations.pop("return", None)
    if not returns:
        returns = getattr(cls, "RESPONSE_TYPE", None)
    return {
        "name": name,
        "methods": methods,
        "arguments": arguments,
        "annotations": annotations,
        "returns": returns,
    }

def set_view_attributes(view: types.MethodType, attributes: dict) -> types.MethodType:
    view.__func__.__attributes__ = attributes
    return view