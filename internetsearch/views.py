from django.shortcuts import render_to_response
from internetsearch.web_search import google
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.conf import settings

def search(request, term = None, results_number = 10):
    if request.POST or term:
        results_number = int(results_number)
        current_site = Site.objects.get(id=settings.SITE_ID)
        site_search_term = " site:%s" % current_site.domain
        if request.POST:
            term = request.POST['term']
        result = google(term + site_search_term, results_number)
        return render_to_response('search/search.html', {'term': term, 'result': result, 'results_number': results_number}, context_instance=RequestContext(request))
    else:
    	return render_to_response('search/search.html', context_instance=RequestContext(request))
