from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from diary.forms import DiaryEntryForm
from diary.models import DiaryEntry
from users.models import UserPreferences

# def main(request):
#     if request.user.is_authenticated:
#         try:
#             entries = DiaryEntry.objects.filter(creator=request.user)
#         except ObjectDoesNotExist:
#             entries = None

#         if request.method == 'POST':
#             form = DiaryEntryForm(request.POST)
#             if form.is_valid():
#                 instance = form.save(commit=False)
#                 instance.creator = request.user
#                 instance.save()
#                 return redirect('/')
#         else:
#             form = DiaryEntryForm()

#         context = {
#             'pref': UserPreferences.objects.get(user=request.user),
#             'entries': entries,
#             'form': form
#         }
#         return render(request, 'main/dashboard.html', context)
#     return render(request, 'main/dashboard.html')


def main(request):
    context = {}

    if request.user.is_authenticated:
        context['pref'] = UserPreferences.objects.get(user=request.user)
        context['diaryEntries'] = DiaryEntry.objects.filter(
            creator=request.user)
    context['diaryEntryForm'] = DiaryEntryForm()
    return render(request, 'main/dashboard.html', context)


def about(request):
    return render(request, 'main/main-about.html')
