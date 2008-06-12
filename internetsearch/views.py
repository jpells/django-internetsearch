from django.shortcuts import render_to_response
from internetsearch.web_search import google
from django.template import RequestContext
from django.contrib.sites.models import Site

def search(request, term = None, results_number = 10):
    if request.POST or term:
        results_number = int(results_number)
        site_search_term = " site:%s" % Site.objects.get_current().domain
        if request.POST:
            term = request.POST['term']
        result = google(term + site_search_term, results_number)
        return render_to_response('internetsearch/search.html', {'term': term, 'result': result, 'results_number': results_number}, context_instance=RequestContext(request))
    else:
    	return render_to_response('internetsearch/search.html', context_instance=RequestContext(request))
