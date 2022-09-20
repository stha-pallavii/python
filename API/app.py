#SET 5
# Data: https://jsonplaceholder.typicode.com/posts

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#Q1 Create an API to list title and body of posts  in uppercase  based on the userid provided.

@app.route('/posts/<int:userId>', methods = ['GET', 'POST'])
def get_post(userId):
    try:
        with open('posts.json', 'r') as file:
            data = json.load(file)
        userdata = []
        for post in data:
            if post['userId'] == userId:
                userdata.append({"userId": post["userId"], "title":post['title'].upper(), "body":post["body"].upper()})
        if not userdata:
            return jsonify({
                'status': 404,
                'userId': userId,
                'message': 'No record found',
            })
        return jsonify({"posts": userdata})

        
    except Exception as e:
        return jsonify({'message':e})




#Q2 Create an API to return no of posts of provided userid.
@app.route('/posts/count/<int:userId>', methods=['GET', 'POST'])
def count_post(userId):
    try:
        with open('posts.json', 'r') as file:
            data = json.load(file)
        count = 0
        for post in data:
            if post['userId'] == userId:
                count = count+1
                print(count)
        if count==0:
            return jsonify({
                'status': 404,
                'userId': userId,
                'message': 'No record found with userId={}'.format(userId),
            })
        return jsonify({"number of posts of userId={}".format(userId): count})


    except Exception as e:
        return jsonify({'message': e})




#3 Create an API to insert a new record.
@app.route('/insert/', methods=['POST'])
# json schema expected
def insert_record():
    body = request.get_json()
    try:
        with open('posts.json', mode='r') as file:
            posts = json.load(file)
            for record in posts:
                if record['id'] == body['id']:
                    raise Exception
            posts.append(body)

        with open('posts.json', mode='w') as w_file:
            w_file.write(json.dumps(posts, indent=4))
        return jsonify({
            'status': 200,
            'message': 'Insertion successful',
            'data': body,
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': 'Record not inserted! Id already exists.',
            'data': {},
        })


#4 Create an API  to delete the record by id (post id ) given by the user and return the success message of the id provided.
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
    try:
        file = open('posts.json', mode='r')
        posts = json.load(file)
        new_post = []
        post_record = dict()
        id_found = False
        for record in posts:
            if record['id'] == id:
                id_found = True
                post_record = record
                continue
            new_post.append(record)

        file.close()
        if not id_found:
            raise Exception
        else:
            with open('posts.json', mode='w') as file:
                file.write(json.dumps(new_post, indent=4))

            return jsonify({
                'status': 200,
                'message': 'Record (id={}) has been successfully deleted'.format(id),
                'data': post_record,
            })

    except Exception:
        return jsonify({
            'error': 404,
            'message': 'The record doesn\'t exist',
        })



#5 Create an API that updates title in uppercase of provided id(post id)

@app.route('/title/<int:id>', methods=['PUT'])
def update_title(id):
    try:
        file = open('posts.json', mode='r')
        posts = json.load(file)
        post_record = dict()
        for record in posts:
            if record['id'] == id:
                record['title'] = record['title'].upper()
                post_record = record
                break

        file.close()
        if len(post_record) == 0:  # record not found
            raise Exception
        else:
            with open('posts.json', mode='w') as file:
                file.write(json.dumps(posts, indent=4))

            return jsonify({
                'status': 200,
                'message': 'Post title was successfully updated',
                'data': post_record,
            })

    except Exception:
        return jsonify({
            'error': 404,
            'message': 'Post not found',
            'data': {},
        })



if __name__ == '__main__':
  app.run(debug=True)
