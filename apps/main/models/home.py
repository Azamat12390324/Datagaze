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
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name=_('menu'))

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

 class Contact(BaseModel, OrderModel):
     email = models.EmailField(verbose_name=_("email"))
     phone = models.CharField(max_length=255, verbose_name=_("phone"))

     class Meta:
       db_table = 'contact'
       verbose_name = _("Contact")
       verbose_name_plural = _("7 Contacts")
       ordering = ("order",)

     def __str__(self):
      return self.email


