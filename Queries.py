from Connector import Connection

class Queries:
    def __init__(self):
        self.con = Connection()

    def add_contact(self, fname, lname, group, number, email, address):
        query = "INSERT INTO contacts (fname, lname, contact_group, phone_no, email, address) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (fname, lname, group, number, email, address)
        return self.con.iud(query, values)
    
    def update_contact(self, fname, lname, group, number, email, address, id):
        query = "UPDATE contacts SET fname=%s, lname=%s, contact_group=%s, phone_no=%s, email=%s, address=%s WHERE id=%s"
        values = (fname, lname, group, number, email, address, id)
        return self.con.iud(query, values)

    def delete_contact(self, values):
        query = "DELETE FROM contacts WHERE id=%s"
        values = (values,)
        return self.con.iud(query, values)

    def fetch_contact(self):
        query = "SELECT * FROM contacts"
        return self.con.show(query)

    def add_note(self, note):
        query = "INSERT INTO notes (note) VALUES (%s)"
        values = (note,)
        return self.con.iud(query, values)

    def update_note(self, note, id):
        query = "UPDATE notes SET note=%s WHERE id=%s"
        values = (note, id)
        return self.con.iud(query, values)

    def delete_note(self, values):
        query = "DELETE FROM notes WHERE id=%s"
        values = (values,)
        return self.con.iud(query, values)

    def fetch_note(self):
        query = "SELECT * FROM notes"
        return self.con.show(query)

    def add_user(self, username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES (%s,%s,%s)"
        values = (username, email, password)
        return self.con.iud(query, values)

    def fetch_user(self):
        query = "SELECT username, password FROM users"
        return self.con.show(query)

    def add_category(self, category):
        query = "INSERT INTO categories (category) VALUES (%s)"
        values = (category,)
        return self.con.iud(query, values)

    def add_password(self, account, category, username, password):
        query = "INSERT INTO accounts (account, category, username, password) VALUES (%s,%s,%s,%s)"
        values = (account, category, username, password)
        return self.con.iud(query, values)

    def update_password(self, account, category, usrename, password, id):
        query = "UPDATE accounts SET account=%s, category=%s, username=%s, password=%s WHERE id=%s"
        values = (account, category, usrename, password, id)
        return self.con.iud(query, values)

    def fetch_category(self):
        query = "SELECT * from categories"
        return self.con.show(query)

    def fetch_password(self):
        query = "SELECT * from accounts"
        return self.con.show(query)

    def delete_category(self, values):
        query = "DELETE FROM categories WHERE category=%s"
        values = (values,)
        return self.con.iud(query, values)

    def delete_password(self, values):
        query = "DELETE FROM accounts WHERE id=%s"
        values = (values,)
        return self.con.iud(query, values)
