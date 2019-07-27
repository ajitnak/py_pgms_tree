def NumberOfBST(root): 
  
    # Base case  
    if (root == None): 
        return 0, INT_MIN, INT_MAX, True
  
    # If leaf node then return from function and store  
    # information about the leaf node  
    if (root.left == None and root.right == None): 
        return 1, root.data, root.data, True
  
    # Store information about the left subtree  
    L = NumberOfBST(root.left)  
  
    # Store information about the right subtree  
    R = NumberOfBST(root.right)  
  
    # Create a node that has to be returned  
    bst = [0]*4
  
    # If whole tree routed under the current root  
    # is BST  
    if (L[3] and R[3] and root.data > L[1] and root.data < R[2]): 
        bst[2] = min(root.data, (min(L[2], R[2]))) 
        bst[1] = max(root.data, (max(L[1], R[1]))) 
  
        # Update the number of BSTs  
        bst[0] = 2 + L[0] + R[0]  
  
        return bst  
  
    # If the whole tree is not a BST,  
    # update the number of BSTs  
    bst[3] = False
    bst[0] = 1 + L[0] + R[0]  
  
    return bst 
