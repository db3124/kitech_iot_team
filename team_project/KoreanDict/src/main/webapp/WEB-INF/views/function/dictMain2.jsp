<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page trimDirectiveWhitespaces="true"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport"
	content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">

<title>5G</title>

<!-- 기본 CSS 처리 시작 -->
<%@ include file="/WEB-INF/views/include/basic.jsp"%>
<!-- 기본 CSS 처리 끝 -->

<style>
img {
	display: block;
	margin: 0px auto;
}

#submit {
	cursor: pointer;
}

#select {
	cursor: pointer;
}
</style>

<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

<script>
	function submitCheck() {

		if (document.f.q.value == "") {

			alert('표제어 정보 또는 대상 코드를 입력해주세요.');

			return false;

		}

		return true;

	}
</script>

</head>

<body>

	<!-- 해더 시작 -->
	<%@ include file="/WEB-INF/views/include/header.jsp"%>
	<!-- 해더 끝 -->

	<!-- 메인 컨텐트 시작 -->

	<main role="main" class="container my-auto p-3">

		<br> <br>

		<div
			class="p-3 my-3 text-white-50 text-center bg-secondary rounded box-shadow"
			id="nav">

			<div class="lh-100">
				<h3 class="mb-0 text-white lh-100">함께 만들고 모두 누리는 우리말 사전</h3>
			</div>

		</div>

		<div>
			<br> <br> <img
				src="<%=request.getContextPath()%>/images/logo.png"
				class="img-fluid" alt="logo"> <br> <br>

			<div class="my-3 p-3 bg-white rounded box-shadow">
				<form name="f" method="post"
					action="<c:url value="/function/dictContent"/>"
					onsubmit="return submitCheck()">

					<div class="input-group mb-3" id="searchBox">

						<div class="input-group mb-3">
							<div class="input-group-prepend">
								<label class="input-group-text" for="inputGroupSelect01">검색
									방식</label>
							</div>
							<select class="custom-select" id="select" name="method">
								<option value="word_info">표제어 정보(표제어+의미 번호)</option>
								<option value="target_code">대상 코드(target_code)</option>
							</select>
						</div>

						<div class="input-group mb-3">
							<input type="text" name="q" class="form-control text-center"
								placeholder="표제어 정보 예시 : 나무001, 사랑002 / 대상 코드 예시 : 368281, 1353206" 
								aria-label="표제어 정보 예시 : 나무001, 사랑002 / 대상 코드 예시 : 368281, 1353206"
								aria-describedby="button-addon2">
							<div class="input-group-append">
								<button
									class="btn btn-outline-secondary bg-secondary text-white align-center"
									type="submit" id="submit">검색</button>
							</div>
						</div>
						
					</div>

				</form>

			</div>

			<br> <br> <br> <br> <br> <br> <br>
			<br> <br> <br> <br> <br>
		</div>

		<small class="d-block text-right mt-3 border-top border-gray">

			<br> 출처 : <a href="https://opendict.korean.go.kr/main">국립국어원,
				우리말샘</a>

		</small>

	</main>

	<!-- 메인 컨텐트 끝 -->

	<!-- 푸터 시작 -->
	<%@ include file="/WEB-INF/views/include/footer.jsp"%>
	<!-- 푸터 끝 -->

</body>

</html>