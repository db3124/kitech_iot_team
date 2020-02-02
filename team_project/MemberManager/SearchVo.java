package com.kite.mm.controller;

public class SearchVo {
	
	

	private String word;
	private String definition;
	private String pos;
	private String link;
	private String type;
	
	
	public String getWord() {
		return word;
	}


	public void setWord(String word) {
		this.word = word;
	}


	public String getDefinition() {
		return definition;
	}


	public void setDefinition(String definition) {
		this.definition = definition;
	}


	public String getPos() {
		return pos;
	}


	public void setPos(String pos) {
		this.pos = pos;
	}


	public String getLink() {
		return link;
	}


	public void setLink(String link) {
		this.link = link;
	}


	public String getType() {
		return type;
	}


	public void setType(String type) {
		this.type = type;
	}
	
	

	@Override
	public String toString() {
		return "SearchVo [word=" + word + ", definition=" + definition + ", pos=" + pos + ", link=" + link + ", type="
				+ type + "]";
	}


	public void setTestName(String string) {
		// TODO Auto-generated method stub
		
	}

}
