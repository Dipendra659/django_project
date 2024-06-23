from django.shortcuts import render, redirect


def create_note(request):
    if request.method == 'post':
        post_data = request.POST.copy()

        post_data [' is_completed'] = request.POST.get('is_completed')== 'on'


        form = note(post_data)
        if form.is_valid():
            form.save()
             return redirect ('create')
    else:
        form = note()
    notes = note.objects.all()
    context ={'form': form,'notes':notes}
    return render (request, template_name:'base/create.html',context)



# Create your views here.
