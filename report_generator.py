def student_report(name,backend,frontend,design):
    average = (backend + frontend+design)/3
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"


    report = {
        'name': name,
        'Backend': backend,
        'Frontend': frontend,
        'Design': design,
        'average': round(average),
        'grade': grade
    }
    print(report)

        

print("--- Enter Student Details ---")
name = input(" Enter student's name: ")
backend = int(input("Enter Backend marks: "))
frontend= int(input("Enter Frontend marks: "))
design = int(input("Enter Design marks: "))



student_report(name,backend,frontend,design)
