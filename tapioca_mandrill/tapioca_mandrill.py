# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin, FormAdapterMixin)

from resource_mapping import RESOURCE_MAPPING


class MandrillClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://mandrillapp.com/api/1.0/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        if 'data' not in kwargs:
            kwargs['data'] = {}
        kwargs['data'].update({'key': api_params.get('key')})

        return super(MandrillClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        return


Mandrill = generate_wrapper_from_adapter(MandrillClientAdapter)
