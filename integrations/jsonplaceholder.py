import os
import requests

from .utils import METHOD_ROUTE


API_URL = 'https://jsonplaceholder.typicode.com/'

JPH_ROUTE = {
    'post': 'posts/',
}


def __build_method(method):
    return METHOD_ROUTE[method]

def __build_url(action):
    return API_URL + JPH_ROUTE[action]

def __build_request(action, method, **kwargs):
    _url = __build_url(action)
    _pk = kwargs.pop('pk', False)
    print(_pk)
    if _pk:
        _url += '{}/'.format(_pk)

    _request = __build_method(method)
    return _request(_url, **kwargs)

def post(endpoint, data={}, **kwargs):
    response = __build_request(endpoint, 'post', json=data, **kwargs)
    return response.json()

def patch(endpoint, pk, data, **kwargs):
    response = __build_request(endpoint, 'patch', pk=pk, json=data, **kwargs)
    return response.json()

def delete(endpoint, pk, **kwargs):
    response = __build_request(endpoint, 'delete', pk=pk, **kwargs)
    return response.json()

def get(endpoint, pk=None, params={}, **kwargs):
    response = __build_request(endpoint, 'get', pk=pk, params=params, **kwargs)
    return response.json()


def retrieve_post(pk):
    return get('post', pk=pk)

def list_posts():
    return get('post')

def create_post(data):
    return post('post', data=data)

def update_post(pk, data):
    return patch('post', pk=pk, data=data)

def delete_post(pk):
    return delete('post', pk=pk)
