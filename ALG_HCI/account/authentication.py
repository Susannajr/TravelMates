from django.contrib.auth.models import User


class PhoneAuthBackend:
    """authenfication the mails """

    def authentification(self, request, Phone=None, password=None):
        try:
            user = User.objects.get(Phone=username)
            if user.check_password(password):
                return user
            return None
        except(User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        
    def get_user(self, user_id):
        try: 
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None