from rest_framework import serializers
from .models import Todo, Service, Payment, ExpiredPayments

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id","title","body","created_at","done_at","updated_at","deleted_at","status",)
        read_only_fields = ("created_at","done_at","updated_at","deleted_at",)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ExpiredpaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = ("payment_user_id","penalty_fee",)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"