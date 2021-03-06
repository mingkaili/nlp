# -*- encoding: utf-8 -*-
#stanNLP
import sys
import os
import code
class StanfordCoreNLP():
	def __init__(self,jarpath):
		self.root = jarpath
		self.tempsrcpath = "tempsrc" # temp path
		self.jarlist = ["ejml-0.23.jar","javax.json.jar","jollyday.jar","joda-time.jar","protobuf.jar","slf4j-api.jar","slf4j-simple.jar","stanford-corenlp-3.6.0.jar","xom.jar"]
		self.jarpath = ""
		self.buildjars()
	
	def buildjars(self): # bulid all jar package path by root
		for jar in self.jarlist:
			self.jarpath += self.root+jar+";"
	
	def savefile(self,path,sent): # create temp file path
		fp = open(path,"wb")
		fp.write(sent)
		fp.close()
	
	def delfile(self,path):
		os.remove(path)

class StanfordPOSTagger(StanfordCoreNLP):
	def __init__(self,jarpath,modelpath):
		StanfordCoreNLP.__init__(self,jarpath)
		self.modelpath = modelpath  # model file path
		self.classfier = 'edu.stanford.nlp.tagger.maxent.MaxentTagger'
		self.delimiter = '/' #tag split
		self.__buildcmd()
	
	def __buildcmd(self): #bulid cmd
		self.cmdline = 'java -mx300m -cp "'+self.jarpath+'" '+self.classfier+' -model "'+self.modelpath+'" -tagSeparator '+self.delimiter
	
	def tag(self,sent): # tag 
		self.savefile(self.tempsrcpath,sent)
		#print self.tempsrcpath +"---"+code.coder(sent)
		tagtxt = os.popen(self.cmdline+" -textFile "+self.tempsrcpath,'r').read() #result 
		#print self.cmdline
		self.delfile(self.tempsrcpath)
		return tagtxt
	
	def tagfile(self,inputpath,outpath):
		os.system(self.cmdline+' -textFile '+inputpath+' > '+outpath )

class StanfordNERTagger(StanfordCoreNLP):
	def __init__(self,modelpath,jarpath):
		StanfordCoreNLP.__init__(self,jarpath)
		self.modelpath = modelpath
		self.classfier = "edu.stanford.nlp.ie.crf.CRFClassifier"
		self._buildcmd()
	
	def _buildcmd(self):
		self.cmdline = 'java -mx1g -cp "'+self.jarpath+'" '+self.classfier+ ' -loadClassifier "'+self.modelpath+'"'
	
	def tag(self,sent):
		self.savefile(self.tempsrcpath,sent)
		tagtax = os.popen(self.cmdline +'-textFile '+self.tempsrcpath,'r').read()
		return tagtxt
	
	def tagfile(self,sent,outpath):
		self.savefile(self.tempsrcpath,sent)
		os.system(self.cmdline+' -textFile '+self.tempsrcpath+' > '+outpath)
		self.delfile(self.tempsrcpath)

class StanfordParser(StanfordCoreNLP):
	def __init__(self,modelpath,jarpath,opttype):
		StanfordCoreNLP.__init__(self,jarpath)
		self.modelpath = modelpath
		self.classfier = 'edu.stanford.nlp.parser.lexparser.LexicalizedParser'
		self.opttype = opttype
		self._buildcmd()
		
	def _buildcmd(self):
		self.cmdline = 'java -mx500m -cp "'+self.jarpath+'" '+self.classfier+' -outputFormat "'+self.opttype+'" '+self.modelpath+' '
	
	# �䷨�������
	def parse(self,sent):
		self.savefile(self.tempsrcpath,sent)
		tagtxt = os.popen(self.cmdline+self.tempsrcpath,'r').read()
		self.delfile(self.tempsrcpath)
		return tagtxt
	
	def tagfile(self,sent):
		self.savefile(self.tempsrcpath,sent)
		os.system(self.cmdline+self.tempsrcpath +' > '+outpath)
		self.delfile(self.tempsrcpath)
		
		
	

		
		