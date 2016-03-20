from aiohttp_jinja2 import render_template

from guajiro.core.exceptions import HTTPFound


def redirect(location):
    """
    Redirects client to given location.
    """
    raise HTTPFound(location)


def render(template, request, context):
    """
    Wraps aiohttp_jinja2.render_template functions
    """
    return render_template(template, request, context)