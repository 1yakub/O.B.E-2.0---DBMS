from django.shortcuts import render
from django.db import connection

# Create your views here.


def login(request):
    return render(request, 'login.html')


def question(request):
    if request.method == 'POST':
        question_no = request.POST["question_no"]
        question_type = request.POST["question_type"]
        question_details = request.POST["question_details"]
        sample_answer = request.POST["sample_answer"]
        if question_no == "" or question_type == "" or question_details == "" or sample_answer == "":
            pass
        else:
            with connection.cursor() as cursor_2:
                cursor_2.execute("INSERT INTO question(quesID, quesType,quesDetail,sampleAns) VALUES ('"+str(
                    question_no) + "','"+str(question_type) + "','" + str(question_details) + "' ,'"+str(sample_answer) + "' )")
            connection.close()
        with connection.cursor() as cursor_1:
            cursor_1.execute("select * from question")
            row1 = cursor_1.fetchall()
        return render(request, 'question.html', {"row1": row1})
    with connection.cursor() as cursor_1:
        cursor_1.execute("select * from question")
        row1 = cursor_1.fetchall() 
    return render(request, 'question.html', {"row1": row1})


def course(request):
    if request.method == 'POST':
        courseCode = request.POST["courseCode"],
        courseTitle = request.POST["courseTitle"],
        courseType = request.POST["courseType"],
        courseDescription = request.POST["courseDescription"],
        courseObjective = request.POST["courseObjective"],
        coursePolicy = request.POST["coursePolicy"],
        ads = request.POST["ads"],
        swdas = request.POST["swdas"],
        ndp = request.POST["ndp"],
        courseContent = request.POST["courseContent"],
        clom = request.POST["clom"],
        lpmclo = request.POST["lpmclo"],
        tas = request.POST["tas"],
        assessment = request.POST["assessment"],
        grading = request.POST["grading"],
        referenceBook = request.POST["referenceBook"],
        additionalMaterials = request.POST["additionalMaterials"],
        return render(request, 'course.html', {"courseCode": courseCode, "courseTitle": courseTitle, "courseType": courseType, "courseDescription": courseDescription, "courseObjective": courseObjective, "coursePolicy": coursePolicy, "ads": ads, "swdas": swdas, "ndp": ndp, "courseContent": courseContent, "clom": clom, "lpmclo": lpmclo, "tas": tas, "assessment": assessment, "grading": grading, "referenceBook": referenceBook, "additionalMaterials": additionalMaterials})
    return render(request, 'course.html')
