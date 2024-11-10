## 이가희

### 역할 분담
이가희 : 리뷰 좋아요 기능, OpenWeatherMap API를 활용한 영화 추천 기능

### 새로 배운 점
AJAX를 활용한 비동기 좋아요 기능을 구현했다.
url작성에 필요한 review_pk를 작성하는 법으로, 각 좋아요 form에 review_pk를 부여 후 , HTML의 review.pk값을 JavaScript에서 참조했다. 문서 상 input hidden 타입으로 존재하는 csrf token데이터를 axios로 전송하는 법도 배웠다.
csrf값을 가진 input 요소를 querySelector를 사용해 직접 선택 후, axios에 작성했다.
또한 API를 활용하는 과정에서 .env파일을 만들어 보안과 유지보수에 용이하게 해야함을 배웠다.

### 어려웠던 점
좋아요 수를 구현하는 과정이 어려웠다.
좋아요 수를 화면에 비동기적으로 구현하는 과정에서 해당 요소를 선택할 수 있도록 span 태그와 id속성을 작성하고,
querySelector를 사용해 각 span태그를 선택했다. 이후 뷰함수에서 수를 연산하고, 응답데이터를 받아왔다.