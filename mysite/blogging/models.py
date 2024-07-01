from django.db import models

# Create your models here.
class User(models.Model):
   name= models.CharField(max_length=100)
   email=models.EmailField(unique=True)
   phone_number = models.CharField(max_length=12, null=True)  # Phone number field with validation
   created_at = models.DateTimeField(auto_now_add=True)  # Renamed to created_at and added auto_now_add
  
   def __str__(self):
        return self.name
    
CATEGORY_CHOICES = (
    ("Fashion", "Fashion"),
    ("Nature", "Nature"),
    ("News", "News"),
    ("Food blogs", "Food blogs"),
    ("Travel blogs", "Travel blogs"),
    ("Health and fitness blogs", "Health and fitness blogs"),
    ("Tech","Tech")
)

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)  # Changed related_name to lowercase
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES,
        default="Fashion",  # Updated to a valid default choice
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Renamed to created_at and added auto_now_add
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comment by {self.user.name} on {self.post.title}"
    
class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes", related_query_name="like"
    )
    post = models.ForeignKey(
        Post, related_name="likes", related_query_name="like", on_delete=models.CASCADE
    )
    liked = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
    def __str__(self):
        return f"{self.user.name} {'liked' if self.liked else 'disliked'} {self.post.title}"