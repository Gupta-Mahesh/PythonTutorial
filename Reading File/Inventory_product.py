
## Reading data from text file

PRODUCT_ID=0
PRODUCT_NAME=1
PRODUCT_PRIZE=2
PRODUCT_QUANTITY=3

print("Reading data from inventory")
prod= open("D:\Python Practice\Reading File\Inventory.txt","r")
print("Data loaded :\n")
prod_details=prod.read().split("\n")
print(prod_details)
print("Loaded data type: ",type(prod_details))
print("\n")

for prod_row in prod_details:
    product_identy=prod_row.split(",")
    print(f"Enter the product id {product_identy[PRODUCT_ID]} for",product_identy[PRODUCT_NAME])

user_pro_num =input("Enter the product id which you want to purchase : ")
user_quantity=input("Enter the quantity                              : ")
for prod_row in prod_details:
    product_identy=prod_row.split(",")
    if product_identy[PRODUCT_ID]==user_pro_num:
        print("\n###### Preparing Bill ######\n")
        print("Product Name     :",product_identy[PRODUCT_NAME])
        print("Product Prize    :",product_identy[PRODUCT_PRIZE])
        print("Product Quantity :",user_quantity)
        print("Total Ammount    :",int(user_quantity)*int(product_identy[PRODUCT_PRIZE]))
    



