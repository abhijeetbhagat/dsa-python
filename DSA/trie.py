'''
Dictionary :
{'a': { is_end : true, c : { 'b' : { is_end: false, c : {}}, 'n' : {}}}, 'b' : {is_end : false, c: {}}, 'c' : {is_end: false, c: {}}}
'''

class Trie:
    def __init__(self):
        self.__root = None

    def add(self, word: str, meaning: str): 
        if self.__root is None:
            self.__root = {}

        m = self.__root 
        p = None
        for c in word:
            p = m
            if c not in m:
                m[c] = {'is_word': False, 'children': {}}
                m = m[c]['children']
            else:
                m = m[c]['children']
        p[word[len(word) - 1]]["is_word"] = True
 
t = Trie()
t.add("ban", "to prohibit")
t.add("banana", "a fruit")
t.add("abstract", "exist as an idea")
t.add("banana", "insane")