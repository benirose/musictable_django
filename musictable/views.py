from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Song

# Create your views here.

class IndexView(generic.ListView):
	model = Song
	template_name = 'songs/index.html'
	paginate_by = 50

	def get_queryset(self):
		if self.request.method == "POST":
			q = Song.objects.search(self.request.POST['search'])
		else:
			q = Song.objects.all()
		return q

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		# get subset of page range for paginator
		if context['page_obj'] is not None:
			range_max = min(context['paginator'].num_pages-1, context['page_obj'].number+9)
			range_min = max(1, range_max-10);
			context['page_range'] = list(context['paginator'].page_range)[range_min:range_max] # current page plus up to 10 pages, not including first and last
			context['page_range'].insert(0,1); # first page
			context['page_range'].append(context['paginator'].num_pages);
		return context

	def post(self, request, *args, **kwargs):
		return self.get(request, *args, **kwargs)

class DetailView(generic.DetailView):
	model = Song
	template_name = 'songs/detail.html'