from django.shortcuts import render
from django.http import Http404
from .models import *


def index(request):
    if request.method == "POST":
        try:
            seat_number = int(request.POST['seat-number'])
            student = Student.objects.get(seat_number=seat_number)
            subjects = []

            for subject in Subject.objects.filter(student_seat_number=seat_number):
                subject.succeeded = subject.student_mark >= subject.minimum_mark
                subject.got_full_mark = subject.full_mark == subject.student_mark
                subjects.append(subject)

            total_percentage = sum([subject.student_mark if subject.in_total_result else 0 for subject in subjects]) * 100 /\
                               sum([subject.full_mark if subject.in_total_result else 0 for subject in subjects])
            total_percentage = str(total_percentage)[:str(total_percentage).find('.')+2]


            return render(request, 'main/result.html', {
                'subjects': subjects, 'total_percentage': total_percentage, 'student': student
            })
        except:
            return render(request, 'main/404.html', {'seat_number': request.POST['seat-number']})

    else:
        return render(request, 'main/index.html')
