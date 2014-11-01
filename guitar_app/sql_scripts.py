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

def set_up_vars():
    cursor = connection.cursor()
    cursor.execute("""  use guitar_schema;
                        SET GLOBAL TRIGGER_GUITAR_AFTER_INSERT_DISABLED = 0;
                        SET @global.TRIGGER_GUITAR_AFTER_UPDATE_DISABLED = 0;
                        SET @global.TRIGGER_GUITAR_BEFORE_DELETE_DISABLED = 0;
                        """)

update = "checked"
delete = "checked"

def disable_history_insert(disable):
    cursor = connection.cursor()
    if disable == True:
        cursor.execute("UPDATE `Variables` SET value=1 where name='TRIGGER_GUITAR_AFTER_INSERT_DISABLED'")
    if disable == False:
        cursor.execute("UPDATE `Variables` SET value=0 where name='TRIGGER_GUITAR_AFTER_INSERT_DISABLED'")

def get_trigger_insert_value():
    cursor = connection.cursor()
    cursor.execute("SELECT value from `Variables` where name='TRIGGER_GUITAR_AFTER_INSERT_DISABLED';")
    res = cursor.fetchone()
    if res == 1:
        return False
    if res == 0:
        return True

