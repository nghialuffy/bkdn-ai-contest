from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers import HtmlDocumentSerializer
from api.models import HtmlDocument

class HtmlDocumentApi(generics.GenericAPIView):

    def get(self, request):
        doc1 = HtmlDocument(name='SampleCodeHelp', html_content='This is sample code')
        doc1.save()
        print('savve')
        return Response(doc1)

class SampleCodeHelp(generics.GenericAPIView):
    serializer_class = HtmlDocumentSerializer
    queryset = HtmlDocument.objects.filter(name='SampleCodeHelp')
    def get(self, request, *args, **kwargs):
        obj = self.get_queryset()[0]
        ser = self.get_serializer(obj)
        return Response(ser.data)

    def put(self, request, *args, **kwargs):
        try:
            obj = self.get_queryset()[0]
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        lookup_field = 'pk'
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update sample code successful"})
        else:
            return Response({"message": "failed", "details": serializer.errors})
