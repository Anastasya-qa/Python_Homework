from sqlalchemy import create_engine, text


class TeacherTable:
    __scripts = {
        "insert_new": text(
            "INSERT INTO teacher(teacher_id, email, group_id) "
            "values (:teacher_id, :email, :group_id)"),
        "update_teacher": text(
            "UPDATE teacher "
            "SET email = :email, group_id = :group_id "
            "WHERE teacher_id = :teacher_id"),
        "delete_by_id": text(
            "DELETE FROM teacher WHERE teacher_id = :teacher_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_new_teacher(self, teacher_id, email, group_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["insert_new"],
            {
                "teacher_id": teacher_id,
                "email": email,
                "group_id": group_id
            }
        )
        conn.commit()
        conn.close()

    def update_teacher(self, teacher_id, email, group_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["update_teacher"],
            {
                "teacher_id": teacher_id,
                "email": email,
                "group_id": group_id
            }
        )
        conn.commit()
        conn.close()

    def delete_teacher(self, teacher_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete_by_id"],
            {
                "teacher_id": teacher_id
            }
        )
        conn.commit()
        conn.close()
