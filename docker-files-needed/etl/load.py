import psycopg2

def load_to_postgresql(data, db_name="etl_db", user="postgres", password="joshuadun", host="localhost", port="5432"):
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
                (record["platform"], record["topic"], record["source"])
            )

        # Commit changes
        connection.commit()
        print(f"Inserted {len(data)} records into PostgreSQL")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
