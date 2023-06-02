
def even_finder(num):
    list = []
    for num in range(num+1):
        if num % 2 == 0:
            if num != 0:
                list.append(num != 0)
    print(len(list))
        
           
        
primates = ['monkey','gorilla', 'baboon','ape','george', 'lemur','chimp', 'orangatang']

cars = ['honda', 'chevy', 'mclaren', 'ford', 'prius', 'mazda', 'tesla', 'bugatti']

#merge these lists


def merge_lists(list1, list2):
    list3 = []
    for position in range(len(list1)):
        try:
            list3.append(list2[position])
        except:
            print('broke')

        try:
            list3.append(list1[position])
        except:
            print('broke')
    print(list3)
    

merge_lists(primates, cars)
    
    
