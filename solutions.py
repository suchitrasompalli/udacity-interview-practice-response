"""
Given two strings s and t, determine whether some anagram of t is a 
substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return 
a boolean True or False.
"""
def question1(s, t):
    if ((s == None) or (t == None)):
        return False
    if ((len(s) == 0) or (len(t) == 0)):
        return False
    if (s == t):
        return True
    if (len(s) < len(t)):
        return False
    # place all characters and the number of times there occur in t into a hash
    dictionary = {}
    for char in t:
        count= dictionary.get(char)
        if count:
            dictionary[char] = count + 1
        else:
            dictionary[char] = 1
            
    # iterate through s as a sliding window
    start = 0 
    end = len(t)
    while (end <= len(s)):
        sliding_window = s[start:end]
        temp_dict = dictionary.copy()
        # for each character check if it has a count in the dictionary
        for character in sliding_window:
            count = temp_dict.get(character)
            if (count and count > 0):
                temp_dict[character] = count - 1
        # check if all counts are 0 in the hash
        if isDictionaryCountZero(temp_dict):
            return True 
        start += 1
        end += 1
    return False

""" Given a hash with keys and values of count.
Check to see that all count values in dictionary are zero """
def isDictionaryCountZero(temp_dict):
    for value in temp_dict.values():
        if (value != 0):
            return False
    return True

# Tests for question1
print(question1('', ''))
# expecting False when inputs of either string is ''

print(question1(None, None))
# expecting False when inputs of either string is null

print(question1('udacity', 'ad'))
# expecting True when s has anagram of t

print(question1('udacity', 'da'))
# expecting True when s has anagram of t

print(question1('udacity', 'cityud')) 
# expecting False when one character from t is missing in s

print(question1('corrupt', 'rupt'))
# expecting True when there is a double r in string s

print(question1('corrupt', 'rrupt'))
# expecting True when there is a double r in string t

print(question1('the cat in the hat', 'etph  '))
# expecting False when there are spaces in string s and t

print(question1('the cat in the hat', 'eth  '))
# expecting True when there are spaces in string s and t

"""
Given a string a, find the longest palindromic substring contained 
in a. Your function definition should look like question2(a), 
and return a string.
"""
"""
This alogorithim is my python version of java code which is available on 
https://www.programcreek.com/
"""
def question2(a):
    
    if ((a==None) or (len(a) <= 1)):
        return a;
    
    length = len(a);
    maxLen = 1;
    
    # table[i][j] will be false if substring str[i..j] is not palindrome. 
    # else table[i][j] will be true
    table = [[0 for x in range(length)] for y
                          in range(length)] 
 
    longest = 'No palindrome found.';
    for k in range(length):
        for i in range(length-k):
            j = i + k
            if (a[i] == a[j] and (j-i <= 2 or table[i+1][j-1])):
                table[i][j] = True
 
                if(j-i+1 > maxLen):
                    maxLen = j-i+1
                    longest = a[i:j+1]
    return longest

print(question2('a'))
# Expecting a

print(question2('the cat in the hat'))
# Expecting No palindrome

print(question2('banana'))
# Expecting value anana

print(question2('avid diva'))
#Expecting avid diva

"""
Given an undirected adjacency_list G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a adjacency_list 
with the smallest possible total weight of edges. 
The function will take in and return an adjacency list.
 
"""
# Finding cycle in a graph is code from, https://www.geeksforgeeks.org/
# the rest of code was written by me.
# First part is Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one edge for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both
  
from collections import defaultdict
  
#This class represents a undirected graph using adjacency list representation
class Graph:
  
    def __init__(self, vertices):
        self.V = vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    def removeVertice(self):
        self.V = self.V - 1
         
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # function to remove an edge from graph
    def removeEdge(self, u):
        del self.graph[u]
  
    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])
 
    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set
 
  
  
    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):
         
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1]*(self.V)
 
        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i) 
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
 

def question3(adjacency_list):
    """
    Finding MST will be through Krushkal's algorithm.    
    1. Sort all the edges in non-decreasing order of their weight.
    2. Pick the smallest edge. Check if it forms a cycle with the spanning tree 
    formed so far. If cycle is not formed, include this edge. Else, discard it.
    3. Repeat step#2 until there are (V-1) edges in the spanning tree.
    """
    if adjacency_list == None:
        return None
    
    # we need minimum of 3 nodes to check for cycle in graph
    if (len(adjacency_list.keys()) < 3):
        return adjacency_list
   
    # The algorithim to detect cycle requires numeric node names. The nodes in adjacency list will be converted to numbers 0 To N
    # using the dict strings_to_numeric
    strings_to_numeric = {}
    count = 0
    # convert the alphabetic keys to numbers to represent vertices as numbers 0 to N
    for key in adjacency_list.keys():
        if strings_to_numeric.get(key) == None:
            strings_to_numeric[key] = count
            count += 1   
    
    #print('vertices ', strings_to_numeric) 
    # First step in Krushkals algorithim is to sorts the edges with lowest weigth first.
    edges = getSortedEdges(adjacency_list)
   
    # Step 2: check if adding a edge to a graph makes it cyclic. if so do not use this edge. 
    edges_to_delete = []
    index = 0
    g = Graph(len(adjacency_list.keys()))
    for edge in edges:
        # checking for cycle in graph is done till V-1 times. (V means vertices)
        if (index == len(adjacency_list.keys())):
            break;
        index += 1
        #print('edge1 ', strings_to_numeric.get(edge[1]))
        #print('edge2 ', strings_to_numeric.get(edge[2]))
        g.addEdge(strings_to_numeric.get(edge[1]), strings_to_numeric.get(edge[2]))
        if (g.isCyclic()):
            #print('g is cyclic')
            g.removeEdge(strings_to_numeric.get(edge[1]))
            edges_to_delete.append([edge[1], edge[2], edge[0]])
    
    # get any leftover edges and add them to edges_to_delete
    if (index < len(edges)):
        captureAnyRemainingEdges(edges, index, edges_to_delete)
    #print('all edges to remove from adj list are ', edges_to_delete)
    
    # remove any remaining edges from adjacency list
    if edges_to_delete:
        trimResultAdjacenyList(adjacency_list, edges_to_delete)
    return adjacency_list

# takes the adjacency_list, removes duplicates(A-B is same as B-A) and 
# sorts the edges with lowest weight first.      
def getSortedEdges(adjacency_list):
    edges = []
    for key in adjacency_list.keys():
        for value in adjacency_list[key]:
            edge = [value[1], key, value[0]]
            if isDuplicate(edges, edge) == False:
                    edges.append(edge)
    edges = sorted(edges, key=getKey)
    #print(edges)
    return edges

# for sorting the edges by weight
def getKey(edge):
    return edge[0]

# A-B is same as B-A
def isDuplicate(edges, newEdge):
    for edge in edges:
        if (edge[0] == newEdge[0]):
            if (edge[1] == newEdge[2]) and (edge[2] == newEdge[1]):
                return True;
    return False

# Get all the edges that did not go through Krushkal algorithim.
def captureAnyRemainingEdges(edges, begin, edges_to_delete):
    index = begin
    while index < len(edges):
        #print("remaining indexes ", index, edges[index])
        edge = edges[index]
        edges_to_delete.append([edge[1], edge[2], edge[0]])
        index += 1

# Remove edges that are not needed from the adjacency list  
def trimResultAdjacenyList(adjacency_list, edges):
    for edge in edges:
        
        values = adjacency_list.get(edge[0])
        new_values = values
        if values:
            for value in values:
                #print('value ', value)
                #print('(\'{src}\', {destination})'.format(src=edge[1], destination=edge[2]))
                if (str(value) == '(\'{src}\', {destination})'.format(src=edge[1], destination=edge[2])):
                    new_values.remove(value)
                    #print('new_values ', new_values)
        adjacency_list[edge[0]] = new_values
        
        values = adjacency_list.get(edge[1])
        new_values = values
        if values:
            for value in values:
                #print('value ', value)
                if (str(value) == '(\'{src}\', {destination})'.format(src=edge[0], destination=edge[2])):
                    new_values.remove(value)
        adjacency_list[edge[1]] = new_values
        
                       
        
result = question3({'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]})
print(result)
# Expecting the same adjacency list back

result = question3({'A': [('B', 4), ('C', 8)],
 'B': [('A', 4), ('C', 11)], 
 'C': [('A', 8), ('B', 11)] })
 
print(result)
# Expecting the edge B to C to be removed since it forms a cycle. 
# so result is now, {'A': [('B', 4), ('C', 8)], 'B': [('A', 4)], 'C': [('A', 8)]}

result = question3({'A': [('B', 4), ('C', 8)],
 'B': [('A', 4), ('C', 11)], 
 'C': [('A', 8), ('B', 11), ('D', 11)],
 'D': [('C', 11)] })
print(result)
# Expecting the edge B to C removed since it forms a cycle 
# {'A': [('B', 4), ('C', 8)], 'B': [('A', 4)], 'C': [('A', 8), ('D', 11)], 'D': [('C', 11)]}

result = question3({'A': [('B', 4), ('C', 8)],
 'B': [('A', 4), ('C', 11), ('D', 5)], 
 'C': [('A', 8), ('B', 11), ('D', 11)],
 'D': [('B', 5), ('C', 11)] })
print(result)
# The edge C to D is a cycle so it is removed.
# Expected: {'A': [('B', 4), ('C', 8)], 'B': [('A', 4), ('D', 5)], 'C': [('A', 8)], 'D': [('B', 5)]}

"""
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an 
ancestor of both nodes. For example, the root is a common ancestor of all 
nodes on the tree, but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all 
BST properties. 

The function definition should look like question4(T, r, n1, n2), where T is the tree 
represented as a matrix, where the index of the list is equal to the integer stored 
in that node and a 1 represents a child node, r is a non-negative integer representing 
the root, and n1 and n2 are non-negative integers representing the two nodes in no 
particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""

def findAncestors(T, r, n, ancestors):
    if n == r:
        return
      
    left = T[r].index(1)
    try:
        right = T[r].index(1, left + 1)
    except:
        right = left
        
    #print(left, right)
    ancestors.append(r)
    if n < r:
        findAncestors(T, left, n, ancestors)
    if n > r:
        findAncestors(T, right, n, ancestors)
            
        
        """  
        for index, elem in enumerate(T[r]):
            if elem == 1:
                ancestors.append(r)           
                findAncestors(T, index, n, ancestors)
                if n < r:
                    break;
        """       
        
def question4(T, r, n1, n2):
    
    n1_ancestors = []
    n2_ancestors = []
    
    findAncestors(T, r, n1, n1_ancestors)
    findAncestors(T, r, n2, n2_ancestors)
    #print(n1_ancestors, n2_ancestors)
    # check the last ancestor that is common to both nodes.
    for node1 in reversed(n1_ancestors):
        for node2 in reversed(n2_ancestors):
            if node1 == node2:
                return node1            
    return -1


bst = [[0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]]

print(question4(bst, 3, 0, 4))
# Expecting 3 as the least common ancestor

bst = [[0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]]
print(question4(bst, 3, 1, 4))
# Expecting 3 as the least common ancestor


bst = [[0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0]]
print(question4(bst, 4, 0, 3))
# Expecting 2 as LCA

bst = [[0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0]]
print(question4(bst, 4, 1, 5))
# Expecting 4 as LCA

"""
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the 
end is the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end".
 
You should copy/paste the Node class below to use as a representation of a node in 
the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        """
        Adds new nodes to the back of linked list.
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def getPosition(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position > self.getLength() or position < 0:
            return None
        current = self.head
        if self.head:
            count = 0
            while (count <= position and current.next):
                if (count == position):
                    return current
                current = current.next
                count += 1
            return current    
        else:        
            return None

    def getLength(self):
        """
        loops through nodes and returns the number of nodes.
        """
        current = self.head
        if current == None:
            return 0
        count = 0
        while (current.next):
            current = current.next
            count += 1
        return count + 1
               
# Test cases
# Set up some Elements
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Start setting up a LinkedList
mylist = LinkedList(node1)
mylist.append(node2)
mylist.append(node3)
mylist.append(node4)

def question5(ll, m):
    if m <= 0:
        return None
    length = ll.getLength()
    if m > length:
        return None
    return ll.getPosition(length - m)

if question5(mylist, 2):
    print(question5(mylist, 2).data)
# Expecting 3 (2nd node from last)

print(question5(mylist, 1).data)
# Expecting 4 (1st node in the back of list)

print(question5(mylist, 3).data)
# Expecting 2 (3nd node from last)

print(question5(mylist, 4).data)
# Expecting 1 (4th node from last)

print(question5(mylist, 11))
# Expecting None when asked for node location that does not exist

print(question5(mylist, 0))
# Expecting None when asked for node location that does not exist