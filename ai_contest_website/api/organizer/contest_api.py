from api.models import Contest, User
from .serializers.contest_serializers import OrganizerContestSerializer, OrganizerContestInfoSerializer
from .serializers.user_serializers import OrganizerContestantsInContestSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class OrganizerContestList(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = OrganizerContestSerializer

    def list(self, request):
        queryset = self.get_queryset().filter(created_user=request.user.id).defer('created_user')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer()(queryset, many=True)
        return Response(serializer.data)

    # Create a new contest
    def create(self, request, *args, **kwargs):
        # Get created user by auth token in header
        user = User.objects.filter(pk=request.user.id).first()
        # Copy QuerySet to temp data 'QuerySet is immun..'.
        # We can modified field in QuerySet to pass isValid() by using objectID
        # isValid() require created user is a object ID
        temp_request = request.data.copy()
        temp_request['created_user'] = user._id

        serializer = self.get_serializer()(data=temp_request)
        if serializer.is_valid():
            # created user require a User instance not ObjectID
            serializer.validated_data['created_user'] = user
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

# Get contest info
class OrganizerContestInfo(APIView):
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :return:
        """
        contest_id = kwargs.get('contest_id')
        contest = Contest.objects.get(_id=contest_id, created_user=request.user.id)
        serializer = OrganizerContestInfoSerializer(contest)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    # Update a contest
    def put(self, request, *args, **kwargs):
        try:
            # Update contest with the given id
            contest_id = kwargs.get('contest_id')
            contest = Contest.objects.get(_id=contest_id)
            if contest.created_user != request.user:
                return Response({'message': 'You are not the creator of this contest'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            # clone the contest and append the updated data
            updated_contest = contest.__dict__
            for key, value in request.data.items():
                updated_contest[key] = value
            serializer = OrganizerContestSerializer(contest, data=updated_contest)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Contest not found'}, status=status.HTTP_404_NOT_FOUND)


    # Delete a contest
    def delete(self, request, *args, **kwargs):
        try:
        # Delete a contest with the given id
            contest_id = kwargs.get('contest_id')
            contest = Contest.objects.get(_id=contest_id)
        
            if str(contest.created_user._id) != request.user.id:
                return Response({'message': 'You are not the creator of this contest'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            contest.delete()
            return Response({'message': 'Delete successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Contest not found'}, status=status.HTTP_404_NOT_FOUND)

class OrganizerListContestants(generics.ListAPIView):
    serializer_class = OrganizerContestantsInContestSerializer

    # Get the contestants of the contest
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :return:
        """
        contest_id = kwargs.get('contest_id')
        
        contest = Contest.objects.get(_id=contest_id, created_user=request.user.id)
        queryset = contest.attended_contestants.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer()(contest.attended_contestants, many=True)
        return Response(serializer.data)

