from django.contrib import admin
from .models import Post, Author, Category, Comment, Subscriber
from django.db.models import QuerySet


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'categoryType', 'postAuthor', 'rating']
    list_filter = ['categoryType', 'postAuthor']
    search_fields = ['title', 'categoryType', 'postAuthor']

    @admin.action(description='Обнулить рейтинг')
    def null_rating(self, request, qs: QuerySet):
        qs.update(rating=0)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['authorUser', 'ratingAuthor']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['types']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post_com', 'user_com', 'text_com', 'time_in_com', 'rating_com']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['user', 'category']