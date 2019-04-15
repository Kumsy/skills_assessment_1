# Kristen Campbell
# House Hufflepuff
# Ada-June-2019


"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.
"""


###############################################################################


# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

   # 1.  Write a function that takes a town name as a string and returns
   #     `True` if it is your hometown, and `False` otherwise.

def hometown(town):
   """ Return True if hometown, otherwise return False
   
   *******************************************
   * Pseudocode:                             *
   * 1. Take a string as a parameter.        *
   * 2. Return boolean if it's my hometown   *
   *******************************************
   """

   kristen_hometown = "Fairfield"

   return town == kristen_hometown

# TEST_CASES
# print(hometown("Fairfield"))
# print(hometown("Hogswart"))
# print(hometown("Oakland"))


   # 2.  Write a function that takes a first and last name as arguments and
   #     returns the concatenation of the two names in one string.

def fullname(first_name, last_name):
   """ Return the concatenation of first_name and last_name

   *******************************************
   * Pseudocode:                             *
   * 1. Return concatenation of both args    *
   *******************************************
   """
   
   return first_name + " " + last_name

# TEST_CASE:
# print(fullname("Kristen", "Campbell"))
# print(fullname("Thomas", "Riddle"))

   # 3.  Write a function that takes a home town, a first name, and a last name
   #     as arguments, calls both functions from part (a) and (b) and prints
   #     "Hi, 'full name here', we're from the same place!", or "Hi 'full name
   #     here', I'd like to visit 'town name here'!" depending on what the function
   #     from part (a) evaluates to.

def hometown_greetings(town, first_name, last_name):
   """ Returns a greeting based on hometown

   ********************************************
   * Pseudocode:                              *
   * 1. Call hometown() function              *
   * 2. Print message depending on hometown   *
   ********************************************
   """

   if hometown(town):
      print("Hi, " + fullname(first_name, last_name) + ", we're from the same place!")

   else:
      print("Hi, " + fullname(first_name, last_name) + ", I'd like to visit Fairfield, CA!")

# TEST_CASES:
# hometown_greetings("Fairfield", "Kristen", "Campbell")
# hometown_greetings("San Francisco", "Thomas", "Riddle")

   # 4.  Write a function, `is_berry()`, which takes a fruit name as a string
   #     and returns a boolean if the fruit is a "strawberry", "raspberry",
   #     "blackberry", or "currant."

def is_berry():
   """ Return boolean if a certain berry

   **************************************
   * Pseudocode:                        *
   * 1. Take input and assign to berry  *
   * 2. Return berry based on matches   *
   **************************************
   """

    berry = input("Please enter a delicious berry: ")

    berry = berry.lower()

    if berry == "strawberry":
        return True
    elif berry == "raspberry":
        return True
    elif berry == "currant":
        return True
    else:
        return False
   
# TEST_CASE: 
# print(is_berry())


   # 5.  Write another function, shipping_cost(), which calculates shipping
   #     cost by taking a fruit name as a string and calling the `is_berry()`
   #     function within the `shipping_cost()` function. Your function should
   #     return 0 if is_berry() == True, and 5 if is_berry() == False.

def shipping_cost():
   """ Return value based on is_berry()

   ****************************************
   * Pseudocode:                          *
   * 1. Return 0 if berry, else return 5  *
   ****************************************
   """

    if is_berry():
        return 0
    else:
        return 5

# TEST_CASE:
# print(shipping_cost())

   # 6.  Make a function that takes in a fruit name and a list of fruits. It should
   #     return a new list containing the elements of the input list, along with
   #     given fruit, which should be at the end of the new list.

def add_fruit(fruit, fruit_list):
   """ Return new list with added new fruit

   *********************************************************
   * Pseudocode:                                           *
   * 1. Append fruit with fruit_list then return new list  *
   *********************************************************
   """

    fruit_list.append(fruit)
    return fruit_list

# TEST_CASES:
# print(add_fruit("watermelon", ["apple", "pear", "orange"]))
# print(add_fruit("banana", ["apple", "pear", "orange"]))

   # 7.  Write a function calculate_price to calculate an item's total cost by
   #     adding tax and any fees required by state law.

   #     Your function will take as parameters (in this order): the base price of
   #     the item, a two-letter state abbreviation, and the tax percentage (as a
   #     two-digit decimal, so, for instance, 5% will be .05). If the user does not
   #     provide a tax rate it should default to 5%.

   #     CA law requires stores to collect a 3% recycling fee, PA requires a $2
   #     highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
   #     items with a base price of $100 or less and $3 for items over $100. Fees are
   #     added *after* the tax is calculated.

   #     Your function should return the total cost of the item, including tax and
   #     fees.

def calculate_price(base_price, state_abbreviation, tax_percentage):
   """ Return calculated price after state fees and tax

   ******************************************
   * Pseudocode:                            *
   * 1. Calculate total fee after tax       *
   * 2. Apply state fees and get new total  *
   ******************************************
   """

    # Caculate Tax
    total_after_tax = (base_price * tax_percentage) + base_price

    # Determine what state fees
    if state_abbreviation == "CA":
        CA_total_after_fees = (total_after_tax * .03) + total_after_tax
        return CA_total_after_fees

    elif state_abbreviation == "PA":
        PA_total_after_fees = (total_after_tax + 2) #Highway Safety Fee
        return PA_total_after_fees

    elif state_abbreviation == "MA":
        if base_price > 100:
            MA_total_after_fees = (total_after_tax + 3) # Commonwealth Fund Fee
            return MA_total_after_fees
        else:
            MA_total_after_fees = (total_after_tax + 1) # Commonwealth Fund Fee
            return MA_total_after_fees
    else:
        return total_after_tax
    

# print(calculate_price(100, "CA", .05))
# print(calculate_price(100, "PA", .05))
# print(calculate_price(100, "MA", .05))
# print(calculate_price(200, "MA", .05))
# print(calculate_price(100, "DE", .05))













