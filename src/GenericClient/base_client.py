import requests
from src.GenericClient._utils import parse_optional_parameters

from src.GenericClient.RequestBuilder import RequestDirector


class Client:
    """Base OpenWeather API Client."""

    def __init__(self, api_key: str):
        """Initialization

        Args:
            api_key (str): OpenWeather API Key.
        """
        self.api_key = api_key
        self._request_director = RequestDirector(api_key)
        self._allowed_optional_pras = []

    def _send_request(self, req_type, url, data, headers=None, exception=None):
        """send http request with passed parameters.

        Args:
            req_type str: type of the request: 'GET', 'POST' etc.
            url str: URL address.
            data dict: request data.
            headers (str, optional): request header. Defaults to None.
            exception (Exception, optional): custom exception passed by the user. Defaults to None.

        Raises:
            exception: it's raised when the exception fail.
            Exception: it's raised when the exception fail

        Returns:
            Request.Response: request response
        """
        request_session = requests.Session()
        prepared_request = self._request_director.build_request(req_type, url, data, headers)
        try:
            response = request_session.send(prepared_request)
            response.raise_for_status()
        except Exception as exc:
            if exception:
                raise exception(exc)
            else:
                raise Exception(exc)

        return response

    def _verify_and_add_optional_params_to_request(self, request_params, kwargs):
        """Extend request parameter with optional parameters.

        Args:
            request_params dict: current request parameters
            kwargs dict: kwargs
        """
        optional_args = parse_optional_parameters(
            self._allowed_optional_pras,
            kwargs
        )
        request_params.update(optional_args)
