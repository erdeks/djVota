from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Respuesta, Pregunta

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lista_respuesta'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pregunta.objects.order_by('-fecha_publicacion')[:5]
class DetailView(generic.DetailView):
    model = Pregunta
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = 'polls/results.html'

def vote(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        selected_respuesta = pregunta.respuesta_set.get(pk=request.POST['respuesta'])
    except (KeyError, Respuesta.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'pregunta': pregunta,
            'error_message': "No has seleccionado ninguna respuesta.",
        })
    else:
        selected_respuesta.votos += 1
        selected_respuesta.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(pregunta.id,)))
