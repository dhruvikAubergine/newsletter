from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Subscriber, Blog
from . serializer import SubscribeSerializer, BlogSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string


class SubscribeView(APIView):

    def get(self, request):
        """
            SubscribeView's get method used to redirect the subscribe page.
        """
        return render(request, 'subscribe.html')

    def post(self, request):
        """
            SubscribeView's post method used to subscribe to newsletter.
        """
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {'message': 'Successfully subscribed to newsletter.'}
            return render(request, 'subscribe.html', message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogView(APIView):
    def get(self, request):
        """
            BlogView's get method used to redirect to add blog page.
        """
        return render(request, 'add_blog.html')

    def post(self, request, format=None):
        """
            BlogView's post method used to add new blog and send e-mail to all subscribers.
        """
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()

            # Send email notification to subscribers
            subscribers = Subscriber.objects.all()
            subject = 'New Blog: {}'.format(blog.title)
            html_message = render_to_string('blog_email.html', {'blog': blog})
            plain_message = 'A new blog has been added. Check it out!'
            from_email = 'greatblogs.mail@gmail.com'
            recipient_list = [subscriber.email for subscriber in subscribers]
            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
            message = {'message': 'Blog added and email send successfully to subscribers.'}

            return render(request, 'add_blog.html', message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    def get(self, request, pk):
        """
            BlogDetailView's get method used to get blog details.
        """
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        return render(request, 'blog_page.html', {'blog': blog})