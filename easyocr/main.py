import os
import easyocr
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gowshik@123",
    database="mydb"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Check if the table 'Bib_Data' exists
cursor.execute("SHOW TABLES LIKE 'Bib_Data'")
table_exists = cursor.fetchone()

if not table_exists:
    # Create the 'employees' table if it doesn't exist
    create_table_query = """
    CREATE TABLE Bib_Data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Bib_No VARCHAR(255),
        Img1 VARCHAR(300),
        Img2 VARCHAR(300),
        Img3 VARCHAR(300),
        Img4 VARCHAR(300),
        Img5 VARCHAR(300),
        Img6 VARCHAR(300),
        Img7 VARCHAR(300),
        Img8 VARCHAR(300),
        Img9 VARCHAR(300),
        Img10 VARCHAR(300)
    )
    """
    cursor.execute(create_table_query)
    print("Table 'employees' created.")
else:
    print("Table already created..!")


def is_number(input_string):
    try:
        # Try to convert the input string to an integer
        int(input_string)
        return True
    except ValueError:
        # If the conversion fails, it's not a number
        return False


def is_valid_bib_number(text):
    # Check if the string has exactly 4 characters
    if len(text) != 4:
        return False

    # Check if the first character is 'F'
    if text[0] != 'F':
        return False

    # Check if the remaining characters are digits
    if not text[1:].isdigit():
        return False

    # If all checks pass, it's a valid bib number
    return True


# Replace 'your_image_directory' with the path to your image directory
image_directory = r'E:\Marathon images (2)\Marathon images'
# Initialize the EasyOCR reader with the desired language(s)
reader = easyocr.Reader(['en'])
# Get a list of image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
# Process each image and print the desired text

# Get input from the user with a prompt
#Bib_No = input("Enter the BIB Number : ")

for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    result = reader.readtext(image_path)

    for ele in result:
        bib = False
        if len(ele[1])==5 and ' ' not in ele[1]:
            if is_number(ele[1]) and ele[1].startswith("2") :
                bib = True
            #elif is_valid_bib_number(ele[1]):
                #bib = True
        if bib:
            binary_key = ele[1]

            # Define your query to check if the data is already present
            query = "SELECT * FROM Bib_Data WHERE Bib_No = %s"

            # Execute the query with the binary key as a parameter
            cursor.execute(query, (binary_key,))

            # Fetch the result
            result = cursor.fetchone()

            # Check if data is already present
            if result:
                cursor.execute("SELECT * FROM Bib_Data WHERE Bib_No = %s", (ele[1],))
                result = cursor.fetchone()
                if result[2]==image_file:
                    continue
                elif result[2] is not None and result[3] is None: #for img2
                    update_query = "UPDATE Bib_Data SET Img2 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-2....!")
                elif result[3]==image_file:
                    continue
                elif result[3] is not None and result[4] is None: #for img3
                    update_query = "UPDATE Bib_Data SET Img3 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-3....!")
                elif result[4]==image_file:
                    continue
                elif result[4] is not None and result[5] is None: #for img4
                    update_query = "UPDATE Bib_Data SET Img4 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-4....!")
                elif result[5]==image_file:
                    continue
                elif result[5] is not None and result[6] is None: #for img5
                    update_query = "UPDATE Bib_Data SET Img5 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-5....!")
                elif result[6]==image_file:
                    continue
                elif result[6] is not None and result[7] is None: #for img6
                    update_query = "UPDATE Bib_Data SET Img6 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-6....!")
                elif result[7] == image_file:
                    continue
                elif result[7] is not None and result[8] is None:  # for img7
                    update_query = "UPDATE Bib_Data SET Img7 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-7....!")
                elif result[8] == image_file:
                    continue
                elif result[8] is not None and result[9] is None:  # for img8
                    update_query = "UPDATE Bib_Data SET Img8 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-8....!")
                elif result[9] == image_file:
                    continue
                elif result[9] is not None and result[10] is None:  # for img9
                    update_query = "UPDATE Bib_Data SET Img9 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-9....!")
                elif result[10] == image_file:
                    continue
                elif result[10] is not None and result[11] is None:  # for img10
                    update_query = "UPDATE Bib_Data SET Img10 = %s WHERE Bib_No = %s"
                    values = (image_file, ele[1])
                    cursor.execute(update_query, values)
                    print("Data is updating for image-10....!")
                elif result[11] is not None:
                    continue
                conn.commit()
            else :
                insert_query = "INSERT INTO Bib_Data (Bib_No, Img1) VALUES (%s, %s)"
                values = (ele[1], image_file)
                cursor.execute(insert_query, values)
                print("Data is updating for image-1....!")
                conn.commit()

conn.commit()
cursor.close()
conn.close()