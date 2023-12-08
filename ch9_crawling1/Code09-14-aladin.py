import bs4
import urllib.request
# 알라딘에서 newbook가져오기

# 함수 선언부

#이미지 하나만 가져오는 fun
def getBookImg(book_tag):
    img_tag = book_tag.find("img")
    img_tag_src = img_tag['src']
    return [img_tag_src]

def getBookText(book_tag):
    title = book_tag.find("a")
    title2 = title.text
    author = book_tag.find("div", {"class": "b-author"})
    author2 = author.text
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong")
    price3 = price2.text
    
 
    return [title2,author2, price3]


# 전역 변수부
# 해당 사이트의 하위 주소 부분 반드시 조사.
bookUrl = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351"

# 메인 코드부
# 가독성
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 태그 의 트리 구조 조사 , 정보 접근하기.
# (.) 점 : 클래스 의미, # : 아이디 의미.
tag = bsObject.find('ul', {'class': 'b-booklist'})

#구조
#일반 이미지 : <div class="b-cover">
#일반 텍스트 : <div class="b-text">
all_books_img = tag.findAll('div',{'class' : 'b-cover'})
all_books_text = tag.findAll('div',{'class' : 'b-text'})

#이미지 주소만 가져오기
for book in all_books_img:
    print(getBookImg(book))

#텍스트 가져오기
for book in all_books_text:
    print(getBookText(book))
