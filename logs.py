import psycopg2
from datetime import datetime

dbName="news"

query_1=("select a.title,count(*) as views "
        "from articles a inner join log b "
        "on a.slug=replace(path,'/article/','') "
        "where status='200 OK' and length(path)>1 group by "
        "a.title order by views desc limit 3")


query_2=("select c.name, count(*) as views "
        "from articles a inner join log b on "
        "a.slug=replace(path,'/article/','') inner join "
        "authors c on (c.id=a.author) "
        "where status='200 OK' and length(path)>1 group by "
        "c.name order by views desc")

query_3 = (
      "select day, perc from ("
      "select day, round((sum(requests)/(select count(*) from log where "
      "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
      "perc from (select substring(cast(log.time as text), 0, 11) as day, "
      "count(*) as requests from log where status like '%404%' group by day)"
      "as log_percentage group by day order by perc desc) as final_query "
      "where perc >= 1")

def get_results(query):
    
    con=psycopg2.connect("dbname={}".format(dbName))
    cur=con.cursor()
    try:
        cur.execute(query)
    except Exception as e:
        print(e)
    else:
        return cur.fetchall()
    finally:
        con.close()

def print_results(qresults):
    for i,rs in enumerate(qresults):
        print ("\t"+str(i+1)+"."+str(rs[0])+" - "+str(rs[1])+" views")

def print_error_results(qresults):
    for result in qresults:
        d=result[0]
        date_obj=datetime.strptime(d,"%Y-%m-%d")
        formatted_date=datetime.strftime(date_obj,"%B %d, %Y")
        print("\t"+str(formatted_date)+"-"+str(result[1])+"% errors")

if __name__=='__main__':
    print("What are the most popular three articles of all time?")
    #get query1 results
    popular_articles=get_results(query_1)

    #print query1 results
    print_results(popular_articles)
    print("Who are the most popular article authors of all time?")

    #get query2 results
    popular_authors=get_results(query_2)
    #print query2 results
    print_results(popular_authors)
    print("On which days did more than 1% of requests lead to errors?")
    #get query3 results

    error_days=get_results(query_3)
    print_error_results(error_days)


    

