package com.kite.mm.controller;


import java.net.URLDecoder;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.soap.Node;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

@Controller
public class DictSearchController2 {
	

	public List<SearchList> getXmlList(
			@RequestParam ("q") String keyword,
			@RequestParam (value="part", defaultValue="word") String part,
			@RequestParam (value="sort", defaultValue="dict") String sort,
			Model model,
			HttpServletRequest req){
		
		List<SearchVo> testList = new ArrayList<SearchVo>();

		
		RestTemplate restTemplate = new RestTemplate();
		String key = "7EDD1EDA2E0D739DA7565168C0C5262E";
		String dcodeKey = URLDecoder.decode(key, "utf-8");
		
		String strUrl = "https://opendict.korean.go.kr/api/search"
				+ "?certkey_no=1209"
				+ "&key=" + dcodeKey
				+ "&target_type=search"
				+ "&part=" + part
				+ "&q=" + keyword // 검색하는 단어
				+ "&sort=" + sort
				+ "&start=1"
				+ "&num=10";
		

		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder = factory.newDocumentBuilder();
		Document document = builder.parse(strUrl);

		// document의 엘리먼트를 rootElement 객체에 반환
		Element rootElement = document.getDocumentElement();

		// rootElement에 있는 item의 node는 nodelist에 담아서 반환됨
		NodeList nodeList = rootElement.getElementsByTagName("item");

		Node current = null;

		// xml 반복문으로 읽어오기

		for (int i = 0; i < nodeList.getLength(); i++) {
			SearchVo gm = new SearchVo();
			
			current = nodeList.item(i);

			NodeList testChildNodes = current.getChildNodes(); // 노드의 자식노드 가져옴

			for (int k = 0; k < testChildNodes.getLength(); k++) {

				Node info = testChildNodes.item(k);

				if (info.getNodeType() == Node.ELEMENT_NODE) {

					Element element = (Element) info;

					// 어휘
					if(element.getTagName()=="word") {
						gm.setTestName(element.getTextContent());	
					}
					// 
					if(element.getTagName()=="definition") {
						gm.setTestName(element.getTextContent());	
					}
					if(element.getTagName()=="pos") {
						gm.setTestName(element.getTextContent());	
					}
					if(element.getTagName()=="link") {
						gm.setTestName(element.getTextContent());	
					}
					if(element.getTagName()=="type") {
						gm.setTestName(element.getTextContent());	
					}
					

				} // end of if

			} // end of for
			testList.add(gm);
		}
		
		return "";
		
		
		
	}
	
	
}