class Node:
    def __init__(self, eol):
        self.eol = eol
        self.d = {}

    def add(self, char, child):
        self.d[char] = child

    def __str__(self):
        return str(self.d)


def add_s(trie, s):
    if len(s) == 1:
        ## add empty leaf end sentinel thinger
        c = s[0]
        if c not in trie.d:
            trie.d[c] = Node(True)

        return
    c = s[0]
    if c not in trie.d:
        trie.d[c] = Node(False)
    add_s(trie.d[c], s[1:])

def print_trie(trie):
    output = {}
    for k, v in trie.d.items():
        output[k] = print_trie(v)
    return output


root = Node(False)
add_s(root, 'abc')
add_s(root, 'abcd')
add_s(root, 'abef')
add_s(root, 'efg')
print(print_trie(root))
