

import json

fd =open("Reading Json\product_details.json","r")
#reeading the json data
js= fd.read()
fd.close()

#converting the string json data into dict
produtcs_details =json.loads(js)

print("**********Multi dictonary**********",end="\n")
for keys in produtcs_details:
    print(keys,":",
          "Name -",produtcs_details[keys]["name"],
          "\tPrice -",produtcs_details[keys]["price"],
          "\tQuantity -",produtcs_details[keys]["qn"]
          )

#User enter for product id and quantity 

user_id=str(input("Enter the product ID              : "))
user_qn=int(input("Enter the quantity ID             : "))
produtcs_details[user_id]["qn"] = int(produtcs_details[user_id]["qn"]) - user_qn

#Generating the bill

print("***************************************************************")
print("                         Billing                               \n")
print("Product Name             : ",produtcs_details[user_id]["name"])
print("Product Price            : ",produtcs_details[user_id]["price"])
print("Product Quantity         : ",user_qn)
print()
print("***************************************************************")
print("Billing amount           : ",int(user_qn)*int(produtcs_details[user_id]["price"]),"INR")
print("***************************************************************")
print("Thank you! Visit again\n")

#Converting dictonary into json
js_file=json.dumps(produtcs_details)

fd=open("Reading Json\product_details.json","w")
fd.write(js_file)
fd.close()

