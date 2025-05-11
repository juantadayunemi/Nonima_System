from django.core.paginator import Paginator

def paginator(request,objects):
    paginator=Paginator(objects,3)
    page_number=request.GET.get('page')
    registers=paginator.get_page(page_number)
    current_page = registers.number
    total_pages = paginator.num_pages

    pages_range = []
    for i in range(1, total_pages + 1):
        if abs(i - current_page) <= 2 or i == 1 or i == total_pages:
            pages_range.append(i)

    return {'registers': registers,'pages_range':pages_range,'current_page':current_page}
    

    