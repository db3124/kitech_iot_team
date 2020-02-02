package com.kite.mm.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class DictSearchResultController {

	@RequestMapping("/function/dictSearchResult")
	public String searchWord(Model model) {
		
		return "function/dictSearchResult";	
		
	}
	
}