from ast import While
from posixpath import split


isigudang = {1 : {'Product Name' : 'Apple', 'Product Variant' : 'iPhone', 'Capacity' : 128, 'Color' : 'Black', 'Stock' : 10},
2 : {'Product Name' : 'Xiaomi', 'Product Variant' : 'Redmi', 'Capacity' : 128, 'Color' : 'Black', 'Stock' : 90}}

def showmenu():
    while(True):
        print('''
    =====Dandy's Warehouse Stockeeping Application=====
    1. Stock(s) List
    2. Create New Stock(s)
    3. Delete Stock(s)
    4. Update Stock(s)
    5. Exit Program
    ===================================================''')
        selectedmenu=int(input('Choose Menu [1-5] : '))

        if selectedmenu == 1:
            showlistmenu()
            break
        if selectedmenu == 2:
            createstockmenu()
            break
        if selectedmenu == 3:
            deletestockmenu()
            break
        if selectedmenu == 4:
            updatestockmenu()
            break
        if selectedmenu == 5:
            exitprogrammenu()
            break
        else :
            print('\nError! Please input correct index [1-5]')

def showisigudang():
    print('''
All Stock(s) List
|ID\t|Product\t|Variant\t|Capacity\t|Color\t\t|Stock\t\t|''')
    for i, id in enumerate(isigudang):
        print('|{}\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|'.format(id, isigudang[id]['Product Name'], isigudang[id]['Product Variant'],isigudang[id]['Capacity'], isigudang[id]['Color'], isigudang[id]['Stock']))

def showlistmenu():
    while(True):
        print('''
=====Warehouse Stock(s) List Menu=====
1. All Stock(s) List
2. Find Stock(s) Based on their ID
3. Exit to Main Menu
======================================''')
        selectedmenulist = int(input('Choose Menu [1-3] : '))
        if selectedmenulist == 1:
            showlistall()
            break
        if selectedmenulist == 2:
            showlistid()
            break
        if selectedmenulist == 3:
            showmenu()
            break
        else : 
            print('Error, Please input the correct Index (1-3)')

def showlistall():
    if len(isigudang) > 0:
        showisigudang()
    elif len(isigudang) == 0:
        print('No Stock(s) Available')
    while(True):
        print('''
What do you want to do next?
1. Back to Stock(s) List Sub Menu
2. Back to Main Menu
3. Exit Application''')
        checker = int(input('Input [1-3] : '))
        if checker == 1:
            showlistmenu()
            break
        elif checker == 2:
            showmenu()
            break
        elif checker == 3:
            exitprogrammenu()
            break
        else : 
            print('Error, Please input the correct Index (1-3)')
        
def showlist():
    showid = (int(input('Please Enter Product ID : ')))
    if showid in isigudang:
        print('''\n|ID\t|Product\t|Variant\t|Capacity\t|Color\t\t|Stock\t\t|
|{}\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|\n'''.format(showid, isigudang[showid]['Product Name'], isigudang[showid]['Product Variant'],isigudang[showid]['Capacity'], isigudang[showid]['Color'], isigudang[showid]['Stock']))
    else :
        print('Invalid ID. Stock not Available\n')


def showlistid():
    showlist()
    while(True):
            print('''What do you want to do next?
1. Input Another ID
2. Back to Stock(s) List Sub Menu
3. Back to Main Menu
4. Exit Application''')
            checker = int(input('Input [1-4] : '))
            if checker == 1:
                showlist()
            elif checker == 2:
                showlistmenu()
                break
            elif checker == 3:
                showmenu()
                break
            elif checker == 4:
                exitprogrammenu()
                break
            else : 
                print('Error, Please input the correct Index (1-4)')


def createstock():
        id = int(input('Please Input Stock ID (Numbers) : '))
        if id in isigudang:
            print('ID is Already Used/Stock Data Already Exist!')   
        else : 
            ProductName = input('Please Input the Product Name : ')
            ProductVarian = input('Please Input the Product Variant : ')
            Capacity = int(input('Please Input the Capacity in GB : '))
            Color = input('Please Input the Color :  ')
            Stock = int(input('Please Input the Stock(s) : '))
            isigudang.update({id : {'Product Name' : ProductName, 'Product Variant' : ProductVarian, 'Capacity' : Capacity, 'Color' : Color, 'Stock' : Stock}})
            showisigudang()
            print('Data Succesfully Added')
            

def createstockmenu():
    showisigudang()
    createstock()
    while(True):
        checker = input('Do you want to add another Stock Data? (Y/N) : ')
        if checker == 'Y':
            createstock()
        if checker == 'N':
            showmenu()
            break
            
def deletestock():
    deletestock = int(input('Please input Stock ID (Numbers) : '))
    if deletestock in isigudang:
        checker = input('Delete Item? (Y/N) : ')
        if checker == 'Y':
            del isigudang[deletestock]
        showisigudang()
        print('Data Deleted')
        if checker == 'N':
            showisigudang()
            print('Data Not Deleted')
    else : 
        print('Stock ID is Not Available!')
        
def deletestockmenu():
    showisigudang()
    deletestock()
    while(True):
        checker2 = input('Do you want to delete another stock? (Y/N) : ')
        if checker2 == 'Y':
            deletestock()
        if checker2 == 'N':
            checker3 = int(input('''
What do you want to do next?
1. Exit to Main Menu
2. Exit Program

Please input [1-2] : '''))
            if checker3 == 1:
                showmenu()
                break
            if checker3 == 2:
                exitprogrammenu()
                break
            else :
                print('Error, Please input the correct Index (1-2)')
                
def updatestock():
    showisigudang()
    updateid = int(input('Please input Stock ID (Numbers) : '))
    if updateid in isigudang:
        column = input('What do you want to Update/Change? (Case Sensitive) : ')
        change = input('Please insert updated Numbers or Condition : ')
        isigudang[updateid][column]=change
        showisigudang()
        print('Stock ID {} Updated'.format(updateid))
    else :
        print('Stock ID is not Available!')

def updatestockmenu():
    updatestock()
    while(True):
        checker = input('Do you want to update another stock? (Y/N) : ')
        if checker == 'Y':
            updatestock()
        if checker == 'N':
            while(True):
                checker2 = int(input('''
What do you want to do next?
1. Exit to Main Menu
2. Exit Program

Please input [1-2] : '''))
                if checker2 == 1:
                    showmenu()
                    break
                if checker2 == 2:
                    exitprogrammenu()
                    break
                else :
                    print('Error! Please input the correct index [1-2]')

    

def exitprogrammenu():
    while(True):
        exit=input('Are you sure? (Y/N) : ')
        if exit == 'Y':
            print('Goodbye, See you later!')
            break
        if exit == 'N':
            showmenu()
            break
        else :
            print('Error! Please input correct index [Y/N] (Case-sensitive)')


showmenu()

        

