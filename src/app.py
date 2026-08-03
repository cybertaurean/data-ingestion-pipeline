import os
import time
import psycopg2

# 1. Grab database connection info from environment variables (Enterprise Practice)
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "mysecurepassword")

def connect_db():
    print(f"Connecting to database at {DB_HOST}:{DB_PORT}...", flush=True)
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASS
    )

def main():
    # Wait for database availability and insert records in a loop
    while True:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            # Generate mock ingestion metrics
            print("Successfully connected! Ingesting chunk data...", flush=True)
            cursor.execute(
                "INSERT INTO data_pipeline (source_system, records_processed, status) VALUES (%s, %s, %s);",
                ("CI_CD_Mock_API", 2500, "SUCCESS")
            )
            conn.commit()
            print("Chunk written successfully. Sleeping for 10 seconds...", flush=True)
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Database unavailable or error occurred: {e}. Retrying in 5s...", flush=True)
        
        time.sleep(10)

if __name__ == "__main__":
    main()
