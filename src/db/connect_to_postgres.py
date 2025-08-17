import psycopg2
from psycopg2 import OperationalError
from ..config.env_variables import settings


def create_connection():
    try:
        connection = psycopg2.connect(
            dbname=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            host="user_platform_db",
        )
        print("✅ Connection to PostgreSQL successful")
        return connection
    
    except OperationalError as e:
        print(f"❌ The error '{e}' occurred")
        return None
    
    
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()