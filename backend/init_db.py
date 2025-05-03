from sqlalchemy import create_engine
from .models import Base
from .config import get_settings

settings = get_settings()


def init_db():
    """
    Initialize the database by creating all tables.
    """
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!") 