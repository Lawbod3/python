sentence = "Hawanat was defining a dictionary and kept repeating diet the class had to encourage her to educate the use of the word dict"

list = {}


for key in sentence.split():
         if key in list:    
            list[key] += 1
         else:
            list[key] = 1
print(list)
          
            
          
        