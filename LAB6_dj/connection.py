import MySQLdb


class Connection:

    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.db = db
        self.password = password
        self.host = host
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset='utf8',
                use_unicode=True
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Services:
    def __init__(self, db_connection, service_price, service_type, service_class_of_price):
        self.db_connection = db_connection.connection
        self.service_price = service_price
        self.service_type = service_type
        self.service_class_of_price = service_class_of_price

    def save(self):
        c = self.db_connection.cursor()
        c.execute('INSERT INTO lab6_dj_servicemodel (service_price, service_type, service_class_of_price) '
                  'VALUES (%s, %s, %s)',
                  (self.service_price, self.service_type, self.service_class_of_price))
        self.db_connection.commit()
        c.close()

    def delete(self):
        c = self.db_connection.cursor()
        c.execute('DELETE FROM lab6_dj_servicemodel WHERE service_price=5000')
        self.db_connection.commit()
        c.close()

    def update(self):
        c = self.db_connection.cursor()
        c.execute('UPDATE lab6_dj_servicemodel SET service_price = 0 WHERE id = 3')
        self.db_connection.commit()
        c.close()

con = Connection('dbuser', '123', 'service')

with con:
    service=Services(con, '7000', 'Окна', 'Низкий класс')
    service.save()
    #service.delete()
    service.update()