from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Poll, Choice, Vote

# Create your views here.

@require_POST
def vote(request, poll_id, choice_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choice = get_object_or_404(Choice, id=choice_id, poll=poll)

    # Ensure the user has not voted on this poll before
    if Vote.objects.filter(user=request.user, poll=poll).exists():
        return JsonResponse({"error": "You have already voted on this poll."}, status=400)

    # Record the vote
    Vote.objects.create(user=request.user, poll=poll, choice=choice)
    choice.votes += 1
    choice.save()

    return JsonResponse({"message": "Vote recorded successfully!", "choice_votes": choice.votes})

