def remove_item(dict, key_given):

    if key_given in dict:
        del dict[key_given]
        print("removed successfully.")
    else:
        print("Item not in the dictionary.")


dict = {"name":"pratham" , "age":21 , "year" : 2002}

print("Your_dict - ",dict)

key_given = input("give the key of item to remove: ")

remove_item(dict,key_given)
print("new dictionary is : ",dict)