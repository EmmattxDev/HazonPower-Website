from django.contrib import admin
from .models import CompanyInfo, TeamMember, Department

# Register your models here.

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'founded_year', 'mission_statement', 'vision_statement')
        }),
        ('Company Statistics', {
            'fields': ('projects_completed', 'kilowatts_installed', 'customers_served')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')
        }),
        ('SEO', {
            'fields': ('meta_description',)
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'title', 'department', 'bio', 'photo',)
        }),
        ('Contact Information', {
            'fields': ('email', 'phone',)
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')
        }),
        ('Experience', {
            'fields': ('years_experience', 'certifications',)
        }),
        ('Display Option', {
            'fields': ('is_featured', 'display_order', 'is_active',)
        }),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
