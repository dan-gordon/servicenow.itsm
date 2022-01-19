class ScriptedRESTClient:
    def __init__(self, client):
        self.client = client

    def get_data(self, path, query=None):
        response = self.client.get(path, query)
        result = response.json["result"]
        return self.validate_data(result)

    def validate_data(self, data):
        return data
