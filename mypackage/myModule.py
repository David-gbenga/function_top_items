def top_n(items,n):
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j]> items[j+1]:
                items[j], items[j+1]= items[j+1], items[j]



    top_n = items[-n:]

    return top_n[::-1]
     
""" Return the first n items in desc order
Args 
items : the array
n : the number of items to be picked from the array
""" 
    






   
    