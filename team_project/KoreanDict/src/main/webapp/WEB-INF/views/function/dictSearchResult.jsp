<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page trimDirectiveWhitespaces="True"%>

<!DOCTYPE html>
<html>

<head>
    <title>국어사전</title>
    <style>
        div.box {
            border : 5px solid #DDD;
            padding : 10px;
            margin : 5px;
            line-height: 160%;
            width: 300px;
            float: left;
        }
    </style>
    <script src="https://code.jquery.com/jquery-1.12.1.min.js"></script>
</head>

<body>
    <!--<a href="http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?&&&"> 확인 </a>-->

    <script>

        $(document).ready(function(){
           
            $.ajax({
                url : 'https://opendict.korean.go.kr/api/search',
                data : {
					certkey_no:1209,
					key:'7EDD1EDA2E0D739DA7565168C0C5262E',
					target_type:'search',
					part: $('#part').val(),// 검색 대상
					q: $('#q').val(), // 검색하는 단어
					sort: $('#sort').val(), // 정렬 방식
					start:1,
					num:10
                },
                success : function(res){
                    
                    var str = '';
                    
                    $(res).find('item').each(function(){
                        
                        var word = $(this).find('word').text();
                        var definition = $(this).find('definition').text();
                       
                        
                        str += '<div class="box">\n';
                        str += '<div>표제어 : '+word+'</div>\n';
                        str += '<div>뜻풀이 : '+definition+'</div>\n';
            
                        str += '</div>\n';
                    });
                    
                    
                    $('body').html(str);
                } 
            
            });
            
        });
    </script>
    
</body>

</html>