from django_tenants.clone import CloneSchema
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from Educhum import settings
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
    def __str__(self):
        return self.name
class Domain(DomainMixin):
    domain = models.CharField(max_length=253, unique=True, db_index=True)
    tenant = models.ForeignKey(settings.TENANT_MODEL, db_index=True, related_name='domains',
                               on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=True, db_index=True)

    visit_num = models.PositiveIntegerField(default=0)

    
    def __str__(self):
    	return self.domain

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)