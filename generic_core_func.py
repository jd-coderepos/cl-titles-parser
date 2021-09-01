import re
from utils import *
from core_func_titled_solution import *

def no_connector_heuristics(phrase):
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	
	if ':' in phrase:
		phrase = phrase[0:phrase.find(':')]
	language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(phrase)
	return language, tool, method, resource, research_problem

def one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method):
	#Where in the heuristcs for 'NAME: title' pattern, the beginning of the phrase was often a solution
	#in Using patterns, the beginning of the phrase may be a resource or a tool or a method
	#thus after processing the line using the 'NAME: title' pattern heuristics, we change the result
	#so we check if the solution is a tool or a language or a method or a resource
	if len(solution) == 1:
		lang, t, meth, res = language_or_tool_or_method_or_resource(solution[0])
		language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
		if len(lang) == 1 or len(t) == 1 or len(meth) == 1 or len(res) == 1:
			solution = []
	return solution, research_problem, resource, language, tool, method

def two_connectors_process(phrase, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	part_0_1 = phrase[0:connector_indexes[0]]
	lang, t, meth, res = language_or_tool_or_method_or_resource(part_0_1)
	language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
	if len(language) == 0 and len(tool) == 0 and len(method) == 0 and len(resource) == 0:
		if non_content(part_0_1, part_0_1.lower()):
			solution.append(part_0_1)
	
	phrase_1 = phrase[connector_indexes[0]:].lstrip()
	connector = ''
	if ' ' in phrase_1:
		connector = phrase_1[0:phrase_1.lower().find(' ')]
		i = phrase_1.find(' ')
		phrase_1 = phrase_1[i:].lstrip()		

	#we apply one connector heuristics to the second part
	connector = connector.lower()
	sol = []
	rp = []
	res = []
	lang = []
	t = []
	meth = []					
		
	sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(phrase_1, phrase_1.lower(), connector)			
	solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	return solution, research_problem, resource, language, tool, method

def two_connectors_process_for_casestudy(phrase, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	part_1 = phrase[0:connector_indexes[0]]
	language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(part_1)
	
	part_2 = phrase[connector_indexes[0]:].lstrip()
	i = part_2.find(' ')
	part_2 = part_2[i:].lstrip()
	
	if contains_one_connector(part_2, 'of', non_of_connectors_rx):
		lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(part_2)
		research_problem, resource, language, tool, method = extend_lists_five(research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	else:	
		part_2_lower = part_2.lower()				
		sol, rp, res, lang, t, meth = one_connector_heuristics_titled_solution(part_2, part_2_lower)	
		solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
		solution, research_problem, resource, language, tool, method = one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method)
		
	return solution, research_problem, resource, language, tool, method

def two_connectors_process_generic(phrase, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	part_1 = phrase[0:connector_indexes[0]]
	
	if not non_content(part_1, part_1.lower()):
		language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(part_1)
	
	phrase_1 = phrase[connector_indexes[0]:].lstrip()
	connector = ''
	if ' ' in phrase_1:
		connector = phrase_1[0:phrase_1.lower().find(' ')]
		i = phrase_1.find(' ')
		phrase_1 = phrase_1[i:].lstrip()		

	#we apply one connector heuristics to the second part
	connector = connector.lower()
	sol = []
	rp = []
	res = []
	lang = []
	t = []
	meth = []					
	
	sol, rp, res, lang, t, meth	= two_connectors_heuristics_generic(phrase_1, phrase_1.lower(), connector)			
		
	solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
								
	return solution, research_problem, resource, language, tool, method

def three_connectors_process_generic(phrase, phrase_lower, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []	
	
	first_connector = phrase[connector_indexes[0]:].lstrip()
	i = first_connector.find(' ')
	first_connector = first_connector[0:i]
	first_connector_lower = first_connector.lower()
	
	if 'with' == first_connector_lower or 'of' == first_connector_lower:
		part_1 = phrase[0:connector_indexes[1]]
		solution.append(part_1)

		part_2 = phrase[connector_indexes[1]:].lstrip()
		i = part_2.find(' ')
		connector = part_2[0:i]
		part_2 = part_2[i:].lstrip()
		sol, research_problem, resource, language, tool, method = two_connectors_heuristics_generic(part_2, part_2.lower(), connector)
		
		if len(sol) == 1:
			solution.extend(sol)
	
	elif 'to' == first_connector_lower:
		part_0 = phrase[0:connector_indexes[0]]
		
		#first solution name
		if is_language(part_0):
			language.append(part_0)
		else:
			solution.append(part_0)
				
		part_1 = phrase[connector_indexes[0]:connector_indexes[1]].lstrip()
		i = part_1.find(' ')
		part_1 = part_1[i:].lstrip()

		part_2 = phrase[connector_indexes[1]:connector_indexes[2]].lstrip()
		i = part_2.find(' ')
		connector = part_2[0:i]
		connector_lower = connector.lower()
		part_2 = part_2[i:].lstrip()
										
		if 'of' == connector_lower:
			
			part_middle = part_1+' '+connector+' '+part_2
			
			sol, research_problem, method, resource = something_of_something(part_1, part_2)
			if len(sol) == 1:
				solution.extend(sol)
			
			part_rem = phrase[connector_indexes[2]:].lstrip()
			i = part_rem.find(' ')
			#connector = part_rem[0:i]
			part_rem = part_rem[i:].lstrip()

			lang, t, rp, meth, res = last_part_of_phrase_heu(part_rem)
			language, tool, research_problem, method, resource = extend_lists_five(language, lang, tool, t, research_problem, rp, method, meth, resource, res)

		else:
			
			if is_research_problem(part_1):
				research_problem.append(part_1)
			else:
				lang, tool, method, resource = language_or_tool_or_method_or_resource(part_1)
				if len(lang) == 1:
					language.extend(lang)

			if 'to' == connector_lower or 'as' == connector_lower:
				if is_research_problem(part_2):
					research_problem.append(part_2)
				else:
					lang, t, meth, res = language_or_tool_or_method_or_resource(part_2)
					language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
			else:
				lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(part_2)
				language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
			
			part_rem = phrase[connector_indexes[2]:].lstrip()
			i = part_rem.find(' ')
			part_rem = part_rem[i:].lstrip()
			
			lang, t, rp, meth, res = last_part_of_phrase_heu(part_rem)	
			language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
			
	else:
		part_0 = phrase[0:connector_indexes[0]]
		solution.append(part_0)

		part_1 = phrase[connector_indexes[0]:connector_indexes[1]].lstrip()
		i = part_1.find(' ')
		second_connector = part_1[0:i]
		part_1 = part_1[i:].lstrip()
		if 'on' == first_connector_lower or 'or' == first_connector_lower or 'via' == first_connector_lower or 'through' == first_connector_lower or 'in' == first_connector_lower or 'as' == first_connector_lower or 'using' == first_connector_lower:
			language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(part_1)
		else:
			research_problem, language, tool, method, resource = rp_or_language_or_tool_or_method_or_resource(part_1)
			if len(research_problem) == 1:
				solution.append(research_problem[0])
				research_problem = []
		
		part_2 = phrase[connector_indexes[1]:].lstrip()
		i = part_2.find(' ')
		connector = part_2[0:i]
		part_2 = part_2[i:].lstrip()
		if 'on' == first_connector_lower or 'or' == first_connector_lower or 'via' == first_connector_lower or 'through' == first_connector_lower or 'in' == first_connector_lower or 'as' == first_connector_lower or 'using' == first_connector_lower:
			sol, rp, res, lang, t, meth = last_part_of_phrase_heu_of_special(part_2, connector)
		else:
			sol, rp, res, lang, t, meth = two_connectors_heuristics_generic(part_2, part_2.lower(), connector)
		
		if len(sol) == 0 or not connector == 'with':
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)		
		elif connector == 'with':	
			research_problem, resource, language, tool, method = extend_lists_five(research_problem, rp, resource, res, language, lang, tool, t, method, meth)			
			if len(sol) == 1:
				lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(sol[0])
				language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
				sol = []
				
	return solution, research_problem, resource, language, tool, method	
	
def three_connectors_process(phrase, phrase_lower, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	first_connector = phrase[connector_indexes[0]:].lstrip()
	i = first_connector.find(' ')
	first_connector = first_connector[0:i]		
	if 'of' == first_connector or first_word_ending(det_rx, phrase_lower):
		solution_phrase = phrase[0:connector_indexes[1]]
		solution.append(solution_phrase)

		rest_of_part1 = phrase[connector_indexes[1]:].lstrip()
		i = rest_of_part1.find(' ')
		connector = rest_of_part1[0:i]
		phrase_1 = rest_of_part1[i:].lstrip()
		sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(phrase_1, phrase_1.lower(), connector)				
		solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)		
	else:
		part_0_1 = phrase[0:connector_indexes[0]]
		solution.append(part_0_1)
		
		phrase_1 = phrase[connector_indexes[0]:connector_indexes[1]].lstrip()
		i = phrase_1.find(' ')
		phrase_1 = phrase_1[i:].lstrip()
		lang, t, meth, res = language_or_tool_or_method_or_resource(phrase_1)
		language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
		
		part_2_1 = phrase[connector_indexes[1]:].lstrip()
		i = part_2_1.find(' ')
		connector = part_2_1[0:i]
		rest_of_part_2_1 = part_2_1[i:].lstrip()
		
		sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(rest_of_part_2_1, rest_of_part_2_1.lower(), connector)
		solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	return solution, research_problem, resource, language, tool, method

def more_than_four_connectors_process_generic(phrase, connector_indexes):
	solution = []
	research_problem = []	
	resource = []	
	language = []
	tool = []
	method = []
	
	b = len(connector_indexes)-3
	e = len(connector_indexes)-2
	part_1_1 = phrase[connector_indexes[b]:connector_indexes[e]].lstrip()
	i = part_1_1.find(' ')
	part_1_1 = part_1_1[i:].lstrip()
	
	lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(part_1_1)
	language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
	
	b = len(connector_indexes)-2
	part_2_1 = phrase[connector_indexes[b]:].lstrip()
	i = part_2_1.find(' ')
	connector = part_2_1[0:i]
	rest_of_part_2_1 = part_2_1[i:].lstrip()
					
	sol, rp, res, lang, t, meth	= two_connectors_heuristics_generic(rest_of_part_2_1, rest_of_part_2_1.lower(), connector)

	if len(sol) == 1:
		research_problem, resource, language, tool, method = extend_lists_five(research_problem, rp, resource, res, language, lang, tool, t, method, meth)
		lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(sol[0])
		sol = []
	
	solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	
	return solution, research_problem, resource, language, tool, method
	
def more_than_three_connectors_process_generic(phrase, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	first_connector = phrase[connector_indexes[0]:].lstrip()
	i = first_connector.find(' ')
	first_connector = first_connector[0:i]
	first_connector_lower = first_connector.lower()

	second_connector = phrase[connector_indexes[1]:].lstrip()
	i = second_connector.find(' ')
	second_connector = second_connector[0:i]
	second_connector_lower = second_connector.lower()
		
	if second_connector_lower == 'of':
		solution_phrase = phrase[0:connector_indexes[2]]
		solution.append(solution_phrase)
						
		if len(connector_indexes) == 4:
			part_1_1 = phrase[connector_indexes[2]:].lstrip()
			i = part_1_1.find(' ')
			connector = part_1_1[0:i]
			rest_of_part_1_1 = part_1_1[i:].lstrip()				
							
			sol, rp, res, lang, t, meth	= two_connectors_heuristics_generic(rest_of_part_1_1, rest_of_part_1_1.lower(), connector)
			
			if len(sol) == 1 and not('of' == first_connector_lower or 'with' == first_connector_lower or 'using' == first_connector_lower):
				research_problem, resource, language, tool, method = extend_lists_five(research_problem, rp, resource, res, language, lang, tool, t, method, meth)
				lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(sol[0])
				sol = []				
			
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	else:
		solution_phrase = phrase[0:connector_indexes[1]]
		solution.append(solution_phrase)	
	
		if len(connector_indexes) == 4:
			part_1_1 = phrase[connector_indexes[1]:connector_indexes[2]].lstrip()
			i = part_1_1.find(' ')
			part_1_1 = part_1_1[i:].lstrip()
			lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(part_1_1)
			language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
			
			part_2_1 = phrase[connector_indexes[2]:].lstrip()
			i = part_2_1.find(' ')
			connector = part_2_1[0:i]
			rest_of_part_2_1 = part_2_1[i:].lstrip()
			
			sol, rp, res, lang, t, meth	= two_connectors_heuristics_generic(rest_of_part_2_1, rest_of_part_2_1.lower(), connector)
			
			if len(sol) == 1 and not('of' == first_connector_lower or 'with' == first_connector_lower or 'using' == first_connector_lower):
				research_problem, resource, language, tool, method = extend_lists_five(research_problem, rp, resource, res, language, lang, tool, t, method, meth)
				lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(sol[0])
				sol = []
			
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
												
	if len(connector_indexes) > 4:			
		sol, research_problem, resource, language, tool, method = more_than_four_connectors_process_generic(phrase, connector_indexes)
		if not len(sol) == 0:
			solution.extend(sol)
			
	return solution, research_problem, resource, language, tool, method	
	
def more_than_three_connectors_process(phrase, connector_indexes):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	third_connector = phrase[connector_indexes[2]:].lstrip()
	i = third_connector.find(' ')
	third_connector = third_connector[0:i]
	
	if 'of' == third_connector:
		solution_phrase = phrase[0:connector_indexes[1]]
		solution.append(solution_phrase)
	
		if len(connector_indexes) == 4:
			part_1_1 = phrase[connector_indexes[1]:connector_indexes[2]].lstrip()
			i = part_1_1.find(' ')
			part_1_1 = part_1_1[i:].lstrip()
			lang, t, meth, res = language_or_tool_or_method_or_resource(part_1_1)
			language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
			
			part_2_1 = phrase[connector_indexes[2]:].lstrip()
			i = part_2_1.find(' ')
			connector = part_2_1[0:i]
			rest_of_part_2_1 = part_2_1[i:].lstrip()
			
			sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(rest_of_part_2_1, rest_of_part_2_1.lower(), connector)
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)	
	else:			
		solution_phrase = phrase[0:connector_indexes[2]]
		solution.append(solution_phrase)
		
		#for the rest of phrase we only process the remaining phrase for those candidates with four connectors
		#the remaining phrase should have only two connectors
		
		if len(connector_indexes) == 4:
			part_1_1 = phrase[connector_indexes[2]:].lstrip()
			i = part_1_1.find(' ')
			connector = part_1_1[0:i]
			rest_of_part_1_1 = part_1_1[i:].lstrip()				
							
			sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(rest_of_part_1_1, rest_of_part_1_1.lower(), connector)
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)	
			
	if len(connector_indexes) > 4:	
		print('Title: '+phrase)
		print('too long.. cannot parse')
		print()
			
	return solution, research_problem, resource, language, tool, method
	
def extract_title_elements(phrase, phrase_lower, connector):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
		
	connector_indexes = get_list_of_connector_indexes(phrase_lower, connectors_rx)
	connector_indexes.sort()
		
	#the first set of heuristics looks for phrases with no connector
	if len(connector_indexes) == 0:
		language, tool, method, resource, research_problem = no_connector_heuristics(phrase)
	#the next set of heuristics looks for phrase groups with just one connector
	elif len(connector_indexes) == 1:
		solution, research_problem, resource, language, tool, method = one_connector_heuristics_titled_solution(phrase, phrase_lower)
		solution, research_problem, resource, language, tool, method = one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method)
	elif len(connector_indexes) == 2:
		if connector == '1':
			solution, research_problem, resource, language, tool, method = two_connectors_process(phrase, connector_indexes)
		elif connector == '2':
			solution, research_problem, resource, language, tool, method = two_connectors_process_for_casestudy(phrase, connector_indexes)			
		else:
			solution, research_problem, resource, language, tool, method = two_connectors_process_generic(phrase, connector_indexes)
	elif len(connector_indexes) == 3:
		if connector == '3':
			solution, research_problem, resource, language, tool, method = three_connectors_process_generic(phrase, phrase_lower, connector_indexes)
		else:
			solution, research_problem, resource, language, tool, method = three_connectors_process(phrase, phrase_lower, connector_indexes)
	else:	
		if connector == '3':
			solution, research_problem, resource, language, tool, method = more_than_three_connectors_process_generic(phrase, connector_indexes)
		else:
			solution, research_problem, resource, language, tool, method = more_than_three_connectors_process(phrase, connector_indexes)
				
	return solution, research_problem, resource, language, tool, method
	