"""
GraghQL API resolvers
"""

from datetime import datetime

from integrations import jsonplaceholder

from .common import query, mutation


########
# Query
########

@query.field('currentDay')
def resolve_current_day(*_):
    return datetime.now().strftime('%d-%m-%Y')

@query.field('listPosts')
def resolve_list_posts(*_):
    response = {'errors': None, 'success': True}
    try:
        response['posts'] = jsonplaceholder.list_posts()
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response

@query.field('getPost')
def resolve_retrieve_post(*_, id):
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


############
# Mutations
############

@mutation.field('createPost')
def resolve_create_post(*_, title, body, userId=1):
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

@mutation.field('updatePost')
def resolve_update_post(*_, id, title=None, body=None):
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

@mutation.field('deletePost')
def resolve_delete_post(*_, id):
    response = {'errors': None, 'success': True}
    try:
        post = jsonplaceholder.delete_post(id)
    except Exception as e:
        response['errors'] = [str(e)]
        response['success'] = False
    return response
