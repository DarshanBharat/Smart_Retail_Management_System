import datetime
import sys

import mysql.connector as mysql #Importing mysql connector which is used to connect python and MySQL
mydb=mysql.connect(host='localhost', user='root', passwd='0000', database='retailsys')
mycursor=mydb.cursor(buffered=True) #Assigning variable for the MySQL database cursor

x=None

a=0

true_condition = True
date=str(datetime.date.today())
today_date="\'" + date + "\'"

def employee_detials():
    employee_code = input('Please Enter Your Employee Code - ')
    mycursor.execute("select password from employee_details where employee_code=%s"%(employee_code))
    mydata4=mycursor.fetchone()[0]
    mycursor.execute("select employee_name from employee_details where employee_code=%s"%(employee_code))
    employee_name=mycursor.fetchone()[0]
    mycursor.execute("select employee_access_level from employee_details where employee_code=%s"%(employee_code)) # employee_access_level =mycursor.fetchone()[0]
    
    password = input("Please Enter Your Employee Password - ")
    
    if password == mydata4:
        print('Welcome ',employee_name)
        global verified_user_check
        verified_user_check = True

def new_invoice(): #Function to create a new invoice
    print() #Prints empty line
    print() #Prints empty line
    temp1 = 1
    serial_number=1
    itemc=0
    tammount=0

    mycursor.execute('delete from transaction') #Clearing records from the transaction table from the previous execution run

    while temp1 == 1: #Creating a loop to enter all the items
        product_code=int(input('Enter the product code: ')) #Asking the user to enter the product code
        product_quantity=int(input('Enter the quantity of the product: ')) #Asking the user to enter the product quantity
        mycursor.execute("select product_code, product_name, product_mrp from product where product_code=%s"%(product_code))
        mydata=mycursor.fetchone() #Fetches one record from the MySQL table
        reterived_product_code = mydata[0] #Takes the product code from MySQL database for the user entered product code
        reterived_product_name = mydata[1] #Takes the product name from MySQL database for the user entered product code
        reterived_product_mrp = mydata[2] #Takes the product mrp from MySQL database for the user entered product code

        mycursor.execute("insert into transaction (sno, product_code, product_name, product_mrp, product_quantity, total_products_ammount, invoice_date) values (%s, %s, '%s', '%s', %s, %s, %s)"%(serial_number, reterived_product_code, reterived_product_name, reterived_product_mrp, product_quantity, product_quantity*reterived_product_mrp, today_date))
        mydb.commit() #Executes the mycursor statement
        mycursor.execute("insert into master_transaction(sno, product_code, product_name, product_mrp, product_quantity, total_product_ammount, invoice_date) values (%s, %s, '%s', '%s', %s, %s, %s)"%(serial_number, reterived_product_code, reterived_product_name, reterived_product_mrp, product_quantity, product_quantity*reterived_product_mrp, today_date))
        mydb.commit() #Executes the mycursor statement
        mycursor.execute('select product_units from product where product_code=%s'%(product_code))
        existing_units=mycursor.fetchone() #Fetches one record from the MySQL table
        new_product_units=existing_units[0]-product_quantity
        mycursor.execute('update product set product_units=%s where product_code=%s'%(new_product_units,product_code))
        mydb.commit() #Executes the mycursor statement
        
        add_more_products_loop_choice=input('Do you want to add more items (y/n)? ') #Asking if the user wants to enter more products to the invoice
        if add_more_products_loop_choice.lower() == 'y': #If user does want to enter more products
            serial_number+=1 #Incrementing the serial number by one for every loop
            continue #Continuing the previous loop
        
        elif add_more_products_loop_choice.lower() == 'n': #If user does not want to enter more products
            print()
            print('Inovice Created') #Printing Program Finished
            print()
            print()
            temp1 = 0 #Breaking the Invoice entry loop

        else:
            print('Enter a vaild response') #If user enters values other than 'y' or 'n'
        if true_condition == True:
            mycursor.execute('select * from transaction')
            mydata2=mycursor.fetchall()
            for row in mydata2:
                itemc+=row[4]
                tammount+=row[5]
                print(row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5])
                mycursor.execute("select count(*) from transaction")
                item_count_list=mycursor.fetchmany()
                item_count_int=int(item_count_list[0][0])
            print()
            print('Number of Items is - ', item_count_int)
            print('Total Item Count is - ', itemc)
            print('Grand Total is - ₹',tammount)
        temp1 += 2
        program_menu()
    
def search_product(): #Function to search a product
    print() #Prints empty line
    print() #Prints empty line
    user_item_code=input('Enter the code of the item you want to search: ')
    mycursor.execute("select * from product where product_code=%s"%(user_item_code))
    mydata3=mycursor.fetchone()
    if mydata3 is not None:
        print('Product Found!')
        print()
        print(mydata3[0]," ",mydata3[1]," ",mydata3[2]," ",mydata3[3]," ",mydata3[4])
        program_menu()
    else:
        print('Product does not exist, Please enter a valid Product code ')
        program_menu()
    
def add_product():
    user_product_code=int(input('Enter the product code you want to add: '))
    user_product_name=input('Enter the product name you want to add: ')
    user_product_mrp=int(input('Enter the product price you want to add: '))
    user_product_company=input('Enter the product company you want to add: ')
    user_product_units=int(input('Enter the product units you want to add: '))
    user_product_rol=int(input('Enter the product rol you want to add: '))
    mycursor.execute("insert into product (product_code, product_name, product_mrp, product_company,product_units,product_rol) values (%s, '%s', %s, '%s', %s, %s)"%(user_product_code, user_product_name, user_product_mrp, user_product_company, user_product_units, user_product_rol))
    mydb.commit()
    print('Record successively inserted')
    program_menu()
    
def update_product():
    user_product_code=int(input('Enter the product code you want to update: '))
    user_product_name=input('Enter the product name you want to update: ')
    user_product_mrp=int(input('Enter the product price you want to update: '))
    user_product_company=input('Enter the product company you want to update: ')
    user_product_units=int(input('Enter the product units you want to update: '))
    user_product_rol=int(input('Enter the product rol you want to update: '))
    mycursor.execute("update product set product_name="+str(user_product_name)+", product_mrp="+str(user_product_mrp)+", product_company="+(user_product_company)+", product_units="+str(user_product_units)+", product_rol="+str(user_product_rol)+" where product_code="+str(user_product_code))
    mydb.commit()
    print('Record successively updated')
    program_menu()
    
def delete_product():
    user_product_code=input('Enter the product code you want to delete: ')
    mycursor.execute('delete from product where product_code='+user_product_code)
    mydb.commit()
    print('Record successively deleted')
    program_menu()
    
def product_reports():
    variable = 0
    mycursor.execute('select product_name, product_units, product_rol from product')
    p_names=mycursor.fetchall()
    mycursor.execute('select count(product_code) from product')
    mycursor.execute('select count(product_code) from product')
    r=mycursor.fetchall()
    print()
    print()
    for i in range(0,r[0][0]):
        if p_names[i][1]>p_names[i][2]:
            print('The inventory level of',p_names[i][0],'is OK')
            pass
        elif p_names[i][1]<p_names[i][2]:
            variable += 1
            print('You need to place order for ',p_names[i][0],)
    if 0 == 0:
        print()
        print()
        mycursor.execute('select product_code, product_name, sum(product_quantity), invoice_date as product_quantity from master_transaction GROUP BY product_code, invoice_date')
        mydata6=mycursor.fetchall()
        for f in mydata6:
            print(f[0]," ",f[1]," ",f[2]," ",f[3])
    program_menu()
    
def program_exit():
    print('Program Exited')
    sys.exit()

def program_menu():
    if verified_user_check == True:
        main_menu_choice = int(input("1-Create a new invoice \n2-Search a product\n3-Add product details\n4-Update product details\n5-Delete product details\n6-View Reports\n7-Exit\n>>> "))
            
        while True:
            if main_menu_choice == 1:
                new_invoice()
            elif main_menu_choice == 2:
                search_product()
            elif main_menu_choice == 3:
                add_product()
            elif main_menu_choice == 4:
                update_product()
            elif main_menu_choice == 5:
                delete_product()
            elif main_menu_choice == 6:
                product_reports()
            elif main_menu_choice == 7:
                program_exit()
            else:
                print('Please Enter a Valid Option')
    else:
        print('Password Incorrect')
    
def program_run():
    employee_detials()
    program_menu()

program_run()