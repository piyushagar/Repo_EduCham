from teacher.models import Client, Domain

# create your public tenant
tenant = Client(schema_name='public',
                name='Schemas Inc.')
tenant.save()

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'mainsite.com' # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()

###############################################

# create lancashire tenant
tenant = Client(schema_name='lancashire',
                name='Lancashire County')
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'lancashire.mainsite.com' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()

##############################################

# create real tenant
tenant = Client(schema_name='Cumbria',
                name='Cumbria County')
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'cumbria.mainsite.com' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()

##############################################

# create real tenant
tenant = Client(schema_name='london',
                name='Greater London')
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'london.mainsite.com' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()