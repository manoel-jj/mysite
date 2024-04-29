import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='teste')



@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'teste'