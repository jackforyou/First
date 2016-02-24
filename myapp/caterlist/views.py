
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from .models import ChineseTable, FoodImage, SetMenu

class IndexView(generic.ListView):
    model = ChineseTable
    template_name = 'caterlist/index.html'
# Create your views here.

class CateringList(generic.ListView):
	model = ChineseTable
	template_name = 'caterlist/chinesetable_list.html'

class ChineseDetailView(generic.DetailView):
    model = ChineseTable
    template_name = 'caterlist/chinesetable_detail.html'
    # def get_context_data(self, **kwargs):
    #     context = super(ChineseDetailView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

def search(request):
	if 'placeText' in request.GET and request.GET['placeText']:
		q = request.GET['placeText']
		order_some = 'price_start_asc'
		url_order_by_prst_asc = '/search/?placeText=' + request.GET['placeText'] + '&price_start=' + request.GET['price_start'] + '&price_end=' + request.GET['price_end'] + '&order_by=price_start_asc'
		url_order_by_prst_desc= '/search/?placeText=' + request.GET['placeText'] + '&price_start=' + request.GET['price_start'] + '&price_end=' + request.GET['price_end'] + '&order_by=price_start_desc'
		url_order_by_pren_asc= '/search/?placeText=' + request.GET['placeText'] + '&price_start=' + request.GET['price_start'] + '&price_end=' + request.GET['price_end'] + '&order_by=price_end_asc'
		url_order_by_pren_desc= '/search/?placeText=' + request.GET['placeText'] + '&price_start=' + request.GET['price_start'] + '&price_end=' + request.GET['price_end'] + '&order_by=price_end_desc'
		if request.GET['price_start']:
			price_start = request.GET['price_start']
		else:
			price_start = 0
		if request.GET['price_end']:
			price_end = request.GET['price_end']
		else:
			price_end = 10000
		if 'order_by' in request.GET and request.GET['order_by']:
			order_some = request.GET['order_by']
			print(order_some)
		# else if request.GET['order_by_prst_desc']:
		# 	order_some = request.GET['order_by_prst_desc']

        places = ChineseTable.objects.filter(Q(place_for_service_text__icontains=q,price_start_number__lte= price_start) | Q(price_start_number__lte = price_end),Q(price_end_number__gte= price_start) | Q(price_end_number__gte = price_end)).order_by('price_start_number')
        setMenu = SetMenu.objects.all()
        return render(request, 'caterlist/chinesetable_searchresult.html',
            {'places': places, 'order': order_some, 'url_order_by_prst_asc':url_order_by_prst_asc, 'url_order_by_prst_desc': url_order_by_prst_desc, 'url_order_by_pren_asc':url_order_by_pren_asc, 'url_order_by_pren_desc':url_order_by_pren_desc, 'setmenu': setMenu,'query': q, 'price_start': price_start, 'price_end': price_end})
