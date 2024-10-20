from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b4a40f9a83934bcebe3ee1e827d20b5e')



all_articles = newsapi.get_everything(q='Bitcoin',
                                      language='en',
                                      sort_by='relevancy')
##print (all_articles)

print (all_articles["totalResults"])



