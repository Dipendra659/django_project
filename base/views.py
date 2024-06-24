from django.http import request
from django.shortcuts import render, redirect

from base.form import NoteForm
from base.models import Note





def create_Note(request):
    if request.method == 'POST':
        post_data = request.POST.copy()

        post_data ['is_completed'] = request.POST.get('is_completed')== 'on'


        form = NoteForm(post_data)
        if form.is_valid():
            form.save()
            return redirect ('create')
    else:
         form = NoteForm()

    notes = Note.objects.all()
    context = {'form': form,'notes':notes}
    return render(request,'create.html',context)



# Create your views here.
