import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "school_schedule.sqlite3"


def get_connection():
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            branch TEXT NOT NULL,
            max_weekly_hours INTEGER NOT NULL DEFAULT 24
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            weekly_hours INTEGER NOT NULL,
            level_group TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade INTEGER NOT NULL,
            section TEXT NOT NULL,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_id INTEGER NOT NULL,
            lesson_id INTEGER NOT NULL,
            teacher_id INTEGER NOT NULL,
            room_id INTEGER,
            day TEXT NOT NULL,
            hour INTEGER NOT NULL,
            UNIQUE (class_id, day, hour),
            UNIQUE (teacher_id, day, hour),
            FOREIGN KEY (class_id) REFERENCES classes(id),
            FOREIGN KEY (lesson_id) REFERENCES lessons(id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id),
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            room_type TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher_unavailability (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER NOT NULL,
            day TEXT NOT NULL,
            hour INTEGER NOT NULL,
            UNIQUE (teacher_id, day, hour),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    ensure_column(cursor, "schedules", "room_id", "INTEGER")
    seed_default_rooms(cursor)
    seed_default_users(cursor)

    conn.commit()
    conn.close()


def ensure_column(cursor, table_name: str, column_name: str, column_type: str):
    columns = cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
    exists = any(column[1] == column_name for column in columns)
    if not exists:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")


def seed_default_rooms(cursor):
    rooms = [
        ("Spor Salonu 1", "Beden Eğitimi"),
        ("Spor Salonu 2", "Beden Eğitimi"),
        ("Resim Atölyesi 1", "Resim"),
        ("Resim Atölyesi 2", "Resim"),
        ("Müzik Odası 1", "Müzik"),
        ("Müzik Odası 2", "Müzik"),
        ("Satranç Sınıfı 1", "Satranç"),
        ("Satranç Sınıfı 2", "Satranç"),
        ("Fen Laboratuvarı 1", "Fen Bilgisi"),
        ("Fen Laboratuvarı 2", "Fen Bilgisi"),
        ("Fen Laboratuvarı 3", "Fen Bilgisi"),
        ("Genel Derslik 1", "Genel"),
        ("Genel Derslik 2", "Genel"),
        ("Genel Derslik 3", "Genel"),
        ("Genel Derslik 4", "Genel"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO rooms (name, room_type) VALUES (?, ?)",
        rooms,
    )


def seed_default_users(cursor):
    users = [
        ("Sistem Yöneticisi", "Admin"),
        ("Öğretmen Kullanıcı", "Öğretmen"),
    ]
    cursor.execute(
        """
        DELETE FROM users
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM users
            GROUP BY name, role
        )
        """
    )
    for name, role in users:
        exists = cursor.execute(
            "SELECT 1 FROM users WHERE name = ? AND role = ?",
            (name, role),
        ).fetchone()
        if not exists:
            cursor.execute(
                "INSERT INTO users (name, role) VALUES (?, ?)",
                (name, role),
            )
