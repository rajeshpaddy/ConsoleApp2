    import sys
from termcolor import colored,cprint
from time import time
from datetime import datetime as dt
import random as rand
import math
from collections import deque
error_color="red"

class top_coder:
    fib_cache = dict()
    stack = list()
    queue = deque()
    print_color=["magenta","white","cyan"]
<<<<<<< Updated upstream
    
    def find_missing_numbers(list_of_no):
	   return_string=””
	   temp_string=””
	   last_item=0
    for i in range(0,100):
	   last_item=i
		if i not in list_of_no:
			if len(temp_string)==0:
			temp_string=i
			prev_item=i
        else:
            if len(temp_string)>0:
	           if i!=prev_item+1:
                  temp_string+	=”-”+prev_item
		          return_string+=temp_string+”,”
                  temp_string=””

      if (prev_item==last_item) and prev-item!=temp_string and len(temp_string)>0:
		         temp_string+	=”-”+prev_item
	           	 return_string+=temp_string
	
       if (prev_item==last_item) and prev_item=temp_string:
	           temp_string=prev_item
	           return_string+=temp_string
	 return return_string	

    
    def binary_search(btree,data):
        '''
        binary_search - searchs a sorted balanced binary tree
        
        args
            btree: root of the binary tree
            data: data to search for
        returns
            attempts: # of attempts it took to find the data O(log N)
        '''
        attempt=1
        while btree is not None:
            if btree.data==data:
                return ("total attempt",attempt)
             
            if btree.data<data: # if the data is greater then search right
                btree=btree.right
                print("Right")
            else:    
                btree=btree.left #else search left
                print("Left")
            attempt+=1
            print("node:"+str(btree.data))
                  
            
=======
    phone_array=["0","0","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    uber_list=set()
    count=0
    uber_word_list=set()

    def find_all_words(uber_word,parent=""):
        return_item=""
        if len(uber_word)==0:
            return ""
        else:
            for i in list(uber_word):
                top_coder.count+=1
                if len(uber_word)==1:
                    return_item=i
                    top_coder.uber_word_list.add(i)
                else:
                    return_item=top_coder.find_all_words(uber_word[1:],i)    
                    top_coder.uber_word_list.add(i+return_item)
                    
        if parent=="":
            return_item=top_coder.uber_word_list
            print(top_coder.count)
            return return_item
        else:    
            return return_item

    def find_all_phone_combination(phone_number,parent=""):
        
        return_item = ""
        # print("Phone Number is {0}   {1}".format(phone_number,len(phone_number)))
        if len(phone_number)==0:
            return "" 
        else:
            for i in list(top_coder.phone_array[int(phone_number[0])]):
                top_coder.count+=1 #get a count of total iterations
                newparent=parent+i;
                if len(phone_number)==1: 
                    top_coder.uber_list.add(newparent)
                else:    
                    top_coder.find_all_phone_combination(phone_number[1:],newparent)
        if parent=="":
            return_item = top_coder.uber_list
            print (top_coder.count)            
        return return_item

    def find_start_of_cll(ll):
        '''
        The algo is to have two pointers and make one run twice as fast as the other. Where ever they meet that node to start 
        of circular link list distance is same as the start of link to start of circular link list
        '''

    def find_nth_fromlast(ll,n):
        '''
        trick question to find the nth node from the last. The algo is to have one point move to the nth element
        and then have both pointers navigate together until the 1st point reaches the end of linked list
        '''
        p1=ll
        p2=ll
        for i in range(1,n):
            if (p2.next is not None):
                p2=p2.next
            else:
                break
        while (p2.next is not None):
            p1=p1.next
            p2=p2.next
        
        return p1
        
    def count_ll_elements(ll):
        count=0
        a=ll
        while(a is not None):
            count+=1
            a=a.next
        return count


    class ll:
        def __init__(self,data = None):
            self.data=data
            self.next=None
        def create_nodes(self,numberof_nodes=5):
            return_item = self
            for i in range(1,numberof_nodes):
                self.next=top_coder.ll(i)
                self=self.next

            return return_item

    def delete_node(node):
        '''
        to delete an arbitary node in linked list is straight forward. Copy the content of the next node to current and the 
        current node becomes next and next node is discarded
        '''
        if (node is None and node.next is None):
            return 
        else:
            n = node.next
            node.data=n.data
            node.next=n.next


        

>>>>>>> Stashed changes
    def dfs(btree):
        '''
        dfs - Traverse the tree "Depth first" and prints the node. The 
        search is done using a list as stack. When a new parent node is hit it 
        pushes the left and right node into a stack and then pop's the first node 
        and treats it as parent node, this happens in recusive manner 
        until there is no more node is left.
        
        args
            btree: root node of the binary tree 
        '''
        level=0 # for decorating the output
        linker="" # for decorating the output
        flatten_tree=list()
        while(btree is not None):
<<<<<<< Updated upstream
            flatten_tree.append(btree.data)
=======
            if level==0:
                linker=""
            else:
                linker="└──"

>>>>>>> Stashed changes
            print("  "*int(level-1)+linker+colored(str(btree.data),top_coder.print_color[level%3]))
            if btree.left is not None:
                level+=2
                top_coder.stack.append((btree.left,level))
        
            if btree.right is not None:
                top_coder.stack.append((btree.right,level))
        
            if len(top_coder.stack)==0:
                return flatten_tree
            else:
                tup=top_coder.stack.pop()
                btree=tup[0]
                level=tup[1]
            linker="└──"
            
        
    def bfs(btree):
        '''
        bfs - Traverse the tree "Breadth first" and prints the node. The search is done 
        using a deque as queue. When a new parent node is hit it pushes the left and right node into 
        a stack and then popleft the first node and treats it as parent node, this happens in recusive manner 
        until there is no more node is left.
        
        args
            btree: root node of the binary tree 
        returns
            flatten_tree:flatten list from the tree
        '''
        j=0
        flatten_tree=list()
        while(btree is not None):
            flatten_tree.append(btree.data)
            j+=2
            print(str(btree.data))
            
    
            if btree.left is not None:
                top_coder.queue.append(btree.left)
    
            if btree.right is not None:
                top_coder.queue.append(btree.right)
    
            if len(top_coder.queue)==0:
                return flatten_tree
            else:
                btree=top_coder.queue.popleft()


    class btree:
        def __init__(self, data=None):
            self.data=data
            self.left = None
            self.right= None

    def create_bt(list,btreeinstance):
        if list is None or len(list)==0:
            return None
        else:
            mid=int(len(list)/2)
            btreeinstance.data=list[mid]
            if(len(list)>1):
                btreeinstance.left=top_coder.btree()
                top_coder.create_bt(list[:mid],btreeinstance.left)
            if(len(list)>2): # right node is needed only if the array length is > 2 
                btreeinstance.right=top_coder.btree()
                top_coder.create_bt(list[mid+1:],btreeinstance.right)
                    
    
    def make_tree(list):
        '''
        make_tree - takes any list and binary traverse through the list and put them in a balanced 
        tree. This is a useful for balancing any tree
        
        args
            list: array 
        '''
        if list is None:
            return None
        else:
            btreeinstance = top_coder.btree()
            top_coder.create_bt(list,btreeinstance)
            return btreeinstance


    def remove_dup_linkedlist(linkedlist):
        '''
        remove_dup_linkedlist - takes the root node of the linked list and creates a hash
        tables (dict()) of the node item, if a same node item is found subsequently then the node is 
        discarded by linking the previous node to the next node. 
        
        args 
            linkedlist
        return
            non duplicate linked list
         
        '''
        dup_value=dict()
        head_node = linkedlist.head
        dup_value[linkedlist.data]=1
        prev_node = linkedlist.head
        while (linkedlist.next_node is not None):
            linkedlist = linkedlist.next_node
            if linkedlist.data in dup_value:
                dup_value[linkedlist.data]+=1
                prev_node.next_node= linkedlist.next_node
            else:
                dup_value[linkedlist.data]=1
                prev_node=prev_node.next_node
        return head_node

    def create_us_linkedlist(length=100):
        us_linkedlist = top_coder.linked_list(0)
        return_item = us_linkedlist.head
        for i in range(1,length):
            val=int(rand.random()*i)
            us_linkedlist.set_next(top_coder.linked_list(val))
        return return_item

    def print_linkedlist(linkedlist):
        print (linkedlist.data)
        while (linkedlist.next_node is not None):
            linkedlist=linkedlist.next_node   
            print (linkedlist.data)
        
    def replace_space(string,replace_with):
        l=list(string)
        print (l)
        i=0
        for c in l:
           if c==" ":
               l[i]="%20"
           i+=1
        
        return "".join(l)


    def is_anagram(string1,string2):
        return top_coder.sorting.mergesort(list(string1.lower()))==top_coder.sorting.mergesort(list(string2.lower()))

    def string_sort(string):
        return top_coder.sorting.mergesort(list(string))
        
    def get_fib(number):
        if number<=1:
            top_coder.fib_cache[number] = 1
          
        else:
            if number not in top_coder.fib_cache:
                top_coder.fib_cache[number] = top_coder.get_fib(number-1) + top_coder.get_fib(number-2)
        return top_coder.fib_cache[number]
    
    class sorting:
        '''
        sorting class implements various sort algorithms like merge sort and quicksort. 
        For more information refer help(top_coder.sorting)  
        '''
        glob=0

        def mergesort(sortlist):
            '''
            mergesort - given a list of items, the merge sort function applies divide and conquer 
            strategy to sort the list. The division occurs all the way until each of the sub array 
            has only one element. 
            
            Then the merge applies to each combination of the sub array. It compares each element of the 
            two array and appends the minimum to the original array until all the element of one of the 
            array is exhausted. Then it loops thru either of the array and appends any remaining item
            to the original array. This occurs recursively up the chain
            
            args
                unsorted list
            returns
                sorted list
            '''
            
            if len(sortlist)>1:
                middle_point = int(len(sortlist)/2)
         
                leftlist = top_coder.sorting.mergesort(sortlist[:middle_point])
                rightlist= top_coder.sorting.mergesort(sortlist[middle_point:])
                
                i=0 #left iterator
                j=0 #right iterator
                k=0 #original list iterator

                while(i<len(leftlist) and j<len(rightlist)):
                    if leftlist[i]<rightlist[j]:
                        sortlist[k]=leftlist[i]
                        i+=1
                    else:
                        sortlist[k]=rightlist[j]
                        j+=1
                    k+=1
                
                while(i<len(leftlist)):
                    sortlist[k]=leftlist[i]
                    i+=1
                    k+=1
                
                while (j<len(rightlist)):
                    sortlist[k]=rightlist[j]
                    j+=1
                    k+=1
                
            return sortlist


        def printsort_lean(sortlist):
            top_coder.sorting.glob=0
            result = top_coder.sorting.quicksort_lean(sortlist,0,len(sortlist))
            return result

        def printsort(sortlist):
            top_coder.sorting.glob=0
            result = top_coder.sorting.quicksort(sortlist)
            return_list =[]
            for i in result.split("-"):
                if(i!="-" and len(i)>0):
                    return_list.append(int(i))
            return ("BestCase="+str(top_coder.sorting.glob),"WorstCase="+str(int(math.pow(len(sortlist),2))),return_list)

        def quicksort_lean(sortlist,left,right):
            if left==right:
                return sortlist
            elif len(sortlist)>1:
                if top_coder.sorting.glob>3000:
                    print(top_coder.sorting.glob)
                    print(sortlist)
                    print("left",left)
                    print("right",right)
                    return sortlist
                r=int((left+right)/2) # get an mid position
                val=sortlist[r]
                position=0   
                for i in range(0,len(sortlist)):
                    top_coder.sorting.glob+=1
                    if (sortlist[i]<val and position>r) or (sortlist[i]>=val and position<r):
                        temp=sortlist[position]
                        sortlist[position]=val
                        sortlist[r]=temp
                        r=position
                    position+=1
                left=r
                right=len(sortlist)
                if right-left>0:
                    top_coder.sorting.quicksort_lean(sortlist,0,left)
                    top_coder.sorting.quicksort_lean(sortlist,left,right)

        def quicksort(sortlist):
            '''
            quicksort - take an unsorted list and find an arbitary element. Create two sub list as
            left and right. Compares every element of the original list to the arbitary element and 
            puts all element smaller than arbitary element in left and rest in right. This happens 
            recursively until there is only one element in the sub list. 
            
            Then it merge the left sub list, arbitary element and the right sub list and recursively 
            return up the chain to get the sorted list
            '''
            if len(sortlist)==1:
                
                return str(sortlist[0])+"-"

            elif len(sortlist)>1:
                r=int(rand.random()*len(sortlist)) # get an arbitary position
                left=[] # left bucket
                right=[] # right bucket
                position=0

                for i in sortlist:
                    top_coder.sorting.glob+=1
                    if i<sortlist[r]: 
                        left.append(i)
                    elif i>=sortlist[r] and position!=r:
                        right.append(i)
                    position+=1
                returnlist="" # conquer using the return list

                if len(left)>0:
                    le=top_coder.sorting.quicksort(left)
                    returnlist=str(le)+"-"
                returnlist+=str(sortlist[r])+"-"
                if len(right)>0:
                    ri=top_coder.sorting.quicksort(right)
                    returnlist+=str(ri)+"-"
                return returnlist

    class linked_list:
        def __init__(self, data=None,next_node=None):
            self.data=data
            self.next_node = next_node
            self.head=self

        def get_next(self):
            return self.next_node
            
        
        def get_data(self):
            return self.data

        def set_next(self,next_node):
            while(self.next_node is not None):            
                self = self.next_node
            self.next_node = next_node

        def search(self,data):
            while (self.data!=data or self is None):
                self=self.next_node
            return self

        def print(self):
            while (self is not None):
                print(str(self.data) + "-->")
                self=self.next_node             
        def delete(self,data):
            if (self.data == data): # special case for head node
                print(self.data)
                self=self.head.next_node
                self.head=self
                return self
            else:
                prev_node=top_coder.linked_list()
                while(self is not None and self.data!=data):
                    prev_node=self
                    self=self.next_node
                if (self is not None):
                    prev_node.next_node = self.next_node
    
    def calculate_waste(files,folder_count,cluster_size):
        hash = dict()
        return_value =[]
        file_id = -1
        for file in files:
            file_id = file.split()[0]
            if file_id in hash.keys():
                hash[file_id]+=int(file.split()[1])
            else:
                hash[file_id]=int(file.split()[1])
        for i in sorted(hash):
            return_value.append(cluster_size-hash[i]%cluster_size)
        return tuple(return_value)

    def tokenize(string,tokens):
        '''
        function that takes a string and returns a list of tokens found in the string.
        args
            string: the string on which the tokens have to be parsed for
            token: list of legitimate tokens to be searched
        returns
            list of tokens found in the string
        '''
        return_tokens = list()
        max_token_size=""
        while (len(string)>0):
            for tok in tokens:
                if string[0:len(tok)]==tok and len(max_token_size)<len(tok):
                    max_token_size=tok
            if len(max_token_size)==0:
                string=string[1:]
            else:
                return_tokens.append(max_token_size)
                string=string[len(max_token_size):]
                max_token_size=""
        return return_tokens
                
        
    def picture(size,markers=[],print_color="red"):
        '''
        this function call the hex_print function and prints the hexagon grid with markers  
        '''
        k=top_coder.hex_print(size,markers,print_color)
        for i in k:
            print(i)
        
    def hex_print(size,markers=[],print_color="red"):
        '''
        [linear implementation]
        this function prints a diagnol hexagon grid and places the markers with in the specified 
        hexagon
        args
        size: the n*n hexagon matrix. 
        markers: list of string with values on where the markers has to be places. 
        For example ["00v","11h"] will place the v market on the 0,0 cell and h marker on 
        the 1,1 cell 
        '''
        
        hex_parts=[" _","/"+colored({0},print_color)+"\\","\\_/"]

        marker=" "
        # state machine 
        hex_width=list()
        hex_height=list()

        #return result
        return_list=list()
        loops=0
        markers_hash=dict()

        # place the markers in a hash map for quick access
        for l in markers:
            loops+=1
            if(len(l)==3):
                markers_hash[l[0:1]+"-"+l[1:2]]=l[2:3]

        # seeding the state machine with initializers
        for i in range(0,size):
            loops+=1
            hex_width.append(-1*i) #state to determine which Hex part has to be placed
            hex_height.append(-1) # state to determine when to place the markers inside hex part (1)
        

        for i in range(0,size*3*len(hex_width)):
            loops+=1

            j=i%size # state for new lines
            
            if j==0:
                return_list.append("") # new line 
            
            if hex_width[j]==0:
                return_list[len(return_list)-1]+=hex_parts[0]

            elif hex_width[j]%2==1 and hex_width[j] in range(1,size*2+1,1):
                hex_height[j]+=1 # increment the row for the corresponding hex column
                
                # check if a marker has to be placed and then get the marker
                find_key= str(hex_height[j])+"-"+str(j) 
                if(find_key in markers_hash):
                    marker = markers_hash[find_key]
                
                return_list[len(return_list)-1]+=hex_parts[1].format(marker) #place the marker
                marker=" "

            elif hex_width[j]%2==0 and hex_width[j] in range(1,size*2+1,1):
                return_list[len(return_list)-1]+=hex_parts[2]
            hex_width[j]+=1    
        
            # can be improved to do this work in line
            return_list[len(return_list)-1]=return_list[len(return_list)-1].replace("//","/")
            return_list[len(return_list)-1]=return_list[len(return_list)-1].replace("\\\\","\\")
            if(len(return_list)>1):
                return_list[len(return_list)-1]=return_list[len(return_list)-1].replace(" _","_")

        # add leading space to shift the hex to right
        for last_few_rows in range(1,size):
            loops+=1
            return_list[len(return_list)-last_few_rows]="  "*(size-last_few_rows)+return_list[len(return_list)-last_few_rows]

        print (
            str("total cost : \n reading the markers " +colored({0},"white")+
            ", \n initializing the width " + colored({1},"white")+ " of the grid matrix, \n 1 loop thru the grid matrix " + colored({2},"white")+ 
            " and \n prettying the grid " + colored({3},"white") + 
            "\n = " 
            + colored({4},"white")).format(len(markers_hash),len(hex_width),size*3*len(hex_width),size-1,loops))
        return return_list

def print_MxN_matrix(m,n,color):
    
    try:
        if (m>9 or n>17):
            raise ValueError('OutofBoundMatrix')
            return 
        matrix = list([])
        for i in range(1,m+1):
            for j in range(1,n+1):
                matrix.append([i,j])

        print("\n")
        rowbuffer=""    
        row="|"
        rowlen=0

        for i in range(0,(m*n)):
            row+=colored(str(matrix[i][0])+":"+str(matrix[i][1]),color) + "|"
            if (i in range(n-1,m*n+1,n)):
                rowlen=n*4+1
                if n>=10:
                    rowlen+=n-10+1        
                rowbuffer+="-"*rowlen+"\n"
                rowbuffer+=row+"\n"
                row="|"
        rowbuffer+="-"*rowlen
        print(rowbuffer)
    except ValueError as e:   
        print(colored("Incorrect input caused Error <<{0}>>:".format(e),error_color)+"The screen allows to print a max matrix of 9X17")
    except:
        print(colored("Error <<Unknown>>:",error_color)+"some error occured, most likely incorrect color")
        
    
def string_replace(s,replace_with):
    '''
    function to replace a " " character in string with another character
    args
    s:string to be searched for " " and replace with <replacewith>
    replace_with: the string to be replaced with
    '''
    h=""
    for c in s:
        if c==" ":
            h+=replace_with
        else:
            h+=c
    return h

def is_uniquecharacters(s,sensitivity="CI"):

    '''
    [With Data Structure]
    function to determine if all the characters in the string are unique
    args
        s:string to search for unique characters
        sensitivity:case sensitive or insensitive search (CI or CS)
    '''
    tempstore=dict()
    if sensitivity=="CI":
        s=str(s).upper()
    for _ in s:
        if _ in tempstore.keys():
            print("One of the duplicate key is ", tempstore[_])
            return False
        else:
            tempstore[_] = _ 
    return True

def is_uc_loop(s):
    '''
    [Without Data Structure] 
    function to determine if all the characters in the string are unique
    args
        s:string to search for unique characters
        sensitivity:case sensitive or insensitive search (CI or CS)
    '''
    i=0
    j=0
    for _ in s:
        i+=1
        for a in s:
            j+=1
            if _==a and i!=j: 
                print("One of the duplicate key is ", _)
                return False  
        j=0   
    return True
    

def analyse_file(filename):
    try:
        file=open(filename,"rt")
        file_length=len(file.read())
        # file_word_count=[sum(1) for x in file.readline().split()]
        # file.seek(0)
        file_line_count=[sum(1) for x in file]
    finally:
        file.close()

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:	
            return False
    return True

def find_angle(hour,minute):
    """
    function that returns the angle between the hour and minute handle of the clock
    args
        hour
        minute
    return
    the minimum angle  between the hour and the minute handle of the clock
    """
# if hour== 12 and minute==00 :
#return 0   
    hour_angle_h = 30*int(hour)
    hour_angle_m = int(minute)/2 # for every minute, there is .5 degree displacement in hour needle
    hour_angle = hour_angle_h + hour_angle_m
    minute_angle = 6*int(minute)
    return min(360-abs(hour_angle-minute_angle),abs(hour_angle-minute_angle))
    
def fetch_words():
    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            line_words=line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)
            for word in story_words:
                print(word)

def print_arg(url):
    """
    print_arg(arl)	
    Args:
        url is the thing that you want to pass
    """
    print(url)

attempt=0
time_start=time()
time_end=time()
position=0

def find(array,value):
    """
    function that binary traverse an array to find the value	
    Args:
    array, to be searched in  
    value, to be found
    returns
    the position of the found value in the array
    """	
    global attempt
    global time_start
    global time_end
    global position
    
    attempt+=1	
    length=len(array)
    mid = int(length/2)
    #print("length",length,array)
    
    if attempt==1:
        position=mid
        time_end=time()
    
    if value not in array:
        print("{0} does not exist in the list collection".format(value))
        return		 
    
    if(length==1):
        #time_end=dt.now().microsecond
        #print (array)
        # print ("attempt",attempt)
        # print("ET {0} milliseconds".format(float(time_end-time_start)/1000))
        print("value {0} is found in the position {1}".format(value,math.floor(position)))
        position=0
        attempt=0
        return array
    
    if(value<array[mid]):
        position-=mid/2;	
        # print("left {0} attempt {1}".format(attempt,position),array[:mid])
        find(array[:mid],value)
    else:
        position+=mid/2;
        # print("right {0} attempt {1}".format(attempt,position),array[mid:])
        find(array[mid:],value)
    
if __name__=="__main__":
    print_arg(sys.argv[1])