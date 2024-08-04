from django.contrib import admin
from .models import Booking, Menu


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date')
    list_filter = ('booking_date',)  # Add a filter for booking dates
    search_fields = ('name',)  # Add search functionality by name
    # Default ordering by booking date, descending
    ordering = ('-booking_date',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    list_filter = ('price',)  # Add a filter for price
    search_fields = ('title',)  # Add search functionality by title
    ordering = ('title',)  # Default ordering by title


admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)
