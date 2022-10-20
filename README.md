## 내일배움캠프 project 2. PetDictionary

<p>
    <img src="https://img.shields.io/badge/Django-4.1.1-green"/>
</p>

***

### 소개
'PetDictionary'은 동물 검색 기능을 제공 하는 서비스입니다.

***



### 개발 일정
**진행기간** 2022년 10월 17일 ~ 2022년 10월 20일


***


### 팀 구성 및 작업 분배

|작업자|구현기능|비고|
|------|------|------|
|이태은|이미지 업로드|  -|
|이현재|데이터셋 학습|  -|
|장준표|프론트엔드, 재검색|  -|
|정진엽|설문조사| -|
|조지현|이미지검색결과|  -|

***


### API 설계

|페이지|기능|API URL|Method|Request(요청)|Response(응답)|
|------|------|------|------|------|------|
|메인|-|home/|GET|-|-|
|검색|-|input/|GET|-|-|
|검색|검색할 이미지 업로드|input/|POST|이미지|이미지|
|검색결과|검색 결과 조회|output/|GET|이미지에서 추출한 검색어|구글 검색 결과|
|검색결과|검색 정확도 설문 참여|output/|POST|설문 결과 (Yes/No)|Yes: 설문 결과 조회 페이지로 이동, No: 재검색 페이지로 이동|
|재검색|-|except/|GET|-|-|
|재검색|검색어를 입력하여 재검색|except/|POST|검색어|구글 검색 결과|
|정확도 설문 결과|검색 정확도 설문 결과 조회|graph/|GET|-|검색 정확도 설문 결과 그래프|


***


### 와이어프레임

* home

  ![image](https://user-images.githubusercontent.com/109597814/196083994-59fdf482-3208-4d3c-b308-ae968da8da5d.png)


* 검색 화면

  ![image](https://user-images.githubusercontent.com/109597814/196084019-c098c9f2-7f79-46f7-b9e9-51b16d0020fe.png)


* 검색 결과

  ![image](https://user-images.githubusercontent.com/109597814/196084073-86d70fa0-2c11-4646-958e-82f928d8f5bd.png)


* 결과값이 틀렸을 시 

  ![image](https://user-images.githubusercontent.com/109597814/196084099-80b4c28b-cad8-4619-b48f-bb54b9029635.png)


* 정확도 비교 그래프

  ![image](https://user-images.githubusercontent.com/112169271/196152153-bcac192b-bce3-4535-9bff-e37234ac14a1.png)

***


### ERD
  
![image](https://user-images.githubusercontent.com/112169271/196931377-166efd4d-4549-409c-9373-bec1d3801b1a.png)


***



### 주요 기능 <a href="https://github.com/Taeeun99/sparta_PetDictionary_2L3J_project2/wiki/2.-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C" >(상세보기)</a>

- #### 동물의 종 인식
  - 업로드된 동물 이미지의 종을 판단

사용한 데이터셋 모델 - Oxford pets Dataset

https://universe.roboflow.com/brad-dwyer/oxford-pets



- #### 사용자 평가를 통해 정확도 데이터 축적
  - 찾는 결과가 맞는지 확인
  - 틀린 값일 시, 사용자가 원하는 답을 적어 활용할 수 있게 만들기



<br/>

***


### 트러블 슈팅 <a href="https://github.com/Taeeun99/sparta_PetDictionary_2L3J_project2/wiki/3.-%ED%8A%B8%EB%9F%AC%EB%B8%94-%EC%8A%88%ED%8C%85" >(상세보기)</a>

***


### 시연영상
영상링크 추가 예정


