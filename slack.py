import yaml
import os
import re
from slackclient import SlackClient
import logging

path = os.environ["WORKDIR"]

try:
    with open(path + "/trigger_plugins/slack/dnifconfig.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        slacktoken = cfg['trigger_plugins']['SLACK_TOKEN']
except Exception,e:
    logging.error("SLACK trigger error in reading dnifconfig.yml: {}".format(e))


def chan_write(inward_array, var_array):
    logging.info("In chan_write ")
    sc = SlackClient(slacktoken)
    tmp_lst=[]
    for i in inward_array:
        try:
            var_array[0] = str(var_array[0]).strip()
            s1 = var_array[0].split('"')
            s = str(s1[1]).strip()
            d = re.findall('\s*_(.*?)_\s*', s)
            nt = s
            for di in d:
                nt = re.sub("_{}_".format(di), '{$' + di + '}', nt)
            d = dict((x[1], '~~') for x in nt._formatter_parser())
            d.update(i)
            c = nt.format(**d)
            i["Channel"] = s1[0].strip()
            i["Message"] = c
            sc.api_call(
            "chat.postMessage",
            channel=i["Channel"],
            as_user="true",
            text=i["Message"])
            tmp_lst.append(i)
        except Exception, e:
            tmp_lst.append(i)
            logging.error("SLACK trigger error posting to channel {} : {}".format(str(var_array[0]),e))
    return tmp_lst
