import os.path
import logging

from aiohttp.web import Application as BaseApplication

from jinja2 import FileSystemLoader
from aiohttp_jinja2 import setup as setup_jinja2_env

from guajiro.core.middlewares import handle_exceptions, handle_response_annotations


class Application(BaseApplication):

    BASE_SETTINGS = {
        "DEBUG": False,
        "MIDDLEWARES": [
            handle_exceptions,
            handle_response_annotations,
        ],
        "TEMPLATES_PATH": os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
    }

    SETTINGS = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.BASE_SETTINGS.update(self.SETTINGS)
        self.SETTINGS = self.BASE_SETTINGS
        self._middlewares = self.SETTINGS["MIDDLEWARES"]

        logging.basicConfig(
            level=logging.DEBUG if self.SETTINGS.get("DEBUG", False) else logging.INFO,
            format='[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s',
        )

        setup_jinja2_env(self, loader=FileSystemLoader(self.SETTINGS["TEMPLATES_PATH"]))
