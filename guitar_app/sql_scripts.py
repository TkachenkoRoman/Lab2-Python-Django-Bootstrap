from django.db import connection

def load_data_from_files():
    cursor = connection.cursor()
    cursor.execute(""" DELETE FROM produser """)
    cursor.execute(""" DELETE FROM body """)
    cursor.execute(""" DELETE FROM bridge """)
    cursor.execute(""" DELETE FROM pickups """)
    cursor.execute(""" DELETE FROM guitar_types """)
    cursor.execute(""" DELETE FROM guitar """)
    cursor.execute("""LOAD DATA LOCAL INFILE 'produser.csv' INTO TABLE produser FIELDS TERMINATED BY ';'
                    LINES TERMINATED BY '\n';""")
    cursor.execute("""LOAD DATA LOCAL INFILE 'body.csv' INTO TABLE Body FIELDS TERMINATED BY ';'
                    LINES TERMINATED BY '\n';""")
    cursor.execute("""LOAD DATA LOCAL INFILE 'bridge.csv' INTO TABLE Bridge FIELDS TERMINATED BY ';'
                    LINES TERMINATED BY '\n';""")
    cursor.execute("""LOAD DATA LOCAL INFILE 'guitar_types.csv' INTO TABLE guitar_types FIELDS TERMINATED BY ';'
                    LINES TERMINATED BY '\n';""")
    cursor.execute("""LOAD DATA LOCAL INFILE 'pickups.csv' INTO TABLE pickups FIELDS TERMINATED BY ';'
                    LINES TERMINATED BY '\n';""")
    cursor.execute("""LOAD DATA LOCAL INFILE 'guitar.csv' INTO TABLE Guitar FIELDS TERMINATED BY ';'
                    LINES TERMINATED BY '\n' (name, string_amount, price, neck_material, Fretboard_material, Pick_guard,
                     Type_id, Body_id, Bridge_id, Pickups_id, Guitar_produser_id);""")

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

def get_statistics():
    cursor = connection.cursor()
    cursor.execute("CALL statistics();")
    return  dictfetchall(cursor)