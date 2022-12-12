from rest_framework import serializers

from applications.films.models import Films, Review


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = '__all__'
        
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(instance.rate)
        return rep
    