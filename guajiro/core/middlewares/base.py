
import json
import asyncio
import traceback
import aiohttp.web
from guajiro.core.response_types import ResponseType


@asyncio.coroutine
def handle_response_annotations(app, view):
    @asyncio.coroutine
    def middleware(request):
        response = yield from view(request)
        if not isinstance(response, aiohttp.web.Response):
            attributes = getattr(view, "__attributes__", None)
            if attributes:
                returns = attributes.get("returns")
                if isinstance(returns, ResponseType):
                    handler = returns.value.get("handler", None)
                    if handler:
                        response = handler(response)
                    headers = returns.value.get("headers", {})
                    return aiohttp.web.Response(
                        text=response,
                        headers=headers,
                    )
        return response
    return middleware


@asyncio.coroutine
def handle_exceptions(app, view):
    @asyncio.coroutine
    def middleware(request):
        try:
            response = yield from view(request)
        except Exception as exception:
            if app.SETTINGS["DEBUG"]:
                plain_traceback = traceback.format_exc()
                return aiohttp.web.Response(
                    text=plain_traceback,
                    status=500,
                )
            raise
        return response
    return middleware