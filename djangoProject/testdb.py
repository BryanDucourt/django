from django.http import HttpResponse
from testmodel.models import Test


def testdb(request):
    test1 = Test(name='bryand')
    test1.save()
    return HttpResponse("<p>succeed!</p>")