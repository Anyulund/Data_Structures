class HashTableBase:
  def __init__(self, size = 10):
    self.length = size
    self.count = 0
    self.carton = [] #this is our storage

  def load_factor(self):
    lfactstore = self.count / self.length
    if lfactstore > self.loadf:
        self.rehash()
    return self.count / self.length

  def _hash(self, string):
    return sum(map(ord, string)) #we are using this for the key - integer

  def _index(self, value):
    return value % self.length

  def __str__(self):
     hstring = ''
     for item in self.carton:
         if item is not None:  #can try != Null
            hstring += str(item) + '\n'
         else:
             hstring += 'None' + '\n'
     return hstring


class ProbingHashTable(HashTableBase):
  def __init__(self, length = 10):
    HashTableBase.__init__(self,length)
    self.loadf = 0.75 #load factor
    for i in range (0,self.length):
        self.carton.append (None)


  def add(self, key, value):
    hkey = self._index(key)
    empty = False
    if self.carton[hkey] is None:
        self.count += 1
        self.carton [hkey] = [key, value]
        #print(self.load_factor())
        empty = True
    else:
        for i in range(hkey+1,self.length):
            if self.carton[i] is None and empty == False:
                self.count += 1
                self.carton[i] = [key, value]
                #print(self.load_factor())
                empty = True
        for i in range(0,hkey):
            if self.carton[i] is None and empty == False:
                self.count += 1
                self.carton[i] = [key, value]
                #print(self.load_factor())
                empty = True


  def lookup(self, key):
    hkey = self._index(key)
    for i in range(hkey,self.length):
        if self.carton[i] is None:
            return None
        if self.carton[i][0] == key:
            return self.carton[i]
    for i in range(0, hkey):
        if self.carton[i] is None:
            return None
        if self.carton[i][0] == key:
            return self.carton[i]


  def delete(self, key):
    hkey = self._index(key)
    for i in range(hkey,self.length):
        if self.carton[i] is None:
            return None
        if self.carton[i][0] == key:
            self.carton[i] = None
    for i in range(0, hkey):
        if self.carton[i] is None:
            return None
        if self.carton[i][0] == key:
            self.carton[i] = None

  def rehash(self):
    tempspot = self.carton
    self.length = self.length*2
    self.count = 0
    for i in range (0,self.length):
        self.carton.append (None)
    for item in tempspot:
        if item is not None:
            self.add(item[0], item[1])

class ChainingHashTable(HashTableBase):
  def __init__(self, length = 10):
    HashTableBase.__init__(self,length)

  def add(self, key, value):
    pass

  def lookup(self, key):
    pass

  def delete(self, key):
    pass

  def rehash(self):
    pass

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.pointer = None

class LinkedList:
  def __init__(self):
    self.head = None

  def add(self, key, value):
    pass

  def lookup(self, key):
    pass

  def delete(self, key):
    pass

HT = ProbingHashTable()
HT.add(12,'banana')
HT.add(22,'coyote')
HT.add(39, 'running')
HT.add(13,'peach')
HT.add(23,'dog')
HT.add(49, 'swimming')
HT.add(14,'pear')
HT.add(24,'cat')
HT.add(59, 'flying')
print(HT.delete(12))
print(HT)
