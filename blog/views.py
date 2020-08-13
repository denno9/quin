from django.shortcuts import render
from django.views.generic import ListView,DetailView
import datetime
from .models import BlogPost
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
# Create your views here.


def blogPage(request):
    posts = BlogPost.objects.all().order_by('-date_added')
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context = {
         "year": year,
        
     }
    pagiator = Paginator(posts,10)
    page = request.GET.get('page')

    
    try:
        queryset = pagiator.page(page)
    except PageNotAnInteger:
        queryset = pagiator.page(1)
    except EmptyPage:
        queryset = pagiator.page(pagiator.num_pages)
    context['posts'] = queryset

     
      
    return render(request,'blogPage.html',context)


class BlogPostDetailView(DetailView):
    obj_queryset = BlogPost.objects.all()
    template_name ="postDetailPage.html"
    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        pk = 1
        instance1 = None
       
        try: 
            instance = BlogPost.objects.get(slug=slug)
            
        except Event.DoesNotExist:
               instance = blogPage.objects.all().first()
               if instance is None:
                    raise Http404("product doesnt exist")
       
        except:
            raise Http404("OOOPS")
        # print(instance.body)
        return instance

    def get_context_data(self,*args,**kwargs):
        context = super(BlogPostDetailView,self).get_context_data(*args,**kwargs)
        context['recents'] = BlogPost.objects.all()[:4]
        print(context)
        return context
    
    # def get_queryset(self,*args,**kwargs):
    #     request= self.request
    
    #     return Product.objects.all().featured( )

