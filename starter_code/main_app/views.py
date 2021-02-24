import django
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import SESSION_KEY, login as auth_login
from django.shortcuts import render , get_object_or_404
from .models import Category , Topic , Post
from .forms import PostForm, NewTopicForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, query
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse
from django.db.models import Q
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    category = Category.objects.all()
    topic = Topic.objects.all()
    print(category)
    return render(request, 'home.html', {'categories': category , 'topics':topic})
def category_topics(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category ,pk=category_id)
    topics = category.topics.order_by('-created_dt').annotate(topicPost=Count('posts'))
    return render(request, 'topics.html', {'categories': categories, 'category': category,'topics':topics})
def signup(request):
    form=CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('/')
    return render(request,'signup.html',{'form':form})
class UserUpdateView(UpdateView):
      model = User

      fields = ['first_name','last_name','email',]
      

      success_url = reverse_lazy('my_account')

      def get_object(self):
          return self.request.user



class topicCreate(CreateView):
  model = Topic
  fields = ['subject',
            'content_text', ]
  def form_valid(self, form):
    form.instance.created_by_id = self.request.user.id
    form.instance.category_id = self.kwargs['category_id']
    return super(topicCreate, self).form_valid(form)
  def get_success_url(self):
      topic = get_object_or_404(Topic, pk=self.object.id)
      return reverse('topic', args=[topic.category.pk, self.object.id]
                     )
class topicUpdate(UpdateView):
    model = Topic
    fields = ['subject',
              'content_text',]
    def get_success_url(self):
        topic = get_object_or_404(Topic, pk=self.object.id)
        return reverse('topic', args=[topic.category.pk , self.object.id]
                       )
class topicDelete(DeleteView):
    model = Topic
    def get_success_url(self):
        topic = get_object_or_404(Topic, pk=self.object.id)
        category = topic.category.pk
        return reverse('category_topics', args=[category]
                       )
@login_required
def create_post(request, category_id, topic_id):
    topic = get_object_or_404(Topic, category__pk=category_id, pk=topic_id)
    categories = Category.objects.all()
    SESSION_KEY = 'view_topic_{}'.format(topic.pk)
    if not request.session.get(SESSION_KEY, False):
        topic.views += 1
        topic.save()
        request.session[SESSION_KEY] = True
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic', category_id=topic.category.id, topic_id=topic.pk)
    else:
        form = PostForm()
    return render(request, 'topic.html', {'topic': topic, 'form': form, 'categories': categories})
class postUpdate(UpdateView):
    model = Post
    fields = ['message', ]
    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.object.id)
        category = post.topic.category.pk
        topic = post.topic_id
        return reverse('topic', args=[category, topic])
class postDelete(DeleteView):
    model = Post
    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.object.id)
        category = post.topic.category.pk
        topic = post.topic_id
        return reverse('topic', args=[category, topic]
                       )

        


def search(request):
    categories = Category.objects.all()

    query = request.GET.get('q')
    print(query)
    category=Category.objects.filter(name=query)
    return render(request,'search.html',{"categories":categories,"category":category})
    
