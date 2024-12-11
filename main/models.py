from django.db import models

class Reja(models.Model):
    sarlavha = models.CharField(max_length=255, verbose_name="Sarlavha")
    izoh = models.TextField(blank=True, null=True, verbose_name="Izoh")
    bajarildi = models.BooleanField(default=False, verbose_name="Bajarildi")
    sana = models.DateField(auto_now_add=True, verbose_name="Sana")

    class Meta:
        verbose_name = "Reja"
        verbose_name_plural = "Rejalar"

    def __str__(self):
        return self.sarlavha
