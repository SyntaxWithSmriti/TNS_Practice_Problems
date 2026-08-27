FRIENDS = {
    "Aisha": ["Ben", "Carla"],
    "Ben":   ["Aisha", "Dev"],
    "Carla": ["Aisha", "Dev"],
    "Dev":   ["Ben", "Carla", "Eli"],
    "Eli":   ["Dev"],
}


def add_person(graph, name):
    """Put `name` in the graph with no friends yet - unless already there."""
    # TODO: if name is not already a key in graph, give it an empty list.
    if name not in graph:
        graph[name] = []
    


def add_friendship(graph, a, b):
    """Link a and b BOTH ways. Friendship is mutual."""
    # TODO: make sure BOTH names exist, then append each to the other's
    #       list - but only if they are not already in there.
    add_person(graph, a)
    add_person(graph, b)

    if b not in graph[a]:
        graph[a].append(b)

    if a not in graph[b]:
        graph[b].append(a)

print(FRIENDS)
add_person(FRIENDS,"Kajal")
add_friendship(FRIENDS,"Kajal","Eli")
print(FRIENDS)

# ----------------------Task 1--------------------

def friend_count(graph, name):
    """How many friends does `name` have?"""
    # TODO: 0 if the name is not in the graph, otherwise len of their list.
    if name not in graph:
        return 0
    else:
        return len(graph[name])
    
print("Aisha has", friend_count(FRIENDS, "Aisha"), "friends")
print("Dev has", friend_count(FRIENDS, "Dev"), "friends")
print("Rahul has", friend_count(FRIENDS, "Rahul"), "friends")



# ---------------Task 2---------------

def are_friends(graph, a, b):
    """Is there a direct link between a and b?"""
    # TODO: careful - check that `a` is in the graph before looking a up,
    #       or you will get a KeyError.


    if a not in graph:
        return False

    return b in graph[a]


name1 = input("Enter first person's name: ")
name2 = input("Enter second person's name: ")

if are_friends(FRIENDS, name1, name2):
    print(name1, "and", name2, "are friends.")
else:
    print(name1, "and", name2, "are not friends.")

# -----------Task 3------------
    # TODO: loop over the graph keeping the best name and best count so far.
    #       Return them as a tuple:  return best, best_count

def most_friends(graph):
    """Return the name with the most friends, and how many."""

    best = ""
    best_count = 0

    for name in graph:
        count = len(graph[name])

        if count > best_count:
            best = name
            best_count = count

    return best, best_count


# Test the function
best_name, best_count = most_friends(FRIENDS)

print("Person with the most friends:", best_name)
print("Number of friends:", best_count)