import mysql.connector
class BookManager:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Abhi@123",
                database="library_db"
            )

            self.cursor = self.connection.cursor(dictionary=True)

            print("Database connected successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            query = "SELECT * FROM book"
            self.cursor.execute(query)

            records = self.cursor.fetchall()

            return records

        except Exception as e:
            print(e)
            return []

    def get_object(self, id):
        try:
            query = "Select * from book WHERE id=%s"

            self.cursor.execute(query, (id,))

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)
            return None

    def retrieve(self, id):
        try:
            record = self.get_object(id)

            if record is not None:
                print("Book Details")
                print("ID:", record["id"])
                print("Title:", record["title"])
                print("Author:", record["author"])
                print("Category:", record["category"])
                print("Price:", record["price"])
                print("Published Date:", record["published_date"])

            else:
                print("Book does not exist")

        except Exception as e:
            print(e)


    def post(self, **kwargs):
        try:
            query = """
            Insert into book
            (title, author, category, price, published_date)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                kwargs["title"],
                kwargs["author"],
                kwargs["category"],
                kwargs["price"],
                kwargs["published_date"]
            )

            self.cursor.execute(query, values)

            self.connection.commit()

            print("New book added successfully")

        except Exception as e:
            print(e)

    def put(self, id, **kwargs):
        try:
            # Check whether book exists
            record = self.get_object(id)

            if record is not None:

                placeholder = ""

                for key in kwargs.keys():
                    placeholder += key + "=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE book SET {placeholder} WHERE id=%s"

                values = list(kwargs.values())
                values.append(id)

                self.cursor.execute(query, values)

                self.connection.commit()

                print("Book details updated successfully")

            else:
                print("Book does not exist")

        except Exception as e:
            print(e)

    def delete(self, id):
        try:
            # Check whether book exists
            record = self.get_object(id)

            if record is not None:

                query = "DELETE FROM book WHERE id=%s"

                self.cursor.execute(query, (id,))

                self.connection.commit()

                print("Book deleted successfully")

            else:
                print("Book does not exist")

        except Exception as e:
            print(e)

manager = BookManager()

manager.post(
    title="Python Programming",
    author="van Rossum",
    category="Programming",
    price=50,
    published_date="2025-01-10"
)


print(manager.get())

print(manager.get_object(1))

manager.retrieve(1)

manager.put(
    1,
    title="Python Fullstack",
    price=600
)

manager.retrieve(1)

manager.delete(1)