def print_menu():
    
    menu = """
    Welcome to Semicolon Movie Rating App
    —------------------------------------------
    1. Add a movie
    2. Rate a movie
    3. view Average Ratings
    4. Exit

"""
    return print(menu)       
        
def validate_add_movie(movie):
    
    if movie.strip():
       return True
    
    else:
        return False

def check_movie_exist(movie, add_movie):
    if movie in add_movie.values():
           return True

    else:
       return False

def validate_ratings(ratings):
    
       if ratings < 1 or ratings > 5:
          return False

       else:
          return True

def check_movie_existance(my_dict, checkers):
    
    for value in my_dict.values():
             if value == checkers:
                return True

    else:
       return False

def get_ratings(list_ratings):
    if len(list_ratings) == 0:
        return 0

    return sum(list_ratings) / len(list_ratings)

def main():
 
    add_ratings = {}
    add_movie = {}
    count = 0
    counter = 0;
    selection = 0
   
    while True:
          print_menu()
          try:
               
               selection = int(input("Enter a selection from(1-4): "))
               if selection < 1 or selection > 4:
                  print("Please let your input be from range of 1 to 4")
               
          except ValueError:
                 print("Please only input an Integer") 

          if selection == 1:
              count += 1
              while True:
                  movie = str(input("Enter the movie name: "))

                  if validate_add_movie(movie):
                     if  check_movie_exist(movie, add_movie):
                         print("movie already exist")
                     else:  
                         add_movie[count] = movie 
                         add_ratings[movie] = []
                         break
                  else:
                     print("Your movie cant be empty")
              
              print("\nMovie added Successfully")

          elif selection == 2:
              while True:
                  try:
                    check = str(input("Enter the movie name: "))
                    if check_movie_existance(add_movie, check):
                         ratings = float(input("Enter your rating: "))
                         if validate_ratings(ratings):
                            add_ratings[check].append(ratings)
                            counter += 1
                            break
                     
                         else:
                            print("Your amount shouldnt be less than 1 or greater than 5")
       
                    else:
                        print("Movie does not exist")

                  except ValueError:
                          print("Invalid Input, must be a number")
                     
              print(f"\nRating added for {check} Successfully")

          elif selection == 3:
                if counter == 0:
                   print("No ratings added yet")
                 
                else:
                   for movie, ratings in add_ratings.items():
                       average_rating = get_ratings(ratings)
                       print(f"movie: {movie} - Average Rating: {average_rating:.2f}")

          elif selection == 4:
               print("\nExiting the app....Goodbye.")
               break

if __name__ == "__main__":
    main()


