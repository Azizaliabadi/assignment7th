products=[]
def read_text_fromfile():
    shopping=open('session7\shopping.txt', 'r')
read_text_fromfile()
print(products)
for product in products:
    print(product[1])
for line in f:
    result=line.split(',')
    my_dict={'id':result[0], 'name':result[1],
    'price':result[2],'count':result[3]}
    products.append(my_dict)
    read_text_fromfile()
    print(products)
    for product in products:
        print(product)
    product=[]
    def add():
        def delete():
         def edit():
          def search():
            def show_list():

                print("id\t name\t price\t count")
                for product in products:
                    print(product["id"], "\t", product["name"],
                    "\t",product["price"],"\t",product["count"],"\t")
                def buy():
                    
                    def exit():
                        def show_menu():
                            print("1-add")
                            print("2-delete")
                            print("3-edit")
                            print("4-search")
                            print("5-show_list")
                            print("6-buy")
                            print("7-exit")
                            read_text_fromfile()
                            show_menu()
                            choice=int(input("enter choice"))
                            if choice==1:
                                add()
                                def add():
                                    id=input("enter id")
                                    name=input("enter name")
                                    price=input("enter price")
                                    count=input("enter count")
                                    new_product={'id':id,'name':name,
                                    'price':price,'count':count}
                            if choice==2: 
                                delete()
                            if choice==3:
                                edit()
                            if choice==5:
                                search()
                                def search():
                                    user_choice=input("enter keyword")
                                    for product in products:
                                        if product['id']==user_choice or product['name']==user_choice:
                                            print(product)
                                            break
                                        else:
                                            print("not found")
                            if choice==5:
                                show_list() 
                            if choice==6:
                                buy() 
                            if chice==7:
                                exit()
                                def write_to_shopping():
                                    if choice==7:
                                        write_to_shopping()
                                        exit(0)
        

