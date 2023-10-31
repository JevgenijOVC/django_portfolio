from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio

# HOME
admin.site.register(Home)


# ABOUT
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine,
    ]


# SKILLS
class SkillsInLine(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInLine,
    ]


# PORTFOLIO
admin.site.register(Portfolio)
