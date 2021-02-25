from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import SESSION_KEY, login as auth_login
from django.shortcuts import render , get_object_or_404
from .models import Category , Topic , Post
from .forms import PostForm,CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, query
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse
from django.db.models import Q
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

#------------------------------ MAIN ------------------------------#

# Index view for home page and main page thats display all category . 
def index(request):
    category = Category.objects.all()
    topic = Topic.objects.all()
    print(category)
    return render(request, 'home.html', {'categories': category , 'topics':topic})


# Topics view display all topics or artical in same page that related with one category 
def topics(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category ,pk=category_id)
    topics = category.topics.order_by('-created_dt').annotate(topicPost=Count('posts'))
    return render(request, 'topics.html', {'categories': categories, 'category': category,'topics':topics})

#------------------------------ AUTH------------------------------#

# Signup view that allow user to registration
def signup(request):
    form=CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('/')
    return render(request,'signup.html',{'form':form})

# Profile update view that allow user update first , last name  and email.
class UserUpdateView(UpdateView):
      model = User
      fields = ['first_name','last_name','email',]
      success_url = reverse_lazy('my_account')

      def get_object(self):
          return self.request.user

#------------------------------ TOPIC ------------------------------#


# Create topic view allow user to create topic with subject and content.
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

# Update topic view allow user to update subject and content of specific topics.
class topicUpdate(UpdateView):
    model = Topic
    fields = ['subject',
              'content_text','img',]
    def get_success_url(self):
        topic = get_object_or_404(Topic, pk=self.object.id)
        return reverse('topic', args=[topic.category.pk , self.object.id]
                       )

# Delete topic view allow user to delete topic.
class topicDelete(DeleteView):
    model = Topic
    def get_success_url(self):
        topic = get_object_or_404(Topic, pk=self.object.id)
        category = topic.category.pk
        return reverse('topics', args=[category]
                       )

#------------------------------ POST ------------------------------#


# Create post view allow user how is login to create post with comment text .
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


# Update post view allow user to update message "comment text " of specific topic.
class postUpdate(UpdateView):
    model = Post
    fields = ['comment', ]
    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.object.id)
        category = post.topic.category.pk
        topic = post.topic_id
        return reverse('topic', args=[category, topic])


# Delete post view allow user to delete post.
class postDelete(DeleteView):
    model = Post
    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.object.id)
        category = post.topic.category.pk
        topic = post.topic_id
        return reverse('topic', args=[category, topic]
                       )

        
#------------------------------ SEARCH ------------------------------#

#Search view that allow user to search about specific category
def search(request):
    categories = Category.objects.all()
    query = request.GET.get('q')
    print(query)
    category=Category.objects.filter(name=query)
    return render(request,'search.html',{"categories":categories,"category":category})
    
