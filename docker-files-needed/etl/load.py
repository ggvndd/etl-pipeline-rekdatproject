import psycopg2
import os

def load_to_postgresql(data, db_name=None, user=None, password=None, host=None, port=None):
    """
    Loads the provided data into a PostgreSQL table.

    Parameters:
        data (list of dict): Data to be inserted into the database.
        db_name (str): Name of the PostgreSQL database.
        user (str): Database user.
        password (str): Database password.
        host (str): Database host address.
        port (str): Database port.

    Returns:
        None
    """
    # Use environment variables or default values for database credentials
    db_name = db_name or os.getenv("DB_NAME", "etl_db")
    user = user or os.getenv("DB_USER", "postgres")
    password = password or os.getenv("DB_PASSWORD", "joshuadun")
    host = host or os.getenv("DB_HOST", "localhost")
    port = port or os.getenv("DB_PORT", "5432")

    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()

        # Insert data into table
        for record in data:
            cursor.execute(
                """
                INSERT INTO trending_topics (platform, topic, source)
                VALUES (%s, %s, %s)
                """,
                (record.get("platform"), record.get("topic"), record.get("source"))
            )

        # Commit changes
        connection.commit()
        print(f"Inserted {len(data)} records into PostgreSQL.")

    except psycopg2.OperationalError as oe:
        print(f"Database connection failed: {oe}")

    except psycopg2.IntegrityError as ie:
        print(f"Data integrity issue: {ie}")
        connection.rollback()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
