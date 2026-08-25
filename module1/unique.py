# create function
# list
# unique list 
# display

def unique_list(lst):
    lst1 = set(lst)
    return list(lst1)

if __name__ == "__main__" :
    print(unique_list([2,3,4,7,5,1,4,2,3,5,7,4,1,3,5]))


