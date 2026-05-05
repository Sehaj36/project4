
import sys
import re

#hash table using array of buckets
class hashtables:
    def __init__(self,size):
        #storing the size & creating list that will hold the buckets
        self.table_size = size
        self.buckets =[]

        for i in range(size):
            self.buckets.append([])
    #H(key) = key % m
    def hash_indexing(self,student_id):
        return student_id% self.table_size
    
    #adding student id or updating the count if it exists
    def add_id(self,student_id):
        index = self.hash_indexing(student_id)
        bucket = self.buckets[index]

        for records in bucket:
            if records[0] == student_id:
                records[1] += 1
                return False
        
        bucket.append([student_id,1])
        return True
    

    #finding and returning the count for a specific student id
    def find(self,student_id):
        index = self.hash_indexing(student_id)
        bucket = self.buckets[index]

        for record in bucket:
            if record[0] == student_id:
                return record[1]
            

        
        return 0
    
#Reading file from input file 
def load(file_name):
    #opening and reading
    with open(file_name, "r") as IDs_file:
        text = IDs_file.read()

    #converting nuymbers from strings to integer
    numbers_read = re.findall(r"\d+", text)
    id_list =[]
    for value in numbers_read:
        id_list.append(int(value))

    
    return id_list

#Finding all the duplicate ids and printing them 
def print_duplicate(id_list):
    #making hash tbale size larger than the number of IDS
    size = (len(id_list)*2)+1

    #creating hashtable
    table = hashtables(size)
    #seen list
    order_seen = []
    #inserting student id into hash table
    for student_id in id_list:
        new_entry = table.add_id(student_id)

        #save it in order if never seen id
        if new_entry:
            order_seen.append(student_id)

    print ("Duplicates found in: ")
    
    number_of_duplicate_ids = 0 
    extra_duplicates = 0
    
    for student_id in order_seen:
        amount = table.find(student_id)
        
        if amount > 1:
            print (student_id,"appears",amount ,"times")
            number_of_duplicate_ids += 1
            extra_duplicates += amount -1 

    print ("Total unique IDs:", extra_duplicates)
    print ("Total duplicate IDs: ", number_of_duplicate_ids)


def main():
    file_name = "ids.txt"
    student_ids = load(file_name)
    print_duplicate(student_ids)
    
main()


