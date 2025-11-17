# Python Flask forms & post & files
form request handle with post, file upload, return a file from download, post json data with javascript

<br />
<br />
 
**Basic form request handle with post**
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'accepted' and password == "y":
            return 'Success'
        else:
            return 'Failure'
```
```html
    index.html

    <h1>Hello World</h1>
    <form method="POST" action="{{ url_for('index') }}">
        <input type="text" name="username" placeholder="Username"><br>
        <input type="password" name="password" placeholder="Password"><br>
        <input type="submit" value="Login">
    </form>
```

**File upload**
```python
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
```
```html
    index.html

    <h1>File Upload</h1>
    <form method="POST" action="{{ url_for('file_upload') }}" enctype="multipart/form-data">
        <input type="file" name="file" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel, text/plain" required>
        <input type="submit" value="Upload file">
    </form>
```

**Return a file from download**
```diff
+ install and import pandas as pd
+ from flask import Response
```
```python
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return response
```
```html
    index.html

    <h1>Convert CSV File</h1>
    <form method="POST" action="{{ url_for('convert_csv') }}" enctype="multipart/form-data">
        <input type="file" name="file" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" required>
        <input type="submit" value="Upload file">
    </form>
```

**Return a file 2**
```diff
+ import os
+ import uuid
+ from flask import send_from_directory
```
```python
@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid()}.csv'
    df.to_csv(os.path.join('downloads', filename))

    return render_template(template_name_or_list='download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(directory='downloads', filename=filename, download_name='result.csv')
```
```html
    index.html

    <h1>Convert CSV Two</h1>
    <form method="POST" action="{{ url_for('convert_csv_two') }}" enctype="multipart/form-data">
        <input type="file" name="file" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" required>
        <input type="submit" value="Upload file">
    </form>
```
```jinja
    download.html

    {% extends 'base.html' %}
    {% block title %}Index Page{% endblock %}

    {% block content %}
        <h1>Download</h1>
        <a href="{{ url_for('download', filename=filename) }}">Download File</a>
    {% endblock %}
```

**Post JSON data with javascript**
```diff
+ from flask import jsonify
```
```python
@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')
    
    return jsonify({'message': 'Successfully written!'})
```
```html
    index.html
 
    <h1>Javascript JSON Request</h1>
    <button id="post_button">Send POST Request</button>

    <script type="text/javascript">
        const postButton = document.getElementById('post_button');

        const jsonData = {name: 'Mike', greeting: 'Hello'}

        postButton.addEventListener('click', () => {
            fetch('{{ url_for("handle_post") }}', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json; charset=utf-8'
                },
                body: JSON.stringify(jsonData)
            })
            .then(response => response.json())
            .then(data => console.log('Success', data))
            .catch((error) => {
                console.error('Error:', error)
            });
        });
    </script>
```
