from django.shortcuts import render, get_object_or_404, redirect
from .models import Host, Feedback
from .forms import FeedbackForm

def host_detail(request, host_id):
    host = get_object_or_404(Host, id=host_id)
    feedbacks = host.feedbacks.all()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.host = host
            feedback.user = request.user
            feedback.save()
            return redirect('host_detail', host_id=host.id)  # Redirect after feedback submission
    else:
        form = FeedbackForm()

    return render(request, 'host_detail.html', {
        'host': host,
        'feedbacks': feedbacks,
        'form': form,
    })
