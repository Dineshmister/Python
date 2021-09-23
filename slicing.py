#unchanged
txt = "this is my github account"
print("Original text  :  ",txt)

#This text  has been jumbled
jumbled = "account my is this github"
print("\nJumbled sentence before slicing  : ",jumbled)

"""enumerate: using enumerate we can know the index values of elements or a string
enumerate will be shown in list or tuple or set here list has been used and inside enumerate 
the variable jumbled inside the enumerate function"""
index = list(enumerate(jumbled))

#with the use of enumerate now we can easily rearrange the string with the index values
print("\nindex values \nof text  :  ",index )

#here in slicing variable the string has been rearranged with respect to the position
#[14:18] - it implies the from 14th index value i.e from't' to 's' will be found
"""here [14:18] 14 = 't' is the start index and 18 is the end index we shouldn't use  
17 as end index it always omit the last range index i.e 17 in order to avoid this it has used 
18 as the last index"""
"""[11:13] - represents "is",if you use [11:12] instead of [11:13] it will print "i" and omit "s"
to avoid this [11:13] was used always increment the last index range"""
#[8:10] - represents "my"
"""[19:] - represents "github" here end range index is not used because the index ends at 24 and 
 "github" has occured at last"""
"""[:7] - represents "account" here start index is not used because  
the word "account" is at first """
# " " - space is concatenated between every words
slicing = jumbled[14:18]+" "+jumbled[11:13]+" "+jumbled[8:10]+" "+jumbled[19:]+" "+jumbled[:7]
print("\nAfter rearrange using slicing :  ",slicing)


#inserting any string in the desired position index using slice

#this word contain no words in the middle
example = "Thisprogram"
print("\nBefore adding : ",example)

#[:4]+string+[4:] specifying  in which position the string need to be added
adding = example[:4]+" is my "+example[4:]
print("\nAfter adding  : ",adding )
