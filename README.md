# Search As You Type (Elasticsearch)

Demo code and sample employees data to implement "Search as you type" feature on elasticsearch. 

Written the middleware API in `python` using [flask](https://flask.palletsprojects.com/en/2.0.x/). Used [JQuery](https://jquery.com/) for javascript operations.

## Installation

Assuming you have successfully installed [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) and [Kibana](https://www.elastic.co/guide/en/kibana/current/install.html) on your machine and its working perfect. Kindly refer respective installation document if there is any issue.

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

Make sure Elasticsearch and kibana is up and running fine on your machine. 

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
curl -s -H "Content-Type: application/x-ndjson" -XPOST "localhost:9200/_bulk" --data-binary "@data.json"
```

### Run `api.py` & test

Start API Server

```
python3 api.py
```

Open `index.html` on your browser. 
