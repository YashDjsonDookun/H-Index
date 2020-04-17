"""
This question was recently asked by Amazon.
An author has n papers that have been cited  n, amount of times. The H-Index is an author-level metric that attempts to measure both the productivity and citation impact of the publications. 

The H-Index is calculated by counting the number of publications for which an author has been cited by other authors at least the same number of times.

Example:
    Input: [20,4,33,30,15,7,6,5]
    Output: 6
"""
def hIndex(publications):
    for i in range(len(publications)):
        for j in range(len(publications)-1):
            if(publications[j] < publications[j+1]):
                publications[j], publications[j+1], publications[j+1], publications[j]
        if i+1 == publications[i]:
            return i+1
# print(hIndex([5,3,3,1,0]))
print(hIndex([33,30,20,15,7,6,5,4]))
