import re
from utils import *

def one_connector_heuristics_titled_solution(part_1, part_1_lower):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []

	#solution: [solution] for [research problem]
	if contains_one_connector(part_1_lower, 'for', non_for_connectors_rx):
		solution, research_problem, resource, language = for_connector(part_1)
	elif contains_one_connector(part_1_lower, 'of', non_of_connectors_rx):
		solution, research_problem, resource, language, tool = of_connector(part_1)
	elif contains_one_connector(part_1_lower, 'using', non_using_connectors_rx) or \
	contains_one_connector(part_1_lower, 'with', non_with_connectors_rx) or \
	contains_one_connector(part_1_lower, 'by', non_by_connectors_rx):
		solution, resource, language, tool, method = using_with_by_connector(part_1)
	elif contains_one_connector(part_1_lower, 'on', non_on_connectors_rx):
		solution, research_problem, resource, language = on_connector(part_1)
	elif contains_one_connector(part_1_lower, 'from', non_from_connectors_rx):
		solution, resource = from_connector(part_1)
	elif contains_one_connector(part_1_lower, 'in', non_in_connectors_rx):
		resource, research_problem, solution, language, tool = in_connector(part_1)
	elif contains_one_connector(part_1_lower, 'through', non_through_connectors_rx) or \
	contains_one_connector(part_1_lower, 'via', non_via_connectors_rx):
		solution, research_problem, method, resource = through_via_connector(part_1)
	elif contains_one_connector(part_1_lower, 'to', non_to_connectors_rx):
		resource, research_problem, solution, language, tool, method = to_connector(part_1)
	elif contains_one_connector(part_1_lower, 'as', non_as_connectors_rx):
		resource, research_problem, solution, method = as_connector(part_1)
	return solution, research_problem, resource, language, tool, method

def two_connectors_heuristics_titled_solution(part, part_lower, connector):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []	
	
	if contains_one_connector(part_lower, 'for', non_for_connectors_rx):
		if 'on' == connector or 'in' == connector or 'using' == connector or 'from' == connector:
			language, tool, method, resource, research_problem = for_connector_phraseend(part)
		else:
			solution, research_problem, resource, language = for_connector(part)			
	elif contains_one_connector(part_lower, 'of', non_of_connectors_rx):
		if 'on' == connector or 'in' == connector or 'using' == connector or 'from' == connector or 'through' == connector or 'via' == connector:
			language, tool, method, resource, research_problem = of_connector_phraseend_heu2(part)
		else:
			solution, research_problem, resource, language, tool = of_connector_phraseend_heu1(part)
	elif contains_one_connector(part_lower, 'using', non_using_connectors_rx) or \
	contains_one_connector(part_lower, 'with', non_with_connectors_rx) or \
	contains_one_connector(part_lower, 'by', non_by_connectors_rx):
		research_problem, resource, language, tool, method = using_with_by_connector_phraseend(part)
	elif contains_one_connector(part_lower, 'on', non_on_connectors_rx):
		if 'with' == connector:
			solution, research_problem, resource, language, tool, method = on_connector_phraseend_heu2(part)
		else:
			solution, research_problem, resource, language, tool, method = on_connector_phraseend_heu1(part)
	elif contains_one_connector(part_lower, 'from', non_from_connectors_rx):
		if 'for' == connector or 'to' == connector:
			research_problem, solution, resource = from_connector_phraseend_heu1(part)
		elif 'on' == connector:
			research_problem, resource = from_connector_phraseend_heu2(part)
		else:
			research_problem, solution, resource, language, method = from_connector_phraseend_heu3(part)
	elif contains_one_connector(part_lower, 'in', non_in_connectors_rx):
		if 'on' == connector:
			resource, research_problem, language, tool, method = in_connector_phraseend_heu2(part)
		else:
			resource, research_problem, solution, language, tool = in_connector_phraseend_heu1(part)
	elif contains_one_connector(part_lower, 'through', non_through_connectors_rx) or \
	contains_one_connector(part_lower, 'via', non_via_connectors_rx):
		if 'on' == connector or 'in' == connector or 'from' == connector:
			language, research_problem, method, tool, resource = through_via_connector_phraseend_heu2(part)
		else:
			solution, research_problem, method, tool, resource, language = through_via_connector_phraseend_heu1(part)
	elif contains_one_connector(part_lower, 'to', non_to_connectors_rx):
		if 'for' == connector or 'on' == connector:
			resource, research_problem, language, tool, method = to_connector_phraseend_heu1(part)
		else:
			resource, research_problem, language, tool, method = to_connector_phraseend_heu2(part)			
	elif contains_one_connector(part_lower, 'as', non_as_connectors_rx):
		if 'with' == connector or 'on' == connector:
			resource, research_problem, solution, tool, method = as_connector_phraseend_heu2(part)
		else:
			resource, research_problem, solution, method = as_connector_phraseend_heu1(part)		
	return solution, research_problem, resource, language, tool, method		

	
def two_connectors_heuristics_generic(part, part_lower, connector):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []	
	
	if contains_one_connector(part_lower, 'for', non_for_connectors_rx):
		if 'on' == connector or 'in' == connector or 'using' == connector or 'from' == connector:
			language, tool, method, resource, research_problem = for_connector_phraseend(part)
		else:
			solution, research_problem, resource, language = for_connector(part)	
	elif contains_one_connector(part_lower, 'of', non_of_connectors_rx):
		language, tool, method, resource, research_problem = of_connector_phraseend_heu2(part)
	elif contains_one_connector(part_lower, 'using', non_using_connectors_rx) or \
	contains_one_connector(part_lower, 'with', non_with_connectors_rx) or \
	contains_one_connector(part_lower, 'by', non_by_connectors_rx):
		research_problem, resource, language, tool, method = using_with_by_connector_phraseend(part)	
	elif contains_one_connector(part_lower, 'on', non_on_connectors_rx):
		if 'with' == connector:
			solution, research_problem, resource, language, tool, method = on_connector_phraseend_heu2(part)
		else:
			solution, research_problem, resource, language, tool, method = on_connector_phraseend_heu1(part)		
	elif contains_one_connector(part_lower, 'from', non_from_connectors_rx):
		if 'for' == connector or 'to' == connector:
			research_problem, solution, resource = from_connector_phraseend_heu0(part)
		elif 'on' == connector:
			research_problem, resource = from_connector_phraseend_heu2(part)
		else:
			research_problem, solution, resource, language, method = from_connector_phraseend_heu3(part)
	elif contains_one_connector(part_lower, 'in', non_in_connectors_rx):
		if 'on' == connector:
			resource, research_problem, language, tool, method = in_connector_phraseend_heu2(part)
		else:
			resource, research_problem, solution, language, tool = in_connector_phraseend_heu1(part)
	elif contains_one_connector(part_lower, 'through', non_through_connectors_rx) or \
	contains_one_connector(part_lower, 'via', non_via_connectors_rx):	
		language, research_problem, method, tool, resource = through_via_connector_phraseend_heu2(part)
	elif contains_one_connector(part_lower, 'to', non_to_connectors_rx):
		resource, research_problem, language, tool, method = to_connector_phraseend_heu0(part)
	elif contains_one_connector(part_lower, 'as', non_as_connectors_rx):
		language, resource, research_problem, solution, tool, method = as_connector_phraseend_heu0(part)
			
	return solution, research_problem, resource, language, tool, method

	
def two_connectors_heuristics_generic_all(part, part_lower, connector):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []	

	if contains_one_connector(part_lower, 'for', non_for_connectors_rx):
		language, tool, method, resource, research_problem = for_connector_phraseend(part)
	elif contains_one_connector(part_lower, 'of', non_of_connectors_rx):
		language, tool, method, resource, research_problem = of_connector_phraseend_heu2(part)
	elif contains_one_connector(part_lower, 'using', non_using_connectors_rx) or \
	contains_one_connector(part_lower, 'with', non_with_connectors_rx) or \
	contains_one_connector(part_lower, 'by', non_by_connectors_rx):
		research_problem, resource, language, tool, method = using_with_by_connector_phraseend(part)	
	elif contains_one_connector(part_lower, 'on', non_on_connectors_rx):
		if 'with' == connector:
			research_problem, resource, language, tool, method = on_connector_phraseend_heu2(part)
		else:
			research_problem, resource, language, tool, method = on_connector_phraseend_heu1(part)		
	elif contains_one_connector(part_lower, 'from', non_from_connectors_rx):
			research_problem, resource = from_connector_phraseend_heu2(part)
	elif contains_one_connector(part_lower, 'in', non_in_connectors_rx):
		resource, research_problem, language, tool, method = in_connector_phraseend_heu2(part)
	elif contains_one_connector(part_lower, 'through', non_through_connectors_rx) or \
	contains_one_connector(part_lower, 'via', non_via_connectors_rx):
		language, research_problem, method, tool, resource = through_via_connector_phraseend_heu2(part)
	elif contains_one_connector(part_lower, 'to', non_to_connectors_rx):
		resource, research_problem, language, tool, method = to_connector_phraseend_heu0(part)
	elif contains_one_connector(part_lower, 'as', non_as_connectors_rx):
		language, resource, research_problem, solution, tool, method = as_connector_phraseend_heu0(part)
			
	return solution, research_problem, resource, language, tool, method
		
def last_part_of_phrase_heu_of_special(part, connector):
	solution = []
	research_problem = []	
	resource = []	
	language = []
	tool = []
	method = []
	
	if ' of ' in part:
		parts = part.split(' of ')
		research_problem, method, resource = something_of_something_no_solution(parts[0], parts[1])
	else:
		solution, research_problem, resource, language, tool, method = two_connectors_heuristics_generic(part, part.lower(), connector)
		if len(solution) == 1:
			rp, lang, t, meth, res = rp_or_language_or_tool_or_method_or_resource(solution[0])
			research_problem, language, tool, method, resource = extend_lists_five(research_problem, rp, language, lang, tool, t, method, meth, resource, res)
			solution = []
	
	return solution, research_problem, resource, language, tool, method
	
def last_part_of_phrase_heu(part):
	language = []
	tool = []
	research_problem = []
	method = []
	resource = []

	if is_language(part):
		language.append(part)
	elif is_tool(part):
		tool.append(part)
	elif is_research_problem(part):
		research_problem.append(part)
	elif is_method(part):
		method.append(part)
	elif is_resource(part.lower()):
		resource.append(part)
		
	return language, tool, research_problem, method, resource

def something_of_something_no_solution(part_1, part_2):
	phrase = part_1 + ' of ' + part_2
	phrase_lower = phrase.lower()
	
	research_problem = []
	method = []
	resource = []	
	
	if is_tool(phrase) or is_method(phrase):
		method.append(phrase)
	elif is_research_problem(phrase) or is_research_problem(part_1):
		research_problem.append(phrase)
	elif is_method(part_1) or is_tool(part_1):
		method.append(phrase)
	elif is_resource(phrase_lower):
		resource.append(phrase)
	
	return research_problem, method, resource
	
def something_of_something(part_1, part_2):
	phrase = part_1 + ' of ' + part_2
	phrase_lower = phrase.lower()
	
	solution = []
	research_problem = []
	method = []
	resource = []
	
	if not 'problem' in phrase_lower and (is_tool(phrase) or is_method(phrase)):
		solution.append(phrase)
	elif is_research_problem(phrase) or is_research_problem(part_1):
		research_problem.append(phrase)
	elif is_method(part_1) or is_tool(part_1):
		method.append(phrase)
	elif is_resource(phrase_lower) and not ' of ' in phrase:
		resource.append(phrase)
	else:
		phrase = remove_and_ending(phrase)		
		solution.append(phrase)
	
	return solution, research_problem, method, resource

def using_with_by_connector(phrase):
	solution = []
	resource = []
	language = []
	tool = []
	method = []
	if ' using ' in phrase.lower():
		phrase = phrase.replace(' Using ', ' using ').replace(' USING ', ' using ')
	elif ' with ' in phrase.lower():
		phrase = phrase.replace(' With ', ' with ').replace(' WITH ', ' with ')	
	else:
		phrase = phrase.replace(' By ', ' by ').replace(' BY ', ' by ')
	
	parts = phrase.split(' using ') if ' using ' in phrase \
	else (phrase.split(' with ') if ' with ' in phrase \
	else phrase.split(' by '))
	
	if not non_content(parts[0], parts[0].lower()):
		parts[0] = remove_and_ending(parts[0])
		solution.append(parts[0])
	lang, t, meth, res = language_or_tool_or_method_or_resource(parts[1])
	language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
	
	return solution, resource, language, tool, method

def using_with_by_connector_phraseend(phrase):
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	if ' using ' in phrase.lower():
		phrase = phrase.replace(' Using ', ' using ').replace(' USING ', ' using ')
	elif ' with ' in phrase.lower():
		phrase = phrase.replace(' With ', ' with ').replace(' WITH ', ' with ')	
	else:
		phrase = phrase.replace(' By ', ' by ').replace(' BY ', ' by ')
	
	parts = phrase.split(' using ') if ' using ' in phrase \
	else (phrase.split(' with ') if ' with ' in phrase \
	else phrase.split(' by '))
	
	if not non_content(parts[0], parts[0].lower()):
		parts[0] = remove_and_ending(parts[0])
		language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(parts[0])
			
	lang, t, meth, res = language_or_tool_or_method_or_resource(parts[1])
	language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
	
	return research_problem, resource, language, tool, method
	
def of_connector(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	phrase = phrase.replace(' Of ', ' of ').replace(' OF ', ' of ')
	i = phrase.find(' of ')
	phrase_lower = phrase.lower()
	
	#some patterns are hard-coded
	if 'part of speech' in phrase_lower:
		phrase = remove_and_ending(phrase)
		solution.append(phrase)
	#otherwise generically applied
	else:
		subparts_0 = phrase[0:i]
		if not non_content(subparts_0, subparts_0.lower()):
			subparts_0 = remove_and_ending(subparts_0)
			solution.append(subparts_0)
		subparts_1 = phrase[i+len(' of '):]	
		if is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		else:
			res, sol, lang = resource_or_solution_or_language(subparts_1)
			resource, solution, language, research_problem = extend_lists(resource, res, solution, sol, language, lang, research_problem, [])
		
	return solution, research_problem, resource, language, tool

def of_connector_phraseend_heu1(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	phrase = phrase.replace(' Of ', ' of ').replace(' OF ', ' of ')
	i = phrase.find(' of ')
	phrase_lower = phrase.lower()
	
	#some patterns are hard-coded
	if 'part of speech' in phrase_lower or 'wizard of oz' in phrase_lower or \
	('semeval' in phrase_lower and 'analysis of' in phrase_lower):
		phrase = remove_and_ending(phrase)
		research_problem.append(phrase)
	elif 'scope of' in phrase_lower or 'thousands of' in phrase_lower or 'game of thrones' in phrase_lower:
		res, sol, lang = resource_or_solution_or_language(phrase)
		resource, solution, language, research_problem = extend_lists(resource, res, solution, [], language, lang, research_problem, sol)
	#otherwise generically applied
	else:
		subparts_0 = phrase[0:i]
		if not non_content(subparts_0, subparts_0.lower()):
			if is_research_problem(subparts_0):
				research_problem.append(subparts_0)
			else:
				subparts_0 = remove_and_ending(subparts_0)
				solution.append(subparts_0)
		subparts_1 = phrase[i+len(' of '):]	
		if is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		else:
			res, sol, lang = resource_or_solution_or_language(subparts_1)
			resource, solution, language, research_problem = extend_lists(resource, res, solution, sol, language, lang, research_problem, [])
		
	return solution, research_problem, resource, language, tool
	
def of_connector_phraseend_heu2(phrase):
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	phrase = phrase.replace(' Of ', ' of ').replace(' OF ', ' of ')
	phrase_lower = phrase.lower()
	
	#some patterns are hard-coded
	if 'web of facts' in phrase_lower or 'game of thrones' in phrase_lower or 'the university of' in phrase_lower:
		phrase = remove_and_ending(phrase)
		resource.append(phrase)
	#otherwise generically applied
	else:
		i = phrase.find(' of ')	
		subparts_0 = phrase[0:i]
		if not non_content(subparts_0, subparts_0.lower()):		
			lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(subparts_0)
			language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
				
		subparts_1 = phrase[i+len(' of '):]	
		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
						
	return language, tool, method, resource, research_problem

def applied_to_connector(phrase):
	tool = []
	solution = []
	research_problem = []
	resource = []
	language = []

	phrase = phrase.replace(' Applied to ', ' applied to ')
	i = phrase.find(' applied to ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' applied to '):]
	
	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0):
			tool.append(subparts_0)
		else:
			subparts_0 = remove_and_ending(subparts_0)
			solution.append(subparts_0)
	
	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)		
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)
		
	return tool, solution, research_problem, resource, language
		
def for_connector(phrase):
	solution = []
	research_problem = []
	resources = []
	language = []
	
	phrase = phrase.replace(' For ', ' for ').replace(' FOR ', ' for ')
	i = phrase.find(' for ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' for '):]
	
	if not non_content(subparts_0, subparts_0.lower()):
		subparts_0 = remove_and_ending(subparts_0)	
		solution.append(subparts_0)
		
	if is_language(subparts_1):
		language.append(subparts_1)
	elif resources_lite(subparts_1):
		resources.append(subparts_1)
	else:
		subparts_1 = remove_and_ending(subparts_1)	
		research_problem.append(subparts_1)
		
	return solution, research_problem, resources, language	
	
def for_connector_phraseend(phrase):
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	
	phrase = phrase.replace(' For ', ' for ').replace(' FOR ', ' for ')
	i = phrase.find(' for ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' for '):]
	
	if not non_content(subparts_0, subparts_0.lower()):		
		language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(subparts_0)
		
	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1):
		resource.append(subparts_1)
		
	return language, tool, method, resource, research_problem
	
def on_connector(phrase):
	solution = []
	research_problem = []
	resources = []
	language = []
	
	phrase = phrase.replace(' On ', ' on ').replace(' ON ', ' on ')
	i = phrase.find(' on ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' on '):]

	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0) or is_method(subparts_0):
			solution.append(subparts_0)	
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		else:
			subparts_0 = remove_and_ending(subparts_0)
			solution.append(subparts_0)
	
	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resources.append(subparts_1)
	else:
		subparts_1 = remove_and_ending(subparts_1)	
		research_problem.append(subparts_1)
		
	return solution, research_problem, resources, language	
	
def on_connector_phraseend_heu1(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	
	phrase = phrase.replace(' On ', ' on ').replace(' ON ', ' on ')
	i = phrase.find(' on ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' on '):]

	if not non_content(subparts_0, subparts_0.lower()):
		if is_language(subparts_0):
			language.append(subparts_0)
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif is_resource(subparts_0.lower()):
			resource.append(subparts_0)
	
	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_tool(subparts_1):
		tool.append(subparts_1)
	elif is_method(subparts_1):
		method.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)
	else:
		subparts_1 = remove_and_ending(subparts_1)	
		research_problem.append(subparts_1)
		
	return solution, research_problem, resource, language, tool, method

def on_connector_phraseend_heu2(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	
	phrase = phrase.replace(' On ', ' on ').replace(' ON ', ' on ')
	i = phrase.find(' on ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' on '):]

	if not non_content(subparts_0, subparts_0.lower()):
		language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(subparts_0)
	
	lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(subparts_1)
	language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)
		
	return solution, research_problem, resource, language, tool, method
	
def from_connector(phrase):
	solution = []
	resources = []

	phrase = phrase.replace(' From ', ' from ').replace(' FROM ', ' from ')
	i = phrase.find(' from ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' from '):]	
	
	subparts_0 = remove_and_ending(subparts_0)
	solution.append(subparts_0)
	subparts_1 = remove_and_ending(subparts_1)
	resources.append(subparts_1)
	
	return solution, resources

def from_connector_phraseend_heu0(phrase):
	research_problem = []
	solution = []
	resources = []

	phrase = phrase.replace(' From ', ' from ').replace(' FROM ', ' from ')
	i = phrase.find(' from ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' from '):]	
	
	if not non_content(subparts_0, subparts_0.lower()):
		if first_word_ending('ing', subparts_0.lower()):
			solution.append(subparts_0)
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif is_resource(subparts_0.lower()):
			resources.append(subparts_0)
	subparts_1 = remove_and_ending(subparts_1)
	resources.append(subparts_1)
	
	return research_problem, solution, resources
	
def from_connector_phraseend_heu1(phrase):
	research_problem = []
	solution = []
	resources = []

	phrase = phrase.replace(' From ', ' from ').replace(' FROM ', ' from ')
	i = phrase.find(' from ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' from '):]	
	
	if not non_content(subparts_0, subparts_0.lower()):
		if first_word_ending('ing', subparts_0.lower()):
			solution.append(subparts_0)
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
	subparts_1 = remove_and_ending(subparts_1)			
	resources.append(subparts_1)
	
	return research_problem, solution, resources

def from_connector_phraseend_heu2(phrase):
	research_problem = []
	resource = []

	phrase = phrase.replace(' From ', ' from ').replace(' FROM ', ' from ')
	i = phrase.find(' from ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' from '):]	
	
	if not non_content(subparts_0, subparts_0.lower()):
		if is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif is_resource(subparts_0.lower()):
			resource.append(subparts_0)
	subparts_1 = remove_and_ending(subparts_1)
	resource.append(subparts_1)
	
	return research_problem, resource	
	
def from_connector_phraseend_heu3(phrase):
	research_problem = []
	solution = []
	resource = []
	language = []
	method = []

	phrase = phrase.replace(' From ', ' from ').replace(' FROM ', ' from ')
	i = phrase.find(' from ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' from '):]	
	
	if not non_content(subparts_0, subparts_0.lower()):
		if is_language(subparts_0):
			language.append(subparts_0)
		elif is_resource(subparts_0.lower()):
			resource.append(subparts_0)
		elif first_word_ending('ing', subparts_0.lower()):
			solution.append(subparts_0)
		elif is_method(subparts_0):
			method.append(subparts_0)
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
	subparts_1 = remove_and_ending(subparts_1)
	resource.append(subparts_1)
	
	return research_problem, solution, resource, language, method
	
def in_connector(phrase):
	resource = []
	research_problem = []
	solution = []
	language = []
	tool = []

	phrase = phrase.replace(' In ', ' in ').replace(' IN ', ' in ')
	i = phrase.find(' in ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' in '):]	

	if not non_content(subparts_0, subparts_0.lower()):
		if is_tool(subparts_0) or is_method(subparts_0) or is_research_problem(subparts_0) or is_resource(subparts_0.lower()):
			solution.append(subparts_0)	

	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_tool(subparts_1):
		tool.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)

	return resource, research_problem, solution, language, tool

def in_connector_phraseend_heu1(phrase):
	resource = []
	research_problem = []
	solution = []
	language = []
	tool = []

	if ':' in phrase:
		phrase_parts = phrase.split(':')

		if 'in' in phrase_parts[0].lower():
			phrase = phrase_parts[0]
		elif 'in' in phrase_parts[1].lower():
			phrase = phrase_parts[1]
		else:
			return resource, research_problem, solution, language, tool
	
	phrase = phrase.replace(' In ', ' in ').replace(' IN ', ' in ')
	i = phrase.find(' in ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' in '):]	

	if not non_content(subparts_0, subparts_0.lower()):
		if is_language(subparts_0):
			language.append(subparts_0)	
		elif is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif is_tool(subparts_0) or is_method(subparts_0):
			solution.append(subparts_0)	
		elif is_resource(subparts_0.lower()):
			resource.append(subparts_0)

	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_tool(subparts_1):
		tool.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)

	return resource, research_problem, solution, language, tool	
	
def in_connector_phraseend_heu2(phrase):
	resource = []
	research_problem = []
	language = []
	tool = []
	method = []

	if ':' in phrase:
		phrase_parts = phrase.split(':')

		if 'in' in phrase_parts[0].lower():
			phrase = phrase_parts[0]
		elif 'in' in phrase_parts[1].lower():
			phrase = phrase_parts[1]
		else:
			return resource, research_problem, solution, language, tool
	
	phrase = phrase.replace(' In ', ' in ').replace(' IN ', ' in ')
	i = phrase.find(' in ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' in '):]	

	if not non_content(subparts_0, subparts_0.lower()):
		if is_research_problem(subparts_0):
			research_problem.append(subparts_0)
		elif is_tool(subparts_0):
			tool.append(subparts_0)
		elif is_method(subparts_0):
			method.append(subparts_0)	
		elif is_resource(subparts_0.lower()):
			resource.append(subparts_0)

	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_tool(subparts_1):
		tool.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)

	return resource, research_problem, language, tool, method
	
def through_via_connector(phrase):
	solution = []
	research_problem = []
	method = []
	tool = []
	resource = []

	if ' through ' in phrase.lower():
		phrase = phrase.replace(' Through ', ' through ').replace(' THROUGH ', ' through ')
	else:
		phrase = phrase.replace(' Via ', ' via ').replace(' VIA ', ' via ')
	i = phrase.find(' through ') if ' through ' in phrase \
	else phrase.find(' via ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' through '):] if ' through ' in phrase \
	else phrase[i+len(' via '):]

	if not non_content(subparts_0, subparts_0.lower()):
		subparts_0 = remove_and_ending(subparts_0)
		solution.append(subparts_0)

	if is_method(subparts_1):
		method.append(subparts_1)
	elif is_tool(subparts_1):
		tool.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)

	return solution, research_problem, method, resource

def through_via_connector_phraseend_heu1(phrase):
	solution = []
	research_problem = []
	method = []
	tool = []
	resource = []
	language = []

	if ' through ' in phrase.lower():
		phrase = phrase.replace(' Through ', ' through ').replace(' THROUGH ', ' through ')
	else:
		phrase = phrase.replace(' Via ', ' via ').replace(' VIA ', ' via ')
	i = phrase.find(' through ') if ' through ' in phrase \
	else phrase.find(' via ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' through '):] if ' through ' in phrase \
	else phrase[i+len(' via '):]

	if not non_content(subparts_0, subparts_0.lower()):
		if first_word_ending('ing', subparts_0.lower()):
			solution.append(subparts_0)
		else:
			subparts_0 = remove_and_ending(subparts_0)
			research_problem.append(subparts_0)

	if is_language(subparts_1):
		language.append(subparts_1)
	elif is_method(subparts_1):
		method.append(subparts_1)
	elif is_tool(subparts_1):
		tool.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)

	return solution, research_problem, method, tool, resource, language

def through_via_connector_phraseend_heu2(phrase):
	language = []
	research_problem = []
	method = []
	tool = []
	resource = []

	if ' through ' in phrase.lower():
		phrase = phrase.replace(' Through ', ' through ').replace(' THROUGH ', ' through ')
	else:
		phrase = phrase.replace(' Via ', ' via ').replace(' VIA ', ' via ')
	i = phrase.find(' through ') if ' through ' in phrase \
	else phrase.find(' via ')
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' through '):] if ' through ' in phrase \
	else phrase[i+len(' via '):]

	if not non_content(subparts_0, subparts_0.lower()):
		language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(subparts_0)
	
	lang, t, meth, res, rp = language_or_tool_or_method_or_resource_or_rp(subparts_1)
	language, tool, method, resource, research_problem = extend_lists_five(language, lang, tool, t, method, meth, resource, res, research_problem, rp)

	return language, research_problem, method, tool, resource
	
def to_connector(phrase):
	resource = []
	research_problem = []
	solution = []
	language = []
	tool = []
	method = []

	if 'end to end' in phrase.lower():
		phrase = remove_and_ending(phrase)	
		solution.append(phrase)
	else:
		phrase = phrase.replace(' To ', ' to ').replace(' TO ', ' to ')
		i = phrase.find(' to ')
		subparts_0 = phrase[0:i]
		subparts_1 = phrase[i+len(' to '):]	

		if not non_content(subparts_0, subparts_0.lower()):
			if begins_phrase('[Uu]sing', subparts_0):
				i = subparts_0.find(' ')
				subparts_0 = subparts_0[i:].lstrip()
				if is_tool(subparts_0):
					tool.append(subparts_0)
				elif is_method(subparts_0):
					method.append(subparts_0)
				elif is_resource(subparts_0.lower()):
					resource.append(subparts_0)
				else:
					subparts_0 = remove_and_ending(subparts_0)
					solution.append(subparts_0)
			else:
				subparts_0 = remove_and_ending(subparts_0)
				solution.append(subparts_0)

		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)

	return resource, research_problem, solution, language, tool, method

def to_connector_phraseend_heu0(phrase):
	resource = []
	research_problem = []
	language = []
	tool = []
	method = []
	solution = []

	if 'end to end' in phrase.lower():
		phrase = remove_and_ending(phrase)
		solution.append(phrase)
	else:
		phrase = phrase.replace(' To ', ' to ').replace(' TO ', ' to ')
		i = phrase.find(' to ')
		subparts_0 = phrase[0:i]
		subparts_1 = phrase[i+len(' to '):]	

		if not non_content(subparts_0, subparts_0.lower()):
			if is_language(subparts_0):
				language.append(subparts_0)
			elif is_resource(subparts_0.lower()):
				resource.append(subparts_0)
			elif is_research_problem(subparts_0):
				research_problem.append(subparts_0)
			elif is_tool(subparts_0):
				tool.append(subparts_0)
			elif is_method(subparts_0):
				method.append(subparts_0)

		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)			
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)

	return resource, research_problem, language, tool, method
	
def to_connector_phraseend_heu1(phrase):
	resource = []
	research_problem = []
	language = []
	tool = []
	method = []

	if 'end to end' in phrase.lower():
		phrase = remove_and_ending(phrase)	
		solution.append(phrase)
	else:
		phrase = phrase.replace(' To ', ' to ').replace(' TO ', ' to ')
		i = phrase.find(' to ')
		subparts_0 = phrase[0:i]
		subparts_1 = phrase[i+len(' to '):]	

		if len(subparts_0.split(' ')) > 1 and not non_content(subparts_0, subparts_0.lower()):
			subparts_0 = remove_and_ending(subparts_0)		
			research_problem.append(subparts_0)

		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)

	return resource, research_problem, language, tool, method
	
def to_connector_phraseend_heu2(phrase):
	resource = []
	research_problem = []
	language = []
	tool = []
	method = []

	if 'sequence to sequence' in phrase.lower():
		phrase = remove_and_ending(phrase)	
		resource.append(phrase)		
	else:
		phrase = phrase.replace(' To ', ' to ').replace(' TO ', ' to ')
		i = phrase.find(' to ')
		subparts_0 = phrase[0:i]
		subparts_1 = phrase[i+len(' to '):]	

		if not non_content(subparts_0, subparts_0.lower()):
			if is_language(subparts_0):
				language.append(subparts_0)
			elif is_resource(subparts_0.lower()):
				resource.append(subparts_0)
			elif len(subparts_0.split(' ')) > 1:
				research_problem.append(subparts_0)

		if is_language(subparts_1):
			language.append(subparts_1)
		elif is_tool(subparts_1):
			tool.append(subparts_1)
		elif is_method(subparts_1):
			method.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)

	return resource, research_problem, language, tool, method	
	
def as_connector(phrase):
	resource = []
	research_problem = []
	solution = []
	method = []
	
	phrase = phrase.replace(' As ', ' as ').replace(' AS ', ' as ')
	i = phrase.find(' as ')	
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' as '):]	
	
	if is_method(subparts_0) and is_method(subparts_1):
		subparts_0 = remove_and_ending(subparts_0)	
		method.append(subparts_0)
		subparts_1 = remove_and_ending(subparts_1)
		solution.append(subparts_1)
	else:
		if is_method(subparts_0):
			method.append(subparts_0)
		elif is_resource(subparts_0.lower()):
			solution.append(subparts_0)
		else:
			subparts_0 = remove_and_ending(subparts_0)		
			solution.append(subparts_0)
		
		if is_method(subparts_1):
			method.append(subparts_1)
		elif len(solution) == 0:
			solution.append(subparts_1)
		elif is_research_problem(subparts_1):
			research_problem.append(subparts_1)
		elif is_resource(subparts_1.lower()):
			resource.append(subparts_1)

	return resource, research_problem, solution, method

def as_connector_phraseend_heu0(phrase):
	language = []
	resource = []
	research_problem = []
	solution = []
	tool = []
	method = []

	phrase = phrase.replace(' As ', ' as ').replace(' AS ', ' as ')
	i = phrase.find(' as ')	
	subparts_0 = phrase[0:i]
	subparts_1 = phrase[i+len(' as '):]		
	
	language, tool, method, resource, research_problem = language_or_tool_or_method_or_resource_or_rp(subparts_0)
	
	if is_method(subparts_1):
		method.append(subparts_1)
	elif is_research_problem(subparts_1):
		research_problem.append(subparts_1)
	elif is_resource(subparts_1.lower()):
		resource.append(subparts_1)	
	else:
		subparts_1 = remove_and_ending(subparts_1)
		solution.append(subparts_1)		
		
	return language, resource, research_problem, solution, tool, method	
	
def as_connector_phraseend_heu1(phrase):
	resource = []
	research_problem = []
	solution = []
	tool = []
	method = []
	
	resource, research_problem, solution, method = as_connector(phrase)
	
	if len(solution) == 1 and not first_word_ending('ing', solution[0].lower()):
		if is_resource(solution[0].lower()):
			resource.append(solution[0])
			solution = []
		else:
			research_problem.append(solution[0])
			solution = []
	if len(method) == 1:
		if first_word_ending('ing', method[0].lower()):
			solution.append(method[0])
			method = []
		elif is_research_problem(method[0]):
			research_problem.append(method[0])
			method = []
		
	return resource, research_problem, solution, method
	
def as_connector_phraseend_heu2(phrase):
	resource = []
	research_problem = []
	solution = []
	tool = []
	method = []
	
	resource, research_problem, solution, method = as_connector(phrase)
	
	if len(solution) == 1 and not first_word_ending('ing', solution[0].lower()):
		if is_resource(solution[0].lower()):
			resource.append(solution[0])
			solution = []
		else:
			research_problem.append(solution[0])
			solution = []
	if len(method) == 1:
		if first_word_ending('ing', method[0].lower()):
			solution.append(method[0])
			method = []
		elif is_research_problem(method[0]):
			research_problem.append(method[0])
			method = []
		
	phrase = phrase.replace(' As ', ' as ').replace(' AS ', ' as ')
	i = phrase.find(' as ')	
	subparts_1 = phrase[i+len(' as '):]			
	
	if not (subparts_1 in resource or subparts_1 in research_problem or subparts_1 in solution or subparts_1 in method):
		if is_tool(subparts_1):
			tool.append(subparts_1)
		
	return resource, research_problem, solution, tool, method	
	
def get_solution(phrase):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	solution, research_problem, resource, language, tool, method = get_scientific_knowledge_elements_all(phrase)
	if len(tool) == 1:
		solution.append(tool[0])
		tool = []
	elif len(method) == 1:
		solution.append(method[0])
		method = []
	elif len(research_problem) == 1:
		solution.append(research_problem[0])
		research_problem = []
	elif len(resource) == 1:
		solution.append(resource[0])
		resource = []
	return solution