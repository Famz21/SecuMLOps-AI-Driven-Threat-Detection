from dotenv import load_dotenv, find_dotenv
import os

# Force reload the .env file
load_dotenv(find_dotenv(), override=True)

# Print the actual connection string being used
print("Current MongoDB URL:", os.getenv('MONGO_DB_URL'))

# Also print the file path to verify
print("ENV file location:", find_dotenv())