 
def des_sort(scores):
    for i in range (n):
        for j in range(i+1 , n):
            if scores[i]<scores[j]:
                scores[i],scores[j]=scores[j],scores[i]



n = int(input("enter number of students: "))

scores = list(map(int,input("scores seperated by space: ").split()))


des_sort(scores)
print("sorted_list: ",scores)
runner_up = scores[1] if len(scores)>1 else scores[0]
print("runner-up score is:",runner_up)