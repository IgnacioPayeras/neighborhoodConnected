from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = "__all__"

class AccountRoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account_role
    fields = "__all__"