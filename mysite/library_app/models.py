from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Profile(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    roles = models.CharField(
        max_length=10,
        choices=[
            ("admin", "admin"),
            ('user', 'user')
        ],
        default="user",
    )
    def __str__(self):
        return self.name
    
class Address(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.PROTECT, related_name="address")
    line1 = models.CharField(max_length=40)
    line2 = models.CharField(max_length=40, blank=True, default="")
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.line1}, {self.line2}"
    
class Author(BaseModel):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class BookDetail(BaseModel):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="book_details")
    def __str__(self):
        return self.name
    
CATEGORY_CHOICES = (
    ("Fiction", "Fiction"),
    ("Horror", "Horror"),
    ("Sci-fi", "Sci-fi"),
    ("Thriller", "Thriller"),
    ("Children", "Children"),
    ("Mystery", "Mystery"),
    ("Biography", "Biography"),
)
    
class BookRecord(BaseModel):
    book = models.ForeignKey(BookDetail, on_delete=models.PROTECT, related_name="book_records")
    edition = models.CharField(max_length=12)
    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES,
        default="Fiction",  
    )
    count = models.IntegerField()
    price = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.book.name
    
class IssueRecord(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="issue_records")
    book = models.ForeignKey(BookDetail, on_delete=models.PROTECT, related_name="issue_records")
    status = models.CharField(
        max_length=20,
        choices=[
            ("issued", "issued"),
            ("overDueDate", "overDueDate"),
            ("submittedOnTime", "submittedOnTime"),
            ("submitAfterDueDate", "submitAfterDueDate")
        ],
        default="issued",
    )
    issue_date = models.CharField(max_length=20)
    return_date = models.CharField(blank=True, null=True, max_length=20)
    fine = models.CharField(max_length=20, blank=True, default="")
    def __str__(self):
        return f"{self.book.name} issued by {self.user.name}"

class Category(models.Model):
   name= models.CharField(max_length=100)
   def __str__(self):
       return self.name


