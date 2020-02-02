<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">

	<a class="navbar-brand mr-auto mr-lg-0" href="<c:url value="/"/>">5G</a>


	<button class="navbar-toggler p-0 border-0" type="button"
		data-toggle="offcanvas">
		<span class="navbar-toggler-icon"></span>
	</button>

	<div class="navbar-collapse offcanvas-collapse"
		id="navbarsExampleDefault">
		<ul class="navbar-nav mr-auto">

				
			<li class="nav-item dropdown"><a
					class="nav-link dropdown-toggle" href="https://example.com"
					id="dropdown01" data-toggle="dropdown" aria-haspopup="true"
					aria-expanded="false">국어사전</a>
					<div class="dropdown-menu" aria-labelledby="dropdown01">
						<a class="dropdown-item" href="<c:url value="/function/dictMain"/>">사전 검색</a> 
						<a class="dropdown-item" href="<c:url value="/function/dictMain2"/>">사전 내용</a>
					</div>
				</li>	

		</ul>

	</div>
</nav>


