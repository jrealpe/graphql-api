"""
GraghQL API resolvers
"""

from integrations import jsonplaceholder


def create_post_resolver(*_, title, body, userId=1):
    response = {'errors': None, 'success': True}
    try:
        data = {
            'title': title,
            'body': body,
            'userId': userId
        }
        post = jsonplaceholder.create_post(data)
        if post:
            response['post'] = post
        else:
            response['errors'] = ['The data entered is wrong']
            response['success'] = False
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response

def update_post_resolver(*_, id, title=None, body=None):
    response = {'errors': None, 'success': True}
    try:
        data = {}

        if title:
            data['title'] = title

        if body:
            data['body'] = body

        post = jsonplaceholder.update_post(id, data)
        if post:
            response['post'] = post
        else:
            response['errors'] = ['The data entered is wrong']
            response['success'] = False
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response

def delete_post_resolver(*_, id):
    response = {'errors': None, 'success': True}
    try:
        post = jsonplaceholder.delete_post(id)
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response
