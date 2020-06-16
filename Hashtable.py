class MyObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_data(self):
        return self.value

    def is_name_equal(self, name):
        # In Python 'is' checks identity, whereas '==' checks equality.
        # Here we want to check that the string contents are the same, so we use an equality comparison.
        return self.name == name

class HashTable:
    def __init__(self):
        self.table = [None] * 997
        self.table_size = 997
        #Python doesn't have built-in support for statically sized arrays,
        # so we're going to use a list as our backing storage. #
        # Mocking it up by pre-populating it with as many Nones as the list size and not using append.

    # Precondition: tableSize > 0
    def get_index(self, hash_value, table_size):
        return hash_value % table_size


    # Precondition: key is not null(None)
    def has_value(self, key):
        return self.get_value(key) is not None

    # Precondition: key is not null(None)
    def get_value(self, key):
        index = self.get_index(self.get_hash_1(key), self.table_size)

        # call is_name_equal to make sure we have the exact same key, and not just another entry
        # that happened to either have the same hash value, or happened to the resolve to the same index
        if self.table[index] and self.table[index].is_name_equal(key):
            return self.table[index]


    @staticmethod
    def get_hash_1(string):
        if not string:
            return 0

        hash_value = 0
        for ii in range(len(string)):
            hash_value += ord(string[ii]) * ii

        return hash_value

    @staticmethod
    def get_hash_2(string):
        if not string:
            return 0

        hash_value = 0
        for ii in range(len(string)):
            hash_value += ((hash_value << 4) + hash_value) + (ord(string[ii]) * ii)
            #hash_value = hash_value * 17 + str[ii] * ii;

        return hash_value # Ints in Python have arbitrary precision, so there's no chance of of overflow.
        # No need to do get the absolute (abs() in the standard library - but we will end up with different
        # Hash keys than the C# version for long strings

    def add(self, key, value):
        index = self.get_index(self.get_hash_1(key), self.table_size)
        self.table[index] = value # will overwrite any existing value. Does not handle collisions. BAD

    @staticmethod
    def generate_hashes():
        s1 = "hello"
        s2 = "This is a long string, but not that long"
        s3 = "This is a longer string, 1234567890 abcdefghijklomno but not that long"

        print(f"Hash1 of s1 {HashTable.get_hash_1(s1)}")
        print(f"Hash2 of s1 {HashTable.get_hash_2(s1)}")

        print(f"Hash1 of s2 {HashTable.get_hash_1(s2)}")
        print(f"Hash2 of s2 {HashTable.get_hash_2(s2)}")

        print(f"Hash1 of s3 {HashTable.get_hash_1(s3)}")
        print(f"Hash2 of s3 {HashTable.get_hash_2(s3)}")

    @staticmethod
    def use_hash_table():
        key1 = "ABC"
        h1 = HashTable()
        print(f"(Should be False) hashtable has key {key1}: {h1.has_value(key1)}")

        HashTable.add_keys_to_hash_table(h1, key1)
        HashTable.check_key_presence(h1, key1)

        HashTable.cause_collisions(h1, key1)

    @staticmethod
    def add_keys_to_hash_table(h, key_prefix):
        for ii in range(5):
            h.add(key_prefix + str(ii), MyObject(key_prefix + str(ii), ii))

    @staticmethod
    def check_key_presence(h, key_prefix):
        # now check if key present, and print value if present
        for ii in range(6):
            key = key_prefix + str(ii)
            if h.has_value(key):
                print(f"key: {key}. Value: {h.get_value(key).get_data()}")
            else:
                print(f"key not present: {key}")

    @staticmethod
    def cause_collisions(h, key_prefix):
        # Add same key again. Note, this will overwrite the value, which is not good.
        new_key = key_prefix + "1"
        h.add(new_key, MyObject(new_key, 100))
        print(f"key: {new_key}. Value: {h.get_value(new_key).get_data()}")


HashTable.generate_hashes()
HashTable.use_hash_table()