import psycopg2
from psycopg2 import Error
class Dbconnect():
    def __init__(self, host, port, dbname):
        self._host = host
        self._port = port
        self._dbname = dbname
        self.authontification = []
        self.conn = None

    def _auth(self, username: str, password: str) -> bool:
        self.authontification.append(username)
        self.authontification.append(password)
        return True

    def connect(self):
        if len(self.authontification) == 0:
            return "postgres Auth. Error  : plaise login first  ! "
        try:
            self.conn = psycopg2.connect(
                database=self._dbname, user=self.authontification[0], sslmode='prefer', host=self._host, port=self._port, password=self.authontification[1])
            self.conn.set_session(autocommit=True)
            print(self.conn.get_dsn_parameters(), "\n")
        except(Exception, Error) as error:
            print("postgressql error : ",  error)
    def getfiliere(self) :
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT (acronyme) FROM filiere")
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
        ndata = ["-----------"]
        for i in data : 
            ndata.append(i[0]) 
        return tuple(list(ndata))
    def getdiplome(self) :
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT (acronyme) FROM diplome")
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
        ndata = ["-----------"]
        for i in data : 
            ndata.append(i[0]) 
        return tuple(list(ndata))
    def getcsp(self) :
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT (titre) FROM categorie_csp")
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
        ndata = ["-----------"]
        for i in data : 
            ndata.append(i[0]) 
        return tuple(list(ndata))
    def getprovince(self) :
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT (nom) FROM province")
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
        ndata = ["-----------"]
        for i in data : 
            ndata.append(i[0]) 
        return tuple(list(ndata))
    def getacademy(self) :
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT (nom) FROM region")
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
        ndata = ["-----------"]
        for i in data : 
            ndata.append(i[0]) 
        return tuple(list(ndata))
    def getserie(self) :
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT (libelle) FROM serie_baccalaureat")
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
        ndata = ["-----------"]
        for i in data : 
            ndata.append(i[0]) 
        return tuple(list(ndata))
    def getbs(self):
        data  ={}
        data["bac_serie"] = "Bac Pro -Services de Restauration"
        cursor = self.conn.cursor()
        first_query = "SELECT id FROM  serie_baccalaureat WHERE libelle='{}'".format(data["bac_serie"])
        try:
            cursor.execute(first_query)
            a = cursor.fetchone()
            data["bac_serie"] = a[0]
        except (Exception, Error) as _config_error:
            print(_config_error)
            return False
        return data
admI = Dbconnect("localhost", 5432, "inscription2")
admI._auth('fiberx01', '0000')
admI.connect()   
pays  = admI.getbs()

print(pays)
