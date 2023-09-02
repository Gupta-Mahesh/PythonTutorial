
import json

fd =open("D:\Visual Studio WorkSpace\Python Practice\Reading Json\product_details_02.json","r")
js=fd.read()
fd.close()
#converting to dict from string
prod =json.loads(js)

print("************************* Menu *************************",end="\n")
for keys in prod:
    print(keys,":",
          "Name -",prod[keys]["name"],
          "\tPrice -",prod[keys]["price"],
          "\tQuantity -",prod[keys]["qn"]
          )
print()
ui_key = str(input("Enter the product Key                  :"))
ui_qn  = int(input("Enter the quantity                     :"))
print()
count =0
for key in prod:
    
    if (key == ui_key):
        if prod[key]["qn"] >= ui_qn:
            print("***************************************************************")
            print("                         Billing                               \n")
            print("Product Name             : ",prod[key]["name"])
            print("Product Price            : ",prod[key]["price"])
            print("Product Quantity         : ",ui_qn)
            print()
            print("***************************************************************")
            print("Billing amount           : ",int(ui_qn)*int(prod[key]["price"]),"INR")
            print("***************************************************************")
            print("Thank you! Visit again\n")
            prod[key]["qn"] = int(prod[key]["qn"]) - int(ui_qn)
        else:
            print("Sorry we don't have enough quantity")
            print(f"We have only {prod[key]['qn']} quantity.")
            user_agree = input("If you want to order this much quantity, please pres Y/y :")
            if (user_agree=="Y" or user_agree=="y"):
                print("***************************************************************")
                print("                         Billing                               \n")
                print("Product Name             : ",prod[key]["name"])
                print("Product Price            : ",prod[key]["price"])
                print("Product Quantity         : ",prod[key]["qn"])
                print()
                print("***************************************************************")
                print("Billing amount           : ",int(prod[key]["qn"])*int(prod[key]["price"]),"INR")
                print("***************************************************************")
                print("Thank you! Please visit again\n")
                prod[key]["qn"] = 0
            else:
                print("\n***************************************************************")
                print("\n                    Sorry for the inconviance                \n")
                print("\n***************************************************************")

    else:
        count +=1
if (count == len(prod)):
    print("Please enter the correct product id \n")

print("\nCurrent Product Deatils")
print("-----------------------\n")

for k in prod:
    print(k,":",
          "Name -",prod[k]["name"],
          "\tPrice -",prod[k]["price"],
          "\tQuantity -",prod[k]["qn"]
          )
    
#Converting dictonary into json
js_file=json.dumps(prod)

fd=open("Python Practice\Reading Json\product_details_02.json","w")
fd.write(js_file)
fd.close()