import pytest
from app import schema

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    #print(res.json())
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("/posts/888")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    #print (res.json())
    post = schema.PostOut(**res.json())
    #print(post)
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title

@pytest.mark.parametrize("title, content, published", [
    ("1st beach", "1st beach content", True),
    ("2nd beach", "2nd beach content", True),
    ("3rd beach", "3rd beach content", True),
    ("4th beach", "4th beach content", True)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts", json={"title": title, "content": content, "published": published})
    create_post = schema.Post(**res.json())

    assert res.status_code == 201
    assert create_post.title == title
    assert create_post.content == content
    assert create_post.published == published
    assert create_post.owner_id == test_user["id"]

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts", json={"title": "Bondi beach", "content": "Bondi beach content!"})
    create_post = schema.Post(**res.json())

    assert res.status_code == 201
    assert create_post.title == "Bondi beach"
    assert create_post.content == "Bondi beach content!"
    assert create_post.published == True
    assert create_post.owner_id == test_user["id"]

def test_unauthorized_user_create_post(client, test_posts):
    res = client.post("/posts/", json={"title": "Bondi beach", "content": "Bondi beach content!"})

    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")

    assert res.status_code == 401

def test_authorized_user_delete_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")

    assert res.status_code == 204

def test_authorized_user_delete_post_not_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/88888")

    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_user,test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
   #print(f"/posts/{test_posts[3].id}")

    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[0].id
    }

    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    update_post = schema.Post(**res.json())
    #print(update_post)
    assert res.status_code == 200
    assert update_post.title == "updated title"
    assert update_post.content == "updated content"
    assert update_post.id == test_posts[0].id

def test_update_other_user_post(authorized_client, test_posts, test_user, test_user1):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": test_posts[3].id
    }
     
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    #print(update_post)
    assert res.status_code == 403

def test_unauthorized_user_update_post(client, test_posts):

    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_authorized_user_update_post(authorized_client, test_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": 88888
    }
    res = authorized_client.put(f"/posts/{data['id']}", json=data)
    
    assert res.status_code == 404