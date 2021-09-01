import re
from utils import *
from core_func import *
		
def titled_solution_elaboration_heuristics(line):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	
	i = line.find(':')
	part_0 = line[0:i]
	solution.append(part_0)
	part_1 = line[i+1:].lstrip().rstrip()
	part_1_lower = part_1.lower()
	
	connector_indexes = get_list_of_connector_indexes(part_1.lower(), connectors_rx)
	connector_indexes.sort()	
		
	#the first set of heuristics looks for phrases with no connector
	if len(connector_indexes) == 0:
		solution.append(part_1)
	elif len(connector_indexes) == 1:
		sol, research_problem, resource, language, tool, method = one_connector_heuristics_titled_solution(part_1, part_1_lower)
		if len(sol) == 1:
			solution.extend(sol)
	elif len(connector_indexes) == 2:
		part_0_1 = part_1[0:connector_indexes[0]]
		sol = get_solution(part_0_1)
		if len(sol) == 1:
			solution.extend(sol)
		
		part_1_1 = part_1[connector_indexes[0]:].lstrip()
		connector = ''
		if ' ' in part_1_1:
			connector = part_1_1[0:part_1_1.lower().find(' ')]
			i = part_1_1.find(' ')
			part_1_1 = part_1_1[i:].lstrip()		

		#we apply one connector heuristics to the second part
		connector = connector.lower()
		sol = []
		rp = []
		res = []
		lang = []
		t = []
		meth = []
		#if 'for' == connector or 'of' == connector or 'with' == connector or 'on' == connector or 'as' == connector or 'to' == connector or 'in' == connector or 'using' == connector or 'from' == connector:
		sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(part_1_1, part_1_1.lower(), connector)			
		solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	elif len(connector_indexes) == 3:		
		first_connector = part_1[connector_indexes[0]:].lstrip()
		i = first_connector.find(' ')
		first_connector = first_connector[0:i]		
		if 'of' == first_connector or first_word_ending(det_rx, part_1.lower()):
			solution_phrase = part_1[0:connector_indexes[1]]
			solution.append(solution_phrase)

			rest_of_part1 = part_1[connector_indexes[1]:].lstrip()
			i = rest_of_part1.find(' ')
			connector = rest_of_part1[0:i]
			part_1_1 = rest_of_part1[i:].lstrip()
			sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(part_1_1, part_1_1.lower(), connector)				
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)		
		else:
			part_0_1 = part_1[0:connector_indexes[0]]
			solution.append(part_0_1)
			
			part_1_1 = part_1[connector_indexes[0]:connector_indexes[1]].lstrip()
			i = part_1_1.find(' ')
			part_1_1 = part_1_1[i:].lstrip()
			lang, t, meth, res = language_or_tool_or_method_or_resource(part_1_1)
			language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
			
			part_2_1 = part_1[connector_indexes[1]:].lstrip()
			i = part_2_1.find(' ')
			connector = part_2_1[0:i]
			rest_of_part_2_1 = part_2_1[i:].lstrip()
			
			sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(rest_of_part_2_1, rest_of_part_2_1.lower(), connector)
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
	else:	
		third_connector = part_1[connector_indexes[2]:].lstrip()
		i = third_connector.find(' ')
		third_connector = third_connector[0:i]
		
		if 'of' == third_connector:
			solution_phrase = part_1[0:connector_indexes[1]]
			solution.append(solution_phrase)
		
			if len(connector_indexes) == 4:
				part_1_1 = part_1[connector_indexes[1]:connector_indexes[2]].lstrip()
				i = part_1_1.find(' ')
				part_1_1 = part_1_1[i:].lstrip()
				lang, t, meth, res = language_or_tool_or_method_or_resource(part_1_1)
				language, tool, method, resource = extend_lists(language, lang, tool, t, method, meth, resource, res)
				
				part_2_1 = part_1[connector_indexes[2]:].lstrip()
				i = part_2_1.find(' ')
				connector = part_2_1[0:i]
				rest_of_part_2_1 = part_2_1[i:].lstrip()
				
				sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(rest_of_part_2_1, rest_of_part_2_1.lower(), connector)
				solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)	
		else:			
			solution_phrase = part_1[0:connector_indexes[2]]
			solution.append(solution_phrase)
			
			#for the rest of phrase we only process the remaining phrase for those candidates with four connectors
			#the remaining phrase should have only two connectors
			
			if len(connector_indexes) == 4:
				part_1_1 = part_1[connector_indexes[2]:].lstrip()
				i = part_1_1.find(' ')
				connector = part_1_1[0:i]
				rest_of_part_1_1 = part_1_1[i:].lstrip()				
								
				sol, rp, res, lang, t, meth	= two_connectors_heuristics_titled_solution(rest_of_part_1_1, rest_of_part_1_1.lower(), connector)
				solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
						
	return solution, research_problem, resource, language, tool, method