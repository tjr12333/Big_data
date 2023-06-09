# Kyochon Store Crawler
본 코드는 교촌치킨 홈페이지에서 매장 정보를 수집하는 웹 크롤링 코드입니다. 

이 파이썬 스크립트는 교촌치킨 웹사이트에서 가게 위치 정보를 추출합니다. 이를 위해 BeautifulSoup 라이브러리를 사용하여 웹사이트의 HTML을 파싱하고 관련 정보를 추출합니다.

추출된 정보는 Pandas DataFrame에 저장되어 CSV 파일로 내보내져 추가적인 분석에 사용됩니다.

## 코드 개요

- `urllib.request` 모듈을 이용하여 교촌치킨 매장정보를 크롤링합니다.
- 크롤링한 정보는 `pandas` 모듈을 이용하여 csv 파일로 저장합니다.

## 사용 모듈

- `BeautifulSoup`: HTML 문서를 파싱하기 위한 파이썬 패키지
- `urllib.request`: URL을 이용한 웹 요청 및 그에 대한 응답을 받기 위한 패키지
- `pandas`: 데이터 처리를 위한 라이브러리

## 코드 실행 방법

```python
python kyochon_store_crawling.py
```

## 사용법
스크립트를 실행하려면 main() 함수를 실행하면 됩니다. 스크립트는 교촌치킨 웹사이트를 크롤링하여 각 가게 위치에 대한 정보를 추출합니다. 결과 데이터는 지정된 디렉토리에 CSV 파일로 저장됩니다.

## 알려진 문제점
* 웹사이트 구조나 레이아웃이 변경될 경우 스크립트가 오류를 발생시킬 수 있습니다.
* 크롤링할 가게 위치가 많은 경우 스크립트가 오랜 시간이 걸릴 수 있습니다.
* 웹사이트와의 연결이 끊어지면 스크립트가 오류를 발생시킬 수 있습니다.
