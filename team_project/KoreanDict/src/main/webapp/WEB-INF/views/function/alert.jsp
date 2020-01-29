<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page trimDirectiveWhitespaces="true"%>
<c:if test="${keyword eq null}">
<script>
	alert('검색어는 한글(공백없음)만 가능합니다.');
	location.href='<c:url value="/function/search"/>';
</script>

</c:if>