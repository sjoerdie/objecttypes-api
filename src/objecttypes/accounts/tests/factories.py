import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user-{n}")

    class Meta:
        model = "accounts.User"


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True
