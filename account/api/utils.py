def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'user_name': user.username
    }
