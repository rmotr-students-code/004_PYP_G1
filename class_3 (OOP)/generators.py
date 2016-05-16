def my_generator(num):
    print("Starting...")
    for elem in range(num):
        #print("Number {}".format(elem))
        yield elem
    print("Finished.")
        
        
mg = my_generator(5)


for elem in mg:
    print("Got an elem: {} from the generator".format(elem))
