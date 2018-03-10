from flask import jsonify, request
from app import post_store, models
from app import app

@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods=["POST"])
def topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["content"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__())

@app.route("/api/topic/delete/<int:id>" ,methods = ["DELETE"])
def delete_topic(id):
    request_data = request.get_json()
    id = request_data["id"]
    post_store.delete(id)
    return jsonify(id)

@app.route("/topic/update/<int:id>" , methods = ["PUT"] )
def update_topic(id):
    request_data = request.get_json()
    post = post_store.get_by_id(id)
    post.title = request_data["title"]
    post.topic = request_data["content"]
    post_store.update(post)
    return jsonify(post_store.__dict__())


