from flask import Flask, render_template
import os
import redis

app = Flask(__name__)


# Connect to redis
def get_client():
    redis_host = os.environ.get('REDIS_HOST')
    r = redis.Redis(host=redis_host, port=6379)
    return r

# Home page
@app.route("/", methods=['GET'])
def home():
    """
    The function to define the homepage. We set a key, value pair on the redis here.

    Returns:
        a html template with the already set key, value pair from redis
    """
    # get redis object
    redis_client = get_client()

    # key, value to set to redis
    key='Hello'
    value='World!'

    redis_client.set(key, value)

    # fetch the return value of the set key from redis
    return_value = get_key('Hello').decode('utf-8')

    # return the values to the html template
    return render_template('index.html', key=key, value=return_value)


# set_key page
@app.route("/set_key/<string:key>/<string:value>", methods=['GET'])
def set_key(key,value):
    """
    The function to set the key value pair in redis
    The URI should be localhost:9001:/set_key/foo/bar to write to redis

    Returns:
        a message that key is not or not
    """
    # get redis object
    redis_client = get_client()

    # set key, value to redis from the URI
    response = redis_client.set(key, value)
    if response == True:
      return f"{key} is set to {value}"
    else:
      return "A string key value is expected"


# get_key page
@app.route("/get_key/<string:key>", methods=['GET'])
def get_key(key):
    """
    The function to get the value of a key if present in redis
    The URI should be localhost:9001:/get_key/foo to get the key's value from redis

    Returns:
        the value if key is found in redis
    """
    # get redis object
    redis_client = get_client()

    # get value from redis with the key in the URI
    response = redis_client.get(key)
    if response is None:
      return "Key not found"
    return response