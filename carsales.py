ordid=695
import cx_Oracle
con=cx_Oracle.connect('SYSTEM/batman@127.0.0.1/xe')
cur=con.cursor()


def addord(xid, oid):
    cur.execute("""update manager set sales={} where mid={}""".format(oid, xid))
    cur.execute("""commit""")

def bookc():
        print('Available cars:')
        cur.execute("""select * from car""")
        for i in cur.fetchall():
            print(i)
        book=input('Book a Car(y/n)? ')
        if book in ['y','Y']:
            c1=customer()
            c1.setcus(input('Name: '))
            c1.setmobile(9896875859)
            if c1.order_car(int(input('Car id: '))):
                global ordid
                ordid+=12
                xmid = int(input('Referred Manager id: '))
                c1.orderid=ordid
                c1.save2db()
                addord(xmid,ordid)
                print('Ordered under: ' + c1.cus)
                print('mobile: ' + str(c1.mobile))
                print('!!!  Kindly Note order id for further use  !!!')
                print('>>>>  Your order id:{} <<<<'.format(str(c1.orderid)))
                print('-'*35+'end'+'-'*35)
            else:
                print('----Invalid Car id----')
                print('--Select a valid one--')
                xx=input('Try again selecting(y/n)?')
                if xx in ['Y','y']:
                    bookc()
def mcheck(ck,xpass):
    try:
        cur.execute("""select {} from manager where pass={}""".format(ck,'\''+xpass+'\''))
        x=cur.fetchone()
        x[0]
        return True
    except:
        return False

def addcar(obj):
    cur.executemany("""insert into car values(:1,:2,:3,:4,:5)""",obj)
    cur.execute("""commit""")

def manage(mid):
    mch=int(input('1.print sales\n2.Customer Status check\n3.Add cars\n'))
    if mch==1:
        cur.execute("""select mid,mcontact,sales from manager where mid={}""".format(mid))
        for _ in cur.fetchall():
            print(_)
    elif mch==2:
        xidd=int(input('Order id: '))
        cur.execute("""select * from customer where oidd={}""".format(xidd))
        try:
            for _ in cur.fetchall():
                print(_)
        except:
            print('invalid customer id')
    elif mch==3:
        obj=[(int(input('Car Id:')),input('Car name:'),input('Car model:'),float(input('price(in lakh):')),input('Color:'))]
        addcar(obj)

class customer():
    def __init__(self,cus=None,mobile=None,orderid=None):
        self.cus = cus
        self.mobile = mobile
        self.orderid=orderid
        self.model=''
    def setcus(self, cus):
        self.cus = cus
    def setmobile(self, mobile):
        self.mobile = mobile
    def setorderid(self, orderid):
        self.orderid = orderid
    def order_car(self,cid):
        self.xx=1
        try:
            cur.execute("""select * from car where cid=:1""", (cid,))
            ot = cur.fetchone()
            print('\n','-' * 35 + 'Booked' + '-' * 35 + '\n'+'{}-{} :{}'.format(ot[1], ot[2], ot[4]))
            self.model = ot[2]
            print('Price: {}L'.format(ot[3]))
            print('-' * 35 + 'Booked' + '-' * 35)
            return True
        except:
            return False

    def save2db(self):
        cur.execute("""insert into customer values (:1,:2,:3,:4)""",(self.orderid,self.cus,self.mobile,self.model))
        cur.execute("""commit""")
    def cusinfo(self):
        return 'Customer name:{},mobile:{}'.format(self.cus,self.mobile)
    def __repr__(self):
        return 'Customer name:{},car:{},price:{}'.format(self.cus,self.name,self.price)

cur.execute("""drop table customer""")
cur.execute("""drop table car""")
cur.execute("""drop table manager""")


cur.execute("""create table car(cid number(6),name varchar(20),model varchar(12) primary key ,price number(6,3),color varchar(19))""")
cars=[(101,'BMW','e90',45.2,'black'),(102,'Suzuki','sx4',8.2,'blue'),(103,'mahindra','bolero',9.5,'creame white')]
cur.executemany("""insert into car values (:1,:2,:3,:4,:5)""",cars)
cur.execute("""create table customer(oidd number(6),cname varchar(30),mobile number (10),model references car(model))""")
cur.execute("""create table manager(mid number,pass varchar(20),mcontact number(10),sales number (6))""")
man=[(501,9558249995),(502,9558359695),(503,9558249969)]
cur.executemany("""insert into manager values (:1,'lego',:3,NULL)""",man)
cur.execute("""commit""")

def welcome():
    print('-'*35+'Welcome'+'-'*35+'')
    ch=int(input('1>Customer\n2>Manager\n3.exit\n'))
    if ch==1:
        bookc()
        welcome()
    elif ch==2:
        chk=int(input('Enter manager id: '))
        xpass=input('Enter password: ')
        if mcheck(chk,xpass):
            manage(chk)
        else:
            print('Invalid Authorisation')
        welcome()
    elif ch==3:
        exit(0)
    else:
        print('---invalid option')
        welcome()


welcome()