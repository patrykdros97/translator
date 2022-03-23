from django.shortcuts import render
from googletrans import Translator, LANGUAGES

# Create your views here.
def translator_application(request, *args, **kwargs):
    if request.method == 'POST':
        new_lang = request.POST.get('lang', None)
        new_txt = request.POST.get('txt', None)
        print(new_lang)
        print(new_txt)

        translator = Translator()
        output = translator.translate(text=new_txt, dest=new_lang, src='auto')
        context = {
            "lang_list": LANGUAGES,
            "result": output.text,
            "to_translate": new_txt
        }
        return render(request, 'translate.html', context)

    return render(request, 'translate.html')
