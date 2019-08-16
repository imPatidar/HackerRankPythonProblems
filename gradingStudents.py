import os

def gradingStudents(grades):
   r=[]
   for i in grades:
       if i>=38 and i%5>=3:
            r.append(i+5-round(i%5))
       else:
           r.append(i)

   return(r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
