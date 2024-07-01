from django.contrib import admin
from .models import Profile, Address, Author, BookDetail, BookRecord, IssueRecord
# Register your models here.


admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Author)
admin.site.register(BookDetail)
admin.site.register(BookRecord)
admin.site.register(IssueRecord)

