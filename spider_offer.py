import re
import json
import time
import random
import requests
import offer_data
import pandas as pd

def get_data(key):
    '''
    key : 搜索框输入的内容，作为岗位关键词
    '''
    be_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?'
    for i in range(1,10):
        headers_ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                      'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44']
        headers_cookie = ['_uab_collina=165448826088508236665907;guid=5694f167d029b0609f6b46db97abd2fe;nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaidu5_153404%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIwXzEuaHRtbD9mcm9tPWJhaWR1YWQ%253D%2526k%253Dd946ba049bfb67b64f408966cbda3ee9%2526bd_vid%253D9311213790741583000%26%7C%26; _ujz=MTQxMDgyNTQ2MA%3D%3D; ps=needv%3D0; 51job=cuid%3D141082546%26%7C%26cusername%3Dm9QiNu3WT4kUj1%252B868MLNR6qzg9F8WUwFtFs36TsadE%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%26%7C%26ccry%3D.0Bd7dJzht3%252Fg%26%7C%26cconfirmkey%3D%25241%2524qm9ada.s%2524Z.dY8FWvLOWIOXRriW4Rp%252F%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524dgiuAyvm%2524IvNb8Mm36l2JSLgrNWKlM.%26%7C%26to%3Dddfef2c7fa7b79af6b7b8082073e267b62aadb47%26%7C%26; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22141082546%22%2C%22first_id%22%3A%2218189d63fa34c1-05dc0a64fece584-26021b51-921600-18189d63fa4c9b%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgxODlkNjNmYTM0YzEtMDVkYzBhNjRmZWNlNTg0LTI2MDIxYjUxLTkyMTYwMC0xODE4OWQ2M2ZhNGM5YiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE0MTA4MjU0NiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22141082546%22%7D%2C%22%24device_id%22%3A%2218189d63fa34c1-05dc0a64fece584-26021b51-921600-18189d63fa4c9b%22%7D; acw_tc=76b20fec16559630755823289e0f6e2a590a2cc817b66b523a63fc5d3fdae4; slife=lastlogindate%3D20220623%26%7C%26; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAweb%C7%B0%B6%CB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BC%E6%D6%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%EE%BC%D9%BC%E6%D6%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; ssxmod_itna=YuD=0KAKBK8hCDzaD2eEfnMDIxDu4DtNkHCdHDlrpexA5D8D6DQeGTrRPhzrqzqbBon+W4gCODXW=lmSiwvW3SjyGYDU4i8DCwucirDem=D5xGoDPxDeDADYoUDAqiOD7qDdLwHyzkDbxi3LxiaDGeDe6FODY5DhxDC0APDwx0CLhAFQb5pR2x+Wi28D7vpDla4vS28i+ffzA5+G38GEWKDXhdDvO51M2PpDB+kl1HG/Wi3Kehahp03Ci2YPBx55Wie5CDoWjrxY14BdixY31xSFBxDiaUSHYD==; ssxmod_itna2=YuD=0KAKBK8hCDzaD2eEfnMDIxDu4DtNkHCdD6hzQFQD05vx03eNu5mhoXD6igOFXxu3Bw4PheNCQmROlS67F0A5zR2ycGKMaDLFfBlZpdOhou9dxSOfgY/1MUjVxc52hPZaNgqlu1m7rpm11pmO9Ov8Ytu4Xen+NKObKPorFK7hepaha/RIUZbze2wv+bS1scqCK68LXQc8M1ujKrrzTO81H1kzZ481TcEjqqfjDThTZBn6H2l1WYkuwFB=tdm2qegaIUj27YekyRknpTC9Mr2fjO8z0coC94SMfHYjYZmrc/pEHUyR0Wje4jmPvz2u/W13cd3wAmH8DaGRTeqbbYiIYRsjTaGnQ/e5PpPyuYqh5wA1luovhoqgsKOFKgheuQ6YQmgDzg51n3ghQHoKFgm9OiVgYEiQyObVnYZEbHEopo3D07zBPD7=DYI5eD==',
                          '_uab_collina=165448826088508236665907; guid=5694f167d029b0609f6b46db97abd2fe; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaidu5_153404%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIwXzEuaHRtbD9mcm9tPWJhaWR1YWQ%253D%2526k%253Dd946ba049bfb67b64f408966cbda3ee9%2526bd_vid%253D9311213790741583000%26%7C%26; _ujz=MTQxMDgyNTQ2MA%3D%3D; ps=needv%3D0; 51job=cuid%3D141082546%26%7C%26cusername%3Dm9QiNu3WT4kUj1%252B868MLNR6qzg9F8WUwFtFs36TsadE%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%26%7C%26ccry%3D.0Bd7dJzht3%252Fg%26%7C%26cconfirmkey%3D%25241%2524qm9ada.s%2524Z.dY8FWvLOWIOXRriW4Rp%252F%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524dgiuAyvm%2524IvNb8Mm36l2JSLgrNWKlM.%26%7C%26to%3Dddfef2c7fa7b79af6b7b8082073e267b62aadb47%26%7C%26; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22141082546%22%2C%22first_id%22%3A%2218189d63fa34c1-05dc0a64fece584-26021b51-921600-18189d63fa4c9b%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgxODlkNjNmYTM0YzEtMDVkYzBhNjRmZWNlNTg0LTI2MDIxYjUxLTkyMTYwMC0xODE4OWQ2M2ZhNGM5YiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE0MTA4MjU0NiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22141082546%22%7D%2C%22%24device_id%22%3A%2218189d63fa34c1-05dc0a64fece584-26021b51-921600-18189d63fa4c9b%22%7D; slife=lastlogindate%3D20220623%26%7C%26; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAweb%C7%B0%B6%CB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BC%E6%D6%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%EE%BC%D9%BC%E6%D6%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; ssxmod_itna=Qq+xBDnDgDRDy0QG8DzhYW40KEWEdmDG22iowDoqGN+3DZDiqAPGhDC+8K2im+rewrKCj8nGQre64Rb=iFEhi2p/7ix0aDbqGkqU8G4GGUxBYDQxAYDGDDPDo2PD1D3qDkD7O1lS9kqi3DbO=Df4DmDGAc3qDgDYQDGdK6D7QDIk=ec+rSAWUximD4FqDMjeGXmBWrFqbWaaeZieWrqCpRDB=CxBQMAkNUAeDHCwXM4l5eFhxaj3Qo8EDTiimxniP=nixPYBqei8D5/9x4Yo+QAA4QexDA3sZQeD; ssxmod_itna2=Qq+xBDnDgDRDy0QG8DzhYW40KEWEdmDG22iowDxA=aKeKKPD/ilDFrR70IO0DWRDOeeOqid3jhiKjwebS7AevYjP1iawQIfOBtm35IpYtE5=ezu2mdaqUkxv83MI6Q6tfUhLeKeebGTPoeqtP7kt6qGtgG=4Zpspxo8biurrBBiH+9w5ha7O=0t0gOwdaArqQavKZbOupf1Og8pTc8a4Od6Fzk7ASSEUBY4uhGfeWEF9bFH8xdxP3muoKFL=fctKCHmKx1I1vWyrsyxt=zyHM1Rem/hmwIBaHyyEY7O2kWwbM1/yu=xxbk1LYESzhTrygGaM8P8oKxF=ltaEYok5q+C9AYtQi8WKPEiehD83GR75ULirji1C5Em5GRKxfTrWrb4IcC5dE3unpRQQLRvtSpBWKu21BRHUlWocb6lmd=i2jm9errefEOfweEt=iuGwFEdzP88fYroi1uK8dj8wGUw60jbzPrsWewP5QAUNiqfDDwrHDjKDeTe4D==',
                          '_uab_collina=165448826088508236665907; guid=5694f167d029b0609f6b46db97abd2fe; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaidu5_153404%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIwXzEuaHRtbD9mcm9tPWJhaWR1YWQ%253D%2526k%253Dd946ba049bfb67b64f408966cbda3ee9%2526bd_vid%253D9311213790741583000%26%7C%26; _ujz=MTQxMDgyNTQ2MA%3D%3D; ps=needv%3D0; 51job=cuid%3D141082546%26%7C%26cusername%3Dm9QiNu3WT4kUj1%252B868MLNR6qzg9F8WUwFtFs36TsadE%253D%26%7C%26cpassword%3D%26%7C%26cname%3D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%26%7C%26ccry%3D.0Bd7dJzht3%252Fg%26%7C%26cconfirmkey%3D%25241%2524qm9ada.s%2524Z.dY8FWvLOWIOXRriW4Rp%252F%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D%26%7C%26cnamekey%3D%25241%2524dgiuAyvm%2524IvNb8Mm36l2JSLgrNWKlM.%26%7C%26to%3Dddfef2c7fa7b79af6b7b8082073e267b62aadb47%26%7C%26; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22141082546%22%2C%22first_id%22%3A%2218189d63fa34c1-05dc0a64fece584-26021b51-921600-18189d63fa4c9b%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgxODlkNjNmYTM0YzEtMDVkYzBhNjRmZWNlNTg0LTI2MDIxYjUxLTkyMTYwMC0xODE4OWQ2M2ZhNGM5YiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjE0MTA4MjU0NiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22141082546%22%7D%2C%22%24device_id%22%3A%2218189d63fa34c1-05dc0a64fece584-26021b51-921600-18189d63fa4c9b%22%7D; slife=lastlogindate%3D20220623%26%7C%26; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAweb%C7%B0%B6%CB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BC%E6%D6%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60080200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%EE%BC%D9%BC%E6%D6%B0%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; acw_tc=76b20fe716559656469344338e7ada6c255d501ff2ae466f14141100b9ecfd; ssxmod_itna=CqjxuDgDcD00iQqGHD8zR5rEi841iorRDD5PQD/zixnqD=GFDK40oE7fbKoDO7ScAnGW=QGEyUWq/p+DTvrb27fNoDU4i8DCuiNopmDYA8Dt4DTD34DYDixibkxi5GRD0KDFF5XUZ9Dm4GWFqGfDDoDY86RDitD4qDBzodDKqGgFq2j7mt3puDesBhcD0tdxBdPtphcGeaaOiNexanDTEQDzqHDtutS9kd3x0PyBMUDZh+WSh4oBoooW7PqzAeeAGxq/i44YDxezAq3tRGxKsG57GE0UDpd7DDAbV1QeD===; ssxmod_itna2=CqjxuDgDcD00iQqGHD8zR5rEi841iorRDD5PG9isQYtDBulx7PDOi7Ia3Oiizxn+hODL=mb08e=tuii3doAdY6+q8/3H2buif69aPXfFwLBhk2f7o4jb6tP8rAYdTLe65YQSe7kUYxeHHcyqg0PxWpqhxZyWDOBQIcAm1roGH8EGueO+i3cqCc5Hr3KibhgEunFGNDpzCRiiL=om3xLELcIEAfo6/UfIbcFsip3Wj/nQHPYWh=MR7oWpxtmWI86n36IEkL1H8fe1oxUTgCegqO3=kTPvFIwbIVU7giulnBcMqQ9Q9HT=SHtbWaAh7A2+R4rRv4hmpWbtnvqrbxHpDhy46WPg546AFUyPE7KpB18YqMAYNWVCBq475wioQgRmodUYV/AKZyquB=5gdWbr9Oir48eHQF+pmuBWSWU4iFqPLR8CbKY4I7+szB8Rf73u4wBNsTdsYHGeqLh7u53D07R4DLxD27GDD===',
                          ]
        headers = {
            'Cookie':'',
            'Host':'search.51job.com',
            'User-Agent':''
        }
        # proxy_choice = [{'http':'165.225.222.16:10605'},{'http':'165.225.72.51:10605'}]
        headers['Cookie'] = random.choice(headers_cookie)
        headers['User-Agent'] = random.choice(headers_ua)
        # proxy = random.choice(proxy_choice)
        r = requests.get(be_url.format(key,i),headers=headers)
        r.encoding = 'gbk' # 注意编码
        if r.status_code == requests.status_codes.codes.OK:
            pattern = re.compile('window.__SEARCH_RESULT__ = (.*?)</script>',re.S)
            html_data = re.findall(pattern,r.text)# 匹配到的数据是字符串
        time.sleep(1)
    return html_data

#利用 json 转化为字典形式
def new_data(key):
    datas = get_data(key)
    ls_data = []
    for k in range(len(datas)):
        json_data = json.loads(datas[k])
        for da in json_data ['engine_jds']:
            # 构建新字典，存储爬取到的数据
            try: # 异常处理，避免网页结构不规范而导致的程序异常
                dt = {
                    '岗位' : da['job_name'],
                    '公司' : da['company_name'],
                    '薪资' : da['providesalary_text'],
                    '福利' : ','.join(da['jobwelf_list']),
                    '行业' : da['companyind_text'],
                    '城市' : da['workarea_text'],
                    '规模' : da['companysize_text'],
                    '经验要求' : da['attribute_text'][1],
                    '学历要求' : da['attribute_text'][2],
                    '发布日期' : da['updatedate'],
                    '详细介绍 Link' : da['job_href']
                }
                ls_data.append(dt)
            except Exception as e:
                pass
        df_offer = pd.DataFrame(ls_data)
        offer_data.offer_lsb(df_offer)
        return df_offer

# 在 if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而 import 到其他脚本中是不会被执行的

if __name__ == '__main__':
    new_data()
