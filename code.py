import datetime
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk


def main():
    global list3, conn, window, c
    list3 = ["Commercial building", "Street shops", "Government buildings", "Residential areas",
             "Shopping mall",
             "Hospital", "Industrial Buildings", "Parks", "Others"]

    no = ''
    conn = sqlite3.connect("newest.db")  # input("Select new or exisitng db: "))
    window = tk.Tk()
    window.title("infected area database")
    # title = tk.Label(text="COVID-19 tracker")
    # title.pack()
    print("connected!")
    c = conn.cursor()

    label = tk.LabelFrame(window, text="Admin login", font=("Arial", 15), padx=10, pady=10)
    label.pack(padx=15, pady=15)
    label2 = tk.Label(label, text="User name: ", font=("Arial", 12)).pack()
    entry2 = tk.Entry(label, width=40, font=("Arial", 10))
    entry2.pack()
    label3 = tk.Label(label, text="Passcode: ", font=("Arial", 12)).pack()
    entry = tk.Entry(label, width=40, font=("Arial", 10))
    entry.pack()

    def temp2():

        test = tk.Label(window, text="Insert your records to check:", font=("Arial", 13))
        test.pack()
        submit['state'] = "disabled"
        submit2['state'] = "disabled"
        mode = 'A'
        menus(window, c, 0, mode)

    def temp():

        try:
            val3 = entry2.get()
            val = int(entry.get())
            print(val, val3)
            c.execute(""" select * from admin_details where User_tag = (?) and UserName = (?)""", (val, val3))
            if not c.fetchall():
                test2 = tk.Label(window, text="invalid input!!! ")
                test2.pack()
                return

            test = tk.Label(window, text="Confirmed cases insertion: ", font=("Arial", 13))
            test.pack()
            submit['state'] = "disabled"
            submit2['state'] = "disabled"
            mode = 'U'
            menus(window, c, val, mode)

        except ValueError:
            test = tk.Label(window, text="invalid input!!! ")
            test.pack()

    submit = tk.Button(label, text="Submit", width=15, command=temp)
    submit.pack()
    submit2 = tk.Button(window, text="Log in as user", font=("Arial", 20), width=15, command=temp2)
    submit2.pack()
    window.mainloop()
    conn.commit()
    conn.close()


""" while (no != '.quit'):
        no = input("Select option: ")
        if no == ".view":
            tb_name = input("Name of table: ")
            # c.execute("INSERT INTO employees VALUES ('3','Cha",inputm',?);)

        elif no == ".3":  # ".make_tb":
            create_tb(c)
            conn.commit()
        elif no == ".get":
            view_tb(c)
        elif no == ".insert":
            conn.commit()
"""


def menus(window, c, tab, mode):
    global record1,disrec
    k= FALSE
    record1= ''
    mydict = ["Central and western districts", "Wan Chai", "Eastern district", "Southern District"]
    lisits = [("Bonham Road"), ("Conaught Road"), ("Kennedy Road"), ("Queen's Road east"),
              ("Queen's Road west"), ("Gloucester Road"), ("Hennessy Road"),
              ("Yee Wo Street"),
              ("Java road"), ("King's road (Tin Hau)"), ("King's road (North Point)"),
              ("King's road (Quarry Bay)"),
              ("Taikoo Shing road"), ("Hong On Street"), ("Electric street"),
              ("Pok Fu Lam Road"), ("Aberdeen Main Road")]
    list6 = ["Male", "Female"]
    list7 = ["<18", "18-25", "26-35", "36-50", "51-60", ">60"]
    strlis = {'Central and western districts': ["Bonham Road", "Conaught Road", "Kennedy Road"],
              'Wan Chai': ["Queen's Road east","Queen's Road west", "Gloucester Road", "Hennessy Road",
              "Yee Wo Street"],
              'Eastern district': ["Java road","King's road (Tin Hau)", "King's road (North Point)","King's road (Quarry Bay)",
              "Taikoo Shing road", "Hong On Street", "Electric street"],
              'Southern District':["Pok Fu Lam Road", "Aberdeen Main Road"]}

    def show(event):
        adminstreet['values'] = strlis[Distr.get()]
        c.execute(
            "select d2.Street_name from District_street d, Street_details d2  where d.Street_ID = d2.Street_ID and d.DistrictID=(?) ",
            (mydict.index(Distr.get()) + 11,))
        disrec = print(c.fetchall())

    def show2(event):
        print(adminstreet.get())

    vdate_label = Label(window, text="Date of visit: ", font=("Arial", 12)).pack()
    vdate = Entry(window, width=30)
    vdate.pack()
    vdateinp = StringVar()
    vdateinp = vdate.get()

    # vdate_label.grid(row = 0, column = 0, sticky = W, pady = 2)
    # vdate_label.grid(column=0, row=0,)
    # vdate_label.grid(row=0,column=0)

    if mode == 'U':
        Type = Label(window, text="Gender : ", font=("Arial", 12)).pack()
        sex = ttk.Combobox(window, value=list6, width=25)
        sex.bind("<<ComboboxSelected>>")
        sex.current(0)
        sex.pack()

        Type = Label(window, text="Age range of the person: ", font=("Arial", 12)).pack()
        age = ttk.Combobox(window, value=list7, width=25)
        age.bind("<<ComboboxSelected>>")
        age.current(0)
        age.pack()


    loca_nm = Label(window, text="Name of building: ", font=("Arial", 12)).pack()
    location_nm = Entry(window, width=30)
    location_nm.pack()
    locainp = StringVar()

    District_label=Label(window, text="District of the location: ", font=("Arial", 12)).pack()
    Distr = ttk.Combobox(window, value=list(strlis.keys()), width=25)
    Distr.bind("<<ComboboxSelected>>", show)
    # Distr.current(0)
    # Distr.grid(row=2,column=0,padx=2,pady=2)
    Distr.pack()
    ty = Distr.get()
    ty = print(Distr.get())

    str_nm = Label(window, text="Name of street: ", font=("Arial", 12)).pack()
    adminstreet = ttk.Combobox(window, width=25)  # Entry(window, width=30)
    adminstreet.bind("<<ComboboxSelected>>",show2)
    #adminstreet.current(0)
    adminstreet.pack()
    streetinp = StringVar()

    Type = Label(window, text="Type of the location: ", font=("Arial", 12)).pack()
    conf2 = StringVar()
    conf2.set(list3[0])
    inp2 = conf2.get()
    type = ttk.Combobox(window, value=list3, width=25)
    type.bind("<<ComboboxSelected>>")
    type.current(0)
    type.pack()

    def userint():
        print(location_nm.get(), vdate.get())
        # print(list1.index(Distr.get()), list3.index(type.get()))

        if mode == 'U':
            print("inserted in to user")
            c.execute("""INSERT INTO case_records  ( User_tag,visit_date,place_name,District_ID,Type_ID,Street_ID,Sex,Age_range)
            VALUES(:usernm,:vdate,:pname,:did,:ltype,:street,:sex,:age)""",
                      {
                          'usernm': tab,
                          'vdate': vdate.get(),
                          'pname': location_nm.get(),
                          'did': mydict.index(Distr.get()) + 11,
                          'ltype': list3.index(type.get()) + 1,
                          'street': lisits.index(adminstreet.get()) + 100,
                          'sex': sex.get(),
                          'age': age.get()

                      })

            c.execute("""select Street_ID, DistrictID from District_street d where d.DistrictID = :DisID and 
                        d.Street_ID =:streetID """, {
                'DisID': mydict.index(Distr.get()) + 11,
                'streetID': lisits.index(adminstreet.get()) + 100
            })
            if not c.fetchall():
                c.execute("""INSERT INTO District_street(DistrictID,Street_ID) values(:DisID,:streetID)""",
                          {
                              'DisID': mydict.index(Distr.get()) + 11,
                              'streetID': lisits.index(adminstreet.get()) + 100
                          }
                          )

        adminstreet.delete(0, END)
        location_nm.delete(0, END)
        vdate.delete(0, END)
        type.current(0)
        Distr.current(0)
        if mode == 'U':
            sex.current(0)
            age.current(0)
        conn.commit()

    def regusers():
        c.execute("""select u.visit_date, u.place_name,d.District_name,l.location_name,s.Street_name from case_records u, 
                        District_type d,location l,Street_details s,District_street d1
                        where 
                        u.visit_date= (?) and u.place_name = (?) AND u.Street_ID =d1.Street_ID and d1.Street_ID= s.Street_ID 
                        and u.District_ID=d1.DistrictID and d1.DistrictID = d.District_ID
                        and u.Type_ID=l.Type and u.Type_ID =(?) and u.Street_ID=(?) and u.District_ID=(?)
    
                          """,
                      ( vdate.get(), location_nm.get(),list3.index(type.get()) + 1 ,lisits.index(adminstreet.get()) + 100,mydict.index(Distr.get()) + 11)
                       )

        location_nm.delete(0, END)
        vdate.delete(0, END)
        type.current(0)
        Distr.current(0)
        adminstreet.current(0)
        output2(c.fetchall())

    if mode == 'U':
        submit = tk.Button(window, text="Submit", command=userint)
        submit.pack()
        quit = tk.Button(window, text="Check current records in DB", command=output)
        quit.pack()
    else:
        quit = tk.Button(window, text="Check current records in DB", command=regusers)
        quit.pack()



def output():
    newwindow = Toplevel(window)
    newwindow.title("Records available in the system")
    x = datetime.datetime.now()
    title = tk.Label(newwindow,text="Records stored in the system: " + x.strftime("%Y-%m-%d"), font=("Times new roman", 12))
    title.pack()
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview',
                    background='silver',
                    foreground='black',
                    fieldbackground='silver'
                    )
    style.map('Treeview')
    graph = ttk.Treeview(newwindow,selectmode='browse',height=400)
    graph.place(x=30, y=95)
    verscrlbar = ttk.Scrollbar(newwindow,
                               orient="vertical",
                               command=graph.yview)
    verscrlbar.pack(side='right', fill='x')
    verscrlbar.place(x=70, y=40, height=200 + 20)

    graph.configure(xscrollcommand=verscrlbar.set)
    graph['columns'] = ("id", "admin", "location name", "date", "district", "type", "street", "sex", "age")
    graph.column("#0", width=0, stretch=NO)
    graph.column("id", width=100, anchor=S)
    graph.column("admin", width=120, anchor=CENTER)
    graph.column("location name", width=120, anchor=CENTER)
    graph.column("date", width=120, anchor=CENTER)
    graph.column("district", width=190, anchor=CENTER)
    graph.column("type", width=120)
    graph.column("street", width=120, anchor=W)
    graph.column("sex", width=120, anchor=W)
    graph.column("age", width=120, anchor=W)

    graph.heading("#0", text="")
    graph.heading("id", text="record ID")
    graph.heading("admin", text="Admin", anchor=CENTER)
    graph.heading("location name", text="Location name")
    graph.heading("district", text="District name", anchor=CENTER)
    graph.heading("type", text="Type name")
    graph.heading("street", text="Street name")
    graph.heading("date", text="Occurance date")
    graph.heading("sex", text="Sex")
    graph.heading("age", text="Age")

    c.execute("""select RecordID, UserName, place_name,visit_date, District_name, location_name , Street_Name, Sex,Age_range 
                        from case_records u, District_type d,location l,Street_details s, admin_details a
                        where u.District_ID = d.District_ID and u.Type_ID =l.type and 
                        u.District_ID= d.District_ID and u.Street_ID= s.Street_ID and a.User_tag=u.User_tag
                     """)

    result = c.fetchall()
    counter = len(result)
    count = 0
    for records in range(counter):
        graph.insert(parent='', index='end', text='', values=(result[count]))
        count += 1
    graph.pack()


def output2(result):
    newwindow = Toplevel(window)
    newwindow.title("Records available in the system")
    x = datetime.datetime.now()
    title = tk.Label(newwindow, text="Records stored in the system: " + x.strftime("%Y-%m-%d"),font=("Times new roman", 12))
    title.pack()
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview',
                    background='silver',
                    foreground='black',
                    fieldbackground='silver'
                    )

    style.map('Treeview')
    graph = ttk.Treeview(newwindow,height=10)
    graph.place(x=50, y=95)
    verscrlbar = ttk.Scrollbar(newwindow,
                               orient="vertical",
                               command=graph.yview)
    verscrlbar.pack(side='right', fill='x')
    verscrlbar.place(x=70, y=40, height=200 + 20)

    graph.configure(xscrollcommand=verscrlbar.set)


    graph['columns'] = ( "date","location name", "district", "type", "street")
    graph.column("#0", width=0, stretch=NO)
    graph.column("location name", width=120, anchor=W,stretch = 1)
    graph.column("date", width=120, anchor=CENTER)
    graph.column("district", width=190, anchor=CENTER)
    graph.column("type", width=120,anchor=W)
    graph.column("street", width=120, anchor=W)

    graph.heading("#0", text="")
    #graph.heading("id", text="record ID")
    graph.heading("location name", text="Location name",anchor=W)
    graph.heading("district", text="District name", anchor=W)
    graph.heading("type", text="Type name")
    graph.heading("street", text="Street name")
    graph.heading("date", text="Occurance date")

    counter = len(result)
    count = 0
    for records in range(counter):
        graph.insert(parent='', index='end', text='', values=(result[count]))
        count += 1
    graph.pack()


def create_tb(c):
    # k=c.execute(""" SELECT name FROM sqlite_master WHERE type='table'  """)
    c.execute(""" SELECT name FROM sqlite_master WHERE type='table'  """)

    if not c.fetchall():
        c.execute(
            """
        create table admin_details(
            User_tag integer(3) primary key,
            UserName varchar(30)
        )
    """)
        c.execute(
            """
                    create table case_records(
                           RecordID INTEGER PRIMARY KEY,
                           User_tag integer(3) NOT NULL,
                           visit_date date NOT NULL,
                           place_name varchar(25) NOT NULL,
                           District_ID varchar(2) ,
                           Type_ID varchar(1) ,
                           Street_ID integer,
                           Sex varchar(2),
                           Age_range varchar(10) ,
                           foreign key(District_ID) references District_type(District_ID),
                           foreign key(Street_ID) references Street_details(Street_ID) 
                           foreign key(Type_ID) references location(Type),
                           foreign key(User_Tag) references users(User_Tag),
                           foreign key(Street_ID)  references District_street(Street_ID),
                            foreign key(District_ID) references District_street(District_ID)
                           )""")
        c.execute(
            """
        create table District_type(
            District_ID varchar(2) primary key,
            District_name varchar(20) NOT NULL
        )
    """)
        c.execute(
            """  
        create table location(
                Type varchar(1) primary key,
                location_name varchar(25) NOT NULL
                )
            """)
        c.execute(

            """create table Street_details(
                       Street_ID integer,
                        Street_name varchar(30),
                        primary key(Street_ID) 
                    )"""
        )
        """
              create table District_street(
                 Street_ID integer ,
                  DistrictID varchar(2),
                  primary key(Street_ID,DistrictID),
                  foreign key(Street_ID) references Street_details(Street_ID),
                  foreign key(DistrictID) references District_type(District_ID)
              )
              """

        print("created")

    else:
        print("tables are present")


def delete(c, tb_name):
    field_ne, record = input("Choose field and what record")
    c.execute("""DELETE FROM ? WHERE ?='?' """, tb_name, field_ne, record)


def view_tb(c):
    c.execute('SELECT name from sqlite_master where type= "table"')
    print(c.fetchall())


if __name__ == '__main__':
    main()
