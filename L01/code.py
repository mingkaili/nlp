#encoding=utf-8
#自定义函数 by deepsky
def coder(message):
	return message.decode("utf-8").encode("gbk")

def coderforlist(wordlists):
	result = [];
	for word in wordlists:
		word = coder(word)
		result.append(word)
	return result
	
def vectrotostr(words,split_char):
	result =''
	for i in words:
		result +=(coder(i)+' | ')
	return result