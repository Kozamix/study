from django.shortcuts import render


from django.shortcuts import render , get_object_or_404 , redirect
from .models models import logic
from .forms import Noteform

def note_list(request):
    notes = Note.objects.all()
    return render(request,'notes/note_detail.html',{ "note": notes })

def note_detail(request, pk):
    note = get_object_or_404(note, pk=pk)
    return  render(request, 'notes/note_detail.html',{'note':note})

def note_new (request):
    if request.method =="POST":
        from = Noteform(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail',pk = note.pk)
        else:
            form = Noteform()
            return render(request, 'notes/note_edit.html', {'form':form})