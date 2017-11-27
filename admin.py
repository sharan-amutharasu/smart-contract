from django.contrib import admin

# Register your models here.

#add_to_end: 2017-11-22 11:26:20.396483

from .models import mt_users

admin.site.register(mt_users)
#add_to_end: 2017-11-22 11:26:20.396518

#add_to_end: 2017-11-22 11:26:20.398543

from .models import mt_transactions

admin.site.register(mt_transactions)
#add_to_end: 2017-11-22 11:26:20.398572

#add_to_end: 2017-11-22 11:26:20.400633

from .models import mt_products

admin.site.register(mt_products)
#add_to_end: 2017-11-22 11:26:20.400665

#add_to_end: 2017-11-22 11:26:20.402513

from .models import mt_services

admin.site.register(mt_services)
#add_to_end: 2017-11-22 11:26:20.402542

#add_to_end: 2017-11-22 11:26:20.405429

from .models import mt_access

admin.site.register(mt_access)
#add_to_end: 2017-11-22 11:26:20.405489
