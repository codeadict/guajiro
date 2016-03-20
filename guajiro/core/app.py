import os.path
import logging

from aiohttp.web import Application as BaseApplication, run_app

from jinja2 import FileSystemLoader
from aiohttp_jinja2 import setup as setup_jinja2_env

from guajiro.core.middlewares import handle_exceptions, handle_response_annotations


class Service(BaseApplication):
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

    def run(self, host='0.0.0.0', port=None,
            shutdown_timeout=60.0, ssl_context=None,
            print=print):
        """
        Run the service locally
        """
        if port is None:
            port = 3000

        loop = self.loop

        handler = self.make_handler()
        srv = loop.run_until_complete(loop.create_server(handler, host, port,
                                                         ssl=ssl_context))

        scheme = 'https' if ssl_context else 'http'
        prompt = '127.0.0.1' if host == '0.0.0.0' else host
        logo = """
        .d8888b.                     d8b d8b
        d88P  Y88b                    Y8P Y8P
        888    888
        888        888  888  8888b.  8888 888 888d888 .d88b.
        888  88888 888  888     "88b "888 888 888P"  d88""88b
        888    888 888  888 .d888888  888 888 888    888  888
        Y88b  d88P Y88b 888 888  888  888 888 888    Y88..88P
        "Y8888P88  "Y88888 "Y888888  888 888 888     "Y88P"
                                      888
                                     d88P
                                   888P
        """
        print(logo)
        print("Seeding on {scheme}://{prompt}:{port}/\n"
              "(Press CTRL+C to quit)".format(
                scheme=scheme, prompt=prompt, port=port))

        try:
            loop.run_forever()
        except KeyboardInterrupt:  # pragma: no branch
            pass
        finally:
            srv.close()
            loop.run_until_complete(srv.wait_closed())
            loop.run_until_complete(self.shutdown())
            loop.run_until_complete(handler.finish_connections(shutdown_timeout))
            loop.run_until_complete(self.cleanup())
        loop.close()
