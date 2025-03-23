from rest_framework.response import Response
from rest_framework.decorators import api_view
from config import TWITTER_BEARER_TOKEN, LINKEDIN_ACCESS_TOKEN, LINKEDIN_ORGANIZATION_ID
from rest_framework.decorators import api_view
from config import FACEBOOK_PAGE_ID, FACEBOOK_ACCESS_TOKEN
import requests

#  API Facebook
@api_view(['GET'])
def get_facebook_post(request):
    url = f"https://graph.facebook.com/v18.0/{FACEBOOK_PAGE_ID}/feed?fields=message,attachments&access_token={FACEBOOK_ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        latest_post = data["data"][0]
        post_text = latest_post.get("message", "")
        post_media = None

        if "attachments" in latest_post:
            post_media = latest_post["attachments"]["data"][0].get("media", {}).get("image", {}).get("src", None)

        return Response({"text": post_text, "image": post_media})

    return Response({"message": "لا يوجد منشورات متاحة"}, status=404)


# API Twitter
@api_view(['POST'])
def post_to_twitter_api(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "النص مطلوب"}, status=400)

    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}", "Content-Type": "application/json"}
    payload = {"text": text}

    response = requests.post(url, headers=headers, json=payload)
    return Response({"message": "تم نشر المنشور على Twitter!"}, status=response.status_code)

#  API LinkedIn
@api_view(['POST'])
def post_to_linkedin_api(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "النص مطلوب"}, status=400)

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    payload = {
        "author": f"urn:li:organization:{LINKEDIN_ORGANIZATION_ID}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    response = requests.post(url, headers=headers, json=payload)
    return Response({"message": "تم نشر المنشور على LinkedIn!"}, status=response.status_code)

