from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment, Follower, UserProfile
import datetime

User = get_user_model()

# Create your tests here.

class PostTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.other_user = User.objects.create_user(username='testuser2', password='12345')
		self.user.save()
		self.other_user.save()
		login = self.client.login(username='testuser', password='12345')
		self.posts_to_delete = []
		self.new_post = Post.objects.create(author=self.user,
		title="Test Title", description="This is a test Post", published=datetime.datetime.now(), content="TEST POST 1",
		images=None, originalPost=None, sharedBy=None)
		self.new_post.save()

	def tearDown(self):
		User.objects.filter(username = self.user).delete()
		self.new_post.delete()
		for post in self.posts_to_delete:
				Post.objects.filter(id=post).delete()

	def test_addingPosts(self):
		# Adding post and checking if post is added
		existing_ID_query = Post.objects.filter(title="Test Title").values_list('id', flat=True)
		
		totalID = len(existing_ID_query)
		response = self.client.post("/post/",data={"author":self.user.id, "contentType":"text/markdown",
		"title":"Test Title", "description":"This is a test Post",
		"visibility":"PUBLIC", "published":datetime.datetime.now(), "content":"TEST POST 2"})
		id_to_delete = ""

		addedPost = Post.objects.filter(title="Test Title").values_list('id', flat=True)
		self.assertEqual(len(addedPost), totalID + 1)
		for id_val in list(addedPost):
				if id_val not in list(existing_ID_query):
						id_to_delete = id_val
						self.posts_to_delete.append(id_to_delete)

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, "/author/"+ str(self.user.username) + "/posts/" + str(id_to_delete))

	def test_editingPosts(self):
		# Editing post and checking if post is edited
		response = self.client.post("/author/"+ str(self.user.id) + "/posts/" + str(self.new_post.id) + "/edit",data={'author': ['1'], "contentType":["text/markdown"],
		"title":["Test Title"], "description":["This is a test Post"],
		"visibility":["PUBLIC"], "content":["TEST POST(EDITED)"],
		"images":[""], "originalPost":[""], "sharedBy":[""]})

		editedPost = Post.objects.filter(id=self.new_post.id)
		self.assertEqual(editedPost[0].content, "TEST POST(EDITED)")

	def test_deletingPosts(self):
		# Deleting post and checking if post is deleted
		oldPost = Post.objects.filter(id=self.new_post.id)
		self.assertEqual(len(oldPost), 1)
		response = self.client.post("/author/"+ str(self.user.id) + "/posts/" + str(self.new_post.id) + "/delete")

		oldPost = Post.objects.filter(id=self.new_post.id)
		self.assertEqual(len(oldPost), 0)

	def test_sharingPosts(self):
		# Sharing post and checking if post is shared
		totalShare = Post.objects.filter(originalPost=self.new_post)
		totalShares = len(totalShare)
		response = self.client.get("/author/"+ str(self.user.id) + "/posts/" + str(self.new_post.id) + "/share")

		totalShare = Post.objects.filter(originalPost=self.new_post)
		self.assertEqual(len(totalShare), totalShares + 1)

	def test_restrictions(self):
		other_post = Post.objects.create(author=self.other_user,
		title="Test Title", description="This is a test Post", published=datetime.datetime.now(), content="TEST POST 1",
		images=None, originalPost=None, sharedBy=None)
		other_post.save()

		response = self.client.get("/"+self.other_user.username + "/posts/" + str(other_post.id))

		# Checking For unauthorized access
		# response_str = str(response.rendered_content)
		response_str = str(response.content)
		self.assertEqual("Edit" in response_str, False)
		self.assertEqual("Delete" in response_str, False)

		login = self.client.login(username='testuser2', password='12345')
		response = self.client.get("/author/"+ str(self.other_user.id) + "/posts/" + str(other_post.id))

		# Checking for authorized access
		response_str = str(response.content)
		self.assertEqual("Edit" in response_str, True)
		self.assertEqual("Delete" in response_str, True)

# User tests
class UserTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="user1", email="u@u.com")
		self.user.set_password('password1')
		self.user.save()

	# Make test when user creation is added
	# def create_user(self):
	#   data = {'username': "user1", 'email': "u@u.com", 'password': "password1"}

	def test_login(self):
		resp = self.client.post(reverse('login'), {'username': "user1", 'password': "password1"}, follow=True)
		self.assertTrue(resp.context['user'].is_active)

class HTMLTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.user.save()

	def test_index(self):
		resp = self.client.get(reverse("index"))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, '<div class="mb-6">')

	def test_login_index(self):
		resp = self.client.get(reverse("index"))
		self.assertContains(resp, '<div class="mb-6">')

		self.client.force_login(self.user)
		resp = self.client.get(reverse("index"))
		self.assertContains(resp, '<p class="non-white-title">Home</p>')

	def test_logout_index(self):
		self.client.force_login(self.user)
		resp = self.client.get(reverse("index"))
		self.assertContains(resp, '<div class="mb-6">')

		resp = self.client.get(reverse("logout"))
		self.assertEqual(resp.status_code, 302)
		resp = self.client.get(reverse("index"))
		self.assertContains(resp, '<div class="mb-6">')

	def test_mystream(self):
		self.client.force_login(self.user)
		resp = self.client.get(reverse("mystream", args=[self.user.id]))
		self.assertContains(resp, '<p class="non-white-title">My Stream</p>')

	def test_profile(self):
		self.client.force_login(self.user)
		resp = self.client.get(reverse("profile", args=[self.user.id]))
		self.assertContains(resp, '<p class="label-field has-text-weight-bold">Username: </p>')

	def test_manage_friends(self):
		self.client.force_login(self.user)
		resp = self.client.get(reverse("friends", args=['user']))
		self.assertContains(resp, '<p class="non-white-title">Manage Friends</p>')

	def test_inbox(self):
		self.client.force_login(self.user)
		resp = self.client.get(reverse("inbox", args=['user']))
		self.assertContains(resp, '<p class="non-white-title mb-1">Inbox</p>')

class FollowerTests(TestCase):
   def setUp(self):
        self.user1 = User.objects.create_user(username='testuser', password='12345')
        self.user1.save()
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.user2.save()
        login = self.client.login(username='testuser', password='12345')
        
   def test_friendships(self):
   	friendship = Follower.objects.create(author='testuser',follower='testuser2')
   	friendship.save()
   	self.assertEqual(len(Follower.objects.filter(author = self.user1.username).values_list('id', flat=True)),1)
   	friendship = Follower.objects.filter(author = self.user1.username)[0]
   	self.assertEqual(friendship.follower, "testuser2")
   	
class CommentTests(TestCase):
   def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()
        login = self.client.login(username='testuser', password='12345')
        self.new_post = Post.objects.create(author=self.user,
		title="Test Title", description="This is a test Post", published=datetime.datetime.now(), content="TEST POST 1",
		images=None, originalPost=None, sharedBy=None)
        self.new_post.save()
        
   def test_comments(self):
   	comment = Comment.objects.create(author=self.user,post=self.new_post,comment='test comment' )
   	comment.save()
   	self.assertEqual(len(Comment.objects.filter(author=self.user).values_list('id', flat=True)),1)
   	
class UserProfileTests(TestCase):
   def setUp(self):
        self.user = User.objects.create_user(id=12345678,username='testuser', password='12345')
        self.user.save()
        login = self.client.login(username='testuser', password='12345')
        
   def test_user_profile(self):
   	user_profile = UserProfile.objects.filter(user_id = self.user.id)[0]
   	user_profile.date_of_birth=datetime.date(2000,1,1) 
   	user_profile.save()
   	self.assertEqual(UserProfile.objects.filter(user_id=self.user.id).values_list('date_of_birth', flat=True)[0],datetime.date(2000,1,1))
