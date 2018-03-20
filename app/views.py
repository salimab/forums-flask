from flask import render_template, request, redirect, url_for, abort
from app import models
from app import app, post_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(title=request.form["title"], content=request.form["content"])
        #new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
         return render_template("topic_add.html")

@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404)
    return redirect(url_for("home"))

@app.route("/topic/show/<int:id>")
def topic_show(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404, "Couldn't find this topic id !")
    return render_template("show_posts.html" ,post = post )

@app.route("/topic/update/<int:id>" , methods = ["GET", "POST"] )
def topic_update(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)

    if request.method == "POST":
        post.title = request.form["title"]
        post.topic = request.form["content"]
        post_store.update(post)
        return redirect(url_for("home"))
    else:
        return render_template("update_post.html", post=post)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', message = error.description)



