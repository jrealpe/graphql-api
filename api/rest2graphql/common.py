"""
Rest2GraphQL API common
"""

from ariadne import ObjectType


query = ObjectType('Query')

mutation = ObjectType('Mutation')
