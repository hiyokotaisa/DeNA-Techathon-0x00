# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

class CallbackModule(object):

    def playbook_on_stats(self, stats):
        deployed_hosts = sorted(stats.processed.keys())

        # Twitter API Info
        consumer_key=""
        consumer_secret=""
        access_token_key=""
        access_token_secret=""

        # Twitter Post URL
        url = "https://api.twitter.com/1.1/statuses/update.json"

        for host in deployed_hosts:
            summary = stats.summarize(host)

            # Tweet Contents
            params = {"status":"Deploy Completed: "+str(host)+"\n"+str(summary) }

            # Tweet after OAuth
            twitter = OAuth1Session(consumer_key, consumer_secret, access_token_key, access_token_secret)
            req = twitter.post(url, params = params)
