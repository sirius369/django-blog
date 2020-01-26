from django.shortcuts import render
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def home(request):
    last_posts = []
    posts = Post.objects.all().order_by('-date')
    for i in range(2):
        last_posts.append(posts[i])
    context = {'posts' : last_posts}
    return render(request, 'posts/home.html', context)

def all(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/all.html', context)

def post(request, post_id):
    selected_post = Post.objects.get(pk = post_id)
    selected_post.number_of_comments = len(Comment.objects.filter(post = selected_post.id))
    selected_post.save()
    comments = Comment.objects.filter(post = selected_post)
    user_authenticated = False
    context = {}
    liked = False
    if request.user.is_authenticated:
        user_authenticated = True
        user = User.objects.get(pk = request.user.id)
        if (Like.objects.filter(post = selected_post, user = user).exists()):
            liked = True
        else:
            liked = False
    context['is_liked'] = liked
    context['post'] = selected_post
    context['comments'] = comments
    context['user_authenticated'] = user_authenticated
    return render(request, 'posts/post.html', context)

@csrf_exempt
def add_comment(request, post_id):
    if request.method == "POST" and request.user.is_authenticated:
        u_pk = request.user.id
        comment_text = request.POST['comment_text']
        post = Post.objects.get(pk=post_id)
        comment = Comment(user = User.objects.get(pk=u_pk), post = post, text = comment_text)
        comment.save()
        post.number_of_comments += 1
        post.save()
        response = JsonResponse({'a' : "a"})
        return response
@csrf_exempt
def like(request, post_id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=request.user.id)
        if (Like.objects.filter(post = post, user = user).exists()):
            response = JsonResponse({'unliked' : True})
            Like.objects.filter(post=post, user=user).delete()
            post.number_of_likes = post.number_of_likes - 1
            post.save()
            return response
        else:
            like = Like(post = post, user=user)
            like.save()
            post.number_of_likes = post.number_of_likes + 1
            post.save()
            response = JsonResponse({'liked' : True})
            return response
    else:
        response = JsonResponse({'error' : 'User not loged in'})
        reponse.status_code = 403
        return response

def delete(request, comment_id):
    post_id = 0
    if request.user.is_authenticated:
        comment = Comment.objects.filter(pk=comment_id)
        if comment.exists():
            post_id = comment[0].post.id
            comment.delete()

    url = reverse('posts:post', kwargs={'post_id' : post_id})
    return HttpResponseRedirect(url)
