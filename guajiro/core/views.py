from guajiro.core.router import get_routes
from guajiro.core.inspector import get_members, get_view_attributes, set_view_attributes
from guajiro.core.decorators import handle_arguments_and_annotations

from guajiro.core.response_types import ResponseType


class View(object):
    """
    Represents a view, based on flask classy view a lot.
    """

    ROUTE_PREFIX = None
    ROUTE_BASE = None
    TRAILING_SLASH = True

    SPECIAL_METHODS = [
        "get",
        "put",
        "post",
        "index",
        "delete",
    ]

    RESPONSE_TYPE = None

    def get_class_name(self) -> str:
        return self.__class__.__name__

    def get_route_base(self) -> str:
        class_name = self.get_class_name().lower()
        # FIXME: this can be a bug if user specifies something like resourceview
        view_name, *rest = class_name.split("resource")
        return "{0}".format(view_name)

    @property
    def routes(self) -> dict:
        for name, view in get_members(self):
            attributes = get_view_attributes(self, view)
            view = set_view_attributes(view, attributes)
            for (method, route) in get_routes(self, attributes):
                yield (method, route, handle_arguments_and_annotations(view))

    def append_to(self, app) -> None:
        for (method, route, handler) in self.routes:
            # FIXME: Use logger here.
            print(method, route, " ==> ", handler)
            app.router.add_route(method, route, handler)


class JSONView(View):

    RESPONSE_TYPE = ResponseType.JSON