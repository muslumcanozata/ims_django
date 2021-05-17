from ims.api.serializers import userSerializer

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': userSerializer(user, context={'request':request}).data
    }