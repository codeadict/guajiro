from guajiro import Service, View
from guajiro import ResponseType


class HelloResource(View):

    def get(self, request) -> ResponseType.JSON:
        return {"hello": "world"}

if __name__ == "__main__":
    service = Service()

    resource = HelloResource()
    resource.append_to(service)

    service.run("localhost", 3000)