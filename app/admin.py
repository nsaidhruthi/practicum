from django.contrib import admin
from django.contrib.auth.models import Group
from .models import entertainment,pubs,outstation,Villas,Farmhouses,Feedback,CupCakes,Add_to_cart,Products,ReturnGift,Hydhalls, Hydbdaygifts, Hydbdaydecoration,Hydbdaycakes,Hydmrghalls,Hydmrggifts,Hydmrgmandapdecoration,Hydmrgfood,Hydmrgbachelorparty,Hydmrgsangeethdecoration
# Register your models here.

#bday event items
class CupCakesAdmin(admin.ModelAdmin):
    list_display=('id','name','area','avilable','flavour','price','noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable','price','noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'flavour')
    list_filter = ('name', 'area')

class ReturngiftAdmin(admin.ModelAdmin):
    list_display=('id','name','area','avilable','Type','price','noofitems')
    list_display_links = ( 'name','area')
    list_editable = ('avilable','price','noofitems')
    list_per_page = 10
    search_fields = ('name', 'area'  ,'avilable', 'Type')
    list_filter = ('name',)

class HydHallsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'hallname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'hallname')
    list_filter = ('name', 'area')


class HydbdaygiftsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'giftname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'giftname')
    list_filter = ('name', 'area')


class HydbdaydecorationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'decorationname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'decorationname')
    list_filter = ('name', 'area')

class HydbdaycakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'decorationname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'decorationname')
    list_filter = ('name', 'area')

# marriage event
class HydmrghallsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'hallname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'hallname')
    list_filter = ('name', 'area')
class HydmrggiftsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'giftname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'giftname')
    list_filter = ('name', 'area')
class HydmrgmandapdecorationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'decorationname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'decorationname')
    list_filter = ('name', 'area')
class HydmrgfoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'foodname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'foodname')
    list_filter = ('name', 'area')
class HydmrgbachelorpartyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'partyname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'partyname')
    list_filter = ('name', 'area')
class HydmrgsangeethdecorationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'decorationname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'decorationname')
    list_filter = ('name', 'area')       
class entertainmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'entertainmentname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'entertainmentname')
    list_filter = ('name', 'area')       

class outstationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'stationname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'stationname')
    list_filter = ('name', 'area')       
class pubsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'pubname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'pubname')
    list_filter = ('name', 'area')       
class VillasAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'villasname', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'villasname')
    list_filter = ('name', 'area')       
class FarmhousesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'avilable',
                    'farmhousename', 'price', 'noofitems')
    list_display_links = ('area', 'name')
    list_editable = ('avilable', 'price', 'noofitems')
    list_per_page = 10
    search_fields = ('name', 'area',  'avilable', 'farmhousename')
    list_filter = ('name', 'area')       
                                           
#ADD to cart    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','noofitems')
class cartAdmin(admin.ModelAdmin):
    list_display=('manager',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'customer_name', 'happy','details')
    list_filter = ('customer_name', )
    search_fields = ('customer_name', 'details',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Add_to_cart,cartAdmin)
admin.site.register(Feedback,FeedbackAdmin)

#event items
admin.site.register(CupCakes, CupCakesAdmin)
admin.site.register(ReturnGift, ReturngiftAdmin)
admin.site.register(Hydhalls, HydHallsAdmin)
admin.site.register(Hydbdaygifts, HydbdaygiftsAdmin)
admin.site.register(Hydbdaydecoration, HydbdaydecorationAdmin )
admin.site.register(Hydbdaycakes, HydbdaycakeAdmin )
admin.site.register(Farmhouses, FarmhousesAdmin )
admin.site.register(outstation,outstationAdmin )
admin.site.register(pubs,pubsAdmin )
admin.site.register(Villas, VillasAdmin)
admin.site.register(entertainment, entertainmentAdmin )
#marriage items
admin.site.register(Hydmrghalls, HydmrghallsAdmin)
admin.site.register(Hydmrggifts, HydmrggiftsAdmin)
admin.site.register(Hydmrgmandapdecoration, HydmrgmandapdecorationAdmin)
admin.site.register(Hydmrgfood, HydmrgfoodAdmin)
admin.site.register(Hydmrgbachelorparty, HydmrgbachelorpartyAdmin )
admin.site.register(Hydmrgsangeethdecoration, HydmrgsangeethdecorationAdmin )


admin.site.unregister(Group)
 

