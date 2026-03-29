from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import Playerform
from .models import Player
from .serializer import PlayerSerializer


def player_list_view(request):
    players = Player.objects.all()
    return render(request, 'players_list.html', {'players': players})

def add_player_view(request):
    if request.method == 'POST':
        form = Playerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players_list')
    else:
        form = Playerform()
    return render(request, 'add_player.html', {'form': form})

#def view_player_view(request, id):
 #   player = get_object_or_404(Player, id=id)
  #  return render(request, 'view_player.html', {'player': player})

def delete_player_view(request, id):
    player = get_object_or_404(Player, id=id)
    if request.method == 'POST':
        player.delete()
        return redirect('players_list')
    return render(request, 'confirm_delete.html', {'player': player})

# views.py

def update_player_view(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == 'POST':
        form = Playerform(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players_list')  # Replace with your player list view name
    else:
        form = Playerform(instance=player)

    return render(request, 'update_player.html', {'form': form, 'player': player})




def player_rankings_odi_view(request):
    players = Player.objects.order_by('-totalruns_odi_matches')
    return render(request, 'odiranking.html', {'players': players})

def player_rankings_test_view(request):
    players = Player.objects.order_by('-totalruns_test_matches')
    return render(request, 'testrankings.html', {'players': players})

def player_rankings_t20_view(request):
    players = Player.objects.order_by('-totalruns_t20_matches')
    return render(request, 't20rankings.html', {'players': players})

#class PlayerView(APIView):
 #   def get(self, request):
  #      players = Player.objects.all() 
   #     serializer = PlayerSerializer(players, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK)

    #def post(self, request):
     #   serializer = PlayerSerializer(data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #def delete(self,request, id):
     #   player = get_object_or_404(Player, id=id)
      #  player.delete()
       # #return redirect('player_list')  # Redirect to the list view or any success page
        #return Response(status=status.HTTP_201_CREATED)


#class PlayerListSortedView_test(APIView):
 #   def get(self, request):
  #      try:
   #         players = Player.objects.all().order_by('-totalruns_test_matches')
    #        serializer = PlayerSerializer(players, many=True)
     #       return Response(serializer.data, status=status.HTTP_200_OK)
      #  except Exception as e:
       #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#class PlayerListSortedView_odi(APIView):
 #   def get(self, request):
  #      try:
   #         players = Player.objects.all().order_by('-totalruns_odi_matches')
    #        serializer = PlayerSerializer(players, many=True)
     #       return Response(serializer.data, status=status.HTTP_200_OK)
      #  except Exception as e:
       #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

#class PlayerListSortedView_t20(APIView):
 #   def get(self, request):
  #      try:
   #         players = Player.objects.all().order_by('-totalruns_t20_matches')
    #        serializer = PlayerSerializer(players, many=True)
     #       return Response(serializer.data, status=status.HTTP_200_OK)
      #  except Exception as e:
       #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    


