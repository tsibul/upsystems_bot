from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from game_management.models import Promo


@login_required()
def promo(request):
    promo = Promo.objects.filter(active=True).order_by('-promo_date')
    context = {'promo': promo}
    return render(request, 'game_management/promo.html', context)


def update_promo(request):
    date = request.POST['date']
    par1 = request.POST['par1']
    text1 = request.POST['text1']
    par2 = request.POST['par2']
    text2 = request.POST['text2']
    par3 = request.POST['par3']
    text3 = request.POST['text3']
    par4 = request.POST['par4']
    text4 = request.POST['text4']
    promo_type = request.POST['promo_type']
    try:
        promo_id = request.POST['promo_id']
        promo = Promo.objects.get(id=promo_id)
        promo.promo_date = date
    except:
        promo = Promo(promo_date=date)
    promo.par1 = par1
    promo.text1 = text1
    promo.par2 = par2
    promo.text2 = text2
    promo.par3 = par3
    promo.text3 = text3
    promo.par4 = par4
    promo.text4 = text4
    promo.promo_type = promo_type
    promo.save()
    return HttpResponseRedirect(reverse('game_management:promo'))

def delete_promo(request):
    promo_id = request.POST['pr_id']
    promo = Promo.objects.get(id=promo_id)
    promo.active = False
    promo.save()
    return HttpResponseRedirect(reverse('game_management:promo'))
