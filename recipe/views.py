from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def recipe_list(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('description')

        # to save data in model
        Recipe.objects.create(
            image=recipe_image,
            name=recipe_name,
            description=recipe_description
        )
        return redirect('/recipe/')
        # Process the form data here
        # For example, you can save it to the database or perform some action

    queryset = Recipe.objects.all()

    context = {
        'recipies': queryset
    }
    return render(request, 'index.html', context)


def delete_recipe(request, recipe_id):
    # queryset = Recipe.objects.get(id=recipe_id)
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    # return HttpResponse("Recipe deleted successfully.")

    return redirect('/recipe/')