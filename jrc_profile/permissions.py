import requests

from rest_framework.permissions import BasePermission


AUTH_API = 'https://auth.jrc.no/'

def check_token(token):
    r = requests.post(
        AUTH_API + 'check-token/',
        data={'token': token}
    )
    return type(r.json()) is not str or 'userid' not in r.json().keys()


class HasValidJrcAuthToken(BasePermission):
    '''
    Only allow access if the auth-token HTTP header is valid.
    '''
    def has_permission(self, request, view):
        assert 'HTTP_AUTH_TOKEN' in request.META.keys(), "Http-Auth-Token header not set"
        return check_token(request.META['HTTP_AUTH_TOKEN'])
