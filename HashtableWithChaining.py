class MyObjectLL:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next = None

    def get_name(self):
        return self.name

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, obj):
        self.next = obj

    def is_name_equal(self, name):
        # In Python 'is' checks identity, whereas '==' checks equality.
        # Here we want to check that the string contents are the same, so we use an equality comparison.
        return self.name == name

class HashTableLL:
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

        obj = self.table[index]
        while obj and not obj.is_name_equal(key):
            obj = obj.get_next()

        return obj

    @staticmethod
    def get_hash_1(string):
        if not string:
            return 0

        hash_value = 0
        for ii in range(len(string)):
            hash_value += ord(string[ii]) # simplify this, to create easy collisions for our example

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
        if not self.table[index]:
            self.table[index] = value
            return

        #   1. IF this exact key is not present, append the value
		#      OR
		#   2. Replace If this exact key is present, replace the value.
        last_obj = None
        obj = self.table[index]
        while obj is not None:
            if obj.is_name_equal(key):
                # Exact key is present so we will replace (option #2 in comment above)
                self.replace_in_list(index, obj, last_obj, value)
                last_obj = None
                break

            last_obj = obj
            obj = obj.get_next()

        if last_obj:
            last_obj.set_next(value)

    def replace_in_list(self, index, obj, last_obj, value):

        if obj == self.table[index]:
            self.table[index] = value
            return

        last_obj.set_next(value)
        value.set_next(obj.get_next())

    @staticmethod
    def generate_hashes():
        s1 = "hello"
        s2 = "This is a long string, but not that long"
        s3 = "This is a longer string, 1234567890 abcdefghijklomno but not that long"

        print(f"Hash1 of s1 {HashTableLL.get_hash_1(s1)}")
        print(f"Hash2 of s1 {HashTableLL.get_hash_2(s1)}")

        print(f"Hash1 of s2 {HashTableLL.get_hash_1(s2)}")
        print(f"Hash2 of s2 {HashTableLL.get_hash_2(s2)}")

        print(f"Hash1 of s3 {HashTableLL.get_hash_1(s3)}")
        print(f"Hash2 of s3 {HashTableLL.get_hash_2(s3)}")

    @staticmethod
    def use_hash_table():
        key1 = "ABC"
        h1 = HashTableLL()
        print(f"(Should be False) hashtable has key {key1}: {h1.has_value(key1)}")

        HashTableLL.add_keys_to_hash_table(h1, key1)
        HashTableLL.check_key_presence(h1, key1)

        HashTableLL.cause_collisions(h1, key1)

    @staticmethod
    def add_keys_to_hash_table(h, key_prefix):
        for ii in range(5):
            h.add(key_prefix + str(ii), MyObjectLL(key_prefix + str(ii), ii))

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
        print("")
        print("------------------------------")
        print("---Now causing collisions-----")
        print("")

        # // Add a key that will resolve to the same index that we used earlier.
        new_key = "1" + key_prefix # instead of saying keyPrefix + 1, I am doing 1 + keyPrefix.
        #                            modified GetHash1 to be naive, and it will return the same hash
        #                            for 1 + keyPrefix as well as keyPrefix + 1

        print(f"Adding colliding key: {new_key}")

        # Adding now should cause a collision, and the hash table will append to the list at that index.
        h.add(new_key, MyObjectLL(new_key, 100))
        print(f"key: {new_key}. Value: {h.get_value(new_key).get_data()}")

        # Let's check if the key (key_prefix+1 is still there (it should be)
        if h.has_value(key_prefix + "1"):
            print(f"key: {key_prefix}1. Value: " + str(h.get_value(key_prefix + "1").get_data()))
        else:
            print(f"key: {key_prefix}1 missing...Oops..Error")

        # cause another collision
        yet_another_collision_causing_key = key_prefix[:1] + "1" + key_prefix[1:]
        print(f"Adding colliding key: {yet_another_collision_causing_key}")
        h.add(yet_another_collision_causing_key, MyObjectLL(yet_another_collision_causing_key, 200))
        h.add(yet_another_collision_causing_key, MyObjectLL(yet_another_collision_causing_key, 300))
        h.add(yet_another_collision_causing_key, MyObjectLL(yet_another_collision_causing_key, 400))
        print(f"key: {yet_another_collision_causing_key}. Value: {str(h.get_value(yet_another_collision_causing_key).get_data())}")

        # Let's check if the keys (key_prefix+1) and (1+key_prefix) are still there (should be)
        if h.has_value(key_prefix + "1"):
            print(f"key: {key_prefix}1. Value:" + str(h.get_value(key_prefix + "1").get_data()))
        else:
            print(f"key: {key_prefix}1 missing...Oops..Error")

        if h.has_value("1" + key_prefix):
            print(f"key: 1{key_prefix}. Value:" + str(h.get_value("1" + key_prefix).get_data()))
        else:
            print(f"key: 1{key_prefix} missing...Oops..Error")



HashTableLL.generate_hashes()
HashTableLL.use_hash_table()