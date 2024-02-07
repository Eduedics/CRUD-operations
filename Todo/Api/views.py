from rest_framework import generics, status
from . serializers import taskSerializer
from rest_framework.response import Response
from Tasks.models import Tasks

class taskListCreate(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = taskSerializer
    ''' here we override delete method based on the all tasks queryset.first we get all tasks 'tasks = self.get_queryset()'
    .call delete method on the result
    '''
    def delete(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        tasks.delete()
        return Response(status=status.HTTP_200_OK)

# retriving single task RetrieveUpdateDestroyAPIView allows you to view, update, or delete a single task.
class taskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = taskSerializer
# overridong queryset for filter using parameters passed in query ie api/tasks/?status=PENDING
class taskListCreate(generics.ListCreateAPIView):
    serializer_class = taskSerializer

    def get_queryset(self):
        # status is ment to show success here
        status = self.request.query_params.get('status', None)
        if status is not None:
            return Tasks.objects.filter(Status=status)
        return Tasks.objects.all()