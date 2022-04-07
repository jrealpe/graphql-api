import requests


METHOD_ROUTE = {
    'get': requests.get,
    'post': requests.post,
    'put': requests.put,
    'patch': requests.patch,
    'delete': requests.delete
}
