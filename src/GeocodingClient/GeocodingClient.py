from typing import Any
from src.GenericClient._utils import parse_text_response
from src.GenericClient.base_client import Client
from src.GeocodingClient._utils import ALLOWED_OPTIONAL_PARS, GeocodingUrls

class GeocodingApiClient(Client):
    _API_URLS = [
        "https://api.openweathermap.org/geo/1.0/direct",
        "http://api.openweathermap.org/geo/1.0/zip",
        "http://api.openweathermap.org/geo/1.0/reverse"
    ]

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self._allowed_optional_pras = ALLOWED_OPTIONAL_PARS

    def get_coordinates_by_location_name(self, city_name: str, country_code: str=None, state_code=None, **kwargs) -> dict[str, Any]:
        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[GeocodingUrls.by_location_name],
            _get_params_dict
        )
        response = parse_text_response(request_response)
        return response

    def get_coordinates_by_zip_code(self, zip_code: str, country_code: str, **kwargs) -> dict[str, Any]:
        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[GeocodingUrls.by_zip_code],
            _get_params_dict
        )
        response = parse_text_response(request_response)
        return response

    def get_name_of_location_by_coordiantes(self, latitude, longitude, **kwargs) -> list:
        _get_params_dict = {
            "lat": latitude,
            "lon": longitude
        }
        self._verify_and_add_optional_params_to_request(kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[GeocodingUrls.reverse],
            _get_params_dict
        )
        response = parse_text_response(request_response)
        return response

