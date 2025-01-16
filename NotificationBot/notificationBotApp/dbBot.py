import sqlite3

async def db_connection():
    try:
        with sqlite3.connect('notificationDB.db') as connection:
            db_cursor = connection.cursor()
            db_cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS notifications (
	            "id"	INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
	            "user_name"	TEXT NOT NULL,
	            "notification_id"	TEXT NOT NULL UNIQUE,
	            "notification_data"	TEXT NOT NULL,
	            "notification_date"	TEXT NOT NULL
                )'''
                )
    except sqlite3.Error as db_error:
        return db_error
    else:
        return db_cursor, connection
    
async def add_notification_DB(user_name, notification_id, notification_text, notification_date):
    db_cursor, connection = await db_connection()
    try:
        db_cursor.execute('INSERT INTO notifications (user_name, notification_id, notification_data, notification_date) VALUES (?, ?, ?, ?)', (user_name, notification_id, notification_text, notification_date))
    except sqlite3.Error as sql_error:
        return sql_error
    else:
        connection.commit()
        return 'Query has done!'
