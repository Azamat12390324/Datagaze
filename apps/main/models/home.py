from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from apps.common.models import OrderModel, BaseModel, ActiveModel


class Menu(OrderModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))

    class Meta:
        db_table = 'Menu'
        verbose_name = _("Menu")
        verbose_name_plural = _("1 Menus")
        ordering = ("order",)

    def __str__(self):
        return self.name


class SubNavbar(OrderModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name=_("menu"))

    class Meta:
        db_table = 'Sub menu'
        verbose_name = _("Sub menu")
        verbose_name_plural = _("2 Sub menus")
        ordering = ("order",)

    def __str__(self):
        return self.name


class Slider(OrderModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub_title"))
    image = models.ImageField(upload_to='slider/image', verbose_name=_("image"))

    class Meta:
        db_table = 'slider'
        verbose_name = _("Slider")
        verbose_name_plural = _("3 Sliders")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Victory(OrderModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    icon = models.ImageField(upload_to='victory/image/', verbose_name=_("icon"))

    class Meta:
        db_table = 'victory'
        verbose_name = _("Victory")
        verbose_name_plural = _("4 Victories")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Statistic(OrderModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    number = models.IntegerField(verbose_name=_("number"))
    icon = models.ImageField(upload_to="statistic/image/", verbose_name=_("icon"))

    class Meta:
        db_table = 'statistic'
        verbose_name = _("Statistic")
        verbose_name_plural = _("5 Statistics")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Partner(OrderModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    url = models.URLField(max_length=255, verbose_name=_("link"))
    icon = models.ImageField(upload_to="partner/image/", verbose_name=_("icon"))

    class Meta:
        db_table = 'partner'
        verbose_name = _("Partner")
        verbose_name_plural = _("6 Partners")
        ordering = ("order",)

    def __str__(self):
        return self.name


class Contact(OrderModel, BaseModel):
    email = models.EmailField(verbose_name=_("email"))
    phone = models.CharField(max_length=255, verbose_name=_("phone"))

    class Meta:
        db_table = 'contact'
        verbose_name = _("Contact")
        verbose_name_plural = _("7 Contacts")
        ordering = ("order",)

    def __str__(self):
        return self.email


class SocialMedia(OrderModel):
    icon = models.ImageField(upload_to="social_media/image/", verbose_name=_("icon"))
    url = models.URLField(max_length=255, verbose_name=_("link"))

    class Meta:
        db_table = 'SocialMedia'
        verbose_name = _("SocialMedia")
        verbose_name_plural = _("8 SocialMedias")
        ordering = ("order",)

    def __str__(self):
        return self.icon


class About(BaseModel):
    title = models.CharField(verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))

    class Meta:
        db_table = 'About'
        verbose_name = _("About")
        verbose_name_plural = _("9 Abouts")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Certificate(OrderModel, ActiveModel):
    image = models.ImageField(upload_to="certificate/image/", verbose_name=_("image"))

    class Meta:
        db_table = 'certificate'
        verbose_name = _("Certificate")
        verbose_name_plural = _("10 Certificates")
        ordering = ("order",)

    def __str__(self):
        return self.image


