#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def query_records():
    search = request.args.get('q')

    if search == "":
        return "Provide parameter(q)", 400


    q = {
      "size" : 20,
      "query": {
        "multi_match": {
          "query": search,
          "type" : "bool_prefix",
          "fields": [
            "first_name","first_name._2gram","first_name._3gram",
            "last_name","last_name._2gram","last_name._3gram",
            "street_address","street_address._2gram","street_address._3gram",
            "company","company._2gram","company._3gram"
            ]
        }
      },
      "highlight": {
        "pre_tags" : ["<strong><u>"],
        "post_tags" : ["</u></strong>"],
        "fields": [
          {"first_name": {"type":"unified"}},
          {"last_name": {"type":"unified"}},
          {"company": {"type":"unified"}},
          {"street_address": {"type":"unified"}}
        ]
      }
    }
    d = es.search(index="sayt", body=q)
    response = jsonify(d['hits']['hits'])
    response.headers.add('access-control-allow-origin', '*')
    response.headers.add('access-control-allow-methods', 'get, post')
    return response

@app.route('/get',methods=['GET'])
def query_getOne():
    id = request.args.get('id')

    if id == "":
        return "Provide paramter(id)", 400

    resp = es.get(index="sayt", id=id)

    response = jsonify(resp['_source'])
    response.headers.add('access-control-allow-origin', '*')
    response.headers.add('access-control-allow-methods', 'get, post')
    return response

app.run(host="0.0.0.0", port=5001)
