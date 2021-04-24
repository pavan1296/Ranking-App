from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Player, PlayerStats

# Create your views here.


def convert_objs_to_dict(list_of_player_objects):
    list_of_player_details = []
    rank = 0
    for player_details in list_of_player_objects:
        rank += 1
        list_of_player_details.append(
            {
                'player_name': player_details.player.player_name,
                'country_name': player_details.player.player_country,
                'rating': player_details.rating,
                'position': rank
            }
        )
    return list_of_player_details


class MensBattingStats(APIView):
    def get(self, request, match_type):

        # caching_with_list_to_reduce_the_db_hits
        list_of_player_objects = list(
            PlayerStats.objects.filter(
                match_type__contains=match_type,
                player_field_type='BATTING',
                player__gender='M'
            ).select_related('player').order_by('-rating', 'player__player_name')
        )

        client_response = convert_objs_to_dict(list_of_player_objects)
        return JsonResponse({'player': client_response}, status=200)


class MensBowlingStats(APIView):
    def get(self, request, match_type):

        # caching_with_list_to_reduce_the_db_hits
        list_of_player_objects = list(
            PlayerStats.objects.filter(
                match_type__contains=match_type,
                player_field_type='BOWLING',
                player__gender='M'
            ).select_related('player').order_by('-rating', 'player__player_name')
        )
        client_response = convert_objs_to_dict(list_of_player_objects)
        return JsonResponse({'player': client_response}, status=200)


class MensAllRounderStats(APIView):
    def get(self, request, match_type):

        # caching_with_list_to_reduce_the_db_hits
        list_of_player_objects = list(
            PlayerStats.objects.filter(
                match_type__contains=match_type,
                player_field_type='ALL',
                player__gender='M'
            ).select_related('player').order_by('-rating', 'player__player_name')
        )
        client_response = convert_objs_to_dict(list_of_player_objects)
        return JsonResponse({'player': client_response}, status=200)


class WomensBattingStats(APIView):
    def get(self, request, match_type):

        # caching_with_list_to_reduce_the_db_hits
        list_of_player_objects = list(
            PlayerStats.objects.filter(
                match_type__contains=match_type,
                player_field_type='BATTING',
                player__gender='F'
            ).select_related('player').order_by('-rating', 'player__player_name')
        )

        client_response = convert_objs_to_dict(list_of_player_objects)
        return JsonResponse({'player': client_response}, status=200)

class WomenBowlingStats(APIView):
    def get(self, request, match_type):

        # caching_with_list_to_reduce_the_db_hits
        list_of_player_objects = list(
            PlayerStats.objects.filter(
                match_type__contains=match_type,
                player_field_type='BOWLING',
                player__gender='F'
            ).select_related('player').order_by('-rating', 'player__player_name')
        )

        client_response = convert_objs_to_dict(list_of_player_objects)
        return JsonResponse({'player': client_response}, status=200)


class WomenAllRounderStats(APIView):
    def get(self, request, match_type):

        # caching_with_list_to_reduce_the_db_hits
        list_of_player_objects = list(
            PlayerStats.objects.filter(
                match_type__contains=match_type,
                player_field_type='ALL',
                player__gender='F'
            ).select_related('player').order_by('-rating', 'player__player_name')
        )
        client_response = convert_objs_to_dict(list_of_player_objects)
        return JsonResponse({'player': client_response}, status=200)
