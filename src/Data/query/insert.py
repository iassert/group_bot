class INSERT:
    userbot = """
        INSERT INTO userbots
        VALUES ('{phone}', {creator_id}, {user_id})
    """

    messages = """
        INSERT INTO messages
        VALUES ({me_id}, {from_user_id}, {msg_id})
    """