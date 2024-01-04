from django.shortcuts import render , get_object_or_404 , redirect
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    return render(request,'notes/note_detail.html',{ "note": notes })

def note_detail(request, pk):
    note = get_object_or_404(note, pk=pk)
    return  render(request, 'notes/note_detail.html',{'note':note})

def note_new (request):
    if request.method =="POST":
        from = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail',pk = note.pk)
        else:
            form = Noteform()
            return render(request, 'notes/note_edit.html', {'form':form})

def note_edit (request, pk ):
    note_new() = get_object_or_404(Note,pk=pk ):
    if request.method == "POST":
        from = NoteForm(request.POST, isinstance=note)
        if form.is_valid()
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail',pk=note.pk)
        else:
            from = NoteForm(instance=note)
            return render(request,'note_edit.html'{'form':form})

def note_delete(request,pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
