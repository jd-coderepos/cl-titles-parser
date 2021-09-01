import re

numeric_short = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
prepositions_short = ['at', 'for', 'in', 'of', 'on', 'over', 'to', 'toward']
adjectives_short = ['efficient', 'improved', 'formal', 'simple', 'new', 'novel', 'mixed', 'robust', 'supervised', 'unsupervised', 'statistical', 'uniform', 'stochastic', 'discriminative', 'iterative']
determiners_short = ['the', 'a', 'an', 'future']

det_rx = 'the|a|an|future'

#case_study_research_problem_splitter prepositions and verbs
cs_rp_splitters_rx = 'in|of|on|over|from|using|for'

lang_rx = 'English|Latin|Spanish|French|German|Russian|Portuguese|Italian|Dutch|Czech|Swedish|Polish|Bulgarian|Hungarian|\
Slovenian|Norwegian|Irish|Romanian|Venetan|Danish|Croatian|Serbian|Icelandic|Greece|Greek|Occitan|Estonian|Welsh|Finnish|Slavic|\
Afrikaans|Odawa|Ainu|Kven|Mi\'kmaq|Gagauz|Kanyen\'k\\\'eha|Chukchi|Shipibo\-Konibo|Kunwinjku|Naija|Wolof|Evenki|Kyrgyz|Setswana|\
Tigrigna|Oromo|Wolaytta|Sundanese|Balinese|Bataks|Egyptian|Levantine|Abui|Wambaya|\
Hindi|Bengali|Lahnda|Telugu|Marathi|Tamil|Urdu|Punjabi|Gujarati|Bangla|Sindhi|Odia|Sanskrit|Bhojpuri|Magahi|Malayalam|Kannada|Dravidian|Indic|Konkani|\
Arabic|Turkish|Turkic|Amharic|Hebrew|Persian|Syriac|Coptic|Farsi|Armenian|Mediterranean|Iberian|\
Taizi|Sanaani|Najdi|Jordanian|Syrian|Iraqi|Moroccan|Mordvinic|Shahmukhi|\
Mandarin|Chinese|Japanese|Kanji|Hakka|Basque|Hiberno-English|\
Indonesian|Javanese|Korean|Vietnamese|Taiwanese|Sinhala|Malay|Malaysian|Malagasy|Thai|Tagalog|Filipino|Latvian|Cantonese|Tuvan|Chintang|\
Maltese|Quechua|Murrinh-Patha|Bambara|Breton|Erzya|Laz|Lakota|Somali|\
Sign|R|Python|Java|Prolog|Accadian|Maori|Tikopia|\
Natural|Minority|Ega|Piu|Arapaho|Braille|\
Prolog|Warao|Error'

nl_parts_rx = 'Adverbs|[vV]erb(s)?|Idioms|Questions|[dD]ialogue(s)?|Dialog|Hypertexts|Discourse|Charts|Subtitles|Interviews|INTER(\-)?VIEW[sS]?|\
Words|Prepositions|Sarcasm|Documents|[tT]ext(s)?|Instructions|[cC]orp(us|ora)|Metaphors|Phrases|[sS]peech|[sS]entence(s)?|[dD]ocument(s)?|[uU]tterance(s)?|\
Captions|Compounds'

living_1_rx = '(human|student|animal|songwriter|\
journalist|interpreter|egyptologist|developer|novice|expert)[s]?'
living_2_rx = 'blind|f\*r\*i\*e\*n\*d\*s\*|everyone|people'
living_3_rx = 'children[s]?'

places_rx = 'taiwan|argentina|mexico|spain|us(a)?|india|africa|china|japan|germany|france'

object_rx = 'Wheelchairs'
abstract_rx = 'Concepts|Events|Courses|Action|Belief/Factuality|Prevention|Research|World'

non_content_words_rx = 'available|prevention|action|course|use'

#tool regular expression patterns
tools_1_rx = 'bert|lstm|memory|controller|perceptron|library|generator|writer|finder|tagger|segmentor|summarizer|realizer|translator|demonstrator|solver|hypernet|facebook|\
segmenter|stemmer|lemmatizer|retriever|aligner|recognizer|baseline|analyzer|synthesizer|diacritizer|identifier|learner|processor|browser|frontend|backend|end|analogue'
tools_2_rx = '(tool|network|protocol|system|pack|suite|interface|architecture|parser|car|toolkit|indexer|classifier|net|engine|field|client|package|kit|computer|application|\
tester|framework|environment|program|annotator|detector|decoder|implementation|agent|platform|transformer|embedding|checker|crf|svm|machine|layer|compiler|software)[s]?'
tools_3_rx = 'workbench(es)?'

#method regular expression patterns
method_1_rx = '(protocol|experiment|science|method|procedure|heuristic|paradigm|algorithm|walk|review|template|model|standard|mechanism|verbalism|\
workflow|specification|spec|proposal|design|recipe|technique|formalism|rule|frame|movement|inference|format|principle|prototype|module|margin)[s]?'
method_2_rx = '(approach|process|search|parse)(es)?'
method_3_rx = '(strateg|methodolog|probabilit|theor|analog)(ies|y)'
method_4_rx = 'lingua|analysis|measure|programming|logic|annotation|feedback|support|loop|cleanup|clean-up|retrieval|descent|retrieval|entropy|\
scheme|schema|look\-up|online|backoff|transfer|closure|prosody|rhetoric|transport|carlo|markov|pivot|retrieval|weighted|learning|formula|theory'

#resource regular expression patterns
resources_1_rx = '(dictionar|stor|typolog|inventor|ontolog|summar|biograph|fluenc|terminolog|accurac|geometr|poetr|polic|vocabular|dependenc|taxonom|commentar|entr|hierarch|quer|obituar)(ies|y)'
resources_2_rx = 'knowledge|information|literature|web|media|twitter|codalab|wikipedia|cloud|news|space|wordnet|slang|time|input|sytax|automata|prose|blogosphere|era|archive|\
discourse|memory|work|wiktionary|wikidata|quran|irony|sarcasm|code|behavior|rebuttal|intent|email|demand|anaphorae|hardware|age|uses|answer|prior|gaze|orthography|reddit|cache|length'
resources_3_rx = '(resource|source|description|catalogue|set|collection|text|annotation|lexicon|dataset|database|data|structure|writing|term|question|comment|content|\
dialogue|bible|game|stream|novel|concept|size|vector|error|reference|influence|forum|accent|phone|number|board|list|portal|filter|metric|set|clause|evidence|cluster|submission|\
computer|board|knowledgebase|base|language|tree|tree[Bb]ank|bank|event|character|output|grammar|synset|lexeme|pair|log|report|image|essay|domain|document|phrase|syllable|\
narrative|subtitle|label|audio|video|name|word|gram|translation|distance|variable|recipe|pattern|forest|client|kernel|structure|aspect|review|graph|behaviour|sequence|feedback)[s]?'
resources_4_rx = 'corp(ora|us)'
resources_5_rx = 'thesaur(i|us)'
resources_6_rx = '(speech|sketch)(es)?'
resources_7_rx = 'anaphor(a)?'

#problem domains
domains_rx = 'bio(-)?medical|healthcare|science|west african|life science(s)?|indian|american|formosan|geography|iberian'

#research_fields
fields = 'computational|linguistics|biochemistry'

#generic resource regular expression patterns
gen_resources_1_rx = '(protocol|system|forum|figure|paper|twitter|tweet|rumour|posting|patent|web|micro(\-)?blog|input|article|\
experiment|pack|argument|science|domain|suite|market|bank|example|case|use(\-)?case|scenario|instance|conference|location)[s]?'
gen_resources_2_rx = "(communit|centur|stud)(y|ies)"
gen_resources_3_rx = "healthcare|e\-Commerce|enterprise|reddit"
gen_resources_4_rx = "business(es)?"

#phrase start
generic_starter_rx = 'efficient|improved|formal|simple|new|novel|mixed|robust|supervised|unsupervised|hybrid|statistical|uniform|stochastic|\
discriminative|iterative|the|a|an|future|one|two|three|four|five|six|seven|eight|nine|ten|lightweight|general|some|tentative|various'

#generic phrase end usually at unigram or bigram level
generic_terms_rx = 'need|procedure|working|getting|heuristic|paradigm|algorithm|workflow|architecture(s)?|prospect|specification|spec|dataset|roadmap|application|preservation|interpretation|\
system(s)?|tester|case|tool|generation|structure|foundation|framework|process|resource(s)?|bases|strateg(ies|y)|problem|challenge|center|experiment|representation(s)?|theory|\
environment|logic|proposal|notion|design|model|recipe|program|attempt|approach(es)?|workbench|detector|lexicon|database|implementation|treatment|interaction|identification|research|\
methodology|mission|method(s)?|agent|rationale|strategy|platform|issue(s)?|corpus|heuristic|technique(s)?|benchmark|formalism|report|infrastructure|analysis|acquisition'

#pronouns regular expression
pronoun_rx = 'this|these|that|those|who|which|as|each|all|either|one|both|any|such'

#used in system
software_rx = 'model|implementation|system|library|application|tool|agent|parser|extractor'

non_of_connectors_rx = 'in|for|on|to|from|with|via|through|using|as|by'
non_from_connectors_rx = 'in|for|on|to|of|with|via|through|using|as|by'
non_on_connectors_rx = 'in|for|from|to|of|with|via|through|using|as|by'
non_for_connectors_rx = 'in|of|on|to|from|with|via|through|using|as|by'
non_to_connectors_rx = 'in|of|on|for|from|with|via|through|using|as|by'
non_in_connectors_rx = 'to|of|on|for|from|with|via|through|using|as|by'
non_as_connectors_rx = 'to|of|on|for|from|with|via|through|using|in|by'
non_with_connectors_rx = 'to|of|on|for|from|as|via|through|using|in|by'
non_through_connectors_rx = 'to|of|on|for|from|as|via|with|using|in|by'
non_via_connectors_rx = 'to|of|on|for|from|as|through|with|using|in|by'
non_using_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|by'
non_by_connectors_rx = 'to|of|on|for|from|as|through|with|via|in|using'

connectors_rx = 'to|of|on|for|from|with|by|via|through|using|in|as'
connectors_list = ['to', 'of', 'on', 'for', 'from', 'with', 'by', 'via', 'through', 'using', 'in', 'as']

question_words = 'how|what|when|where|which|who|whom|whose|why|can|would|should'

def system_solution(part0, part1):
	v = ending(part0.lower(), 'system')
	resource, solution = resource_or_solution(part1)
	return v and solution

def task_dataset_match(phrase):
	return re.match(".*?(([A-Z][A-Z])|([a-z][A-Z])|[\-\d+]).*", phrase)
		
def research_problem_suffixes(phrase):
	return re.match(".*((ing|ion)|(tics|ment|logy|reference|fer|sor|ser|yzer(s)?|lysis)$)", phrase)

def get_solution_or_resource(phrase):	
	if re.match("^.*(ing|ion|pproach)(\b|$)", phrase):
		return phrase, ""
	else:
		return "", phrase

def contains_ion_ing(phrase):
	return re.match('^.*(ion|ing)', phrase)

def ends_ion_ing(phrase):
	return re.match('^.*(ion|ing)$', phrase)
	
def has_specialcase(phrase):
	return not re.match('^.*([a-z][A-Z]|[A-Z][A-Z]|\d+).*', phrase) is None

def get_info_exactly_one_connector(phrase):
	phrase = phrase.lower()
	if contains_one_connector(phrase, 'of', non_of_connectors_rx):
		return 'of'
	elif contains_one_connector(phrase, 'from', non_from_connectors_rx):
		return 'from'
	elif contains_one_connector(phrase, 'on', non_on_connectors_rx):
		return 'on'
	elif contains_one_connector(phrase, 'for', non_for_connectors_rx):
		return 'for'
	elif contains_one_connector(phrase, 'to', non_to_connectors_rx):
		return 'to'
	elif contains_one_connector(phrase, 'in', non_in_connectors_rx):
		return 'in'
	elif contains_one_connector(phrase, 'as', non_as_connectors_rx):
		return 'as'
	elif contains_one_connector(phrase, 'with', non_with_connectors_rx):
		return 'with'
	elif contains_one_connector(phrase, 'through', non_through_connectors_rx):
		return 'through'
	elif contains_one_connector(phrase, 'via', non_via_connectors_rx):
		return 'via'
	elif contains_one_connector(phrase, 'using', non_using_connectors_rx):
		return 'using'
	else:
		return None	
	
def get_info_exactly_one_connector_old(phrase):
	phrase = phrase.lower()
	if contains_one_connector(phrase, 'of', non_of_connectors_rx):
		return 'of', non_of_connectors_rx
	elif contains_one_connector(phrase, 'from', non_from_connectors_rx):
		return 'from', non_from_connectors_rx
	elif contains_one_connector(phrase, 'on', non_on_connectors_rx):
		return 'on', non_on_connectors_rx
	elif contains_one_connector(phrase, 'for', non_for_connectors_rx):
		return 'for', non_for_connectors_rx
	elif contains_one_connector(phrase, 'to', non_to_connectors_rx):
		return 'to', non_to_connectors_rx
	elif contains_one_connector(phrase, 'in', non_in_connectors_rx):
		return 'in', non_in_connectors_rx
	elif contains_one_connector(phrase, 'as', non_as_connectors_rx):
		return 'as', non_as_connectors_rx
	elif contains_one_connector(phrase, 'with', non_with_connectors_rx):
		return 'with', non_with_connectors_rx
	elif contains_one_connector(phrase, 'through', non_through_connectors_rx):
		return 'through', non_through_connectors_rx
	elif contains_one_connector(phrase, 'via', non_via_connectors_rx):
		return 'via', non_via_connectors_rx
	elif contains_one_connector(phrase, 'using', non_using_connectors_rx):
		return 'using', non_using_connectors_rx
	else:
		return None, None
	
def contains_one_connector(phrase, connector, non_connector_candidate_rx):
	return (' '+connector+' ' in phrase and not re.match('^.* ('+non_connector_candidate_rx+') ', phrase))

def contains_any_element(phrase, rx):
	return re.match('^.* ('+rx+') ', phrase)
	
def ending(phrase, end):
	return not re.match('^.*?('+end+')$', phrase) is None
	
def begins_phrase(rx, phrase):
	return not re.match('^('+rx+') ', phrase) is None
	
def split_length(phrase, splitter):
	return len(phrase.split(splitter))
	
def substring_split(phrase, splitter):
	i = phrase.find(splitter)
	part_0 = phrase[0:i]
	part_1 = phrase[i+len(splitter):]
	return part_0, part_1

def first_word_ending(rx, phrase):
	return not re.match('^[^ ]*('+rx+') ', phrase) is None
	
def second_word_ending(rx, phrase):
	return not re.match('^[a-zA-Z]+?\s[a-zA-Z]+?('+rx+') ', phrase) is None
		
def find_index_of_any(rx, phrase):
	for m in re.finditer(' ('+rx+') ', phrase):
		return m.start()
	return -1

def non_content_start(phrase_lower):

	phrase_tokens = phrase_lower.split(' ')
	return re.match('^('+generic_terms_rx+') ', phrase_lower) or \
	(re.match('^('+generic_starter_rx+')$', phrase_tokens[0]) and re.match('^('+generic_terms_rx+')$', phrase_tokens[1])) or \
	'system description' in phrase_lower
	
def non_content(phrase, phrase_lower):
	phrase_tokens = phrase_lower.split(' ')
	length = len(phrase_tokens)
	if length == 1:
		return re.match('^('+generic_terms_rx+')$', phrase_lower)
	elif length == 2:
		return (re.match('^('+generic_starter_rx+')$', phrase_tokens[0]) and re.match('^('+generic_terms_rx+')$', phrase_tokens[1])) or 'system description' in phrase_lower
	#elif length == 3:
	#	return re.match('^('+generic_starter_rx+')', phrase_tokens[0]) and re.match('^('+generic_terms_rx+')', phrase_tokens[2]) and not (task_dataset_match(phrase.split(' ')[1]) or 'coreference' == phrase_tokens[1] or 'database' == phrase_tokens[2] or 'corpus' == phrase_tokens[2])
	return False

def remove_and_ending(phrase):
	if ' ' in phrase and ending(phrase, 'and'):
		i = phrase.rindex(' ')
		phrase = phrase[0:i].strip()
	return phrase
	
def resources_lite(phrase):
	phrase = remove_and_ending(phrase)
	phrase_toks = phrase.split(' ')
	return (len(phrase_toks) == 1 and is_resource(phrase.lower())) or \
	(len(phrase_toks) >= 2 and re.match('^('+domains_rx+')', phrase_toks[0].lower()) and is_resource(phrase_toks[len(phrase_toks)-1].lower())) or \
	(is_language(phrase_toks[0]) and is_resource(phrase_toks[len(phrase_toks)-1].lower()))
	
def is_resource(phrase):
	phrase = remove_and_ending(phrase)
	return (not first_word_ending('ing|ion', phrase.lower()) and
	(ending(phrase, resources_1_rx) or \
	ending(phrase, resources_2_rx) or \
	ending(phrase, resources_3_rx) or \
	ending(phrase, resources_4_rx) or \
	ending(phrase, resources_5_rx) or \
	ending(phrase, resources_6_rx) or \
	ending(phrase, resources_7_rx) or \
	(ending(phrase, 's|es|ity') and not 'process' in phrase and not 'use' in phrase) or \
	ending(phrase, domains_rx))) or \
	begins_phrase(places_rx, phrase) and ending(phrase, 'ion|ing|ment|tics|vity|vities')

def is_living(phrase):
	phrase = remove_and_ending(phrase)
	return ending(phrase, living_1_rx) or \
	ending(phrase, living_2_rx) or \
	ending(phrase, living_3_rx) or \
	begins_phrase(living_1_rx, phrase) or \
	begins_phrase(living_2_rx, phrase) or \
	begins_phrase(living_3_rx, phrase)

def is_language(phrase):
	phrase = remove_and_ending(phrase)
	phrase_toks = phrase.split(' ')	
	phrase_lower = phrase.lower()
	
	if 'corpus' in phrase_lower or 'corpora' in phrase_lower or 'case study' in phrase_lower or 'study' in phrase_lower or \
	'analysis' in phrase_lower or 'learners' in phrase_lower or 'machine' in phrase_lower or 'parsing' in phrase_lower or \
	'segmentation' in phrase_lower or 'twitter' in phrase_lower:
		return False
	
	if begins_phrase(lang_rx, phrase) and ' and ' in phrase and (not(is_research_problem(phrase) or is_resource(phrase)) or ending(phrase.lower(), 'language(s)?')):
		second_language_phrase = phrase.split(' and ')[1].lstrip()
		if not ' ' in second_language_phrase:
			second_language_phrase = second_language_phrase + ' '	
		return begins_phrase(lang_rx, second_language_phrase)
		
	if (len(phrase_toks) > 1 and re.match('^('+lang_rx+')$', phrase_toks[len(phrase_toks)-1])) or re.match('^('+lang_rx+')$', phrase):	
		return not is_research_problem(phrase)
						
	return (len(phrase_toks) >= 3 and not re.match('^('+generic_starter_rx+')', phrase_toks[0]) is None and \
	not re.match('^('+lang_rx+')', phrase_toks[1]) is None and ending(phrase, '(dialect|language)[s]?')) or \
	((begins_phrase(lang_rx, phrase) or begins_phrase(domains_rx, phrase.lower())) and ending(phrase.lower(), '(dialect|language)[s]?'))
	
def is_place(phrase):
	phrase = remove_and_ending(phrase)
	return ending(phrase, places_rx)

def is_tool(phrase):
	phrase = remove_and_ending(phrase)
	return (not first_word_ending('ing|ion', phrase.lower()) and
	(ending(phrase.lower(), tools_1_rx) or \
	ending(phrase.lower(), tools_2_rx) or \
	ending(phrase.lower(), tools_3_rx))) or \
	len(phrase) <= 3 or \
	'crf' in phrase.lower() or 'svm' in phrase.lower() or 'lstm' in phrase.lower() or 'toolkit' in phrase.lower() or \
	(has_specialcase(phrase) and not is_resource(phrase.lower()) and not 'MUC' in phrase and not 'US' in phrase and not 'Eval' in phrase and not 'task' in phrase.lower() and not ending(phrase.lower(), 'ion|ing|challenge') and not first_word_ending('ing|ion', phrase.lower()))
	
def is_method(phrase):	
	phrase = remove_and_ending(phrase)
	return ending(phrase.lower(), method_1_rx) or \
	ending(phrase.lower(), method_2_rx) or \
	ending(phrase.lower(), method_3_rx) or \
	ending(phrase.lower(), method_4_rx) or \
	(ending(phrase.lower(), 'ion|ing|ment|ness|tics|vity|vities') and not 'information' in phrase.lower())
	
def is_research_problem(phrase):
	phrase = remove_and_ending(phrase)
	if non_content(phrase, phrase.lower()):
		return False
	if ':' in phrase:
		phrase = phrase[0:phrase.find(':')]
	if first_word_ending(det_rx, phrase.lower()):
		phrase = phrase[phrase.find(' ')+1:]	
	return (ending(phrase.lower(), 'ion|ing|ment|tics|emy|logy|graphic|dence|style|syntax|charter|discovery|choice|system|systems|triad|inference|causality|phenomena|problem(s)?|project|order|equivalence|domain|domains|analysis|similarity|task|review|architecture|research|retrieval') and not (ending(phrase.lower(), 'information') or is_living(phrase.lower()))) or \
	begins_phrase('improve|enhance|detect|manipulate|read|determine|leverage|recognise|embed|ask|planning|evaluate|support|suggest|fill|interface|represent|acquire|parse|build|recognize|query|find|identify|extract|explore|solve|locate|recommend|distribute|generate|learn|measure|construct|create|maintain|determine|decompose|enrich|overcome|answer|extend|detect|estimate|classify|predict|characterise|disambiguate|assign', phrase.lower()) or \
	begins_phrase(fields, phrase.lower()) or \
	(not is_resource(phrase.lower()) and (has_specialcase(phrase) or (second_word_ending('ing|ion', phrase.lower()) and not second_word_ending('location', phrase.lower())))) or \
	(first_word_ending('ing|ion', phrase.lower()) and not first_word_ending('location', phrase.lower()))
	
def resource_or_solution_or_language(phrase):
	resource = []
	solution = []
	language = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif ending(phrase.split(' ')[0], 'ing'):
		solution.append(phrase)
	elif is_resource(phrase.lower()):
		resource.append(phrase)
	elif not is_living(phrase_lower) and not is_place(phrase_lower) and not ending(phrase_lower, non_content_words_rx):
		solution.append(phrase)
	return resource, solution, language

def language_or_tool_or_method_or_resource(phrase):
	language = []
	tool = []
	method = []
	resource = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)		
	return language, tool, method, resource

def language_or_tool_or_method_or_resource_or_rp(phrase):
	language = []
	tool = []
	method = []
	resource = []
	research_problem = []
	phrase_lower = phrase.lower()
	if is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	elif is_research_problem(phrase):
		research_problem.append(phrase)		
	return language, tool, method, resource, research_problem

def rp_or_language_or_tool_or_method_or_resource(phrase):
	research_problem = []
	language = []
	tool = []
	method = []
	resource = []
	phrase_lower = phrase.lower()
	if is_research_problem(phrase):
		research_problem.append(phrase)	
	elif is_language(phrase):
		language.append(phrase)
	elif is_tool(phrase):
		tool.append(phrase)
	elif is_method(phrase):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	return research_problem, language, tool, method, resource

def get_scientific_knowledge_elements(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	if not non_content(phrase, phrase.lower()):
		if is_research_problem(phrase):
			research_problem.append(phrase)
		else:
			resource, solution, language = resource_or_solution_or_language(phrase)
	return solution, research_problem, resource, language

def get_scientific_knowledge_elements_all(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	if not non_content(phrase, phrase.lower()):
		if is_tool(phrase):
			tool.append(phrase)
		elif is_method(phrase):
			method.append(phrase)
		elif is_research_problem(phrase):
			research_problem.append(phrase)
		else:
			resource, solution, language = resource_or_solution_or_language(phrase)
	return solution, research_problem, resource, language, tool, method
	
def extend_lists(list1, l1, list2, l2, list3, l3, list4, l4):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	return list1, list2, list3, list4

def extend_lists_five(list1, l1, list2, l2, list3, l3, list4, l4, list5, l5):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	if l5:
		list5.extend(l5)
	return list1, list2, list3, list4, list5
	
def extend_lists_all(list1, l1, list2, l2, list3, l3, list4, l4, list5, l5, list6, l6):
	if l1:
		list1.extend(l1)
	if l2:
		list2.extend(l2)
	if l3:
		list3.extend(l3)
	if l4:
		list4.extend(l4)
	if l5:
		list5.extend(l5)
	if l6:
		list6.extend(l6)
	return list1, list2, list3, list4, list5, list6
	
def find_first_occurence(list, phrase):
	indexes = []
	for element in list:
		if ' '+element+' ' in phrase:
			indexes.append(phrase.find(' '+element+' '))
	if not indexes: return -1
	else: return min(indexes)
	
def get_list_of_connector_indexes(phrase, rx):
	indexes = []
	for m in re.finditer(' ('+rx+') ', phrase):
		indexes.append(m.start())
		#print(str(m.start())+"||"+str(m.group()))
	return indexes

def to_pronoun(phrase):
	return re.match('.*to ('+pronoun_rx+')', phrase)

def get_length_without_determiners(phrase):
	if begins_phrase(det_rx, phrase):
		phrase = phrase[phrase.find(' ')+1:]
	return len(phrase.split(' '))
	
def get_string(phrase, start_index):
	str = phrase[start_index+1:]
	str = str[0:str.find(' ')]
	return str
	
def preprocess(phrase):
	phrase = phrase.replace('as a Basis for', 'for')
	phrase = phrase.replace('as a basis for', 'for')
	phrase = phrase.replace('as Basis for', 'for')
	phrase = phrase.replace('as basis for', 'for')
	phrase = phrase.replace('on the basis of', 'of')
	phrase = phrase.replace('to be of', 'of')
	phrase = phrase.replace(' Based on ', ' on ')
	phrase = phrase.replace(' based on ', ' on ')
	phrase = phrase.replace(' Extracted from ', ' from ')
	phrase = phrase.replace(' Focused on ', ' on ')
	phrase = phrase.replace(' Annotated with ', ' with ')
	phrase = phrase.replace(' dedicated to ', ' for ')
	phrase = phrase.replace(' to Study ', ' for ')
	phrase = phrase.replace(' built from ', ' from ')
	phrase = phrase.replace(' by means of ', ' using ')
	phrase = phrase.replace(' by using ', ' using ')
	phrase = phrase.replace(' straight out of ', ' from ')
	phrase = phrase.replace(' Implemented in ', ' in ')
	phrase = phrase.replace(' implemented in ', ' in ')
	phrase = phrase.replace(' Written in ', ' in ')
	phrase = phrase.replace('Towards ', '')
	if 'for using and' in phrase.lower():
		phrase = phrase.lower().replace('for using and', 'for')
	if 'for using' in phrase.lower():
		phrase = phrase.lower().replace('for using', 'for')
	phrase = phrase.replace('as Used for', 'for').replace('as Used For', 'for')
	phrase = phrase.replace('Used for', 'for')
	phrase = phrase.replace('in a tool for', 'for')
	phrase = phrase.replace('for the Development of', 'for')
	phrase = phrase.replace('for Development of', 'for')
	phrase = phrase.replace('for Representing and Using', 'for')
	phrase = phrase.replace('for Use in', 'for')
	phrase = phrase.replace('Trained using', 'using')
	phrase = phrase.replace('`', '')
	phrase = phrase.replace('\'', '')
	phrase = phrase.replace(' - ', ' ')
	phrase = phrase.replace(' in Light of ', ' in ')
	phrase = phrase.replace(' about ', ' on ')
	phrase = phrase.replace(' About ', ' on ')
	phrase = phrase.replace(' -- ', ': ')
	phrase = phrase.replace('---', ': ')
	phrase = phrase.replace(' : ', ': ')
	phrase = phrase.replace(' Used as ', ' as ')
	phrase = phrase.replace('On the Utility of', 'On')
	phrase = phrase.replace('Defined on', 'on')
	phrase = phrase.replace('Left to Right Parsing', 'Left-to-Right Parsing')
	phrase = phrase.replace('used for', 'for')
	phrase = phrase.replace('Augmented with', 'with')
	phrase = phrase.replace('Intermediated by', 'with')
	phrase = phrase.replace('Based On', 'on')
	phrase = phrase.replace('Built From', 'from')
	phrase = phrase.replace('induced from', 'from')
	phrase = phrase.replace('Induced from', 'from')
	phrase = phrase.replace('obtained from', 'from')
	phrase = phrase.replace('Extracted From', 'from')
	phrase = phrase.replace('Generated from', 'from')
	phrase = phrase.replace('Acquired from', 'from')
	phrase = phrase.replace('acquired from', 'from')
	phrase = phrase.replace('Retrieved from', 'from')
	phrase = phrase.replace('Populated from', 'from')
	phrase = phrase.replace('Mined from', 'from')
	phrase = phrase.replace('Selected from', 'from')
	phrase = phrase.replace('Learned from', 'from')
	phrase = phrase.replace('collected from', 'from')
	phrase = phrase.replace('Derived from', 'from')
	phrase = phrase.replace('Stated in', 'in')
	phrase = phrase.replace('expressed in', 'in')
	phrase = phrase.replace(' Used in ', ' in ')
	phrase = phrase.replace('Concept to Speech', 'Concept-to-Speech')
	phrase = phrase.replace('Grapheme to Phoneme', 'Grapheme-to-Phoneme')
	phrase = phrase.replace('Phoneme to Grapheme', 'Phoneme-to-Grapheme')
	phrase = phrase.replace('Learning to Rank', 'Learning-to-Rank')
	phrase = phrase.replace('Learning to rank', 'Learning-to-rank')
	phrase = phrase.replace('learning to rank', 'learning-to-rank')
	phrase = phrase.replace('Learning to Find', 'Learning-to-Find')
	phrase = phrase.replace('Learning to Order', 'Learning-to-Order')
	phrase = phrase.replace('Learning to Compose', 'Learning-to-Compose')
	phrase = phrase.replace('Learning to Extract', 'Learning-to-Extract')
	phrase = phrase.replace('Learning to Map', 'Learning-to-Map')
	phrase = phrase.replace('Learning to Model', 'Learning-to-Model')
	phrase = phrase.replace(' to dialogue', 'text-to-dialogue')
	phrase = phrase.replace('Textextt to 3D', 'Text-to-3D')
	phrase = phrase.replace('Sequence to Sequence', 'Sequence-to-Sequence')
	phrase = phrase.replace('as Applied to', 'applied to')
	phrase = phrase.replace('when applied to', 'applied to')
	phrase = phrase.replace('Designed to', 'to')
	phrase = phrase.replace('Referring to', 'for')
	phrase = phrase.replace('to Enable', 'for')
	phrase = phrase.replace('according to', 'on')
	phrase = phrase.replace('Seen as', 'as')
	phrase = phrase.replace('Represented as', 'as')
	phrase = phrase.replace('by Using', 'using')
	phrase = phrase.replace('through Using', 'using')
	phrase = phrase.replace('with Applications to', 'for')
	phrase = phrase.replace('with application to', 'for')
	phrase = phrase.replace('with Application to', 'for')
	phrase = phrase.replace('Part of Speech', 'Part-of-Speech')
	phrase = phrase.replace('Time to Event', 'Time-to-Event')
	phrase = phrase.replace('Image to Text', 'Image-to-Text')
	phrase = phrase.replace('Bag of Words', 'Bag-of-Words')
	phrase = phrase.replace('Letter to Sound', 'Letter-to-Sound')
	phrase = phrase.replace('term to term', 'term-to-term')
	phrase = phrase.replace('Text to Speech', 'Text-to-Speech')
	phrase = phrase.replace('Constituency to Dependency', 'Constituency-to-Dependency')
	phrase = phrase.replace('designed for', 'for')
	phrase = phrase.replace('with and for', 'for')
	phrase = phrase.replace('as means of', 'for')
	phrase = phrase.replace('by Means of', 'by')
	phrase = phrase.replace('Built using', 'using')
	phrase = phrase.replace('on the Use of', 'on')
	phrase = phrase.replace('for Obtaining a for', 'for')
	phrase = phrase.replace(' Pronounced by ', ' by ')
	phrase = phrase.replace(', ', ' ')
	if begins_phrase('On', phrase):
		phrase = re.sub('On ', '', phrase, count=1)
	if begins_phrase('Learning to', phrase):
		phrase = re.sub('Learning to ', 'Learning-to-', phrase, count=1)
	if begins_phrase('Building and using', phrase):
		phrase = re.sub('Building and using ', 'Using ', phrase, count=1)
	
	if ending(phrase, '\\.'):
		phrase = phrase[0:len(phrase)-1]
	
	return phrase
			