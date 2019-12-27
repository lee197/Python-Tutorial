from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class UserInfoSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = UserInfo
#         fields = [
#             'url',
#             'id',
#             'user',
#             'title',
#             'content',
#             'timestamp',
#         ]
#         read_only_fields = ['id', 'user']
