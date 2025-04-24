-- =============================================
-- KOPO_PRODUCT_VOLUME_YIS 테이블 생성
-- =============================================
CREATE TABLE KOPO_PRODUCT_VOLUME_YIS
(
	REGIONID 		VARCHAR(20),
	PRODUCTGROUP 	VARCHAR(20),
	YEARWEEK 		VARCHAR(6),
	VOLUME 			DOUBLE
);

-- =============================================
-- KOPO_PRODUCT_VOLUME_YIS 테이블 조회
-- =============================================
SELECT * 
FROM KOPO_PRODUCT_VOLUME_YIS;

-- =============================================
-- 현재 데이터베이스의 모든 테이블 목록 조회
-- =============================================
SHOW TABLES;

CREATE TABLE HKCODE_KOPO
(
	REGIONID VARCHAR(20),
	QTY DOUBLE
);


SELECT *
FROM HKCODE_KOPO;


-- =============================================
-- KOPO_HKCODE_YIS 데이터베이스 생성
-- =============================================
CREATE DATABASE KOPO_HKCODE_YIS;

-- =============================================
-- 사용자 계정 생성
-- hkcodeuser: 계정 이름
-- kopo: 비밀번호
-- %: 모든 호스트에서 접근 가능
-- =============================================
CREATE USER hkcodeuser@'%' IDENTIFIED BY 'kopo';
			계정 이름			비밀번호
			%는 원격할때 꼭 써줘야한다.
			

-- =============================================
-- 사용자 권한 부여
-- 모든 데이터베이스에 대한 모든 권한 부여
-- =============================================
GRANT ALL PRIVILEGES
ON *.* TO hkcodeuser@'%';

-- 특정 데이터베이스(kopo)에 대한 모든 권한 부여
-- GRANT ALL PRIVILEGES
-- ON kopo.* TO hkcodeuser@'%';



# 테이블 생성
CREATE TABLE KOPO_PRODUCT_VOLUME_YIS
(
	REGIONID		VARCHAR(20),
	PRODUCTGROUP	VARCHAR(20),
	YEARWEEK 		VARCHAR(6),
	VOLUME 			DOUBLE
);



오라클 
SELECT * FROM TABS;
MariaDB/MySQL 
SHOW TABLES



# 데이터 입력 (전체 컬럼)
INSERT INTO KOPO_PRODUCT_VOLUME_YIS
VALUES('서울', '한국은행', '202401', 1000);




# 데이터 입력 (특정 컬럼)
INSERT INTO KOPO_PRODUCT_VOLUME_YIS
(REGIONID, PRODUCTGROUP, YEARWEEK)
VALUES('서울', '한국은행', '202402');


# 데이터 수정 (조건)
UPDATE KOPO_PRODUCT_VOLUME_YIS
SET VOLUME = 1500
WHERE YEARWEEK = '202402'
AND PRODUCTGROUP = '한국은행';


# 데이터 수정 (조건)
DELETE FROM KOPO_PRODUCT_VOLUME_YIS
WHERE YEARWEEK = '202402';


SELECT * FROM KOPO (X)

SELECT *
FROM KOPO (O)

UPDATE
SET
WHERE (O)

DELETE
WHERE (O)

