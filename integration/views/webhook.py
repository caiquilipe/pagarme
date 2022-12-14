from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import json


class WebhookView(APIView):
    def post(self, request):
        with open("other_test.json", "w+") as file:
            file.write(json.dumps(request.data))
        return Response(
            data={"message": "Success", "code": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )
