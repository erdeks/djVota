from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse

from django.template import loader

from django.http import Http404

from django.views import generic

from .models import Preguntas, Respuestas


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Preguntas.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Preguntas
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Preguntas
    template_name = 'polls/results.html'
def vote(request, question_id):
    pregunta = get_object_or_404(Preguntas, pk=question_id)
    try:
        selected_choice = pregunta.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Respuestas.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': pregunta,
            'error_message': "No has respondido.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
