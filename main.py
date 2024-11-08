import mysql.connector


def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',  
            database='Vegetali',  
            user='root',  
            password='password'  
        )
        if conn.is_connected():
            print("Connessione al database avvenuta con successo!")
            return conn
    except mysql.connector.Error as e:
        print(f"Errore nella connessione al database: {e}")
        return None

mycursor.execute("""
  CREATE TABLE IF NOT EXISTS Frutta (
    id VARCHAR(3),
    nome VARCHAR(255) NOT NULL,
    colore VARCHAR(50),
    stagione VARCHAR(50),
    vitamina_principale VARCHAR(50),
    calorie INT
  );""")

def inserisci_data():
    frutta_data = [
        ('1','Mela', 'Rosso', 'Autunno', 'C', 52),
        ('2','Banana', 'Gialla', 'Tutto l\'anno', 'K', 89),
        ('3','Arancia', 'Arancione', 'Inverno', 'C', 47),
        ('4','Pera', 'Verde', 'Autunno', 'C', 57),
        ('5','Uva', 'Nero', 'Autunno', 'K', 69),
        ('6','Fragola', 'Rosso', 'Primavera', 'C', 32),
        ('7','Ananas', 'Giallo', 'Tutto l\'anno', 'C', 50),
        ('8','Avocado', 'Verde', 'Tutto l\'anno', 'K', 160),
        ('9','Ciliegie', 'Rosso', 'Estate', 'C', 63),
        ('10','Melone', 'Arancione', 'Estate', 'A', 34)
    ]

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:

            cursor.executemany("""
                INSERT INTO Frutta (id, nome, colore, stagione, vitamina_principale, calorie)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, frutta_data)
            conn.commit()
            print(f"{cursor.rowcount} record inseriti nel database.")
        except mysql.connector.Error as e:
            print(f"Errore durante l'inserimento dei dati: {e}")
        finally:
            cursor.close()
            conn.close()


def verifica_data():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Frutta")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()

inserisci_data()

verifica_data()

def estrai_all_data():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Frutta")
        rows = cursor.fetchall()
        for row in rows:
            print(row)  
        cursor.close()
        conn.close()

estrai_all_data()