# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter)

from resource_mapping import RESOURCE_MAPPING


class MandrillClientAdapter(TapiocaAdapter):
    api_root = 'https://mandrillapp.com/api/1.0'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params):
        key = api_params.get('key')
        return {
            'data': {'key': key}
        }

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data):
        return


Mandrill = generate_wrapper_from_adapter(MandrillClientAdapter)
