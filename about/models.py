from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    # Single instance model - use get_solo() to retrieve
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    founded_year = models.PositiveIntegerField()
    mission_statement = models.TextField()
    vision_statement = models.TextField(blank=True)
    
    # Company stats
    projects_completed = models.PositiveIntegerField(default=0)
    kilowatts_installed = models.PositiveIntegerField(default=0)
    customers_served = models.PositiveIntegerField(default=0)
    
    # Contact info
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    
    # Social media
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    # SEO fields
    meta_description = models.CharField(max_length=160, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"


class Department(models.Model):
    name = models.CharField(max_length=100)
    display_order = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['display_order']


class TeamMember(models.Model):
    #basic info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='members')
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')

    #contact info
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # Social media
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    # Experience and expertise
    years_experience = models.PositiveSmallIntegerField(default=0)
    certifications = models.CharField(max_length=255, blank=True)
    
    # Display options
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    display_order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
    class Meta:
        ordering = ['display_order', 'last_name']