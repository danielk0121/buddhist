# 파비콘 이미지 생성

## 개요

`favicon/` 폴더를 신규 구성하여 SVG 기반 파비콘 이미지를 생성한다.
노드(Node.js)와 Sharp 라이브러리를 사용한다.

---

## 결과물 사양

- 검은 배경, 흰색 'B' 글자
- 출력 포맷: `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`, `favicon-192x192.png`, `favicon-512x512.png`
- 소스: `favicon.svg`

---

## 작업 목록

- [x] `favicon/` 폴더 생성
- [x] `favicon/favicon.svg` — SVG 소스 파일 작성
- [x] `favicon/package.json` — Sharp 의존성 정의
- [x] `favicon/generate.js` — 이미지 생성 스크립트 작성
- [x] `npm install` 실행
- [x] `node generate.js` 실행 → 결과물 생성
- [x] 커밋 푸시
