import pymysql

def connect_to_database(host, user, password, db):
    """Connect to the MySQL database and return the connection object."""
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        print("Connection successful")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None
    
def close_connection(connection):   
    """Close the database connection."""
    if connection:
        try:
            connection.close()
            print("Connection closed")
        except pymysql.MySQLError as e:
            print(f"Error closing connection: {e}") 

def main():
    # Database connection parameters
    host = 'localhost'
    user = 'root'  # Replace with your MySQL username      
    password = 'root'  # Replace with your MySQL password
    db = 'biblioteca'  # Replace with your MySQL database name   
    connection = connect_to_database(host, user, password, db)
    if connection:
        # Perform database operations here
        pass  # Replace with your database operations

        # Close the connection after operations
        close_connection(connection)
    else:   
        print("Failed to connect to the database.") 
        return
if __name__ == "__main__":      
    main()
