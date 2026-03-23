import sqlite3

def log_database_knowledgecards():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    results = cursor.execute("SELECT * FROM cards_knowledgecard")
    for result in results:
        print(result)
        
log_database_knowledgecards()