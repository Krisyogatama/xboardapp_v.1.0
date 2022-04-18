from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Dashboardview


def paginateDashboard(request, dashboardviews, results):

    page = request.GET.get('page')
    results = 6 
    paginator = Paginator(dashboardviews, results)

    try:
        dashboardviews = paginator.page(page)
    except PageNotAnInteger: 
        page = 1 
        dashboardviews = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        dashboardviews = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, dashboardviews


def searchDashboard(request):
    search_query =  ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    dashboardviews = Dashboardview.objects.filter(
        Q(project_name__icontains=search_query) |
        Q(bi_software__icontains=search_query) |
        Q(dashboard_title__icontains=search_query))

    return dashboardviews, search_query