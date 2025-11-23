from typing import List, Optional
from domain.user import User
from repositories.user_repository import UserRepository
from infra.db.database import get_db_connection

class UserRepositorySQLite(UserRepository):

    def list_all(self) -> List[User]:
        conn = get_db_connection()
        rows = conn.execute("SELECT * FROM users").fetchall()
        conn.close()
        return [User(id=row["id"], name=row["name"]) for row in rows]

    def get_by_id(self, user_id: int) -> Optional[User]:
        conn = get_db_connection()
        row = conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        conn.close()
        if row is None:
            return None
        return User(id=row["id"], name=row["name"])

    def create(self, name: str) -> User:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        return User(id=new_id, name=name)

    def update(self, user: User) -> None:
        conn = get_db_connection()
        conn.execute("UPDATE users SET name=? WHERE id=?", (user.name, user.id))
        conn.commit()
        conn.close()

    def delete(self, user_id: int) -> None:
        conn = get_db_connection()
        conn.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        conn.close()
