# Git 프로젝트 설정 가이드

## 1. Git Flow 브랜치 전략 설정

### 1.1 기본 브랜치 생성
```bash
# develop 브랜치 생성 및 원격 저장소에 푸시
git checkout -b develop
git push -u origin develop
```

### 1.2 브랜치 전략
- `main`: 프로덕션 배포용 브랜치
- `develop`: 개발용 메인 브랜치
- `feature/*`: 새로운 기능 개발 (예: `feature/user-auth`)
- `hotfix/*`: 긴급 버그 수정 (예: `hotfix/login-error`)
- `release/*`: 릴리스 준비 (예: `release/v1.0.0`)

## 2. 커밋 메시지 컨벤션 설정

### 2.1 필요한 패키지 설치
```bash
# package.json 초기화
npm init -y

# commitlint와 husky 설치
npm install --save-dev @commitlint/cli @commitlint/config-conventional husky
```

### 2.2 commitlint.config.js 생성
```javascript
// commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',    // 새로운 기능
        'fix',     // 버그 수정
        'docs',    // 문서 수정
        'style',   // 코드 포맷팅
        'refactor',// 코드 리팩토링
        'test',    // 테스트 코드
        'chore',   // 빌드 업무 수정
        'ci',      // CI 설정 파일 수정
        'perf',    // 성능 개선
        'build',   // 빌드 시스템 수정
        'revert'   // 이전 커밋으로 되돌림
      ]
    ],
    'type-case': [2, 'always', 'lower-case'],
    'type-empty': [2, 'never'],
    'scope-empty': [2, 'never'],
    'scope-case': [2, 'always', 'lower-case'],
    'subject-empty': [2, 'never'],
    'subject-case': [2, 'always', 'lower-case'],
    'subject-full-stop': [2, 'never', '.'],
    'header-max-length': [2, 'always', 72]
  }
};
```

### 2.3 package.json 수정
```json
{
  "scripts": {
    "prepare": "husky install"
  },
  "devDependencies": {
    "@commitlint/cli": "^19.2.1",
    "@commitlint/config-conventional": "^19.1.0",
    "husky": "^9.0.11"
  }
}
```

### 2.4 커밋 메시지 템플릿 생성
```bash
# .gitmessage 파일 생성
touch .gitmessage
```

```text
# .gitmessage
# <type>(<scope>): <subject>
#
# <body>
#
# <footer>
#
# Types:
#   feat:     새로운 기능
#   fix:      버그 수정
#   docs:     문서 수정
#   style:    코드 포맷팅
#   refactor: 코드 리팩토링
#   test:     테스트 코드
#   chore:    빌드 업무 수정
#   ci:       CI 설정 파일 수정
#   perf:     성능 개선
#   build:    빌드 시스템 수정
#   revert:   이전 커밋으로 되돌림
#
# Scopes:
#   api:      API 관련
#   auth:     인증 관련
#   db:       데이터베이스 관련
#   ui:       UI 관련
#   test:     테스트 관련
#   docs:     문서 관련
#
# Example:
#   feat(auth): JWT 토큰 기반 인증 구현
#
#   - JWT 토큰 발급 로직 추가
#   - 로그인/회원가입 API 구현
#
#   Resolves: #123
```

### 2.5 Git 설정
```bash
# 커밋 메시지 템플릿 설정
git config --local commit.template .gitmessage

# husky 초기화 및 커밋 메시지 검증 설정
npx husky install
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit $1'
```

## 3. 사용 방법

### 3.1 새로운 기능 개발
```bash
# develop 브랜치에서 시작
git checkout develop
git pull origin develop

# feature 브랜치 생성
git checkout -b feature/new-feature

# 작업 후 커밋
git add .
git commit  # 템플릿이 자동으로 열림
```

### 3.2 커밋 메시지 작성 예시
```
feat(auth): JWT 토큰 기반 인증 구현

- JWT 토큰 발급 로직 추가
- 로그인/회원가입 API 구현

Resolves: #123
```

### 3.3 브랜치 전략 사용 예시

1. **기능 개발**
```bash
git checkout develop
git checkout -b feature/user-auth
# 개발 작업
git commit -m "feat(auth): 사용자 인증 기능 구현"
git push origin feature/user-auth
```

2. **버그 수정**
```bash
git checkout main
git checkout -b hotfix/login-error
# 버그 수정
git commit -m "fix(auth): 로그인 시 토큰 만료 오류 수정"
git push origin hotfix/login-error
```

3. **릴리스 준비**
```bash
git checkout develop
git checkout -b release/v1.0.0
# 릴리스 준비 작업
git commit -m "chore(release): v1.0.0 릴리스 준비"
git push origin release/v1.0.0
```

## 4. GitHub 저장소 설정

### 4.1 브랜치 보호 규칙
1. `main` 브랜치:
   - 직접 푸시 금지
   - Pull Request 필수
   - 코드 리뷰 승인 필수
   - CI 테스트 통과 필수

2. `develop` 브랜치:
   - 직접 푸시 금지
   - Pull Request 필수
   - 코드 리뷰 승인 필수

### 4.2 Pull Request 템플릿
```markdown
## 변경사항
- 

## 관련 이슈
- 

## 테스트 방법
- 

## 스크린샷 (선택사항)
- 

## 체크리스트
- [ ] 테스트 코드를 작성했나요?
- [ ] 문서를 업데이트했나요?
- [ ] 코드 리뷰어를 지정했나요?
``` 