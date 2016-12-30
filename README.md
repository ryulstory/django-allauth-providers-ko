
## django-allauth-providers-ko

django-allauth 에 대한 추가 Providers

 * kakao
 * naver

작성자 : AskDjango - http://facebook.com/groups/askdjango , [me@nomade.kr](mailto:me@nomade.kr)

### 연동

[django-allauth installation](https://django-allauth.readthedocs.io/en/latest/installation.html) 공식문서를 참고하여, 먼저 django-allauth 세팅을 합니다. 추천 설정으로 진행하시는 것이 삽질을 줄일 수 있습니다.

현 장고 프로젝트 settings 내 INSTALLED_APP 에 naver provider 추가

 ```python
 INSTALLED_APPS = [
     'askdjango_providers.kakao',
     'askdjango_providers.naver',
 ]
 ```

#### kakao

 * [Kakao Developers / 내 애플리케이션](https://developers.kakao.com/apps) 에서 새 애플리케이션 생성
 * 참고 : Kakao OAuth 인증에서는 Secret Key 를 사용하지 않습니다.
 * 일반 탭
     * 웹 플랫폼을 추가하고, 사이트 도메인에 사용할 모든 도메인을 명시 ( ex - http://localhost:8000 http://127.0.0.1:8000 )
         - 참고 : http://localhost:8000 주소와 http://127.0.0.1:8000 은 OAuth Provider 입장에서는 서로 다른 주소입니다. https 와 http 도 마찬가지입니다.
     * Redirect Path : */accounts/kakao/login/callback/* 기입
 * 사용자 관리 탭
     * 사용자 관리 옵션을 켬.
     * 개인정보 관리항목의 수집목적 기입
 * 일반 탭
     * REST API 키를 복사
 * 장고 Admin 페이지를 열어 Social Accounts / Social Applications 에서 새 Social Application 생성
     * provider : Kakao 선택
     * name : 원하시는 이름 입력
     * client id : 개요 탭에서 복사한 REST API 키 붙여넣기
     * secret key : kakao oauth 인증에서는 사용되지 않는 값인데 social account에서는 필수값이므로, 더미값으로서 none 을 입력해주세요.
     * sites : example.com 사이트를 선택 (오른쪽으로 이동)
     * 저장

#### naver

 * [NAVER Developers :: 내 애플리케이션](https://developers.naver.com/appinfo) 에서 새 애플리케이션 생성
 * 설정 탭
     * "로그인 오픈 API" 활성화
     * 이용목적 : "로그인 오픈 API (네이버 아이디로 로그인)" 체크
     * 로그인 오픈 API 서비스 환경 : "웹" 체크
        * PC웹
            * 서비스 URL 기입 (ex - http://localhost:8000 )
            * 네이버 아이디로 로그인 Callback URL 기입 (ex - http://localhost:8000/accounts/naver/login/callback/ )
     * 애플리케이션 개발 상태 : 릴리즈 시에 '서비스 적용" 체크
        * 미기입시 로그인 아이디 제한 및 개발자 아이디만 로그인 가능
 * 개요 탭
     * Client ID 와 Client Secret 키를 복사
 * 장고 Admin 페이지를 열어 Social Accounts / Social Applications 에서 새 Social Application 생성
     * provider : Naver 선택
     * name : 원하시는 이름 입력
     * client id : 개요 탭에서 복사한 Client ID 붙여넣기
     * secret key : 개요 탭에서 복사한 Client Secret 붙여넣기
     * sites : example.com 사이트를 선택 (오른쪽으로 이동)
     * 저장


### 로그인 템플릿에 로그인 링크 추가

```html
{% load socialaccount %}

<a href="{% provider_login_url "kakao" %}">카카오 로그인</a>
<a href="{% provider_login_url "naver" %}">네이버 로그인</a>
```

장고 서버를 통해 위 링크를 클릭하시면, kakao/naver 로그인을 하실 수 있습니다.

감사합니다. :-)
