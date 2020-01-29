package com.kite.mm.controller;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AlertController {

	@RequestMapping("/function/alert")
	public String searchWord(Model model) {
		
		return "function/alert";	
		
	}
	
}