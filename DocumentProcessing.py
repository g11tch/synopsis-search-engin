import re
import nltk

class Processing:

	ignore_words=['able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'amongst', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'aside', 'ask', 'asking', 'auth', 'available', 'away', 'awfully', 'back', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'date', 'did', "didn't", 'different', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'each', 'edu', 'effect', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'except', 'far', 'few', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'goes', 'gone', 'got', 'gotten', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', "i'll", 'immediate', 'immediately', 'importance', 'important', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', "isn't", 'itd', "it'll", 'its', 'itself', "i've", 'just', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking', 'looks', 'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'might', 'million', 'miss', 'more', 'moreover', 'most', 'mostly', 'mrs', 'much', 'mug', 'must', 'myself', 'name', 'namely', 'nay', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'obtain', 'obtained', 'obviously', 'off', 'often', 'okay', 'old', 'omitted', 'once', 'one', 'ones', 'only', 'onto', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'que', 'quickly', 'quite', 'ran', 'rather', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', "there'll", 'thereof', 'therere', 'theres', 'thereto', 'thereupon', "there've", 'these', 'they', 'theyd', "they'll", 'theyre', "they've", 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'upon', 'ups', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'value', 'various', "'ve", 'very', 'via', 'viz', 'vol', 'vols', 'want', 'wants', 'was', "wasn't", 'way', 'wed', 'welcome', "we'll", 'went', 'were', "weren't", "we've", 'what', 'whatever', "what'll", 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', "who'll", 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', "won't", 'words', 'world', 'would', "wouldn't", 'www', 'yes', 'yet', 'you', 'youd', "you'll", 'your', 'youre', 'yours', 'yourself', 'yourselves', "you've", 'zero']
	def filtering(self,regexp,substitute,data):
		return re.sub(regexp,substitute,data)

	def tokenization(self,regexp,data):
		p = re.compile(regexp)
		return p.findall(data)

	def stemWord(self,wordList):
		for i in xrange(len(wordList)):
			w=wordList[i]
			wordList[i]=nltk.stem.lancaster.LancasterStemmer().stem(w)

	def stopWord(self,wordList):
		newWordList=[]
		for i in xrange(len(wordList)):
			if wordList[i] in ignore_words:
				newWordList.append(wordList[i])
		return newWordList

	def processIt(self,data,disableStopWord=True,disableStemming=False,disableFiltering=False,disableTokenization=False):
		if disableFiltering!=True:
			data=self.filtering("[^A-Za-z0-9 ]","",data)
		if disableTokenization!=True:
			wordList=self.tokenization("[A-Za-z0-9]+",data)
			if disableStemming!=True:
				self.stemWord(wordList)
		else:
			wordList=data
			if disableStemming!=True:
				print "you can't do stemming untill tokenization is enabeled"
		return wordList

data="I almost found the answer to this question in this thread (samplebias's answer); however I need to split a phrase into words, digits, punctuation marks, and spaces/tabs. I also need this to preserve the order in which each of these things occurs (which the code in that thread already does)."
p=Processing()
print p.processIt(data,disableTokenization=True,disableStemming=True)