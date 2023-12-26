class SELECT:
    phone_userbots = "SELECT phone FROM userbots;"
    creator_id = """
        SELECT creator_id
        FROM userbots
        WHERE user_id = {user_id}
        LIMIT 1;
    """
    msg_id = """
        SELECT msg_id
        FROM messages
        WHERE me_id = {me_id} AND from_user_id = {from_user_id}
        LIMIT 1;
    """
    from_user_id = """
        SELECT from_user_id
        FROM messages
        WHERE me_id = {me_id} AND msg_id = {msg_id}
        LIMIT 1;
    """