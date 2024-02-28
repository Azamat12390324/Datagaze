from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from apps.common.models import OrderModel, BaseModel, ActiveModel


class Menu(OrderModel):
    name = models.CharField(max_length=255, verbose_name=_('title'))

    class Meta:
        db_table = 'Menu'
        verbose_name = _("Menu")
        verbose_name_plural = _("1 Menus")
        ordering = ("order",)

  def __str__(self):
      return self.name

# class SubNavbar(OrderModel):
#     name
#
