from urllib.parse import parse_qs

from django.utils.deprecation import MiddlewareMixin

from apps.core.utils import convert_to_snake_case
from apps.metadata.aggregators import countries, sectors


class FiltersMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        Add location and sector from the uri to request
        so the selection is available across the views
        """
        request.location = None
        request.sector = None
        request.query_string = request.META.get("QUERY_STRING")
        params = parse_qs(request.query_string)

        if "location" in params:
            location = params["location"][0]
            if location != "all":
                request.location = getattr(countries, params["location"][0])

        if "sector" in params:
            sector_name = convert_to_snake_case(params["sector"][0])
            if sector_name != "all":
                request.sector = getattr(sectors, sector_name)

    def process_response(self, request, response):
        return response