from blog.models import *

def catagory_list(request):
    catagories = Catagory.objects.all()
    return {'catagories':catagories}
