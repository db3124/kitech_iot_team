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
public class DictSearchController3 {
	

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
		DocumentBuilder doc = factory.newDocumentBuilder();
		Document parser = doc.parse("");
	}
		
		
	}
	
	
}