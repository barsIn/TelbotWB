from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
sinc_link = f'postgresql+psycopg://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'

engine = create_engine(
    url=sinc_link,
    echo=False,
    pool_size=5,
    max_overflow=10
)
