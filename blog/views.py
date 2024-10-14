from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Pollito Pollito',
        'date': date(2024, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': 'There\'s nothing like the views you get when hiking in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
        'content': """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aspernatur est necessitatibus aut ullam unde reiciendis, voluptatem magnam, excepturi maiores, voluptatibus quia. Tenetur eligendi minima corrupti veritatis optio explicabo laborum aut itaque veniam perferendis officiis beatae dolorum repellendus repudiandae eveniet, facilis est dolor perspiciatis sapiente consectetur provident! Saepe cumque iste ab?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aspernatur est necessitatibus aut ullam unde reiciendis, voluptatem magnam, excepturi maiores, voluptatibus quia. Tenetur eligendi minima corrupti veritatis optio explicabo laborum aut itaque veniam perferendis officiis beatae dolorum repellendus repudiandae eveniet, facilis est dolor perspiciatis sapiente consectetur provident! Saepe cumque iste ab?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aspernatur est necessitatibus aut ullam unde reiciendis, voluptatem magnam, excepturi maiores, voluptatibus quia. Tenetur eligendi minima corrupti veritatis optio explicabo laborum aut itaque veniam perferendis officiis beatae dolorum repellendus repudiandae eveniet, facilis est dolor perspiciatis sapiente consectetur provident! Saepe cumque iste ab?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Pollito Pollito",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Pollito Pollito",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post.get('date')

# Create your views here.


def starting_page(req):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(req, 'blog/index.html', context={
        'posts': latest_posts
    })


def posts(req):
    return render(req, 'blog/all-posts.html', context={
        'all_posts': all_posts
    })


def post_detail(req, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(req, 'blog/post-detail.html', context={
        'post': identified_post
    })
