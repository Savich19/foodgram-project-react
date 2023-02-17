from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Tag(models.Model):
    """Класс предустановленных тэгов. Создаются администратором."""

    CHOICES = (
        ('#E26C2D', 'Завтрак'),
        ('#49B64E', 'Обед'),
        ('#8775D2', 'Ужин'),
    )
    name = models.CharField(
        'Название тэга',
        max_length=20,
        unique=True
    )
    color = models.CharField(
        'Цвет',
        max_length=7,
        choices=CHOICES
    )
    slug = models.SlugField(
        'Название пути',
        unique=True
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Класс ингредиентов."""

    name = models.CharField(
        'Название ингредиента',
        max_length=200
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=20
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_ingredient'
            ),
        ]  # after review

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}.'


class Recipe(models.Model):
    """Класс рецептов."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    name = models.CharField(
        'Название рецепта',
        max_length=200
    )
    image = models.ImageField(
        'Изображение рецепта',
        upload_to='recipe/',
    )
    text = models.TextField(
        'Описание рецепта'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
        related_name='recipes'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        validators=[validators.MinValueValidator(
            1,
            message='Минимальное время приготовления: 1 минута',
        )]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.author.email}, {self.name}'


class RecipeIngredient(models.Model):
    """Класс, описывающий связь рецептов и ингредиентов."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient',
        verbose_name='Ингредиент'
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=(
            validators.MinValueValidator(
                1, message='Мин. количество ингридиентов 1'),),
        verbose_name='Количество',)

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique ingredient'
            )
        ]


class Subscribe(models.Model):
    """Класс, описывающий связь подписчиков и авторов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )
    created = models.DateTimeField(
        'Дата подписки',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscription'
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='author_not_user'
            ),
        ]

    def __str__(self):
        return f'Пользователь {self.user} подписался на автора {self.author}'


class FavoriteRecipe(models.Model):
    """Класс избранных рецептов"""

    user = models.OneToOneField(  # hz
        User,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
        verbose_name='Пользователь'
    )
    recipe = models.ManyToManyField(
        Recipe,
        related_name='favorite_recipe',
        verbose_name='Избранный рецепт'
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'

    def __str__(self):
        list_ = [item['name'] for item in self.recipe.values('name')]
        return f'Пользователь {self.user} добавил {list_} в избранные.'


class ShoppingCart(models.Model):
    """Класс списка покупок"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь')
    recipe = models.ManyToManyField(
        Recipe,
        related_name='shopping_cart',
        verbose_name='Покупка')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        list_ = [item['name'] for item in self.recipe.values('name')]
        return f'Пользователь {self.user} добавил {list_} в покупки.'
