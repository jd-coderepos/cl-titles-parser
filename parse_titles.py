import sys
import re
from filters import *
from utils import *
from core_func_titled_solution import *
from generic_core_func import *

def filter(line):
	if question(line): return True
	elif creative(line): return True
	elif proc_overview(line): return True
	elif meeting(line): return True
	elif conference(line): return True
	elif admin_reports(line): return True
	elif review(line): return True
	elif paper_parts(line): return True
	elif institute(line): return True
	elif non_english(line): return True
	return False

def update_rules_statistics(rules_statistics, rule_name):
	if rule_name in rules_statistics:
		count = rules_statistics[rule_name]
		count = count+1
		rules_statistics[rule_name] = count
	else:
		rules_statistics[rule_name] = 1
	return rules_statistics	
	
def parse_line(line, rules_statistics):
	toks = line.split(' ')
	line_lower = line.lower()
	research_problem = []
	solution = []
	resource = []
	language = []
	tool = []
	method = []
												
	#revisit here
	#elif begins_phrase(question_words, line.lower()) or '?' in line:
		#print(line)
		#print()
	#template
	#PHINC: A Parallel Hinglish Social Media Code-Mixed Corpus for Machine Translation
	#Hypernym-LIBre: A Free Web-based Corpus for Hypernym Detection
	#TOCP: A Dataset for Chinese Profanity Processing
	#FlorUniTo@TRAC-2: Retrofitting Word Embeddings on an Abusive Lexicon for Aggressive Language Detection	
	if re.match("[^ ]*?([a-z][A-Z]|[A-Z][A-Z]|\d+)[^ ]*?:", line):
		#-----------
		#done
		#-----------
		solution, research_problem, resource, language, tool, method = titled_solution_elaboration_heuristics(line)
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule1")
	#semantic rule 1	
	#Using the NITE XML Toolkit on the Switchboard Corpus to Study Syntactic Choice
	#Example
	#Using a Probabilistic Class-Based Lexicon for Lexical Ambiguity Resolution
	#Using [resource] for [research problem]	
	#Toward a Task-based Gold Standard for Evaluation of NP Chunks and Technical Terms
	#Toward a Bilingual Legal Term Glossary from Context Profiles	
	elif re.match('Using', line) or begins_phrase('Toward', line):
		if 'using' in line.lower():
			i = line.find(' ')+1
			line = line[i:]
		line_lower = line.lower()	
		solution, research_problem, resource, language, tool, method = extract_title_elements(line, line_lower, '1')
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule2")
	#semantic rule 2
	#... : a case study
	elif ending(line_lower, ': (a )?case study'):		
		phrase = line.split(':')[0].strip()
		phrase_lower = phrase.lower()
		
		solution, research_problem, resource, language, tool, method = extract_title_elements(phrase, phrase_lower, '2')		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule3")
	#semantic rule 3
	#...: a case study ...
	#...: the case of ...
	elif re.match('^.*:( a)? case study', line_lower) or re.match('^.*:( the)? case of', line_lower):	
		parts = line.split(':')	
		
		phrase = parts[0].strip()
		phrase_lower = phrase.lower()		
		solution, research_problem, resource, language, tool, method = extract_title_elements(phrase, phrase_lower, '2')
		
		#A Case Study on Verb-particles
		#A Case Study Using the TREC 2002 Question Answering Track
		#the Case of Amharic
		#the case of the Linguistic Crescent varieties
		parts[1] = parts[1].lstrip()
		
		if 'the case of' in parts[1].lower():
			i = parts[1].find('of ')
			phrase = parts[1][i:].lstrip()
			
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()

			sol, rp, res, lang, t, meth = extract_title_elements(phrase, phrase.lower(), '2')
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
		else:
			connector_indexes = get_list_of_connector_indexes(parts[1].lower(), connectors_rx)
			connector_indexes.sort()
			
			if len(connector_indexes) > 0:
				phrase = parts[1][connector_indexes[0]:].lstrip()
				if ' ' in phrase:
					i = phrase.find(' ')
					phrase = phrase[i:].lstrip()
				
				sol, rp, res, lang, t, meth = extract_title_elements(phrase, phrase.lower(), '2')
				solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
				
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule3")
	#semantic rule 4
	#A Case Study on Inter-Annotator Agreement for Word Sense Disambiguation
	elif re.match('(a )?case study ', line.lower()):			
		connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
		connector_indexes.sort()
								
		if len(connector_indexes) > 0:
			phrase = line[connector_indexes[0]:].lstrip()
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()
			
			sol, rp, res, lang, t, meth = extract_title_elements(phrase, phrase.lower(), '2')
			solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
		else:			
			i = line.lower().find('study ')
			phrase = line[i:].strip()
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()			
			if not phrase == '':
				language, tool, method, resource, research_problem = no_connector_heuristics(phrase)
				
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule4")
	elif re.match('(a )?case study:', line.lower()):		
		i = line.find(':')
		phrase = line[i:].strip()
		
		if ' ' in phrase:
			i = phrase.find(' ')
			phrase = phrase[i:].lstrip()
		
		sol, rp, res, lang, t, meth = extract_title_elements(phrase, phrase.lower(), '2')
		solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule4")
	elif re.match('some ', line.lower()):		
		solution, research_problem, resource, language, tool, method = extract_title_elements(line, line.lower(), '2')
		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule7")
	elif ':' in line:			
		parts = line.split(':')
				
		phrase = parts[0].strip()
		phrase_lower = phrase.lower()		
		solution, research_problem, resource, language, tool, method = extract_title_elements(phrase, phrase_lower, '1')
		
		# if 'Tweeki' in phrase:
			# print(len(solution) == 0 and len(research_problem) == 0 and len(resource) == 0 and len(language) == 0 and len(tool) == 0 and len(method) == 0)
			# print(not ' ' in phrase)
			# solution.append(phrase)
		
		if len(solution) == 0 and len(research_problem) == 0 and len(resource) == 0 and len(language) == 0 and len(tool) == 0 and len(method) == 0:
			if not ' ' in phrase:
				solution.append(phrase)
		
		#postprocess the result
		if not len(tool) == 0:
			solution.append(tool[0])
			tool = []
		
		parts[1] = parts[1].lstrip()
		
		sol, rp, res, lang, t, meth = extract_title_elements(parts[1], parts[1].lower(), '2')
		solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule5")
	elif 'applied to' in line_lower:	
		tool, solution, research_problem, resource, language = applied_to_connector(line)
		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule6")
	elif non_content_start(line.lower()):		
		connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
		if len(connector_indexes) > 0:
			phrase = line[0:connector_indexes[0]]
			if len(phrase.split(' ')) > 2:
				if is_tool(phrase) or is_method(phrase):
					solution.append(phrase)
		
			phrase = line[connector_indexes[0]:].lstrip()
			if ' ' in phrase:
				i = phrase.find(' ')
				phrase = phrase[i:].lstrip()
		
			sol, research_problem, resource, language, tool, method = extract_title_elements(phrase, phrase.lower(), '2')
			if len(sol) > 0:
				solution.extend(sol)				
		else:
			solution.append(line)
			
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule7")
	elif begins_phrase('Description of', line):	
	
		line = line.replace('Description of ', '')
		solution, research_problem, resource, language = for_connector(line)
		
		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule8")
	else:	
		connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)			
				
		if len(connector_indexes) == 0:	
			if is_tool(line) or is_method(line) or is_resource(line.lower()) or is_research_problem(line):
				solution.append(line)
		else:			
			if 'the case of' in line.lower():
				i = line.lower().find('the case of')
				i_end = i+len('the case of')
				
				to_replace = line[i:i_end]
				line = line.replace(' '+to_replace+' ', ' ')	
				connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
				
			if len(connector_indexes) == 1:			
				solution, research_problem, resource, language, tool, method = extract_title_elements(line, line_lower, '1')			
			elif len(connector_indexes) == 2:				
				solution, research_problem, resource, language, tool, method = extract_title_elements(line, line_lower, '3')				
			elif len(connector_indexes) == 3:
				solution, research_problem, resource, language, tool, method = extract_title_elements(line, line_lower, '3')
			else:
				solution, research_problem, resource, language, tool, method = extract_title_elements(line, line_lower, '3')

		if len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0:
			rules_statistics = update_rules_statistics(rules_statistics, "rule9")
				
	if len(language) == 1 and 'nested ner' in language[0].lower():
		print(line)
		
	return solution, research_problem, resource, language, method, tool

def write_out(out_file, values, type):
	out_file.write('TOTAL UNIQUE '+type+': '+str(len(values))+'\n\n')
	for v in values:
		out_file.write(v+'\n')

def write_out_list(out_file, values):
	for v in values:
		out_file.write(v+'\n')
		
def read_file(input_file, output_dir):
	research_problem = []
	solution = []
	resource = []
	language = []
	tool = []
	method = []

	rules_statistics = {}	
	
	titles_count = 0
	solution_count = 0
	research_problem_count = 0
	resource_count = 0
	language_count = 0
	method_count = 0
	tool_count = 0
	
	raw_count = 0
	
	output_file = open(output_dir+'/parsed-titles-full-output.dat', 'w', encoding='utf-8')
		
	with open(input_file, 'r', encoding='utf-8') as f:
		while(True):
			line = f.readline().rstrip("\n")
			if line:

				raw_count = raw_count + 1
								
				if (filter(line)): continue
				
				title = preprocess(line)
				
				if '' == title:
					continue
				elif len(title.split(' ')) <= 4:
					continue			
							
				sol, rp, res, lang, meth, t = parse_line(title, rules_statistics)
				output_file.write(title+'\n')
				output_file.write('research_problem: '+str(rp)+'\n')
				output_file.write('solution: '+str(sol)+'\n')
				output_file.write('resource: '+str(res)+'\n')
				output_file.write('language: '+str(lang)+'\n')
				output_file.write('tool: '+str(t)+'\n')
				output_file.write('method: '+str(meth)+'\n\n')
				
				solution, research_problem, resource, language, tool, method = extend_lists_all(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth)
				
				titles_count = titles_count + 1			
				
			else:			
				break
	
	write_out_list(open(output_dir+'/solutions-list.dat', 'w', encoding='utf-8'), solution)
	v = set(solution)
	write_out(open(output_dir+'/solutions.dat', 'w', encoding='utf-8'), v, 'solutions')
	
	write_out_list(open(output_dir+'/research_problem_list.dat', 'w', encoding='utf-8'), research_problem)
	v = set(research_problem)
	write_out(open(output_dir+'/research_problem.dat', 'w', encoding='utf-8'), v, 'research_problems')

	write_out_list(open(output_dir+'/resource_list.dat', 'w', encoding='utf-8'), resource)	
	v = set(resource)
	write_out(open(output_dir+'/resource.dat', 'w', encoding='utf-8'), v, 'resources')
	
	write_out_list(open(output_dir+'/language_list.dat', 'w', encoding='utf-8'), language)
	v = set(language)
	write_out(open(output_dir+'/language.dat', 'w', encoding='utf-8'), v, 'languages')
	
	write_out_list(open(output_dir+'/method_list.dat', 'w', encoding='utf-8'), method)
	v = set(method)
	write_out(open(output_dir+'/method.dat', 'w', encoding='utf-8'), v, 'methods')
	
	write_out_list(open(output_dir+'/tool_list.dat', 'w', encoding='utf-8'), tool)	
	v = set(tool)
	write_out(open(output_dir+'/tool.dat', 'w', encoding='utf-8'), v, 'tools')	
	
	for key in rules_statistics:
		print(key+'\t'+str(rules_statistics[key])+'\n')
	
	print('done!')
	print('total processed titles: '+str(titles_count))	

# takes two arguments:	
# 1. input data file with a single title in each line
# 2. output directory where the parsed data will be written to
def main(argv):	
	if not len(argv) == 2:
		print('Usage: python parse_titles.py <titles-input-file> <output_data_dir>')
	else:
		read_file(argv[0], argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
	