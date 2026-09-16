# 유틸리티 함수📦
def show_menu(): # 메뉴 출력
    print("\n--- 프롬프트 금고 ---")
    print("1. 프롬프트 추가_C")
    print("2. 프롬프트 목록_R")
    print("3. 프롬프트 수정_U")
    print("4. 프롬프트 삭제_D")
    print("5. 프롬프트 상세 보기")
    print("6. 카테고리별 조회")
    print("7. 프롬프트 검색") 
    print("8. 종료")

def get_non_empty_input(prompt): # 입력값 누락 방지
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("값이 비어 있습니다. 다시 입력해주세요.")

def select_category(): # 카테고리 선택
    preset = ["텍스트 생성", "멀티모달 생성", "기타"]
    while True:
        print("\n--- 카테고리 선택 ---")
        for i, c in enumerate(preset, start=1):
            print(f"{i}. {c}")
        print(f"{len(preset)+1}. 직접 입력")
        choice = input("선택: ").strip()
        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(preset):
                return preset[n-1]
            elif n == len(preset)+1:
                return get_non_empty_input("카테고리 직접 입력: ")
        print("잘못된 선택입니다. 다시 선택해주세요.")

# 기본 데이터📂
def load_default_prompts():
    return [
        {
            "title": "만능 비즈니스 이메일",
            "content": "당신은 전문 비즈니스 커뮤니케이터입니다. 아래 정보를 바탕으로 정중하고 명확한 이메일 초안을 작성해주세요.",
            "category": "텍스트 생성",
            "favorite": True
        },
        {
            "title": "영어 이메일 작성 도우미",
            "content": "당신은 글로벌 기업에서 근무하는 주니어 팀원입니다. 입력하는 한국어 내용을 상황에 맞는 자연스러운 비즈니스 영어 이메일로 번역하고 교정해주세요.",
            "category": "기타",
            "favorite": False
        },
        {
            "title": "블로거 어시스턴트",
            "content": "당신은 최적의 블로그 글을 작성할 수 있도록 돕는 블로그 글 작성 어시스턴트입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
            "category": "텍스트 생성",
            "favorite": False
        }
    ]

# 기능 함수⚙️
def search_prompt(prompts):  # 프롬프트 검색
    keyword = get_non_empty_input("검색할 키워드: ")
    result = [
        p for p in prompts
        if keyword in p.get('title', '') or keyword in p.get('content', '')
    ]

    print(f"\n--- '{keyword}' 검색 결과 ---")
    if not result:
        print("검색 결과가 없습니다.")
        return

    for i, p in enumerate(result, start=1):
        fav = "⭐" if p.get("favorite") else " "
        print(f"{i}. {p.get('category','미정')} | {p.get('title','제목없음')} | {fav}")

def filter_by_category(prompts):  # 카테고리별 조회
    preset = ["텍스트 생성", "멀티모달 생성", "기타"]

    print("\n--- 카테고리 선택 ---")
    for i, c in enumerate(preset, start=1):
        print(f"{i}. {c}")

    try:
        idx = int(input("조회할 카테고리 번호: ")) - 1
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    if not (0 <= idx < len(preset)):
        print("없는 번호입니다.")
        return

    selected = preset[idx]
    result = [p for p in prompts if p['category'] == selected]

    print(f"\n--- [{selected}] 카테고리 목록 ---")
    if not result:
        print("해당 카테고리에 프롬프트가 없습니다.")  
        return

    for i, p in enumerate(result, start=1):
        fav = "⭐" if p.get("favorite") else " "
        print(f"{i}. {p.get('title','제목없음')} | {fav}")

def add_prompt(prompts): # 프롬프트 추가
    title = get_non_empty_input("제목: ")
    content = get_non_empty_input("내용: ")
    category = select_category()
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print(f"'{title}' 프롬프트가 저장되었습니다.")

def show_prompt_list(prompts): # 프롬프트 목록
    print("\n--- 현재 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        fav = "⭐" if p.get("favorite") else " "
        print(f"{i}. {p.get('category','미정')} | {p.get('title','제목없음')} | {fav}")

def show_prompt_detail(prompts): # 프롬프트 상세
    try:
        idx = int(input("상세 보기할 번호: ")) - 1
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    if 0 <= idx < len(prompts):
        p = prompts[idx]
        print("\n--- 프롬프트 상세 보기 ---")
        print(f"제목: {p['title']}")
        print(f"카테고리: {p['category']}")
        print(f"즐겨찾기 여부: {p['favorite']}")
        print(f"내용: {p['content']}")
    else:
        print("없는 번호입니다.")

def update_prompt(prompts): # 프롬프트 수정
    try:
        idx = int(input("수정할 번호: ")) - 1
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    if 0 <= idx < len(prompts):
        prompts[idx]['title'] = input("새 제목: ")
        prompts[idx]['content'] = input("새 내용: ")
        print("수정되었습니다!")
    else:
        print("없는 번호입니다.")

def delete_prompt(prompts): # 프롬프트 삭제 
    try:
        idx = int(input("삭제할 번호: ")) - 1
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    if 0 <= idx < len(prompts):
        deleted = prompts.pop(idx)
        print(f"'{deleted['title']}'이 삭제되었습니다.")
    else:
        print("없는 번호입니다.")


# 메인 실행부🚀
def main():
    prompts = load_default_prompts()

    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1": 
            add_prompt(prompts)

        elif choice == "2": 
            show_prompt_list(prompts)

        elif choice == "3": 
            update_prompt(prompts)

        elif choice == "4": 
            delete_prompt(prompts)
    
        elif choice == "5":
            show_prompt_detail(prompts)

        elif choice == "6":
            filter_by_category(prompts)
            
        elif choice == "7":              
            search_prompt(prompts)    

        elif choice == "8":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴 번호입니다. 1~7 중에서 다시 선택해주세요.")

if __name__ == "__main__":
    main()