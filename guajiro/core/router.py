import types


def get_route_arguments(attributes) -> str:
    arguments = attributes.get("arguments")
    if arguments:
        arguments = get_route_argument_name(arguments)
        arguments = "/".join(arguments)
    return arguments or None


def get_route_argument_name(arguments: list) -> types.GeneratorType:
    for name in arguments:
        yield "{{{name}}}".format(name=name)


def get_route(cls: object, attributes: dict) -> str:
    name = attributes.get("name")
    arguments = get_route_arguments(attributes)

    prefix = cls.ROUTE_PREFIX or "/"
    if cls.ROUTE_BASE is None:
        base = cls.get_route_base()
    else:
        base = cls.ROUTE_BASE.strip("/")

    if name in cls.SPECIAL_METHODS:
        template = [prefix, base or "/", arguments]
    else:
        template = [prefix, base, name, arguments]

    route = "/".join([p.rstrip("/") for p in template if p])

    if cls.TRAILING_SLASH and not route.endswith("/"):
        route = "{0}/".format(route)

    return route


def get_routes(cls: object, attributes: dict) -> types.GeneratorType:
    name = attributes.get("name")
    methods = attributes.get("methods")
    route = get_route(cls, attributes)
    if name in cls.SPECIAL_METHODS:
        if name in ["get", "index"]:
            methods = methods or ["GET"]
        else:
            methods = [name.upper()]
    else:
        methods = methods
    for method in methods:
        yield (method, route)