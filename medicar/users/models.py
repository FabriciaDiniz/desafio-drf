from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError


def clean_email(value):
    user = User.objects.filter(email=value)
    if user.exists():
        raise ValidationError('Já existe um usuário com esse email.')

    return value


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('O campo username precisa ser preenchido')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_staffuser(self, username, email, password):

        user = self.create_user(
            username = self.normalize_email(username),
            email = self.normalize_email(email),
            password = password,
        )
        user.staff = True
        user.set_password(password)
        user.save()

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.'),
        validators=[username_validator],
        error_messages={
        'unique': _("Já existe um usuário com esse username."),
        },
    )

    email = models.EmailField(
        _('email'),
        unique=True,
        max_length=255,
        error_messages={
        'unique': _("Já existe um usuário com esse email."),
        },
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Determina se o usuário pode logar no site de admin.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
        'Determina se o usuário deve ser tratado como ativo. '
        'Desmarque essa opção invés de deletar usuários.'
        ),
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
        'Determina que esse usuário tem todas as permissões sem precisar declarar explicitamente.'
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True
