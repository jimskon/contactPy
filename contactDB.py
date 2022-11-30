
import mariadb

class contactDB:
  '''
  A class for interfacing with a contacts mysql database
  '''
  def __init__(self):
    '''
    Create a connection to the database
    '''
    HOST = "localhost"
    USER = "kenyon"
    DB = "kenyon"
    PASS="GambierOwls"
    self.mydb = mariadb.connect(
      host=HOST,
      user=USER,
      passwd=PASS,
      database=DB
    )
    return

  def find(self,search):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM contacts WHERE Last like '%"+search+"%' OR First like '%"+search+"%' OR Type like '%"+search+"%'");
    myresult = mycursor.fetchall()
    return(myresult)
    
  def findByLast(self,last):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM contacts WHERE Last like '%"+last+"%'");
    myresult = mycursor.fetchall()
    return(myresult)

  def findByFirst(self,first):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM contacts WHERE First like '%"+first+"%'");
    myresult = mycursor.fetchall()
    return(myresult)

  def delete(self,idnum):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("DELETE FROM contacts WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return '{"status","Error","reason":"'+ str(e) + '"}';
    return '{"status":"success"}'

  def add(self,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("INSERT INTO contacts(First,Last,Phone,Type) VALUES ('"+first+"','"+last+"','"+phone+"','"+ptype+"')")
      self.mydb.commit()
    except Exception as e:
      return '{"status":"Error","reason":"'+ str(e) + '"}';

    return '{"status":"success"}'

  def update(self,idnum,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("UPDATE contacts SET First = '"+first+"', Last ='"+last+"', Phone ='"+phone+"', Type ='"+ptype+"' WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return '{"status","Error","reason":"'+ str(e) + '"}';
    return '{"status":"success"}'
