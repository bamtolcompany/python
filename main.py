print('국회의원 정당별 분류표')
raw_text = """
강경숙

조국혁신당

강대식

국민의힘

강득구

더불어민주당

강명구

국민의힘

강민국

국민의힘

강선영

국민의힘

강선우

더불어민주당

강승규

국민의힘

강유정

더불어민주당

강준현

더불어민주당

강훈식

더불어민주당

고동진

국민의힘

고민정

더불어민주당

곽규택

국민의힘

곽상언

더불어민주당

구자근

국민의힘

권성동

국민의힘

권영세

국민의힘

권영진

국민의힘

권칠승

더불어민주당

권향엽

더불어민주당

김건

국민의힘

김교흥

더불어민주당

김기웅

국민의힘

김기표

더불어민주당

김기현

국민의힘

김남근

더불어민주당

김남희

더불어민주당

김대식

국민의힘

김도읍

국민의힘

김동아

더불어민주당

김문수

더불어민주당

김미애

국민의힘

김민석

더불어민주당

김민전

국민의힘

김병기

더불어민주당

김병주

더불어민주당

김상욱

국민의힘

김상훈

국민의힘

김석기

국민의힘

김선교

국민의힘

김선민

조국혁신당

김성원

국민의힘

김성환

더불어민주당

김성회

더불어민주당

김소희

국민의힘

김승수

국민의힘

김승원

더불어민주당

김영배

더불어민주당

김영진

더불어민주당

김영호

더불어민주당

김영환

더불어민주당

김예지

국민의힘

김용만

더불어민주당

김용민

더불어민주당

김용태

국민의힘

김우영

더불어민주당

김원이

더불어민주당

김위상

국민의힘

김윤

더불어민주당

김윤덕

더불어민주당

김은혜

국민의힘

김장겸

국민의힘

김재섭

국민의힘

김재원

조국혁신당

김정재

국민의힘

김정호

더불어민주당

김종민

무소속

김종양

국민의힘

김주영

더불어민주당

김준혁

더불어민주당

김준형

조국혁신당

김태년

더불어민주당

김태선

더불어민주당

김태호

국민의힘

김한규

더불어민주당

김현

더불어민주당

김현정

더불어민주당

김형동

국민의힘

김희정

국민의힘

나경원

국민의힘

남인순

더불어민주당

노종면

더불어민주당

맹성규

더불어민주당

모경종

더불어민주당

문금주

더불어민주당

문대림

더불어민주당

문정복

더불어민주당

문진석

더불어민주당

민병덕

더불어민주당

민형배

더불어민주당

민홍철

더불어민주당

박균택

더불어민주당

박대출

국민의힘

박덕흠

국민의힘

박민규

더불어민주당

박범계

더불어민주당

박상웅

국민의힘

박상혁

더불어민주당

박선원

더불어민주당

박성민

국민의힘

박성준

더불어민주당

박성훈

국민의힘

박수민

국민의힘

박수영

국민의힘

박수현

더불어민주당

박용갑

더불어민주당

박은정

조국혁신당

박정

더불어민주당

박정하

국민의힘

박정현

더불어민주당

박정훈

국민의힘

박주민

더불어민주당

박준태

국민의힘

박지원

더불어민주당

박지혜

더불어민주당

박찬대

더불어민주당

박충권

국민의힘

박해철

더불어민주당

박형수

국민의힘

박홍근

더불어민주당

박홍배

더불어민주당

박희승

더불어민주당

배준영

국민의힘

배현진

국민의힘

백선희

조국혁신당

백승아

더불어민주당

백종헌

국민의힘

백혜련

더불어민주당

복기왕

더불어민주당

부승찬

더불어민주당

서명옥

국민의힘

서미화

더불어민주당

서범수

국민의힘

서삼석

더불어민주당

서영교

더불어민주당

서영석

더불어민주당

서왕진

조국혁신당

서일준

국민의힘

서지영

국민의힘

서천호

국민의힘

성일종

국민의힘

소병훈

더불어민주당

손명수

더불어민주당

송기헌

더불어민주당

송석준

국민의힘

송언석

국민의힘

송옥주

더불어민주당

송재봉

더불어민주당

신동욱

국민의힘

신성범

국민의힘

신영대

더불어민주당

신장식

조국혁신당

신정훈

더불어민주당

안규백

더불어민주당

안도걸

더불어민주당

안상훈

국민의힘

안철수

국민의힘

안태준

더불어민주당

안호영

더불어민주당

양문석

더불어민주당

양부남

더불어민주당

어기구

더불어민주당

엄태영

국민의힘

염태영

더불어민주당

오기형

더불어민주당

오세희

더불어민주당

용혜인

기본소득당

우원식

무소속

우재준

국민의힘

위성곤

더불어민주당

위성락

더불어민주당

유동수

더불어민주당

유상범

국민의힘

유영하

국민의힘

유용원

국민의힘

윤건영

더불어민주당

윤상현

국민의힘

윤영석

국민의힘

윤재옥

국민의힘

윤종군

더불어민주당

윤종오

진보당

윤준병

더불어민주당

윤한홍

국민의힘

윤호중

더불어민주당

윤후덕

더불어민주당

이강일

더불어민주당

이개호

더불어민주당

이건태

더불어민주당

이광희

더불어민주당

이기헌

더불어민주당

이달희

국민의힘

이만희

국민의힘

이병진

더불어민주당

이상식

더불어민주당

이상휘

국민의힘

이성권

국민의힘

이성윤

더불어민주당

이소영

더불어민주당

이수진

더불어민주당

이양수

국민의힘

이언주

더불어민주당

이연희

더불어민주당

이용선

더불어민주당

이용우

더불어민주당

이원택

더불어민주당

이인선

국민의힘

이인영

더불어민주당

이재강

더불어민주당

이재관

더불어민주당

이재명

더불어민주당

이재정

더불어민주당

이정문

더불어민주당

이정헌

더불어민주당

이종배

국민의힘

이종욱

국민의힘

이주영

개혁신당

이준석

개혁신당

이철규

국민의힘

이춘석

더불어민주당

이학영

더불어민주당

이해민

조국혁신당

이해식

더불어민주당

이헌승

국민의힘

이훈기

더불어민주당

인요한

국민의힘

임광현

더불어민주당

임미애

더불어민주당

임오경

더불어민주당

임이자

국민의힘

임종득

국민의힘

임호선

더불어민주당

장경태

더불어민주당

장동혁

국민의힘

장종태

더불어민주당

장철민

더불어민주당

전용기

더불어민주당

전재수

더불어민주당

전종덕

진보당

전진숙

더불어민주당

전현희

더불어민주당

정동만

국민의힘

정동영

더불어민주당

정성국

국민의힘

정성호

더불어민주당

정연욱

국민의힘

정을호

더불어민주당

정일영

더불어민주당

정점식

국민의힘

정준호

더불어민주당

정진욱

더불어민주당

정청래

더불어민주당

정춘생

조국혁신당

정태호

더불어민주당

정혜경

진보당

정희용

국민의힘

조경태

국민의힘

조계원

더불어민주당

조배숙

국민의힘

조승래

더불어민주당

조승환

국민의힘

조은희

국민의힘

조인철

더불어민주당

조정식

더불어민주당

조정훈

국민의힘

조지연

국민의힘

주진우

국민의힘

주철현

더불어민주당

주호영

국민의힘

진선미

더불어민주당

진성준

더불어민주당

진종오

국민의힘

차규근

조국혁신당

차지호

더불어민주당

채현일

더불어민주당

천준호

더불어민주당

천하람

개혁신당

최기상

더불어민주당

최민희

더불어민주당

최보윤

국민의힘

최수진

국민의힘

최은석

국민의힘

최형두

국민의힘

추경호

국민의힘

추미애

더불어민주당

한기호

국민의힘

한민수

더불어민주당

한병도

더불어민주당

한정애

더불어민주당

한준호

더불어민주당

한지아

국민의힘

한창민

사회민주당

허성무

더불어민주당

허영

더불어민주당

허종식

더불어민주당

홍기원

더불어민주당

황명선

더불어민주당

황운하

조국혁신당

황정아

더불어민주당

황희

더불어민주당


"""
    

# 줄 정리
lines = [line.strip() for line in raw_text.strip().split('\n') if line.strip() != '']

# 정당별 이름 저장할 딕셔너리
parties = {}

for i in range(0, len(lines) - 1, 2):
    name = lines[i]
    party = lines[i + 1]
    if party not in parties:
        parties[party] = []
    parties[party].append(name)

# 출력
for party, names in parties.items():
    print(f"({party})")
    for name in names:
        print(name)
    print()
