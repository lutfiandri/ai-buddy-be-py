from typing import Generator
from sqlmodel import Session

from app.core.sql import engine


def db_session() -> Generator[Session, None, None]:
    """
    Create sqlmodel session

    Usage:
    ---

    To use this function, call it to create a session, and then use the session
    to perform database operations. You can add objects to the session using
    the `add()` method, and commit changes using the `commit()` method.

    Example:
    ---
    ```python
    with db_session() as session:
        obj = MyModel(name="Object")
        session.add(obj)
        session.commit()
    ```

    You can also perform multiple transactions within the session:
    ```python
    with db_session() as session:
        obj1 = MyModel(name="Object 1")
        obj2 = MyModel(name="Object 2")
        session.add(obj1)
        session.add(obj2)
        session.commit()

        obj3 = MyModel(name="Object 3")
        obj4 = MyModel(name="Object 4")
        session.add(obj3)
        session.add(obj4)
        session.commit()
    ```

    """
    with Session(engine) as session:
        yield session
