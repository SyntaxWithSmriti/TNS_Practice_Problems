 # TODO: create the seven nodes and join them up.
    #       Start with root = make_node(50), then hang 30 and 70 on it,
    #       then hang 20 and 40 under 30, and 60 and 80 under 70.


def make_node(value):
    return {"value": value, "left": None, "right": None}


def build():
    """Build and return this exact tree:

                 50
               /    \\
             30      70
            /  \\    /  \\
          20    40 60    80
    """
   
    
    root = make_node(50)

    root["left"] = make_node(30)
    root["right"] = make_node(70)

    root["left"]["left"] = make_node(20)
    root["left"]["right"]= make_node(40)

    root["right"]["left"] = make_node(60)
    root["right"]["right"] =make_node(80)

    return root 

tree = build()
print(tree)


# Get the rightmost and leftmost value

def leftmost_value(node):
    while node["left"] is not None:
        node = node["left"]

    return node["value"]

def rightmost_value(node):
    while node["right"] is not None:
        node = node["right"]

    return node["value"]


left_most_value = leftmost_value(tree)
print(f"The leftmost value is : {left_most_value}")

right_most_value = rightmost_value(tree)
print(f"The rightmost value is : {right_most_value}")


