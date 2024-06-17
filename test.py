import html
import re
from pprint import pprint

import swagger_client
from swagger_client.rest import ApiException

RE_TAGS = re.compile(r"<([^>]+)>", re.UNICODE)


def strip_tags(s):
    """Remove tags from `s`.

    Parameters
    ----------
    s : str

    Returns
    -------
    str
        String without tags.

    """
    return RE_TAGS.sub("", s)


def parse_data(api_response: dict, parsed_data: list):
    for item in api_response['items']:
        parsed_data_row = {
            'Id': item['pid'],
            'Description': html.unescape(strip_tags(item['description'])),
            'Precondition': html.unescape(strip_tags(item['precondition'])),
            'Name': item['name'],
            'Test Step Description': '\n'.join(map(str,
                                                   [html.unescape(
                                                       strip_tags(str(item['order']) + '. ' + item['description']))
                                                       for item in item['test_steps']
                                                       for key in item if key == 'description'])),
            'Test Expected Result': '\n'.join(map(str,
                                                  [html.unescape(
                                                      strip_tags(str(item['order']) + '. ' + item['expected']))
                                                      for item in item['test_steps']
                                                      for key in item if key == 'expected'])),
            'Status': ''.join([properties['field_value_name'] for properties in item['properties']
                               if properties['field_name'] == 'Status']),
            'Automation': ''.join([properties['field_value_name'] for properties in item['properties']
                                   if properties['field_name'] == 'Automation']),
            'Type': ''.join([properties['field_value_name'] for properties in item['properties']
                             if properties['field_name'] == 'Type']),
            'Priority': ''.join([properties['field_value_name'] for properties in item['properties']
                                 if properties['field_name'] == 'Priority']),
        }
        parsed_data.append(parsed_data_row)


if __name__ == '__main__':
    configuration = swagger_client.Configuration()
    configuration.host = 'https://ctcprod.qtestnet.com'
    configuration.api_key['Authorization'] = 'f3ea6279-eb6d-44a7-9b1a-e95edb863256'
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
    body = swagger_client.ArtifactSearchParams(object_type='test-cases', fields=['*'],
                                               query="Module in 'MD-78 Master Test Suite'")
    project_id = 124186
    append_test_steps = 'true'
    include_external_properties = 'true'
    page_size = 100
    page = 1
    parsed_data = []

    try:
        api_response = api_instance.search_artifact(project_id, body, append_test_steps=append_test_steps,
                                                    include_external_properties=include_external_properties,
                                                    page_size=page_size, page=page)
        parse_data(api_response, parsed_data)

        # pprint(api_response)
        if api_response['links']:
            while api_response['links'][0]['rel'] == 'next':
                page += 1
                api_response = api_instance.search_artifact(project_id, body, append_test_steps=append_test_steps,
                                                            include_external_properties=include_external_properties,
                                                            page_size=page_size, page=page)
                parse_data(api_response, parsed_data)
                # pprint(api_response)
        # else:
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->search_artifact: %s\n" % e)
