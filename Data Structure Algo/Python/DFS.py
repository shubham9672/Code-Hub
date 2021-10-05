def dfs(start, target):
    """
    Implementation of DFS (depth-first search) algorithm to find the shortest path from a start to a target node..
    Given a start node, this returns the node in the tree below the start node with the target value (or null if it doesn't exist)
    Runs in O(n), where n is the number of nodes in the tree, or O(b^d), where b is the branching factor and d is the depth.
    :param start:  the node to start the search from
    :param target: the value to search for
    :return: The node containing the target value or null if it doesn't exist.
    """
    print("Visiting Node " + str(start["value"]))
    if start["value"] == target:
        print("Found the node we're looking for!")
        return start

  
    for i in range(len(start["children"])):
        result = dfs(start["children"][i], target)
        if result is not None:
            return result

    print("Went through all children of " + str(start["value"]) + ", returning to it's parent.")
    return None
