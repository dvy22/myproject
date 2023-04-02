from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length= 50)
    slug = models.SlugField(max_length=50, unique= True)
    
    class Meta:
        verbose_name_plural = 'categories'
        def __str__(self):
            return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default='admin')
    description = models.TextField() 
    image = models.ImageField(upload_to='image/',blank=True,null=True)
    thumbnail = models.ImageField(upload_to='image/',blank=True,null=True)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    in_stock = models.BooleanField(default = True)
    in_active = models.BooleanField(default = True)

    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ['-created_at',]
        def __str__(self):
            return self.title

    def create_thumbnail(self):
        # Ouvrez l'image avec PIL
        image = Image.open(self.image.path)

        # Définir la taille maximale pour la miniature
        size = (300, 300)

        # Créer la miniature avec la méthode thumbnail() de PIL
        image.thumbnail(size)

        # Enregistrer la miniature
        thumb_path = f'{self.image.path}_thumb'
        image.save(thumb_path)

        # Retourner le chemin de la miniature
        return thumb_path

 
