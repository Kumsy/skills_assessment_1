# Kristen Campbell
# House Hufflepuff
# Ada-June-2019


"""List Assessment

Fill in the following functions according to the directions in the 
docstrings.

"""


def get_indexed_items(items):
    """Given a list of items, get a list of items with their indices.

	Each item should be included in a tuple, formatted like::

	    (item, index) 

	So, the return value should be a list of tuples.


	Examples:
    
    If you got this list as input: ["Toyota", "Jeep", "Volvo"]
    You should return: [(Toyota, 0), (Jeep, 1), (Volvo, 2)]
    
    
    Another example input: ["Toyota", "Jeep", "Toyota", "Volvo"]
    Return value should be: [(Toyota, 0), (Jeep, 1), (Toyota, 2), (Volvo, 3)]

    *******************************************************
    * Pseudocode:                                         *
    * 1. Get a list and loop through.                     *
    * 2. Put each list element with it's index position   *
    *    into a tuple, then append the tuple into a list. *
    * 3. Return indexed_list                              *
    *******************************************************
    """

    indexed_list = []

    for index in range(len(items)):

        # Append a tuple of (list element, index position) into a list
        indexed_list.append(tuple([items[index], index]))
        
    return indexed_list

# TEST_CASES:
# print(get_indexed_items(["Toyota", "Jeep", "Volvo"]))
# print(get_indexed_items(["Toyota", "Jeep", "Toyota", "Volvo"]))


def words_in_common(words1, words2):
    """Find words in common.
    
    Given 2 lists of words, return the words that are in common
    between the two, sorted alphabetically.
    
    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists).
    
    For example, if you got these two lists as arguments:

    
    	["Python", "Ruby", "R", "C++", "Haskell"],
    	["Lizard", "Turtle", "Python"]
    
	Your return value should be:

    	['Python']


    The returned list should not have any duplicates.
        
        ["cheese", "bagel", "cake", "cheese"],
        ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        
	Would return

        ['bagel', 'cake', 'cheese']

    If there are no words in common, return an empty list::
        
        ["lamb", "chili", "cheese"],
        ["cake", "ice cream"]
    
    Would return    

        []

    If a duplicate exists in the original lists, the result will
    contain the value only once::
      
      ["Python", "Ruby", "R", "C++", "Haskell"]
      ["Lizard", "Turtle", "Python", "Python"]
    
    Would return    
    
        ['Python']

    **********************************************************
    * Pseudocode:                                            *
    * 1. Take both lists and compare each element            *
    * 2. If both are equal, append into a new "common" list  *                         
    * 3. Remove duplicate words                              *
    * 4. Return updated words in common list                 *
    **********************************************************
    """

    in_common_list = []

    # For each element in word1 & word2, check if they are equal.
    # If they are equal, append the matched word in a list.
    for word_1 in words1:
        for word_2 in words2:
            if word_1 == word_2:
                in_common_list.append(word_1)

    # Remove duplicates
    common_words = set(in_common_list)

    # Return non-duplicated list in alphabetical order
    return list(sorted(common_words))

# TEST_CASES:
# print(words_in_common(["Python", "Ruby", "R", "C++", "Haskell" ], 
#                       ["Lizard", "Turtle", "Python"]))

# print(words_in_common(["cheese", "bagel", "cake", "cheese"],
#         ["hummus", "cheese", "beets", "kale", "bagel", "cake"]))


def every_other_item(items):
    """Return every other item in `items`, starting at first item.
    
    For example, if you got this list as your argument:

        ['a', 'b', 'c', 'd', 'e', 'f']
    
    You would return:

        ['a', 'c', 'e']
    

	If you got this list as your argument:

    	["pickle", "pickle", "juice", "pickle", "juice", "pop"])
    
    You would return:

        ['pickle', 'juice', 'juice']
    

    Last example: 
    

    	["you", "z", "are", "z", "good", "z", "at", "x", "code"]
    
    Would return:

       ['you', 'are', 'good', 'at', 'code']

    *******************************************
    * Pseudocode:                             *
    * 1. Take a list and loop through it      *
    * 2. Return every other item in the list  *
    *******************************************
    """

    every_other_item_list = []

    for item in range(len(items)):
        if item % 2 == 0:
            every_other_item_list.append((items[item]))

    return every_other_item_list

# TEST_CASES:
# print(every_other_item(['a', 'b', 'c', 'd', 'e', 'f']))
# print(every_other_item(["you", "z", "are", "z", "good", 
#                               "z", "at", "x", "code"]))


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list, in descending order.
    
    You can assume that `n` will be less than the length of the list.
    
    
    For example, if you got the following two arguments:
    
        [2, 6006, 700, 42, 6, 59], 3

    You would return

        [42, 6, 2]

    
    If n is 0, return an empty list:

        [3, 4, 5], 0

    Return:

    	[]

    
    If there are duplicates in the list, they should be counted
    separately:

    	[3, 1, 3, 2, 1, 1], 2
    
    Return:
    	[1, 1]

    **********************************************************
    * Pseudocode:                                            *
    * 1. Take a list and loop through it                     *
    * 2. Can use a sorting algorithm to reorder the list in  *                         
    *    descending order.                                   *
    * 3. Return the "n" smallest index of the sorted list    *
    **********************************************************
    """

    # I used the selection sort algorithm to help with my understanding of it
    for item in range(len(items)):
        # We set max_position to first index of item list
        max_position = item
        """ Loop through the unsorted portion of the list and
            compare values finding the max number position 
        """
        for j in range(item + 1, len(items)):
            if items[j] > items[max_position]:
                max_position = j

        # Swamp position in the list
        temp = items[item]
        items[item] = items[max_position]
        items[max_position] = temp

    # Return list of "n" length, else return empty []
    if n:
        return (items[-n:])
    else:
        return []
    
# TEST_CASES:
# print(smallest_n_items([2, 6006, 700, 42, 6, 59], 0))
# print(smallest_n_items([3, 1, 3, 2, 1, 1], 2))

def get_unique_characters(word):
    """ Given a string, return a sorted LIST of the unique letters.

        For example, if you got the string "olives" as the argument,
        you shoudl return the list ['e', 'i', 'l', 'o', 's', 'v']

        If you got the string "tissue" as the argument, you should return
        the list ['e', 'i', 's', 't', 'u']

    *****************************************************
    * Pseudocode:                                       *
    * 1. Take a string and loop through it              *
    * 2. Append each index from the string into a list  *                         
    * 3. Remove duplicates                              *
    * 4. Return new set in a sorted a list              *
    *****************************************************
    """

    unique_list = []

    for index in range(len(word)):
        unique_list.append(word[index])

    unique_characters = set(unique_list)

    return list(sorted(unique_characters))

# TEST_CASES:
# print(get_unique_characters("tissue"))
# print(get_unique_characters("olives"))

# END
# Kristen Campbell
