import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
from datetime import datetime,timedelta,date
from time import sleep

def create_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publisher TEXT,
        publish_date TEXT,
        total_books INTEGER,
        available_books INTEGER,
        issued_books INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issue_books (
        issuer_id INTEGER,
        book_id INTEGER,
        issued_books INTEGER,
        issued_date TEXT,
        return_date TEXT,
        FOREIGN KEY(book_id) REFERENCES books(id)
    )
    ''')
    conn.commit()
    conn.close()

create_database()

class LibraryManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("1366x768")
        self.configure(bg="purple1")
        self.create_widgets()
        self.temp=0
        self.style=ttk.Style()
        
    def loading_frame(self):

        self.main_frame.config(bg="black")
        Label(self.main_frame,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09",).place(x=530,y=200)

        for i in range(16):
            Label(self.main_frame,bg="#1F2732",width=2,height=1).place(x=(i+23)*23,y=230)

        self.main_frame.update()
        self.loading()

    def loading(self):
        for i in range(1):
            for j in range(16):
                Label(self.main_frame,bg="#FFBD09",width=2, height=1).place(x=(j+23)*23, y=230)
                sleep(0.06)
                self.main_frame.update_idletasks()
                Label(self.main_frame,bg="#1F2732",width=2,height=1).place(x=(j+23)*23,y=230)

    def create_widgets(self):
        # Top Frame for buttons and logo
        logo_frame = tk.Frame(self, height=77, bg="darkviolet", highlightbackground="BLACK", highlightthickness=1, relief="ridge")
        logo_frame.pack(side=tk.TOP, fill=tk.X)
        
        logo_label = tk.Label(logo_frame, text="Library   Management   System", font=("Helvetica", 25, "bold"), bg="darkviolet",fg="white")
        logo_label.pack(pady=10)

        nav_frame = tk.Frame(self, height=40, bg="yellow", highlightbackground="BLACK", highlightthickness=1)
        nav_frame.pack(side=tk.TOP, fill=tk.X)

        addbook__indicate=tk.Label(nav_frame,text='',bg='yellow')
        addbook__indicate.place(x=20,y=0,height=45,width=175)
        editbook__indicate=tk.Label(nav_frame,text='',bg='yellow')
        editbook__indicate.place(x=235,y=0,height=45,width=175)
        issuebook__indicate=tk.Label(nav_frame,text='',bg='yellow')
        issuebook__indicate.place(x=457,y=0,height=45,width=175)
        returnbook__indicate=tk.Label(nav_frame,text='',bg='yellow')
        returnbook__indicate.place(x=692.5,y=0,height=45,width=175)
        deletebook__indicate=tk.Label(nav_frame,text='',bg='yellow')
        deletebook__indicate.place(x=928,y=0,height=45,width=175)
        showbook__indicate=tk.Label(nav_frame,text='',bg='yellow')
        showbook__indicate.place(x=1160,y=0,height=45,width=175)

        def hide_indicators():
            addbook__indicate.config(bg="yellow")
            add_btn.config(bg="yellow")
            editbook__indicate.config(bg="yellow")
            edit_btn.config(bg="yellow")
            issuebook__indicate.config(bg="yellow")
            issue_btn.config(bg="yellow")
            returnbook__indicate.config(bg="yellow")
            return_btn.config(bg="yellow")
            deletebook__indicate.config(bg="yellow")
            delete_btn.config(bg="yellow")
            showbook__indicate.config(bg="yellow")
            show_btn.config(bg="yellow")

        def indicate(lb,btn):
             hide_indicators()
             lb.config(bg="tomato")
             btn.config(bg="tomato")
        
        add_btn = tk.Button(nav_frame, text="Add Book", command=lambda:[self.add_book_frame(),indicate(addbook__indicate,add_btn)],
                            font=("Helvetica", 14, "bold"), bg="yellow", bd=0, activebackground="tomato")
        add_btn.pack(side=tk.LEFT, padx=55.5, pady=5)
    
        edit_btn = tk.Button(nav_frame, text="Edit Book", command=lambda:[self.edit_book_frame(),indicate(editbook__indicate,edit_btn)], 
                             font=("Helvetica", 14, "bold"), bg="yellow", bd=0, activebackground="tomato")
        edit_btn.pack(side=tk.LEFT, padx=55, pady=5)

        issue_btn = tk.Button(nav_frame, text="Issue Book", command=lambda:[self.issue_book_frame(),indicate(issuebook__indicate,issue_btn)], 
                              font=("Helvetica", 14, "bold"), bg="yellow", bd=0, activebackground="tomato")
        issue_btn.pack(side=tk.LEFT, padx=55, pady=5)

        return_btn = tk.Button(nav_frame, text="Return Book", command=lambda:[self.return_book_frame(),indicate(returnbook__indicate,return_btn)],
                               font=("Helvetica", 14, "bold"), bg="yellow", bd=0, activebackground="tomato")
        return_btn.pack(side=tk.LEFT, padx=55, pady=5)

        delete_btn = tk.Button(nav_frame, text="Delete Book", command=lambda:[self.delete_book_frame(),indicate(deletebook__indicate,delete_btn)],
                                font=("Helvetica", 14, "bold"), bg="yellow", bd=0, activebackground="tomato")
        delete_btn.pack(side=tk.LEFT, padx=55, pady=5)

        show_btn = tk.Button(nav_frame, text="Show Books", command=lambda:[self.show_books_frame(),indicate(showbook__indicate,show_btn)],
                              font=("Helvetica", 14, "bold"), bg="yellow", bd=0, activebackground="tomato")
        show_btn.pack(side=tk.LEFT, padx=55, pady=5)

        # Main frame for content
        self.main_frame = tk.Frame(self, bg="#FEB1B3")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(self.main_frame, text="    Welcome    ", font=("Times" ,25,'bold',"underline"),bg="#FEB1B3").pack(pady=10)

        self.head1="   Vision of the Library   "
        self.head2="   Mission Of The Library   "

        self.txt1="To Support the Institution and its stackholders by providing wide\naccess to the resources such as print and online Materials relevent to\nthe Curriculam and Research needs of the Academic Community."
        self.txt2="To provide user with the relevent information they need to\nAchieve their Highest Academic Status Aware then the\nVarious Skill for Life Long Learning."
        
        self.dev="@Developer :  P.Yuvaraj"
        
        self.count=0
        self.text=''

        self.head1_label=Label(self.main_frame,text=self.head1,font=("times",17,"bold",'underline'),fg='black',bg="#FEB1B3")
        self.head1_label.place(x=250,y=100)

        self.txt1_label=Label(self.main_frame,text=self.txt1,font=("times",15,"bold"),fg='black',bg="#FEB1B3")
        self.txt1_label.place(x=50,y=130)

        self.head2_label=Label(self.main_frame,text=self.head2,font=("times",17,"bold",'underline'),fg='black',bg="#FEB1B3")
        self.head2_label.place(x=925,y=270)

        self.txt2_label=Label(self.main_frame,text=self.txt2,font=("times",15,"bold"),fg='black',bg="#FEB1B3")
        self.txt2_label.place(x=800,y=300)

        self.dev_label=Label(self.main_frame,text=self.dev,font=("times",16,"bold"),fg='black',bg="#FEB1B3")
        self.dev_label.place(x=550,y=500)
        
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def add_book_frame(self):
        self.clear_frame()
        self.loading_frame()

        def add_book_to_db():
            id = id_entry.get()
            name = name_entry.get()
            author = author_entry.get()
            publisher = publisher_entry.get()
            publish_date = publish_date_entry.get()
            total_books = total_books_entry.get()
            
            if not (id and name and author and publisher and publish_date and total_books):
                messagebox.showwarning("Incomplete data", "Please fill all fields")
                return
            
            if int(total_books)<0:
                messagebox.showwarning("Negative data", "Please fill total books greater then 0")
                return
            
            available_books = int(total_books)
            issued_books = 0

            confirm = messagebox.askyesno("Confirm", f"Add the book with ID {id}?")
            if confirm:
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                try :
                    cursor.execute('''
                    INSERT INTO books (id, name, author, publisher, publish_date, total_books, available_books, issued_books)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (id, name, author, publisher, publish_date, total_books, available_books, issued_books))
                    messagebox.showinfo("Success", "Book added successfully")
                    self.add_book_frame()
                    
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Book Id is Already Exist")
                conn.commit()
                conn.close()
                

                

        self.main_frame.config(bg="#DEACD1")
        tk.Label(self.main_frame, text="   Add  Book   ", font=("Helvetica" ,20,'bold',"underline"),bg="#DEACD1").pack(pady=10)

        tk.Label(self.main_frame,bg="#FAAC8C",borderwidth=10,relief="ridge").place(height=500,width=900,x=225,y=50)

        tk.Label(self.main_frame, text="Book ID :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=100)
        id_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        id_entry.place(x=700,y=100,width=250)

        tk.Label(self.main_frame, text="Book Name :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=160)
        name_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        name_entry.place(x=700,y=160,width=250)

        tk.Label(self.main_frame, text="Book Author :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=220)
        author_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        author_entry.place(x=700,y=220,width=250)

        tk.Label(self.main_frame, text="Book Publisher :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=280)
        publisher_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        publisher_entry.place(x=700,y=280,width=250)

        tk.Label(self.main_frame, text="Book Publish Date:",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=340)
        publish_date_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        publish_date_entry.place(x=700,y=340,width=250)

        tk.Label(self.main_frame, text="Total Books :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=400)
        total_books_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        total_books_entry.place(x=700,y=400,width=250)

        tk.Button(self.main_frame, text="Add Book", command=add_book_to_db,font=("Helvetica", 17,'bold'),bg="#C2F3F1"
                  ,activebackground="#99D9F9",relief="raised",border=5).place(x=625,y=475)

    def edit_book_frame(self):
        self.clear_frame()
        self.loading_frame()

        def search_book():
            book_id = id_entry.get()
            if not book_id:
                messagebox.showwarning("Incomplete data", "Please enter a book ID")
                return

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
            book = cursor.fetchone()
            conn.close()

            if book:
                id_entry.config(state='disabled')
                search_btn.config(state="disabled")
                name_entry.config(state='normal')
                name_entry.insert(0, book[1])
                author_entry.config(state='normal')
                author_entry.insert(0, book[2])
                publisher_entry.config(state='normal')
                publisher_entry.insert(0, book[3])
                publish_date_entry.config(state='normal')
                publish_date_entry.insert(0, book[4])
                total_books_entry.config(state='normal')
                total_books_entry.insert(0, book[5])
                available_books_entry.config(state='normal')
                available_books_entry.insert(0, book[6])
                available_books_entry.config(state='disabled')
                issued_books_entry.config(state='normal')
                issued_books_entry.insert(0, book[7])
                issued_books_entry.config(state='disabled')
                self.temp= int(total_books_entry.get())
            else:
                messagebox.showerror("Error", "Book not found")

        def update_book_in_db():
            book_id = id_entry.get()
            name = name_entry.get()
            author = author_entry.get()
            publisher = publisher_entry.get()
            publish_date = publish_date_entry.get()
            total_books = total_books_entry.get()
            issued_books = issued_books_entry.get()
            available_books = available_books_entry.get()
            available_books_entry.config(state="disabled")

            if not (book_id and name and author and publisher and publish_date and total_books and issued_books and available_books):
                messagebox.showwarning("Incomplete data", "Please fill all fields")
                return
            
            if int(total_books)<0:
                messagebox.showwarning("Negative data", "Please fill total books greater then 0")
                return
            
            if int(issued_books)<0:
                messagebox.showwarning("Negative data", "Please fill issued books greater then 0")
                return
            
            total_books=int(total_books)
            issued_books=int(issued_books)
            
            if total_books==0:
                available_books=0
            else:
                available_books = total_books - issued_books
                if available_books<0:
                    available_books=0

            confirm = messagebox.askyesno("Confirm", f"Update the book with ID {book_id}?")
            if confirm:
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                cursor.execute('''
                UPDATE books
                SET name = ?, author = ?, publisher = ?, publish_date = ?, total_books = ?, available_books = ?, issued_books = ?
                WHERE id = ?
                ''', (name, author, publisher, publish_date, total_books, available_books, issued_books, book_id))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Book updated successfully")
                self.edit_book_frame()

        self.main_frame.config(bg="#DEACD1")
        tk.Label(self.main_frame, text="   Edit   Book   ", font=("Helvetica" ,20,'bold',"underline"),bg="#DEACD1").pack(pady=10)

        tk.Label(self.main_frame,bg="#FAAC8C",borderwidth=10,relief="ridge").place(height=500,width=900,x=225,y=50)

        tk.Label(self.main_frame, text="Enter Book ID :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=90)
        id_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3)
        id_entry.place(x=700,y=90,width=225)

        search_btn = tk.Button(self.main_frame, text="Search", command=search_book,relief="raised")
        search_btn.place(x=930,y=90)

        tk.Label(self.main_frame, text="Book Name :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=135)
        name_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        name_entry.place(x=700,y=135,width=225)

        tk.Label(self.main_frame, text="Book Author :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=180)
        author_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        author_entry.place(x=700,y=180,width=225)

        tk.Label(self.main_frame, text="Book Publisher :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=225)
        publisher_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        publisher_entry.place(x=700,y=225,width=225)

        tk.Label(self.main_frame, text="Book Publish Date :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=270)
        publish_date_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        publish_date_entry.place(x=700,y=270,width=225)

        tk.Label(self.main_frame, text="Total Books :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=315)
        total_books_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        total_books_entry.place(x=700,y=315,width=225)

        tk.Label(self.main_frame, text="Available Books :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=360)
        available_books_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        available_books_entry.place(x=700,y=360,width=225)
   
        tk.Label(self.main_frame, text="Issued Books :  ",font=("Helvetica", 17,'bold'),bg="#FAAC8C").place(x=450,y=405)
        issued_books_entry = tk.Entry(self.main_frame,font=("Helvetica", 13,'bold'),relief="sunken",border=3,state="readonly")
        issued_books_entry.place(x=700,y=405,width=225)

        tk.Button(self.main_frame, text="Update Book", command=update_book_in_db,font=("Helvetica", 17,'bold'),bg="LIGHTGRAY",
                  activebackground="GRAY",relief="raised",border=5).place(x=625,y=475)

    def issue_book_frame(self):
        self.clear_frame()
        self.loading_frame()

        def select_book(event):
            selected_item = tree.selection()[0]
            book = tree.item(selected_item)['values']
            book_id_entry.config(state='normal')
            book_id_entry.delete(0, tk.END)
            book_id_entry.insert(0, book[0])
            book_id_entry.config(state='disabled')
            
        def set_book():
            total_dates = total_dates_entry.get()
            if not total_dates:
                messagebox.showwarning("Incomplete data", "Please enter a Total Dates")
                return
            
            total_dates_entry.config(state="disabled")
            change_btn.place(x=1215,y=410)
            set_btn.place(x=1400,y=410)
        
            return_date_entry.config(state="normal")
            return_date_entry.delete(0, tk.END)
            return_date_entry.insert(0,date.today() + timedelta(int(total_dates)))
            return_date_entry.config(state="disabled")

        def change_book():
            total_dates_entry.config(state="normal")
            change_btn.place(x=1400,y=410)
            return_date_entry.config(state="normal")
            return_date_entry.delete(0, tk.END)
            return_date_entry.config(state="disabled")
            set_btn.place(x=1230,y=410)
            
        def issue_book_to_user():
            book_id = book_id_entry.get()
            issuer_id = issuer_id_entry.get()
            issued_books = issued_books_entry.get()
            if not book_id or not issuer_id or not issued_books:
                messagebox.showwarning("Incomplete data", "Please fill all fields")
                return
            
            issued_date = datetime.now().strftime("%Y-%m-%d")
            return_date = return_date_entry.get()

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()

            cursor.execute("SELECT available_books FROM books WHERE id = ?", (book_id,))
            available_books = cursor.fetchone()[0]

            if available_books > 0:
                if available_books>=int(issued_books):
                    cursor.execute("SELECT *from issue_books WHERE issuer_id = ? AND book_id= ?",(issuer_id,book_id))
                    result=cursor.fetchall()
                    if len(result)!=0:
                        cursor.execute('''UPDATE issue_books SET issued_books = issued_books + ?, issued_date=?, return_date=? 
                                    WHERE issuer_id = ? AND book_id= ?
                        ''',(issued_books, issued_date, return_date, issuer_id, book_id))
                    else:
                        cursor.execute('''
                        INSERT INTO issue_books (issuer_id, book_id, issued_books,issued_date, return_date)
                        VALUES (?, ?, ?, ?, ?)
                        ''', ( issuer_id,book_id,issued_books, issued_date, return_date))
                else:
                    messagebox.showwarning("Error", f"    {available_books} Books are Available\n But, You Issued {issued_books} Books")
                    return

                cursor.execute('''
                UPDATE books
                SET available_books = available_books - ?, issued_books = issued_books+?
                WHERE id = ?
                ''', (issued_books,issued_books,book_id,))
                conn.commit()

                messagebox.showinfo("Success", "Book issued successfully")
                self.issue_book_frame()
            else:
                messagebox.showerror("Error", "No available books to issue")
            conn.close()

        self.main_frame.config(bg="THISTLE")

        tk.Label(self.main_frame, text="Issue Book", font=("Helvetica", 18,'bold','underline'),bg="THISTLE").pack(pady=10)

        self.style.theme_use('clam')
        self.style.configure('Treeview', font=('times', 12),fieldbackground = 'PEACHPUFF', background="PEACHPUFF",foreground='Black')
     
        self.style.configure('Treeview.Heading', font=('times', 12,'bold'), background='KHAKI')
        self.style.map('Treeview',background = [('selected','blue2')])

        tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "Author", "Publisher", "Publish Date"
                                                      , "Total Books", "Available Books", "Issued Books"), show='headings')
        tree.pack(padx=125,  fill=tk.BOTH, expand=True)
        tree.place(x=0 ,y=50,height=580)
        
        i=0
        for col in tree['columns']:
            tree.heading(col, text=col)
            if i==0:
                tree.column(col, width=120,anchor="center")
            elif i>=1 and i<=3:
                tree.column(col, width=175,anchor="center")
            else:
                tree.column(col, width=120,anchor="center")
            i+=1

        tree.bind("<ButtonRelease-1>", select_book)

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

        tk.Label(self.main_frame,bg="LIGHTGREEN",borderwidth=5,relief="ridge").place(height=580,width=235,x=1130,y=50)

        tk.Label(self.main_frame, text="   <== Select the Book   ", font=("Helvetica" ,13,'bold','underline'),bg="LIGHTGREEN").place(x=1150,y=70)

        tk.Label(self.main_frame, text="Book ID :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=130)
        book_id_entry = tk.Entry(self.main_frame, state='readonly')
        book_id_entry.place(x=1175,y=160,width=150)

        tk.Label(self.main_frame, text="Issuer ID :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=200)
        issuer_id_entry = tk.Entry(self.main_frame)
        issuer_id_entry.place(x=1175,y=230,width=150)

        tk.Label(self.main_frame, text="No.Issued books :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=275)
        issued_books_entry = tk.Entry(self.main_frame)
        issued_books_entry.place(x=1175,y=305,width=150)

        tk.Label(self.main_frame, text="Total Dates :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=350)
        total_dates_entry = tk.Entry(self.main_frame)
        total_dates_entry.place(x=1175,y=380,width=150)

        set_btn = tk.Button(self.main_frame, text="  set  ", command=set_book,relief="raised")
        set_btn.place(x=1230,y=410)

        change_btn = tk.Button(self.main_frame, text="  change  ", command=change_book,relief="raised")
        change_btn.place(x=1400,y=410)
        
        tk.Label(self.main_frame, text="Return Date(YYYY-MM-DD) :", font=("Helvetica" ,10,'bold'),bg="LIGHTGREEN").place(x=1160,y=450)
        return_date_entry = tk.Entry(self.main_frame,state="readonly")
        return_date_entry.place(x=1175,y=480,width=150)

        tk.Button(self.main_frame, text="Issue Book", command=issue_book_to_user,font=("Helvetica", 12,'bold')
                  ,bg="GOLD1",activebackground="#99D9F9",relief="raised",border=5).place(x=1200,y=550)

    def return_book_frame(self):
        self.clear_frame()
        self.loading_frame()

        def select_issue(event):
            selected_item = tree.selection()[0]
            issue = tree.item(selected_item)['values']
            issuer_id_entry.config(state='normal')
            issuer_id_entry.delete(0, tk.END)
            issuer_id_entry.insert(0, issue[0])
            issuer_id_entry.config(state='disabled')
            book_id_entry.config(state='normal')
            book_id_entry.delete(0, tk.END)
            book_id_entry.insert(0, issue[1])
            book_id_entry.config(state='disabled')
            temp_issued_books_entry.config(state='normal')
            temp_issued_books_entry.delete(0, tk.END)
            temp_issued_books_entry.insert(0, issue[2])
            temp_issued_books_entry.config(state='disabled')
            return_date_entry.config(state='normal')
            return_date_entry.delete(0, tk.END)
            return_date_entry.insert(0, issue[4])
            return_date_entry.config(state='disabled')

        def return_book_from_user():
            book_id = book_id_entry.get()
            issuer_id = issuer_id_entry.get()
            return_date = return_date_entry.get()
            current_date = datetime.now().strftime("%Y-%m-%d")
            return_books= return_books_entry.get()
            temp_issued_books=int(temp_issued_books_entry.get())

            if not book_id or not issuer_id or not return_date or not return_books:
                messagebox.showwarning("Incomplete data", "Please fill all fields")
                return

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()

            cursor.execute("SELECT issued_books FROM books WHERE id = ?", (book_id,))
            issued_books = cursor.fetchone()[0]

            if temp_issued_books>=int(return_books):
                cursor.execute('''
                UPDATE issue_books
                SET issued_books = issued_books-?
                WHERE book_id = ? AND issuer_id = ? 
                ''', (return_books, book_id, issuer_id))

                cursor.execute('''
                UPDATE books
                SET available_books = available_books + ?, issued_books = issued_books - ?
                WHERE id = ?
                ''', (return_books,return_books,book_id,))

                cursor.execute('''
                DELETE FROM issue_books WHERE issued_books = 0''')
                
                conn.commit()
                conn.close()
                if return_date < current_date:
                    messagebox.showinfo("Success", "Book returned with fine")
                else:
                    messagebox.showinfo("Success", "Book returned successfully")
            else:
                 messagebox.showwarning("Error", f"    You are Issued {temp_issued_books} Books \n But, You are Return {return_books} Books")
                 return
            self.return_book_frame()

        self.main_frame.config(bg="THISTLE")

        tk.Label(self.main_frame, text="   Return  Book   ", font=("Helvetica", 18,'bold','underline'),bg="THISTLE").pack(pady=10)
    
        self.style.theme_use('clam')

        self.style.configure('Treeview', font=('times', 12),fieldbackground = 'PEACHPUFF', background="PEACHPUFF",foreground='Black')
     
        self.style.configure('Treeview.Heading', font=('times', 12,'bold'), background='KHAKI')
        self.style.map('Treeview',background = [('selected','blue2')])

        tree = ttk.Treeview(self.main_frame, columns=( "Issuer ID", "Book ID", "Issued Books", "Issue Date", "Return Date"), show='headings')
        tree.pack(padx=125, fill=tk.BOTH, expand=True)
        tree.place(x=0,y=50,height=580)

        for col in tree['columns']:
            tree.heading(col, text=col)
            tree.column(col, width=225,anchor="center")

        tree.bind("<ButtonRelease-1>", select_issue)

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM issue_books")
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

        tk.Label(self.main_frame,bg="LIGHTGREEN",borderwidth=5,relief="ridge").place(height=580,width=235,x=1130,y=50)

        tk.Label(self.main_frame, text="   <== Select the Book   ", font=("Helvetica" ,13,'bold','underline'),bg="LIGHTGREEN").place(x=1150,y=70)

        tk.Label(self.main_frame, text="Issuer ID :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=120)
        issuer_id_entry = tk.Entry(self.main_frame, state='readonly')
        issuer_id_entry.place(x=1175,y=150,width=150)

        tk.Label(self.main_frame, text="Book ID :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=200)
        book_id_entry = tk.Entry(self.main_frame, state='readonly')
        book_id_entry.place(x=1175,y=230,width=150)

        tk.Label(self.main_frame, text="Return Date :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=280)
        return_date_entry = tk.Entry(self.main_frame, state='readonly')
        return_date_entry.place(x=1175,y=310,width=150)

        tk.Label(self.main_frame, text="No.Issued Books:", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=360)
        temp_issued_books_entry = tk.Entry(self.main_frame, state='readonly')
        temp_issued_books_entry.place(x=1175,y=390,width=150)

        tk.Label(self.main_frame, text="No.Return Books:", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=440)
        return_books_entry = tk.Entry(self.main_frame)
        return_books_entry.place(x=1175,y=470,width=150)

        tk.Button(self.main_frame, text="Return Book", command=return_book_from_user,font=("Helvetica", 12,'bold'),bg="GOLD1"
                  ,activebackground="#99D9F9",relief="raised",border=5).place(x=1200,y=550)

    def delete_book_frame(self):
        self.clear_frame()
        self.loading_frame()

        def select_issue(event):
            selected_item = tree.selection()[0]
            issue = tree.item(selected_item)['values']
            book_id_entry.config(state='normal')
            book_id_entry.delete(0, tk.END)
            book_id_entry.insert(0, issue[0])
            book_id_entry.config(state='disabled')
            book_name_entry.config(state='normal')
            book_name_entry.delete(0, tk.END)
            book_name_entry.insert(0, issue[1])
            book_name_entry.config(state='disabled')
            author_entry.config(state='normal')
            author_entry.delete(0, tk.END)
            author_entry.insert(0, issue[2])
            author_entry.config(state='disabled')

        def delete_book_from_db():
            book_id = book_id_entry.get()

            confirm = messagebox.askyesno("Confirm", f" You Want to Delate the Book {book_id} ?")
            if confirm:
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                cursor.execute('''
                DELETE FROM books WHERE id = ?''', (book_id,))

                cursor.execute('''
                DELETE  FROM issue_books WHERE book_id = ?''',(book_id,))
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Book Deleted successfully")
            self.delete_book_frame()

        self.main_frame.config(bg="THISTLE")

        tk.Label(self.main_frame, text="Delete Book", font=("Helvetica", 18,'bold','underline'),bg="THISTLE").pack(pady=10)

        self.style.theme_use('clam')
        self.style.configure('Treeview', font=('times', 12),fieldbackground = 'PEACHPUFF', background="PEACHPUFF",foreground='Black')
     
        self.style.configure('Treeview.Heading', font=('times', 12,'bold'), background='KHAKI')
        self.style.map('Treeview',background = [('selected','blue2')])

        tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "Author", "Publisher", "Publish Date", "Total Books"
                                                      , "Available Books", "Issued Books"), show='headings')
        tree.pack(padx=125,  fill=tk.BOTH, expand=True)
        tree.place(x=0 ,y=50,height=580)
        
        i=0
        for col in tree['columns']:
            tree.heading(col, text=col)
            if i==0:
                tree.column(col, width=120,anchor="center")
            elif i>=1 and i<=3:
                tree.column(col, width=175,anchor="center")
            else:
                tree.column(col, width=120,anchor="center")
            i+=1

        tree.bind("<ButtonRelease-1>", select_issue)

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

        tk.Label(self.main_frame,bg="LIGHTGREEN",borderwidth=5,relief="ridge").place(height=580,width=235,x=1130,y=50)

        tk.Label(self.main_frame, text="   <== Select the Book   ", font=("Helvetica" ,13,'bold','underline'),bg="LIGHTGREEN").place(x=1150,y=70)

        tk.Label(self.main_frame, text="Book ID :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=150)
        book_id_entry = tk.Entry(self.main_frame, state='readonly')
        book_id_entry.place(x=1175,y=180,width=150)

        tk.Label(self.main_frame, text="Book Name :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=250)
        book_name_entry = tk.Entry(self.main_frame, state='readonly')
        book_name_entry.place(x=1175,y=280,width=150)

        tk.Label(self.main_frame, text="Author :", font=("Helvetica" ,12,'bold'),bg="LIGHTGREEN").place(x=1180,y=350)
        author_entry = tk.Entry(self.main_frame, state='readonly')
        author_entry.place(x=1175,y=380,width=150)

        tk.Button(self.main_frame, text="Delete Book", command=delete_book_from_db,font=("Helvetica", 12,'bold'),bg="GOLD1",
                  activebackground="#99D9F9",relief="raised",border=5).place(x=1200,y=450)

    def show_books_frame(self):
        self.clear_frame()
        self.loading_frame()

        self.main_frame.config(bg="THISTLE")
        tk.Label(self.main_frame, text="All Books", font=("Helvetica", 18,'bold','underline'),bg="THISTLE").pack(pady=10)

        self.style.theme_use('clam')
        self.style.configure('Treeview', font=('times', 12),fieldbackground = 'PEACHPUFF', background="PEACHPUFF",foreground='Black')
     
        self.style.configure('Treeview.Heading', font=('times', 12,'bold'), background='KHAKI')
        self.style.map('Treeview',background = [('selected','blue2')])

        tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "Author", "Publisher", "Publish Date", "Total Books", 
                                                      "Available Books", "Issued Books"), show='headings')
        tree.pack(pady=10, fill=tk.BOTH, expand=True)

        for col in tree['columns']:
            tree.heading(col, text=col)
            tree.column(col, width=150,anchor="center")

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

if __name__ == "__main__":
    app = LibraryManagementSystem()
    app.mainloop()