from django.shortcuts import render

def show(request):
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)

    # 인자 3개 request , 템플릿, context(딕셔너리)
    return render(request,'party/show.html')