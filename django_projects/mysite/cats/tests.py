from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from cats.models import Breed, Cat

class CatsTest(TestCase):
    def setUp(self):
        # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        
        # Create some test data
        self.breed = Breed.objects.create(name='Test Breed')
        self.cat = Cat.objects.create(
            nickname='Test Cat',
            breed=self.breed,
            weight=10.0
        )

    def test_breed_list_has_add_link(self):
        """Test that breed list page has 'Add a breed' link"""
        print("=== DEBUG: test_breed_list_has_add_link ===")
        
        # Check user authentication
        print(f"User authenticated: {self.client.session.get('_auth_user_id')}")
        
        # Get the breed list page
        url = reverse('cats:breed_list')
        print(f"Testing URL: {url}")
        
        response = self.client.get(url)
        
        print(f"Status code: {response.status_code}")
        
        # Check if redirected
        if response.status_code == 302:
            print(f"REDIRECTED to: {response.url}")
            response = self.client.get(response.url, follow=True)
            print(f"After redirect - Status code: {response.status_code}")
        
        # Check templates used
        if hasattr(response, 'templates') and response.templates:
            print("Templates used:")
            for template in response.templates:
                print(f"  - {template.name}")
        else:
            print("No template information available")
        
        # Check content
        content = response.content.decode()
        print(f"Content length: {len(content)}")
        print(f"Contains 'Add a breed': {'Add a breed' in content}")
        
        # Check for specific elements
        print(f"Contains 'breed_list' context: {'breed_list' in str(response.context) if response.context else 'No context'}")
        
        # Print first 1000 chars of content for inspection
        print("=== CONTENT (first 1000 chars) ===")
        print(content[:1000])
        print("==================================")
        
        # The actual assertion
        self.assertContains(response, "Add a breed")

    def test_breed_list_status_code(self):
        """Test that breed list page loads successfully"""
        response = self.client.get(reverse('cats:breed_list'))
        self.assertEqual(response.status_code, 200)

    def test_breed_list_uses_correct_template(self):
        """Test that breed list uses correct template"""
        response = self.client.get(reverse('cats:breed_list'))
        self.assertTemplateUsed(response, 'cats/breed_list.html')

    def test_breed_list_context(self):
        """Test that breed list has breed_list in context"""
        response = self.client.get(reverse('cats:breed_list'))
        self.assertIn('breed_list', response.context)
        self.assertEqual(len(response.context['breed_list']), 1)  # Should have our test breed

    def test_breed_create_link_works(self):
        """Test that the 'Add a breed' link goes to the correct URL"""
        response = self.client.get(reverse('cats:breed_list'))
        self.assertContains(response, 'href="{}"'.format(reverse('cats:breed_create')))

    def test_cat_list_has_add_link(self):
        """Test that cat list page has 'Add a cat' link"""
        response = self.client.get(reverse('cats:cat_list'))
        self.assertContains(response, "Add a cat")

    # Additional tests to ensure basic functionality
    def test_breed_create_view(self):
        """Test that breed create view works"""
        response = self.client.get(reverse('cats:breed_create'))
        self.assertEqual(response.status_code, 200)

    def test_breed_creation(self):
        """Test creating a new breed"""
        response = self.client.post(reverse('cats:breed_create'), {
            'name': 'New Test Breed'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertTrue(Breed.objects.filter(name='New Test Breed').exists())

    def tearDown(self):
        # Clean up
        Breed.objects.all().delete()
        Cat.objects.all().delete()