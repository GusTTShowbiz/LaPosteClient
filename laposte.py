import requests
from exceptions import TrackShipmentError

class LaPoste(object):

    BASE_URL = "https://api.laposte.fr/"
    TRACK_SHIPMENT_URL = "suivi/v1/"

    def __init__(
    self, api_key=None
    ):
        self.api_key = api_key

    def trackShipment(self, code):
        trackShipmentResponse = requests.get(
        self.BASE_URL + self.TRACK_SHIPMENT_URL + code,
        headers={"X-Okapi-Key": self.api_key}
        )
        jsonResponse = trackShipmentResponse.json()
        if trackShipmentResponse.status_code != 200:
            raise TrackShipmentError(jsonResponse['code'], jsonResponse['message'])

        return jsonResponse
