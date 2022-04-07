from datetime import datetime

from integrations import jsonplaceholder


def current_day_resolver(*_):
    return datetime.now().strftime('%d-%m-%Y')

def list_posts_resolver(*_):
    response = {'errors': None, 'success': True}
    try:
        response['posts'] = jsonplaceholder.list_posts()
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response

def retrieve_post_resolver(*_, id):
    response = {'errors': None, 'success': True}
    try:
        post = jsonplaceholder.retrieve_post(id)
        if post:
            response['post'] = post
        else:
            response['errors'] = ['The ID was not found']
            response['success'] = False
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response
