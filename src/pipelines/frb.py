import io

import requests

from sources.frb.constants import URL
from sources.frb.readers import read_xml_from_response_with_columns

response = requests.get(URL)
file = io.BytesIO(response.content)
read_xml_from_response_with_columns(file)
