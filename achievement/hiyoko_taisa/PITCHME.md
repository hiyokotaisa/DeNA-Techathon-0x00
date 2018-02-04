---
# AnsibleのPlaybook実行結果をTwitterにつぶやこう!
## @hiyoko_taisa
---
## やったこと
- PythonでAnsibleのCallback Pluginを書いた
- Twitter API経由でAnsible Playbookの実行が完了するとつぶやかれる
---
## つかいかた
- playbookがあるディレクトリ直下にcallback_pluginsフォルダ作る
- tweet.pyをおく(個人で使う場合は別途API Keyとかもろもろ入手して書き換えてね)
- あとは普通にPlaybookを実行するだけ！
---
## 実行すると
<img src="https://pbs.twimg.com/media/DVLPEctV4AACT1e.jpg">
---
## 問題点
- **超汚いコード** (ごめん)
- **Keyとか埋め込んじゃってる**
- 失敗判定してない(時間なかった)
- 100台とかデプロイしたら連投制限でアカウント規制されそう
---
## つくったやつ
```
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

class CallbackModule(object):

    def playbook_on_stats(self, stats):
        deployed_hosts = sorted(stats.processed.keys())

        # Twitter API Info
        consumer_key="(略)"
        consumer_secret="(略)"
        access_token_key="(略)"
        access_token_secret="(略)"

        # Twitter Post URL
        url = "https://api.twitter.com/1.1/statuses/update.json"

        for host in deployed_hosts:
            summary = stats.summarize(host)

            # Tweet Contents
            params = {"status":"Deploy Completed: "+str(host)+"\n"+str(summary) }

            # Tweet after OAuth
            twitter = OAuth1Session(consumer_key, consumer_secret, access_token_key, access_token_secret)
            req = twitter.post(url, params = params)
```
---
# [EOF]
---
~                                        
