from flask import Flask, request, jsonify
import json
# noinspection PyPackageRequirements
from werkzeug.exceptions import HTTPException

app = Flask(__name__, static_url_path='', static_folder='')
app.config["DEBUG"] = True


def get_dummy_response():
    # instantiate coding data handler
    # initiate response
    result = {'result_message': "SUCCESS", 'result_code': 200}
    if 'n' in request.args:
        names = request.args.getlist('n')
        # already decoded in args
        # terms = [urllib.parse.unquote_plus(x).upper() for x in terms_encoded]
        result['names'] = names
    else:
        result['names'] = 'no names'

    return jsonify(result)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def get_index():
    return app.send_static_file('index.html')


@app.route('/request', methods=['GET'])
def dummy_request():
    return get_dummy_response()


if __name__ == "__main__":
    app.run()
