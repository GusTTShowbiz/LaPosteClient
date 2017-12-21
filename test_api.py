import mock
import unittest
from laposte import LaPoste
from exceptions import TrackShipmentError

class LaPosteTestCase(unittest.TestCase):
    def setUp(self):
        self.laposte = LaPoste(api_key="123")

    @mock.patch('laposte.requests.get')
    def test_trackshipment_ok(self, mock_get):

        mock_response = mock.Mock()
        api_response_dict = {
            "code": "1111111111111",
            "date": "06/09/2016",
            "status": "PRIS_EN_CHARGE",
            "message": "Envoi pris en charge par Chronopost chez l'expéditeur",
            "link": "http://www.chronopost.fr/expedier/inputLTNumbersNoJahia.do?lang=fr_FR&listeNumeros=1111111111111",
            "type": "Chronopost"
        }
        mock_response.json.return_value = api_response_dict
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response_dict = self.laposte.trackShipment('1111111111111')

        url = 'https://api.laposte.fr/suivi/v1/1111111111111'
        mock_get.assert_called_once_with(url, headers={"X-Okapi-Key": "123"})
        self.assertEqual(1, mock_response.json.call_count)
        self.assertEqual(response_dict, api_response_dict)

    @mock.patch('laposte.requests.get')
    def test_trackshipment_not_found(self, mock_get):
        mock_response = mock.Mock()
        api_response_dict = {
            "code": "BAD_REQUEST",
            "message": "Mauvais format pour le paramètre code"
        }
        mock_response.json.return_value = api_response_dict
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        with self.assertRaises(TrackShipmentError):
            self.laposte.trackShipment('B232')
        url = 'https://api.laposte.fr/suivi/v1/B232'
        mock_get.assert_called_once_with(url, headers={"X-Okapi-Key": "123"})
