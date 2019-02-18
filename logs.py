#!/usr/bin/env python3
import psycopg2
from datetime import datetime

dbName = "news"

query_1 = ("SELECT a.title, count(*) AS views "
           "FROM articles a INNER JOIN log b "
           "on a.slug=replace(path,'/article/','') "
           "WHERE status='200 OK' AND length(path)>1 GROUP by "
           "a.title ORDER by views DESC limit 3")

query_2 = ("SELECT c.name, count(*) AS views "
           "FROM articles a INNER JOIN log b "
           "on a.slug=replace(path,'/article/','') INNER JOIN "
           "authors c on (c.id=a.author) "
           "WHERE status='200 OK' AND length(path)>1 GROUP by "
           "c.name ORDER by views DESC")

query_3 = ("SELECT day, perc FROM ("
           "SELECT day, round((sum(requests)/(SELECT count(*) FROM log WHERE "
           "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
           "perc FROM (select substring(cast(log.time as text), 0, 11) as "
           "day, count(*) as requests FROM log "
           "WHERE status like '%404%' GROUP by day) "
           "as log_percentage GROUP by day ORDER by perc desc) as final_query "
           "WHERE perc >= 1")


def get_results(query):
    con = psycopg2.connect("dbname={}".format(dbName))
    cur = con.cursor()

    try:
        cur.execute(query)
    except Exception as e:
        print(e)
    else:
        return cur.fetchall()
    finally:
        con.close()


def print_results(query_results):
    for i, res in enumerate(query_results):
        print("\t"+str(i+1)+"."+str(res[0])+" - "+str(res[1])+" views")


def print_errors(query_results):
    for result in query_results:
        date = result[0]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = datetime.strftime(date_obj, "%B %d,%Y")
        print("\t"+str(formatted_date)+" - "+str(result[1])+"% errors")


if __name__ == '__main__':
    print("What are the most popular three articles of all time?")
    articles = get_results(query_1)
    print_results(articles)

    print("Who are the most popular article authors of all time?")
    authors = get_results(query_2)
    print_results(authors)

    print("On which days did more than 1% of requests lead to errors?")
    error_days = get_results(query_3)
    print_errors(error_days)
