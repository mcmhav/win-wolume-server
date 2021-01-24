from flask import Flask, Response, jsonify
from flask_restx import Api, Resource

import subprocess

def setup_server() -> Flask:
  app = Flask(__name__)
  api = Api(
    app,
    version='1.0',
    title='volume adjuster, windows',
    description='adjust volume',
  )
  ns = api.namespace('', description='endpoints for adjusting volume on windows')

  @ns.route('/volume_adjust/<adjustment>')
  class VolumeAdjust(Resource):

    @staticmethod
    def get(adjustment: str) -> Response:
      print(subprocess.run(['cscript.exe', f'volume_scripts/volume{adjustment}.js']))
      return jsonify({'status': 'okiii'})


  return app
