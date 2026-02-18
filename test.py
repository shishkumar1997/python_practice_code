# 1------------------ 

n=1221 
temp =n 
power=len(str(temp)) 
result=0 
while temp>0: 
     digit=temp%10 
     result=result*10+digit 
     temp =temp//10 
print(result,n) 
if result==n: 
     print('number is polidram') 
else: 
     print('number is not polidram') 

 

# 2------------------------- 

arr = [2,3,4,5,6] 

l,r = 1,3  # Index 

# Output = [2,5,4,3,6] 

  

while l<r: 

    arr[l],arr[r]=arr[r],arr[l] 

    l=l+1 

    r=r-1 

print(arr) 

 

 

 

 

 

 

# 3------------------------ 

arr = [2,3,4,5,6] 

n=len(arr)+1 

  

excepredsum=(n*(n+1))/2 

actual=sum(arr) 

result=excepredsum-actual 

print(result) 

 

# 4-------------------- 

text ,d,s= "programming",{},[] 

for i in text: 

    if i in d: 

        d[i]+=1 

    else: 

        d[i]=1 

        s.append(i) 

# print(d['']) 

print('non repeated data:',s[0]) 

# 5---------------------------- 

s="I love Python programming" 

# Output: 

"programming Python love I" 

  

result="" 

s=s.split(' ')[::-1] 

for i in s: 

    result+=i+' ' 

print(s) 

print(result) 

# 6-------------------------------- 

arr = [1,2,3,4,1,3,5] 
# Output = [1,3] 
d = {} 
res = [] 
for i in range(0,len(arr)): 
     if arr[i] in d: 
         d[arr[i]] +=1 
     else: 
         d[arr[i]] = 1 
 
     if d[arr[i]] >1: 
         res.append(arr[i]) 
 
print(res) 

  

# Time Complexcity: O(n) 
# Space Complexcity: O(n) 

 

# 7--------------------------- 

s="I love python programming" 

# Output: 

#Vowels: 4   

#Consonants: 13 

  

re=['a','e','i','o','u'] 

vowel,consonant=[],[] 

for i in s.lower(): 

    if i in re: 

        vowel.append(i) 

    if i not in re and i not in " ": 

        consonant.append(i) 

     

print('Vowels:', len(vowel),vowel) 

print('Consonants:', len(consonant),consonant) 

 

 

# 8---------------------- 

 

 

l = [1, 5, 7, -1, 5] 

#output    [(1, 5), (7, -1), (1, 5)] 

Sum = 6 

res = [] 

d = {} 

  

for i in l: 

    x=Sum-i 

    if x in d: 

        res.append((x,i)) 

    if i in d: 

        d[i]+=1 

    else: 

        d[i]=1 

print(res) 

         

# 9-------------------- 

def iteratevalue(n, l=[]): 

    if n == 0: 

        print("good bay",l) 

        return 

    print(n) 

    l.append(n) 

    iteratevalue(n - 1) 

iteratevalue(5) 

 

# 10----------------- 

def iteratevalue(n): 

    result=0 

    if n ==1: 

        return 1 

    result=n*iteratevalue(n-1) 

    return result 

     

c=iteratevalue(5) 

print(c) 

# 11----------------- 

def fib(n): 

    if n <= 1: 

        return n 

    return fib(n-1) + fib(n-2) 

  

# print first `n` numbers 

n = 7 

for i in range(n): 

    print(fib(i), end=" ") 

 

 

# 12---------------- 

matrix = [ 

    [1, 2, 3], 

    [4, 5, 6], 

    [7, 8, 9] 

] 

  

# Step 1: Transpose matrix 

for i in range(len(matrix)): 

    for j in range(i, len(matrix)): 

        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

  

# #Step 2: Reverse each row 

for row in matrix: 

    row.reverse() 

  

# Final Output 

print(matrix) 

 

 

 

 

# 13--------------- 

# Two matrices 

A = [ [1, 2, 3], [4, 5, 6], ] 

B = [ [7, 8, 9], [1, 2, 3], ] 

# Result matrix (same size) 

result = [] 

for i in range(len(A)): # rows loop row = []  

    for j in range(len(A[0])): # columns loop  

        row.append(A[i][j] + B[i][j]) 	 

    result.append(row) 

print("Matrix Addition Result:")  

for r in result:  

    print(r) 

 

# 14-------------- 

m1=[ 

    [1,3,4], 

    [10,20,30], 

    

    ] 

     

m2=[[100, 10, 1],  

    [200, 20, 3], 

    ] 

result=[] 

for i in range(len(m1)): 

    row=[] 

    for j in range(len(m1[0])): 

        row.append(m1[i][j]+m2[i][j]) 

    result.append(row) 

# print(result) 

for r in result: 

    print(r) 

 

# 15-------------- 

nums=[2,[7,11],15,6,3,[12,13,[15,19],10,20,(90,1)],(100,200)] 

  

#output 

#[2, 7, 11, 15, 6, 3, 12, 13, 15, 19, 10, 20, 90, 1, 100, 200] 

def flatten(lst, result=[]): 

    for i in lst: 

        if type(i) == list: 

            flatten(i, result) 

        elif type(i) == tuple: 

            flatten(i, result) 

        else: 

            result.append(i) 

    return result 

print(flatten(nums)) 

# 16-------------- 

 

l=[2,4,6,7] 

target =6 

#0utput [0,1] 

  

d={} 

for i ,num in enumerate(l): 

    x=target - num 

    if x in d: 

        print(d[x],i) 

    else: 

        d[num]=i 
 
# 17_________________________________________________________________ 

l=[2,4,6,7] 

target =6 

#0utput [0,1] 

  

for i in range(len(l)): 

    for j in range(i+1,(len(l))): 

        if l[i]+l[j]==target: 

            print([i,j]) 

# 18+++++++++++++++++++++++++++++++++++++++++++++++++++ 

import pandas as pd 
d={'salary':900000,'name':'Ashish'}
d.update(salary=20000)
print(d)
salary,name=[],[] 

print(list(d)) 

for k,v in d.items(): name.append(k)
salary.append(v) 

print(list(d.items())) 

df = pd.DataFrame(list(d.items()),columns=['name','salary'])
print(df) 

 

# 19++++++++++++++++++++++++++++++++++++++++++++++++++++ 

s="google" 

d={} 

l=[] 

for i in s: 

    if i not in d: 

        d[i]=1 

        l.append(i) 

    else: 

        d[i]=2 

print(d) 

  

for i in s: 

    if d[i]==1: 

        print(i) 

        break 

# 20+++++++++++++++++++++++++++++++++++++++++++++++++++++ 

# 21++++++++++++++++++++++++++++++++++++++++++++++++++++= 

# 22+++++++++++++++++++++++++++++++++++++++++++++++++ 

# 23+++++++++++++++++++++++++++++++++++++++++++++++++++++ 

 
 
 
 