# Retrieve 'hoK' from the following tuple using indexing and slicing
t = ([30, 'hi', (4, {'names': ['Kohli', 'Sunil'], 'Ages': (45, 47)})])
print("1.", t[2][1]['names'][0][2::-1])

# WAP to retrieve ' OE' in reverse order using the positive indexing from following string
s1 = 'I LOVE PYTHON Java'
print("2.", s1[5:2:-2])      #reverse of 'OE' is 'EO' to retrieve

# WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
s2 = 'Hello I am going to Bengaluru How are you doing?'
print("3.", s2[-20:-29:-1])

# WAP to print the complete string in 7 ways using the slicing. String is given below
s3 = 'Program'
print("4.", s3, s3[::], s3[0::], s3[:len(s3):], s3[::1], s3[-7::], s3[:])

# WAP to retrieve the 'Iam' from following string using slicing
s4 = 'I ama jam'
print("5.", s4[::4])

"""
WAP to retrieve 'Python' in reverse order using negative indexing.
You should use Indexing and slicing Together. Please use below list.
"""
l1 = [1, 7.3, [33, 22], 'Hello Python']
print("6.", l1[3][-1:-7:-1])

"""
WAP to retrieve Jayansh and Shanvika ages in reverse order using positive indexing.
Output should be [7,4].
Please use below dictionary.
"""
students_info = {'student_names': ['Anil', 'Jayansh', 'Shanvika'], 'ages': [19, 4, 7],
                 'roll_nos': (201, 202, 205), 'classes': ['Intermediate', 'UKG', '2nd Grade'],
                 'sections': ['A', 'E', 'G'], 'percentages': [65.6, 78.9, 99.1]
                 }
print("7.", students_info['ages'][2:0:-1])

"""
WAP to retrieve (4,5) using positive indexing.
You should use Indexing and slicing Together.
Please use below list.
"""
l2 = [21, ['hi', 'hello', (3, 4, 5)], 45, 765, 2001, 51, 2034, 'Jai']
print("8.", l2[1][2][1:])

"""
Retrieve the value 2 using indexing and slicing using positive indexing.
Please use below list.
Write down the differences.
"""
l3 = [1, 2, 3]
print("9.", "By indexing:", l3[1], type(l3[1]), "\n  ", "By slicing:", l3[1:2], type(l3[1:2]))

"""
Difference :
---------------------------------------------------------------------------------------------------------------
1. the major difference between the indexing and slicing is that, by indexing it retrieves the value '2' in the
   form of data type the elements are stored i.e. <class 'int'>
   whereas, by using slicing as it is retrieving the part of a list within a range/boundary the value '2' will
   be extracted in the form of <class 'list'>
2. indexing will only allow to retrieve the data on which it is currently pointing but,
   slicing is flexible for the set or range within boundaries to fetch contiguous set of values/data.
---------------------------------------------------------------------------------------------------------------
"""
