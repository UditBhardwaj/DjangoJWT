from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import routers, serializers, viewsets,status
from .serializers import formserializer
from .models import Client
from django.http import JsonResponse
import json
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
# @csrf_exempt
@permission_classes([IsAuthenticated])
def get_shifts(request):
    user = request.user
    email = user.email
    shifts = Client.objects.all()
    serializer = formserializer(shifts, many=True)
    return JsonResponse({'shifts': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_shift(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        shift = Client.objects.create(
            date=payload["date"],
            email = user.email,
            repeat_type=payload["repeat_type"],
            shift=payload["shift"],
            start_time=payload["start_time"],
            end_time=payload["end_time"],
            my_field=payload["my_field"],
            weekdays_only=payload["weekdays_only"]
        )

        serializer = formserializer(shift)
        return JsonResponse({'shifts': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_shift(request, shift_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        shift_item = Client.objects.filter(id=shift_id)
        # returns 1 or 0
        shift_item.update(**payload)
        shift = Client.objects.get(id=shift_id)
        serializer = formserializer(shift)
        return JsonResponse({'shift': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
# @csrf_exempt
@permission_classes([IsAuthenticated])
def delete_shift(request, shift_id):
    # user = request.user.id
    try:
        shift = Client.objects.get(id=shift_id)
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)