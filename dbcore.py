from database import engine
from sqlalchemy import text, insert, select, desc, delete
from models import metadata_obj, subscribers_table, history_table
import datetime as dt


def create_tabels():
    metadata_obj.create_all(engine, checkfirst=True)


def delete_tables():
    metadata_obj.drop_all(engine)


def insert_history(user_id, good_id):
    create_tabels()
    with engine.connect() as conn:
        stmt = insert(history_table).values(
            {'user_id': user_id, 'good_id': good_id}
        )
        conn.execute(stmt)
        conn.commit()


def insert_subscribers(user_id, good_id):
    create_tabels()
    with engine.connect() as conn:
        stmt = insert(subscribers_table).values(
            {'user_id': user_id, 'good_id': good_id}
        )
        conn.execute(stmt)
        conn.commit()


def select_history():
    stmt = select(history_table).order_by(desc('req_date'))
    with engine.connect() as conn:
        res = conn.execute(stmt).fetchmany(5)
    return res


def select_subscribers():
    stmt = select(subscribers_table.c['user_id', 'good_id'])
    with engine.connect() as conn:
        res = conn.execute(stmt).fetchall()
    return res


def delete_subscriber(user_id, good_id):
    delete_stmt = delete(subscribers_table).where(subscribers_table.c.user_id == user_id, subscribers_table.c.good_id == good_id)
    with engine.connect() as conn:
        conn.execute(delete_stmt)
        conn.commit()


def delete_subscriber(user_id):
    delete_stmt = delete(subscribers_table).where(subscribers_table.c.user_id == user_id)
    with engine.connect() as conn:
        conn.execute(delete_stmt)
        conn.commit()

# create_tabels()
# delete_tables()
