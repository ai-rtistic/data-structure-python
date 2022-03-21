# Hash Table
class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value
        
    def read(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]
    
    def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False



class Chaining:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:    # 해시 충돌 시
            for a in range(len(self.hash_table[hash_address])):  # 빈 bucket 탐색
                if self.hash_table[hash_address][a][0] == key:    # key 에 맞는 value 매칭
                    self.hash_table[hash_address][a][1] = value
                    return
            self.hash_table[hash_address].append([key, value])
        else:
            self.hash_table[hash_address] = [[key, value]]
            
    def read(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:    # 해시 충돌 시
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key: # 일치하는 key 값 찾음
                    return self.hash_table[hash_address][a][1] # 일치하는 value 반환
            return False
        else:
            return False
    
    def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    if len(self.hash_table[hash_address]) == 1:
                        self.hash_table[hash_address] = 0
                    else:
                        del self.hash_table[hash_address][a]
                    return
            return False
        else:
            return False



class OpenAddressing:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:    # hash 의 값이 이미 존재할때 (해시충돌)
            for a in range(hash_address, len(self.hash_table)):
                if self.hash_table[a] == 0:
                    self.hash_table[a] = [key, value]
                    return
                elif self.hash_table[a][0] == key:
                    self.hash_table[a] = [key, value]
                    return
            return None
        else:    # hash 가 비었을때
            self.hash_table[hash_address] = [key, value]
            
    def read(self, key):
        hash_address = self.getAddress(key)
        
        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a][0] == key:
                return self.hash_table[a][1]
        return None
    
    def delete(self, key):
        hash_address = self.getAddress(key)
        
        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a] == 0:
                continue
            if self.hash_table[a][0] == key:
                self.hash_table[a] = 0
                return
        return False


if __name__ == '__main__':
    h_table = HashTable(8)
    h_table.save('a', '1111')
    h_table.save('b', '2222')
    h_table.save('c', '3333')
    h_table.save('d', '4444')

    print(h_table.hash_table)  # [0, '1111', '2222', '3333', '4444', 0, 0, 0]

    print(h_table.read('d'))  # 4444     

    h_table.delete('d')

    print(h_table.hash_table)  # [0, '1111', '2222', 0, '4444', 0, 0, 0]

    ####
    h_table = Chaining(8)

    h_table.save('aa', '1111')
    print(h_table.read('aa')) # 1111

    data1 = 'aa'
    data2 = 'ab'

    print(ord(data1[0]))   # 97
    print(ord(data2[0]))   # 97  같은 hash 값을 가짐 -> 해시 충돌

    h_table.save('ab', '2222')
    print(h_table.hash_table)  # [0, [['aa', '1111'], ['ab', '2222']], 0, 0, 0, 0, 0, 0]

    print(h_table.read('aa'))  # 1111
    print(h_table.read('ab'))  # 2222

    h_table.delete('aa')
    print(h_table.hash_table)  # [0, [['ab', '2222']], 0, 0, 0, 0, 0, 0]

    print(h_table.delete('Data')) # False

    ####
    h_table = OpenAddressing(8)

    data1 = 'aa'
    data2 = 'ab'
    print(ord(data1[0]), ord(data2[0]))    ## 97 97  -> 해시 충돌

    h_table.save('aa', '1111') 
    h_table.save('ab', '2222')

    print(h_table.hash_table)  # [0, ['aa', '1111'], ['ab', '2222'], 0, 0, 0, 0, 0]

    print(h_table.read('ab'))  # 2222

    h_table.delete('aa') 
    print(h_table.hash_table)  # [0, 0, ['ab', '2222'], 0, 0, 0, 0, 0]