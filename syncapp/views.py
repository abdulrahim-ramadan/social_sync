from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from .models import Post

@api_view(['GET'])
def get_facebook_post(request):
    latest_post = Post.objects.last()
    if latest_post:
        data = {
            "text": latest_post.message,
            "image": latest_post.image_url,
        }
        return Response(data)
    return Response({"message": "لا يوجد منشورات متاحة"}, status=404)