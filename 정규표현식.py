import re

def extract_emails(text):
    # 이메일 주소를 찾기 위한 정규 표현식
    email_pattern = r'\b[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[A-Za-z]{2,}\b'
    
    # 정규 표현식을 사용하여 이메일 주소를 추출
    emails = re.findall(email_pattern, text)
    
    return emails

if __name__ == '__main__':
    input_text = input("텍스트를 입력하세요: ")
    
    email_list = extract_emails(input_text)
    
    if email_list:
        print("추출된 이메일 주소:")
        for email in email_list:
            print(email)
    else:
        print("이메일 주소가 발견되지 않았습니다.")
