![demo](search_as_you_type.gif)

# Search As You Type (Elasticsearch)

Demo code and sample employees data to implement the "Search as you type" feature on elasticsearch. 

Written the middleware API in `python` using [flask](https://flask.palletsprojects.com/en/2.0.x/). Used [JQuery](https://jquery.com/) for javascript operations.

## Installation

Assuming you have successfully installed [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) and [Kibana](https://www.elastic.co/guide/en/kibana/current/install.html) on your machine and it is working perfectly. Kindly refer respective installation document. 

OR

You can run [Elasticsearch on the cloud](https://cloud.elastic.co/registration) with a few clicks. 

### Install Python3 & pip3

1. Refer [Document](https://www.python.org/downloads/) to install `python3` & `pip3` on your system.
2. Install `flask`
```
pip3 install flask
```
3. Install `elasticsearch` package
```
pip3 install elasticsearch
```

### git Clone

```
git clone https://github.com/ashishtiwari1993/search_as_you_type.git
cd search_as_you_type
```

### Create Index and load data

Make sure Elasticsearch and kibana are up and running fine on your machine. 

#### Create Index

```
PUT /sayt?pretty
{
  "mappings": {
    "properties": {
      "first_name": {
        "type": "search_as_you_type"
      },
      "last_name": {
        "type": "search_as_you_type"
      },
      "street_address": {
        "type": "search_as_you_type"
      },
      "company": {
        "type": "search_as_you_type"
      },
      "email": {
        "type": "search_as_you_type"
      }
    }
  }
}
```

#### Load sample data

Sample [data.json](https://github.com/ashishtiwari1993/search_as_you_type/blob/main/data.json) file is given which need to load with the help of [bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html). 

```
curl -s -H "Content-Type: application/x-ndjson" --cacert /path/to/http_ca.crt  -u "username:password" -XPOST "https://localhost:9200/_bulk" --data-binary "@data.json"
```

Do not forget to change the elasticsearch's endpoint. 

### Run `api.py` & test

Open `api.py` and change elasticsearch endpoint accordingly.

```py
es = Elasticsearch(
    "https://localhost:9200",
    ca_certs = "path/to/ca_certificate",
    basic_auth = ("username", "password")
)
```

#### Start API Server

```
python3 api.py
```

This will start the API service on port `5001`.

Open `index.html` on your browser. 



#### Template files in the correct location
```
myproject/
    api.py
    templates/
        index.html
```
