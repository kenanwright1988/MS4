from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Animal, Category
# from .forms import ProductForm

def all_animals(request):
    """ A view to show all animals, including sorting and search queries """

    animals = Animal.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                animals = animals.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            animals = animals.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            animals = animals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            animals = animals.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'animals': animals,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'animals/animals.html', context)


def all_animals_care(request):
    """ A view to show all animal care guides, including sorting and search queries """

    animals = Animal.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                animals = animals.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            animals = animals.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            animals = animals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            animals = animals.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'animals': animals,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'animals/care.html', context)


def animal_details(request, animal_id):
    """
    View for Animal Details.
    """
    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        'animal': animal,
    }
    return render(request, 'animals/animal_details.html', context)


def animal_care(request, animal_id):
    """
    View for Animal Care.
    """
    animal = get_object_or_404(Animal, pk=animal_id)

    context = {
        'animal': animal,
    }
    return render(request, 'animals/care_details.html', context)
