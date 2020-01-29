package com.kite.mm.controller;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;

@Controller
public class DictController {
	
	@CrossOrigin
	@RequestMapping("/function/dict")
	public String getInfo(
			@RequestParam ("q") String keyword,
			Model model) throws UnsupportedEncodingException {
		
		RestTemplate restTemplate = new RestTemplate();
		String key = "7EDD1EDA2E0D739DA7565168C0C5262E";
		String dcodeKey = URLDecoder.decode(key, "utf-8");
		
		String url = "https://opendict.korean.go.kr/api/search"
				+ "?certkey_no=1209"
				+ "&key=" + dcodeKey
				+ "&target_type=search"
				+ "&part=word"
				+ "&q=" + keyword
				+ "&sort=dict"
				+ "&start=1"
				+ "&num=10";
		
		// 한글이 아니거나, 숫자거나, 공백이 있거나...

		String result = restTemplate.getForObject(url, String.class);
		
		model.addAttribute("result", result);

		return "function/dict";		
	}
	
}