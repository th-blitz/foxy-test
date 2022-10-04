import collections

class breakout_trie_node:
    def __init__(self):
        # 26 + '_' + ' ' + 10 
        self.children = [None] * 40
        self.end = None
        self.len = 40

    def index(self, char):
        # 0 node, 1 _, 2 ' ', a - z, 0 - 9
        num = ord(char)
        if num <= 57 and num >= 48:
            return num - 48 + 28
        elif num >= 97 and num <= 122:
            return num - 97 + 3
        elif num == 95:
            return 1
        elif num == 32:
            return 2
        return math.inf  


# class breakout_trie_node:
#     def __init__(self):
#         self.children = [None] * 27
#         self.end = None

#     def index(self, char):
#         if char == ' ':
#             return 26
#         return ord(char) - 97
    
#     def next(self, char):
#         return self.children[index(char)]

#     def insert(self, char, node):
#         self.children[index(char)] = node
#         return

class Breakout_Trie:
    def __init__(self):
        self.root = breakout_trie_node()
        self.len = 0
        self.size = 0
    
    def add(self, args, method):
        def recur(i, node):
            if i < 0:
                if node.end == None:
                    node.end = method
                    self.len += 1
                    return True
                return False
            if args[i] == '<' or args[i] == '>':
                if node.children[0] == None:
                    node.children[0] = breakout_trie_node()
                    self.size += 1
                return recur(i - 1, node.children[0])
            idx = node.index(args[i])
            if node.children[idx] == None:
                node.children[idx] = breakout_trie_node()
                self.size += 1
            return recur(i - 1, node.children[idx])
        args = args[::-1]
        return recur(len(args) - 1, self.root)

    def get_leaves(self, node):
        self.leaves = []
        def recur(node):
            if node.children[0] != None:
                return self.leaves.append(node.children[0])
            return [recur(node) for node in node.children[1:] if node != None]
        recur(node)
        return self.leaves

    def parse(self, args):
        self.collect = []
        self.count = 0
        def recur(i, node, bag):
            self.count += 1
            if i < 0:
                if node.end != None:
                    self.collect.append(bag + [node.end])
                    return 
            idx = node.index(args[i])
            if node.children[idx] != None:
                recur(i - 1, node.children[idx], bag)
            elif node.children[0] != None:
                arg = ''
                while i >= 0 and args[i] != ' ':
                    arg += args[i]
                    i -= 1
                for breakout in self.get_leaves(node.children[0]):
                    recur(i, breakout, bag + [arg])
            return 
        args = args[::-1]
        recur(len(args) - 1, self.root, [])
        return self.collect
    

tree = Breakout_Trie()
import time
old = time.time()
import args_dictionary
for arg in args_dictionary.arguments:
    tree.add('fox ' + arg[0], arg[1])
print(tree.parse('fox clone env from enn'))
print(time.time() - old)