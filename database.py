import sqlite3

DATABASE = "cyberpulse.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_type TEXT NOT NULL,
            target TEXT NOT NULL,
            risk_score INTEGER,
            risk_level TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_scan(scan_type, target, risk_score, risk_level):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO scans
        (scan_type, target, risk_score, risk_level)
        VALUES (?, ?, ?, ?)
    """, (
        scan_type,
        target,
        risk_score,
        risk_level
    ))

    connection.commit()
    connection.close()


def get_scans():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM scans
        ORDER BY id DESC
    """)

    scans = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return scans