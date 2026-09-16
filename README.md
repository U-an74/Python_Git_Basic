# Python & Git 기초: 파이썬 콘솔 프로그램 개발

## ☑️ 과제 목표
- 아이디어 코드화 및 버전 관리 실습
- 동작하는 프롬프트 관리 프로그램 완성

<br>

## ☑️ 프로그램 설명

### 1. 개요
- 프로그램명: 프롬프트 금고 (prompt-vault) 
- 터미널에서 메뉴 번호를 입력해 기능을 선택하는 콘솔 기반 python 도구
- 자주 쓰는 AI 프롬프트를 저장하고 관리하는 프로그램입니다.

### 2. 기능 목록
- CRUD
1. 프롬프트 추가 (Create)
2. 프롬프트 목록 (Read) 
3. 프롬프트 수정 (Update)
4. 프롬프트 삭제 (Delete)
- Detail
5. 프롬프트 상세 보기
6. 카테고리별 조회
7. 프롬프트 검색
8. 즐겨찾기 추가/해제
9. 즐겨찾기 목록
10. 종료
- Git을 이용한 버전 관리

### 3. 실행 방법
- Python 설치(3.14.7버전 권장)
- 저장소 클론: `git clone https://github.com/본인계정/prompt-vault.git`
- 실행: `python main.py`

### 4. 카테고리 종류
1. 텍스트 생성: 텍스트 기반 문서 생성 프롬프트
2. 멀티모달 생성: 이미지/동영상 등 콘텐츠 생성 프롬프트
3. 기타: 위 카테고리에 속하지 않는 프롬프트 일체

<br>

## ☑️ 참고

### 🏗️ 최종 코드 함수 구조도

```
prompt-vault/
│
├── 📦 유틸리티 함수
│   ├── show_menu()             # 메뉴 출력
│   ├── get_non_empty_input()   # 입력값 누락 방지
│   └── select_category()       # 카테고리 선택
│
├── 📂 기본 데이터
│   └── load_default_prompts()  # 샘플 데이터 로드
│
├── ⚙️ 기능 함수
│   ├── toggle_favorite()       # 즐겨찾기 추가/해제
│   ├── show_favorites()        # 즐겨찾기 목록
│   ├── search_prompt()         # 프롬프트 검색
│   ├── filter_by_category()    # 카테고리별 조회
│   ├── add_prompt()            # 프롬프트 추가
│   ├── show_prompt_list()      # 프롬프트 목록
│   ├── show_prompt_detail()    # 프롬프트 상세 보기
│   ├── update_prompt()         # 프롬프트 수정
│   └── delete_prompt()         # 프롬프트 삭제
│
└── 🚀 메인 실행부
    └── main()                  # 프로그램 진입점
```
  ### 💻 git --oneline --graph 결과 화면
  <img width="927" height="258" alt="git log --oneline --graph 결과 화면" src="https://github.com/user-attachments/assets/3feb3f4b-ac75-4156-a5b4-db373a62cf80" />
