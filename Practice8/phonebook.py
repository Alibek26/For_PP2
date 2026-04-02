from connect import execute, fetchall
import json

# Create table if not exists
execute("""
CREATE TABLE IF NOT EXISTS PhoneBook(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    phone VARCHAR NOT NULL
)
""")
print("PhoneBook table created (if it didn't exist).")

# Search for records by pattern
def search(pattern):
    # Calls the search function in PostgreSQL
    query = "SELECT * FROM search_phonebook(%s);"
    return fetchall(query, (pattern,))

# Insert or update a single user
def upsert(name, phone):
    # Calls the upsert procedure in PostgreSQL
    query = "CALL upsert_user(%s, %s);"
    execute(query, (name, phone))

# Bulk insert multiple users
def bulk_insert(users):
    """
    users: list of dictionaries, e.g.
    [
        {"name":"Bob","phone":"555-0000"},
        {"name":"Invalid","phone":"abc123"}
    ]
    """
    users_json = json.dumps(users)
    query = "CALL bulk_insert_users(%s::json);"
    execute(query, (users_json,))

# Retrieve a paginated list of users
def get_page(offset, limit):
    query = "SELECT * FROM get_phonebook_page(%s, %s);"
    return fetchall(query, (offset, limit))

# Delete user by name or phone
def delete(name=None, phone=None):
    query = "CALL delete_user(%s, %s);"
    execute(query, (name, phone))

# Example usage
# Insert or update a user
upsert("Alice", "123-4567")

# Search for a user by pattern
print("Search Alice:", search("Alice"))

# Bulk insert users
bulk_insert([
    {"name":"Bob","phone":"555-0000"},
    {"name":"Invalid","phone":"abc123"}  # This will be flagged as invalid
])

# Retrieve first 10 records
print("First 10 records:", get_page(0, 10))

# Delete a user by phone
delete(phone="555-0000")
print("After deletion:", get_page(0, 10))