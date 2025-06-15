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