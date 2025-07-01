from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append({"name": task, "done": False})
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

