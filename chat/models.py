from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255, default=True)

    # Your additional fields go here

    # Update the 'groups' field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Provide a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    # Update the 'user_permissions' field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Provide a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
