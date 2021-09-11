from hashmap_left_join.hashtable import HashTable

def hashmap_left_join(hash1,hash2):
    '''
    Implement a simplified LEFT JOIN for 2 Hashmaps.
    parameters:
        hash1: hash map
        hash2: hash map
    Arguments: hash1, hash2
    Returns: List - that LEFT JOINs two hashmaps into a single data structure.
    '''
    lj_output = []
    for i in ht1.array:
        if i:
            lj = []
            current_value = i.head
            while current_value:
                lj.append(current_value.value[0])
                lj.append(current_value.value[1])
                if ht2.contains(current_value.value[0]):
                    lj.append(ht2.get(current_value.value[0]))
                else:
                    lj.append(None)
                current_value = current_value.next

            lj_output.append(lj)
    return lj_output


    # buckets=hash1.get_buckets()
    # arr=[]
    # for i in buckets:
    #     if i:
    #         current=i.head
    #         while current:
    #             x=hash2.find(current.value[0])
    #             if not x:
    #                 x='Null'
    #             current.value.append(x)
    #             arr.append(current.value)
    #             current=current.next
    # return arr


if __name__ == "__main__":

    hash1 = HashTable()
    hash1.add('fond', 'enamored')
    hash1.add('wrath', 'anger')
    hash1.add('diligent', 'employed')
    hash1.add('outfit', 'garb')
    hash1.add('guide', 'usher')

    hash2 = HashTable()
    hash2.add('fond', 'averse')
    hash2.add('wrath', 'delight')
    hash2.add('diligent', 'idle')
    hash2.add('guide', 'follow')
    hash2.add('flow', 'jam')

    print(hashmap_left_join(hash1,hash2))
