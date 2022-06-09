import requests

headers = {
    # 假装自己是浏览器    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': 'LIVE_BUVID=AUTO9515753680876948; rpdid=|(k|JkJYklYY0J\'ul)m)|mJmm; blackside_state=1; buvid3=1F7E9CCA-3C52-4E96-B85F-4F791347C5E8143096infoc; CURRENT_QUALITY=0; video_page_version=v_old_home; _uuid=F5BAAF72-B7FC-A38B-2B6F-CA83C2F7A83D42878infoc; fingerprint3=88925602a56580e07ecab48314bfc0c0; fingerprint_s=2037d82e8d6ad65bc490a3407a3d6d81; i-wanna-go-back=-1; buvid4=5B2AC7E4-7250-0335-39B1-B0932BA7AF9704919-022012612-M95/ZDCcufUAg96fooiAuA%3D%3D; buvid_fp_plain=undefined; b_ut=5; CURRENT_BLACKGAP=0; nostalgia_conf=-1; PVID=1; fingerprint=c93d2ef63cc0380c6a6b748e844fe7a4; buvid_fp=c3530f197aabcc94f0348b356c23cb37; SESSDATA=00c3226d%2C1665210533%2Cc5506%2A41; bili_jct=38196842451030679cd9ce1ac00431b4; DedeUserID=31470029; DedeUserID__ckMd5=fbde293b516eb599; sid=j5b9k0db; bp_video_offset_31470029=669198012632793100; CURRENT_FNVAL=4048; innersign=0; b_lsid=11081E165_18142055E93; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_1F7E9CCA%22%3A%2218142057011%22%2C%22333.788.fp.risk_1F7E9CCA%22%3A%221814173FC79%22%7D%7D',
}

session = requests.Session()
response = session.get('https://www.bilibili.com/', headers=headers)

print(response.text)
