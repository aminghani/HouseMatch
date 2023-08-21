# HouseMatch

Scraping and Analysing Houses In Iran \
install the requirements with this command:

```
pip install -r requirements.txt
```

and use this to run the airflow:
```
bash run_airflow.sh
```
note: you need to set the environment variables first

this code extracts cleans, and saves the extracted house data to Postgres and Elasticsearch. then you can use any visualization tool like Grafana to analyze the data.

This is the airflow dag that is used for extracting the data:

![Screenshot 2023-08-21 192740](https://github.com/aminghani/HouseMatch/assets/61684174/bc883aea-904c-429a-a5d7-11189ee04b7d)

And This is an example Grafana dashboard that is used to analyze the extracted data:

![Screenshot 2023-08-21 192621](https://github.com/aminghani/HouseMatch/assets/61684174/922efd65-8c65-4964-911c-43208de18c13)
