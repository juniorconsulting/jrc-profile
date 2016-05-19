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
    Fall back to IsAdminUser when browsing the API.
    '''
    def has_permission(self, request, view):
        if 'application/json' in request.META['HTTP_ACCEPT']:
            assert 'HTTP_AUTH_TOKEN' in request.META.keys(), \
                "Http-Auth-Token header not set"
            return check_token(request.META['HTTP_AUTH_TOKEN'])
        return request.user and request.user.is_staff
