


## Reading data from text file

PRODUCT_ID=0
PRODUCT_NAME=1
PRODUCT_PRIZE=2
PRODUCT_QUANTITY=3

print("Reading data from inventory")
prod= open("D:\Python Practice\Reading File\Inventory copy.txt","r")
print("Data loaded :\n")
prod_details=prod.read().split("\n")
print(prod_details)
print("\n")

for prod_row in prod_details:
    product_details=prod_row.split(",")
    print(f"Enter the product id {product_details[PRODUCT_ID]} for",product_details[PRODUCT_NAME])

user_pro_num =int(input("Enter the product id which you want to purchase : "))
user_quantity=int(input("Enter the quantity                              : "))
updated_inventory_lst=[]

for prod_row in prod_details:
    product_identy=prod_row.split(",")
    if (product_identy[PRODUCT_ID] == str(user_pro_num)):
        print("\n###### Billing Amount ######\n")
        print("Product Name     :",product_identy[PRODUCT_NAME])
        print("Product Prize    :",product_identy[PRODUCT_PRIZE])
        print("Product Quantity :",user_quantity)
        print("Total Ammount    :",int(user_quantity)*int(product_identy[PRODUCT_PRIZE]))
        #Updating quantity inventory details
        product_identy[PRODUCT_QUANTITY] = str(int(product_identy[PRODUCT_QUANTITY]) - user_quantity)
    updated_inventory_lst.append(product_identy)

lst=[]
for rows in updated_inventory_lst:
    cnvtstr = rows[PRODUCT_ID] +","+rows[PRODUCT_NAME]+","+rows[PRODUCT_PRIZE]+","+rows[PRODUCT_QUANTITY]+ "\n"
    lst.append(cnvtstr)

lst[-1]=lst[-1][:-1]
print("Deleted last '\\n' item: ",lst)

prod_update= open("D:\Python Practice\Reading File\Inventory copy.txt","w")
for i in lst:
    prod_update.write(i)
prod_update.close

