class CREATE:
    userbots = """
    CREATE TABLE IF NOT EXISTS userbots (
        phone         TEXT       NOT NULL    UNIQUE,
        creator_id    NUMERIC    NOT NULL,
        user_id       NUMERIC    NOT NULL    UNIQUE,

        PRIMARY KEY(user_id)
    )
    """

    messages = """
    CREATE TABLE IF NOT EXISTS messages (
        me_id           NUMERIC    NOT NULL,
        from_user_id    NUMERIC    NOT NULL,
        msg_id          NUMERIC    NOT NULL,

        FOREIGN KEY(me_id) REFERENCES userbots(user_id)
    )
    """
