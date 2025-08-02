from django.shortcuts import render
import random

def game_view(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['tries'] = 0

    message = ''
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        request.session['tries'] += 1
        number = request.session['number']

        if guess < number:
            message = 'Больше'
        elif guess > number:
            message = 'Меньше'
        else:
            message = f'Угадал за {request.session["tries"]} попыток!'
            del request.session['number']
            del request.session['tries']

    return render(request, 'game.html', {'message': message})
