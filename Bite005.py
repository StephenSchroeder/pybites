"""
In this bite you will work with a list of names.

First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first name is.
For this exercise you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
"""



NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    dedup = list(dict.fromkeys(names))
    return [n.title() for n in dedup]
    
def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    # I am sure there is a better way to do this, and we are getting an Index error on line 34 likely because we are
    # dealing with a list of list...
    splitnames = []
    descsortednames= []
    names = dedup_and_title_case_names(names)

    for name in names:
       splitnames.append([name.split(" ")])
    sortednames = sorted(splitnames, key=lambda wholename: wholename[1], reverse=True)
    
    for item in sortednames:
       descsortednames.append(" ".join(item))
   
    return descsortednames
       


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    pass
    
