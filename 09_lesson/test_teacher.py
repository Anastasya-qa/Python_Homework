import pytest
from sqlalchemy import create_engine, text
from TeacherTable import TeacherTable  # Импортируем класс
import random  # Импорт случайных значений


# Строка подключения к базе данных
db_connection_string = ("postgresql+psycopg2://"
                        "sauberg:nasa2005"
                        "@127.0.0.1:5432/QA")
new_teacher_id = None


@pytest.fixture
def teacher_db():
    # Фикстура для инициализации класса работы с таблицей teacher
    return TeacherTable(db_connection_string)


@pytest.fixture
def db_connection():
    # Фикстура для прямого подключения к базе данных
    engine = create_engine(db_connection_string)
    conn = engine.connect()
    yield conn
    conn.close()


def test_create_teacher(teacher_db, db_connection):
    global new_teacher_id

    new_teacher_id = random.randint(1000, 9999)
    email = "sauber@list.ru"
    group_id = 141

    # Вызываем тестируемый метод создания
    teacher_db.create_new_teacher(new_teacher_id, email, group_id)

    # Проверяем через прямой запрос, что запись появилась
    result = db_connection.execute(
        text("SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": new_teacher_id}
    ).mappings().first()

    assert result is not None
    assert result["email"] == email
    assert result["group_id"] == group_id


def test_update_teacher(teacher_db, db_connection):
    teacher_db.update_teacher(new_teacher_id, "nanamimimimi@gmail.ru", 42)

    result = db_connection.execute(
        text("SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": new_teacher_id}
    ).mappings().first()

    assert result["email"] == "nanamimimimi@gmail.ru"
    assert result["group_id"] == 42


def test_delete_teacher(teacher_db, db_connection):
    teacher_db.delete_teacher(new_teacher_id)

    result = db_connection.execute(
        text("SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": new_teacher_id}
    ).mappings().first()

    assert result is None
