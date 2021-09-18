# -*- coding: utf-8 -*-
"""enjson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F0DCy-Xrg-BRM6JphkHvbFrCDZEzAO9W
"""

en = [
      {
          "label": "Special/Metropolitan City",
          "value": "특별/광역시",
          "options": [
              {"label": "Seoul", "value": "서울"}, 
              {"label": "Busan", "value": "부산"}, 
              {"label": "Daegu", "value": "대구"}, 
              {"label": "Incheon", "value": "인천"}, 
              {"label": "Gwangju", "value": "광주"}, 
              {"label": "Daejeon", "value": "대전"}, 
              {"label": "Ulsan", "value": "울산"}, 
              {"label": "Sejong", "value": "세종"}
          ]
      },
      {
          "label": "Gyeonggi Province",
          "value": "경기도",
          "options" : [
              {"label": "Suwon", "value": "경기도 수원"}, 
              {"label": "Seongnam", "value": "경기도 성남"}, 
              {"label": "Uijeongbu", "value": "경기도 의정부"}, 
              {"label": "Anyang", "value": "경기도 안양"}, 
              {"label": "Bucheon", "value": "경기도 부천"}, 
              {"label": "Gwangmyeong", "value": "경기도 광명"}, 
              {"label": "Pyeongtaek", "value": "경기도 평택"}, 
              {"label": "Dongducheon", "value": "경기도 동두천"}, 
              {"label": "Ansan", "value": "경기도 안산"}, 
              {"label": "Goyang", "value": "경기도 고양"}, 
              {"label": "Gwacheon", "value": "경기도 과천"}, 
              {"label": "Guri", "value": "경기도 구리"}, 
              {"label": "Namyangju", "value": "경기도 남양주"}, 
              {"label": "Osan", "value": "경기도 오산"}, 
              {"label": "Siheung", "value": "경기도 시흥"}, 
              {"label": "Gunpo", "value": "경기도 군포"}, 
              {"label": "Uiwang", "value": "경기도 의왕"}, 
              {"label": "Hanam", "value": "경기도 하남"}, 
              {"label": "Yongin", "value": "경기도 용인"}, 
              {"label": "Paju", "value": "경기도 파주"}, 
              {"label": "Icheon", "value": "경기도 이천"}, 
              {"label": "Ansung", "value": "경기도 안성"}, 
              {"label": "Gimpo", "value": "경기도 김포"}, 
              {"label": "Hwaseong", "value": "경기도 화성"}, 
              {"label": "Kwangju", "value": "경기도 광주"}, 
              {"label": "Yangju", "value": "경기도 양주"}, 
              {"label": "Pocheon", "value": "경기도 포천"}, 
              {"label": "Yeoju", "value": "경기도 여주"}, 
              {"label": "Yeoncheon", "value": "경기도 연천"}, 
              {"label": "Gapyeong", "value": "경기도 가평"}, 
              {"label": "Yangpyeong", "value": "경기도 양평"}
              
          ]
      },
      {
          "label": "Gangwon Province",
          "value": "강원도",
          "options": [
              {"label": "Chuncheon", "value": "강원도 춘천"}, 
              {"label": "Wonju", "value": "강원도 원주"}, 
              {"label": "Gangneung", "value": "강원도 강릉"}, 
              {"label": "Donghae", "value": "강원도 동해"}, 
              {"label": "Taebaek", "value": "강원도 태백"}, 
              {"label": "Sokcho", "value": "강원도 속초"}, 
              {"label": "Samcheok", "value": "강원도 삼척"}, 
              {"label": "Hongcheon", "value": "강원도 홍천"}, 
              {"label": "Hoengseong", "value": "강원도 횡성"}, 
              {"label": "Yeongwol", "value": "강원도 영월"}, 
              {"label": "Pyeongchang", "value": "강원도 평창"}, 
              {"label": "Jeongseon", "value": "강원도 정선"}, 
              {"label": "Cheorwon", "value": "강원도 철원"}, 
              {"label": "Hwacheon", "value": "강원도 화천"}, 
              {"label": "Yanggu", "value": "강원도 양구"}, 
              {"label": "Inje", "value": "강원도 인제"}, 
              {"label": "Gosung", "value": "강원도 고성"}, 
              {"label": "Yangyang", "value": "강원도 양양"}
          ]
      },
      {
          "label": "Chungcheongbuk Province (North Chungcheong)",
          "value": "충청북도",
          "options" : [
              {"label": "Cheongju", "value": "충청북도 청주"}, 
              {"label": "Chungju", "value": "충청북도 충주"}, 
              {"label": "Jecheon", "value": "충청북도 제천"}, 
              {"label": "Boeun", "value": "충청북도 보은"}, 
              {"label": "Okcheon", "value": "충청북도 옥천"}, 
              {"label": "Yeongdong", "value": "충청북도 영동"}, 
              {"label": "Jeungpyeong", "value": "충청북도 증평"}, 
              {"label": "Jincheon", "value": "충청북도 진천"}, 
              {"label": "Goesan", "value": "충청북도 괴산"}, 
              {"label": "Eumseong", "value": "충청북도 음성"}, 
              {"label": "Danyang", "value": "충청북도 단양"}
          ]
      },
      {
          "label": "Chungcheongnam Province (South Chungcheong)",
          "value": "충청남도",
          "options" : [
              {"label": "Dangjin", "value": "충청남도 당진"}, 
              {"label": "Cheonan", "value": "충청남도 천안"}, 
              {"label": "Gongju", "value": "충청남도 공주"}, 
              {"label": "Boryeong", "value": "충청남도 보령"}, 
              {"label": "Asan", "value": "충청남도 아산"}, 
              {"label": "Seosan", "value": "충청남도 서산"}, 
              {"label": "Nonsan", "value": "충청남도 논산"}, 
              {"label": "Gyeryong", "value": "충청남도 계룡"}, 
              {"label": "Geumsan", "value": "충청남도 금산"}, 
              {"label": "Buyeo", "value": "충청남도 부여"}, 
              {"label": "Seocheon", "value": "충청남도 서천"}, 
              {"label": "Cheongyang", "value": "충청남도 청양"}, 
              {"label": "Hongseong", "value": "충청남도 홍성"}, 
              {"label": "Yesan", "value": "충청남도 예산"}, 
              {"label": "Taean", "value": "충청남도 태안"}
          ]
  
      },
      {
          "label": "Jeollanam Province (South Jeolla)",
          "value": "전라남도",
          "options" : [
              {"label": "Mokpo", "value": "전라남도 목포"}, 
              {"label": "Yeosu", "value": "전라남도 여수"}, 
              {"label": "Suncheon", "value": "전라남도 순천"}, 
              {"label": "Naju", "value": "전라남도 나주"}, 
              {"label": "Gwangyang", "value": "전라남도 광양"}, 
              {"label": "Damyang", "value": "전라남도 담양"}, 
              {"label": "Gokseong", "value": "전라남도 곡성"}, 
              {"label": "Gurye", "value": "전라남도 구례"}, 
              {"label": "Goheung", "value": "전라남도 고흥"}, 
              {"label": "Bosung", "value": "전라남도 보성"}, 
              {"label": "Hwasun", "value": "전라남도 화순"}, 
              {"label": "Jangheung", "value": "전라남도 장흥"}, 
              {"label": "Gangjin", "value": "전라남도 강진"}, 
              {"label": "Haenam", "value": "전라남도 해남"}, 
              {"label": "Yeongam", "value": "전라남도 영암"}, 
              {"label": "Muan", "value": "전라남도 무안"}, 
              {"label": "Hampyeong", "value": "전라남도 함평"}, 
              {"label": "Yeonggwang", "value": "전라남도 영광"}, 
              {"label": "Jangseong", "value": "전라남도 장성"}, 
              {"label": "Wando", "value": "전라남도 완도"}, 
              {"label": "Jindo", "value": "전라남도 진도"}, 
              {"label": "Sinan", "value": "전라남도 신안"}
          ]
  
      },
      {
          "label": "Jeollabuk Province (North Jeolla)",
          "value": "전라북도",
          "options": [
              {"label": "Jeonju", "value": "전라북도 전주"}, 
              {"label": "Gunsan", "value": "전라북도 군산"}, 
              {"label": "Iksan", "value": "전라북도 익산"}, 
              {"label": "Jeongeup", "value": "전라북도 정읍"}, 
              {"label": "Namwon", "value": "전라북도 남원"}, 
              {"label": "Gimje", "value": "전라북도 김제"}, 
              {"label": "Wanju", "value": "전라북도 완주"}, 
              {"label": "Jinan", "value": "전라북도 진안"}, 
              {"label": "Muju", "value": "전라북도 무주"}, 
              {"label": "Jangsu", "value": "전라북도 장수"}, 
              {"label": "Imsil", "value": "전라북도 임실"}, 
              {"label": "Sunchang", "value": "전라북도 순창"}, 
              {"label": "Gochang", "value": "전라북도 고창"}, 
              {"label": "Buan", "value": "전라북도 부안"}
          ]
      },
      {
          "label": "Gyeongsangbuk Province (North Gyeongsang)",
          "value": "경상북도",
          "options": [
              {"label": "Pohang", "value": "경상북도 포항"}, 
              {"label": "Gyeongju", "value": "경상북도 경주"}, 
              {"label": "Gimcheon", "value": "경상북도 김천"}, 
              {"label": "Andong", "value": "경상북도 안동"}, 
              {"label": "Gumi", "value": "경상북도 구미"}, 
              {"label": "Yeongju", "value": "경상북도 영주"}, 
              {"label": "Yeongcheon", "value": "경상북도 영천"}, 
              {"label": "Sangju", "value": "경상북도 상주"}, 
              {"label": "Mungyeong", "value": "경상북도 문경"}, 
              {"label": "Gyeongsan", "value": "경상북도 경산"}, 
              {"label": "Gunwi", "value": "경상북도 군위"}, 
              {"label": "Uiseong", "value": "경상북도 의성"}, 
              {"label": "Cheongsong", "value": "경상북도 청송"}, 
              {"label": "Yeongyang", "value": "경상북도 영양"}, 
              {"label": "Yeongdeok", "value": "경상북도 영덕"}, 
              {"label": "Cheongdo", "value": "경상북도 청도"}, 
              {"label": "Goryeong", "value": "경상북도 고령"}, 
              {"label": "Seongju", "value": "경상북도 성주"}, 
              {"label": "Chilgok", "value": "경상북도 칠곡"}, 
              {"label": "Yecheon", "value": "경상북도 예천"}, 
              {"label": "Bonghwa", "value": "경상북도 봉화"}, 
              {"label": "Uljin", "value": "경상북도 울진"}, 
              {"label": "Ulleong", "value": "경상북도 울릉"}
          ]
      },
      {
          "label": "Gyeongsangnam Province (South Gyeongsang)",
          "value": "경상남도",
          "options": [
              {"label": "Changwon", "value": "경상남도 창원"}, 
              {"label": "Jinju", "value": "경상남도 진주"}, 
              {"label": "Tongyeong", "value": "경상남도 통영"}, 
              {"label": "Sacheon", "value": "경상남도 사천"}, 
              {"label": "Gimhae", "value": "경상남도 김해"}, 
              {"label": "Milyang", "value": "경상남도 밀양"}, 
              {"label": "Geoje", "value": "경상남도 거제"}, 
              {"label": "Yangsan", "value": "경상남도 양산"}, 
              {"label": "Uiryeong", "value": "경상남도 의령"}, 
              {"label": "Haman", "value": "경상남도 함안"}, 
              {"label": "Changnyeong", "value": "경상남도 창녕"}, 
              {"label": "Gosung", "value": "경상남도 고성"}, 
              {"label": "Namhae", "value": "경상남도 남해"}, 
              {"label": "Hadong", "value": "경상남도 하동"}, 
              {"label": "Sancheong", "value": "경상남도 산청"}, 
              {"label": "Hamyang", "value": "경상남도 함양"}, 
              {"label": "Geochang", "value": "경상남도 거창"}, 
              {"label": "Hapcheon", "value": "경상남도 합천"}, 
              {"label": "Masan", "value": "경상남도 마산"}, 
              {"label": "Jinhae", "value": "경상남도 진해"}
          ]
      },
      {
          "label": "Jeju Province",
          "value": "제주도",
          "options": [
              {"label": "Jeju", "value": "제주도 제주"}, 
              {"label": "Seogwipo", "value": "제주도 서귀포"}
          ]
      }
  ]


ko = [
    {
        "label": "특별/광역시",
        "value": "특별/광역시",
        "options": [
            {"label": "서울", "value": "서울"}, 
            {"label": "부산", "value": "부산"}, 
            {"label": "대구", "value": "대구"}, 
            {"label": "인천", "value": "인천"}, 
            {"label": "광주", "value": "광주"}, 
            {"label": "대전", "value": "대전"}, 
            {"label": "울산", "value": "울산"}, 
            {"label": "세종", "value": "세종"}
        ]
    },
    {
        "label": "경기도",
        "value": "경기도",
        "options" : [
            {"label": "수원", "value": "경기도 수원"}, 
            {"label": "성남", "value": "경기도 성남"}, 
            {"label": "의정부", "value": "경기도 의정부"}, 
            {"label": "안양", "value": "경기도 안양"}, 
            {"label": "부천", "value": "경기도 부천"}, 
            {"label": "광명", "value": "경기도 광명"}, 
            {"label": "평택", "value": "경기도 평택"}, 
            {"label": "동두천", "value": "경기도 동두천"}, 
            {"label": "안산", "value": "경기도 안산"}, 
            {"label": "고양", "value": "경기도 고양"}, 
            {"label": "과천", "value": "경기도 과천"}, 
            {"label": "구리", "value": "경기도 구리"}, 
            {"label": "남양주", "value": "경기도 남양주"}, 
            {"label": "오산", "value": "경기도 오산"}, 
            {"label": "시흥", "value": "경기도 시흥"}, 
            {"label": "군포", "value": "경기도 군포"}, 
            {"label": "의왕", "value": "경기도 의왕"}, 
            {"label": "하남", "value": "경기도 하남"}, 
            {"label": "용인", "value": "경기도 용인"}, 
            {"label": "파주", "value": "경기도 파주"}, 
            {"label": "이천", "value": "경기도 이천"}, 
            {"label": "안성", "value": "경기도 안성"}, 
            {"label": "김포", "value": "경기도 김포"}, 
            {"label": "화성", "value": "경기도 화성"}, 
            {"label": "광주", "value": "경기도 광주"}, 
            {"label": "양주", "value": "경기도 양주"}, 
            {"label": "포천", "value": "경기도 포천"}, 
            {"label": "여주", "value": "경기도 여주"}, 
            {"label": "연천", "value": "경기도 연천"}, 
            {"label": "가평", "value": "경기도 가평"}, 
            {"label": "양평", "value": "경기도 양평"}
            
        ]
    },
    {
        "label": "강원도",
        "value": "강원도",
        "options": [
            {"label": "춘천", "value": "강원도 춘천"}, 
            {"label": "원주", "value": "강원도 원주"}, 
            {"label": "강릉", "value": "강원도 강릉"}, 
            {"label": "동해", "value": "강원도 동해"}, 
            {"label": "태백", "value": "강원도 태백"}, 
            {"label": "속초", "value": "강원도 속초"}, 
            {"label": "삼척", "value": "강원도 삼척"}, 
            {"label": "홍천", "value": "강원도 홍천"}, 
            {"label": "횡성", "value": "강원도 횡성"}, 
            {"label": "영월", "value": "강원도 영월"}, 
            {"label": "평창", "value": "강원도 평창"}, 
            {"label": "정선", "value": "강원도 정선"}, 
            {"label": "철원", "value": "강원도 철원"}, 
            {"label": "화천", "value": "강원도 화천"}, 
            {"label": "양구", "value": "강원도 양구"}, 
            {"label": "인제", "value": "강원도 인제"}, 
            {"label": "고성", "value": "강원도 고성"}, 
            {"label": "양양", "value": "강원도 양양"}
        ]
    },
    {
        "label": "충청북도",
        "value": "충청북도",
        "options" : [
            {"label": "청주", "value": "충청북도 청주"}, 
            {"label": "충주", "value": "충청북도 충주"}, 
            {"label": "제천", "value": "충청북도 제천"}, 
            {"label": "보은", "value": "충청북도 보은"}, 
            {"label": "옥천", "value": "충청북도 옥천"}, 
            {"label": "영동", "value": "충청북도 영동"}, 
            {"label": "증평", "value": "충청북도 증평"}, 
            {"label": "진천", "value": "충청북도 진천"}, 
            {"label": "괴산", "value": "충청북도 괴산"}, 
            {"label": "음성", "value": "충청북도 음성"}, 
            {"label": "단양", "value": "충청북도 단양"}
        ]
    },
    {
        "label": "충청남도",
        "value": "충청남도",
        "options" : [
            {"label": "당진", "value": "충청남도 당진"}, 
            {"label": "천안", "value": "충청남도 천안"}, 
            {"label": "공주", "value": "충청남도 공주"}, 
            {"label": "보령", "value": "충청남도 보령"}, 
            {"label": "아산", "value": "충청남도 아산"}, 
            {"label": "서산", "value": "충청남도 서산"}, 
            {"label": "논산", "value": "충청남도 논산"}, 
            {"label": "계룡", "value": "충청남도 계룡"}, 
            {"label": "금산", "value": "충청남도 금산"}, 
            {"label": "부여", "value": "충청남도 부여"}, 
            {"label": "서천", "value": "충청남도 서천"}, 
            {"label": "청양", "value": "충청남도 청양"}, 
            {"label": "홍성", "value": "충청남도 홍성"}, 
            {"label": "예산", "value": "충청남도 예산"}, 
            {"label": "태안", "value": "충청남도 태안"}
        ]

    },
    {
        "label": "전라남도",
        "value": "전라남도",
        "options" : [
            {"label": "목포", "value": "전라남도 목포"}, 
            {"label": "여수", "value": "전라남도 여수"}, 
            {"label": "순천", "value": "전라남도 순천"}, 
            {"label": "나주", "value": "전라남도 나주"}, 
            {"label": "광양", "value": "전라남도 광양"}, 
            {"label": "담양", "value": "전라남도 담양"}, 
            {"label": "곡성", "value": "전라남도 곡성"}, 
            {"label": "구례", "value": "전라남도 구례"}, 
            {"label": "고흥", "value": "전라남도 고흥"}, 
            {"label": "보성", "value": "전라남도 보성"}, 
            {"label": "화순", "value": "전라남도 화순"}, 
            {"label": "장흥", "value": "전라남도 장흥"}, 
            {"label": "강진", "value": "전라남도 강진"}, 
            {"label": "해남", "value": "전라남도 해남"}, 
            {"label": "영암", "value": "전라남도 영암"}, 
            {"label": "무안", "value": "전라남도 무안"}, 
            {"label": "함평", "value": "전라남도 함평"}, 
            {"label": "영광", "value": "전라남도 영광"}, 
            {"label": "장성", "value": "전라남도 장성"}, 
            {"label": "완도", "value": "전라남도 완도"}, 
            {"label": "진도", "value": "전라남도 진도"}, 
            {"label": "신안", "value": "전라남도 신안"}
        ]

    },
    {
        "label": "전라북도",
        "value": "전라북도",
        "options": [
            {"label": "전주", "value": "전라북도 전주"}, 
            {"label": "군산", "value": "전라북도 군산"}, 
            {"label": "익산", "value": "전라북도 익산"}, 
            {"label": "정읍", "value": "전라북도 정읍"}, 
            {"label": "남원", "value": "전라북도 남원"}, 
            {"label": "김제", "value": "전라북도 김제"}, 
            {"label": "완주", "value": "전라북도 완주"}, 
            {"label": "진안", "value": "전라북도 진안"}, 
            {"label": "무주", "value": "전라북도 무주"}, 
            {"label": "장수", "value": "전라북도 장수"}, 
            {"label": "임실", "value": "전라북도 임실"}, 
            {"label": "순창", "value": "전라북도 순창"}, 
            {"label": "고창", "value": "전라북도 고창"}, 
            {"label": "부안", "value": "전라북도 부안"}
        ]
    },
    {
        "label": "경상북도",
        "value": "경상북도",
        "options": [
            {"label": "포항", "value": "경상북도 포항"}, 
            {"label": "경주", "value": "경상북도 경주"}, 
            {"label": "김천", "value": "경상북도 김천"}, 
            {"label": "안동", "value": "경상북도 안동"}, 
            {"label": "구미", "value": "경상북도 구미"}, 
            {"label": "영주", "value": "경상북도 영주"}, 
            {"label": "영천", "value": "경상북도 영천"}, 
            {"label": "상주", "value": "경상북도 상주"}, 
            {"label": "문경", "value": "경상북도 문경"}, 
            {"label": "경산", "value": "경상북도 경산"}, 
            {"label": "군위", "value": "경상북도 군위"}, 
            {"label": "의성", "value": "경상북도 의성"}, 
            {"label": "청송", "value": "경상북도 청송"}, 
            {"label": "영양", "value": "경상북도 영양"}, 
            {"label": "영덕", "value": "경상북도 영덕"}, 
            {"label": "청도", "value": "경상북도 청도"}, 
            {"label": "고령", "value": "경상북도 고령"}, 
            {"label": "성주", "value": "경상북도 성주"}, 
            {"label": "칠곡", "value": "경상북도 칠곡"}, 
            {"label": "예천", "value": "경상북도 예천"}, 
            {"label": "봉화", "value": "경상북도 봉화"}, 
            {"label": "울진", "value": "경상북도 울진"}, 
            {"label": "울릉", "value": "경상북도 울릉"}
        ]
    },
    {
        "label": "경상남도",
        "value": "경상남도",
        "options": [
            {"label": "창원", "value": "경상남도 창원"}, 
            {"label": "진주", "value": "경상남도 진주"}, 
            {"label": "통영", "value": "경상남도 통영"}, 
            {"label": "사천", "value": "경상남도 사천"}, 
            {"label": "김해", "value": "경상남도 김해"}, 
            {"label": "밀양", "value": "경상남도 밀양"}, 
            {"label": "거제", "value": "경상남도 거제"}, 
            {"label": "양산", "value": "경상남도 양산"}, 
            {"label": "의령", "value": "경상남도 의령"}, 
            {"label": "함안", "value": "경상남도 함안"}, 
            {"label": "창녕", "value": "경상남도 창녕"}, 
            {"label": "고성", "value": "경상남도 고성"}, 
            {"label": "남해", "value": "경상남도 남해"}, 
            {"label": "하동", "value": "경상남도 하동"}, 
            {"label": "산청", "value": "경상남도 산청"}, 
            {"label": "함양", "value": "경상남도 함양"}, 
            {"label": "거창", "value": "경상남도 거창"}, 
            {"label": "합천", "value": "경상남도 합천"}, 
            {"label": "마산", "value": "경상남도 마산"}, 
            {"label": "진해", "value": "경상남도 진해"}
        ]
    },
    {
        "label": "제주도",
        "value": "제주도",
        "options": [
            {"label": "제주", "value": "제주도 제주"}, 
            {"label": "서귀포", "value": "제주도 서귀포"}
        ]
    }
]

en_ko_format = "\"{}\": \"{}\","

english_list = []
korean_list = []

for sido_object, sido_object_ko in zip(en[1:], ko[1:]):
  sido_en = sido_object["label"]
  sido_en_cleaned = sido_en.split(" ")[0] + " " + sido_en.split(" ")[1]
  # print("")
  sgg_object_list = sido_object["options"]
  for sgg_object in sgg_object_list:
    sgg_en = sgg_object["label"]
    english = sgg_en + ", " + sido_en_cleaned
    english_list.append(english)
    # print(english)

  ko_object_list = sido_object_ko["options"]
  for sgg_object_ko in ko_object_list:
    korean = sgg_object_ko["value"]
    korean_list.append(korean)
    # print(korean)

for english, korean in zip(english_list, korean_list):
  print(en_ko_format.format(english, korean))
