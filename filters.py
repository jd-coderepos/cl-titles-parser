import re
from utils import *


# list of filters for research problem name candidates

#with the first regular expression we try to capture dataset names or task names
#with the suffixes we capture verbals like Parsing, Summarization, or nouns like Phonology, Coreference
def one_word_research_problem_candidate(research_problem):
	if task_dataset_match(research_problem) or research_problem_suffixes(research_problem):
		return True
	return False

# list of filters for solution name candidates

#Not a solution if:
#1. if Challenge is the last word in the solution phrase
#2. based on length of phrase between 1 and 3
#if not (re.match(".*?[A-Z][A-Z].*", solution) or '-' in solution or re.match(".*?\d+.*", solution)) then check
#the above line catches solution phrases that are non standard words as valid, thus doesn't make any further filtering checks
#all single words are filtered
#all two words with the first word as a determiner and the second word a generic reference are filtered
#all three words with the first word a preposition, the second word a determiner, and the third word a generic reference are filtered
#and we also check for a collection of generic at most 4 word phrases
def generic_solution_ref(solution):
	sol_toks = solution.split(' ')
	size = len(sol_toks)-1
	if (not task_dataset_match(solution) and \
	len(sol_toks) == 1 or \
	(len(sol_toks) == 2 and (sol_toks[0].lower() in determiners_short or sol_toks[0].lower() in adjectives_short or sol_toks[0].lower() in numeric_short) and re.search(generic_terms_rx, sol_toks[1])) or \
	(len(sol_toks) == 3 and \
	(sol_toks[0].lower() in prepositions_short or sol_toks[0].lower() in determiners_short or sol_toks[0].lower() in numeric_short) and \
	(sol_toks[1].lower() in determiners_short or sol_toks[1].lower() in adjectives_short) and \
	(re.match(generic_terms_rx, sol_toks[2])))) or \
	('Information Extraction' == solution or \
	'An Empirical Methodology' == solution or \
	'Motivation' in solution or \
	'Articles: A Framework' == solution):
		return True
	return False


#list of filters for full titles

# 0 is the title a question
def question(line):
	if '?' in line \
	or re.search('Wh', line) \
	or re.search('How', line):
		return True
	return False

# 0.1 is the title a line like ``Ask Not What Textual Entailment Can Do for You...''
def creative(line):
	if '``' in line and '\'\'' in line: return True
	return False
	
# 1 proceedings/conference overview
def proc_overview(line):
	if 'International Conference on' in line \
	or 'Journal of' in line \
	or 'Volume' in line \
	or 'Proceedings' in line \
	or 'Newsletter' in line \
	or 'Call for Papers' in line \
	or 'The Handbook of' in line \
	or 'Theoretical Issues' in line:
		return True
	return False

# 2 reports from meetings
def meeting(line):
	if 'ACL Meeting' in line \
	or 'General Meeting' in line \
	or 'Annual Meeting' in line \
	or 'The Consortium for' in line \
	or 'Invited Talk' in line \
	or 'Invited talk' in line \
	or 'INVITED TALK' in line \
	or 'Keynote' in line \
	or 'CALL' in line:
		return True
	return False
	
# 3 name of a specific conference
def conference(line):
	if 'Natural Language Processing Conference' in line \
	or 'Cambridge/ACL Series' in line \
	or 'Session' in line:
		return True
	return False
	
# 4 administrative reports`
def admin_reports(line):
	if 'Program of' in line \
	or 'Results of' in line \
	or 'Minutes of' in line \
	or 'Conference of' in line \
	or 'Remarks on' in line \
	or 'Note on' in line \
	or 'summary of session' in line.lower() \
	or 'Letters to the Editor' in line \
	or 'COLING' in line \
	or 'PANEL:' in line \
	or 'Panel on' in line \
	or 'Panel' in line \
	or 'Panel Chair\'s Introduction' in line:
		return True
	return False
	
# 5 reviews or white papers
def review(line):
	if 'Review:' in line \
	or 'Reviews:' in line \
	or 'White Paper' in line \
	or 'Some Comments on' in line \
	or 'A Progress Report' in line \
	or 'ERRATA' in line:
		return True
	return False
	
# 6 parts of a paper
def paper_parts(line):
	if 'Appendix' in line \
	or 'An Introduction to Computational Linguistics' in line \
	or 'Final Report' in line \
	or 'Summary of Results' in line \
	or 'a summary of' in line:
		return True
	return False
	
# 7 institution
def institute(line):
	if 'Department of' in line \
	or 'institute' in line.lower() \
	or 'university' in line.lower() \
	or 'Research at' in line:
		return True
	return False
	
# 8 non-English languages
def non_english(line):
	if '[' in line \
	or '\\text' in line \
	or '\\mbox' in line \
	or ' et ' in line \
	or ' Et ' in line \
	or 'Pour La' in line \
	or 'pour le' in line \
	or ' de ' in line \
	or ' De ' in line \
	or ' des ' in line \
	or '  Des ' in line \
	or ' Du ' in line \
	or ' du ' in line \
	or 'Project' in line \
	or ' remarks ' in line.lower() \
	or 'Die ' in line \
	or 'Der ' in line \
	or 'Ein ' in line \
	or ' Mit ' in line \
	or 'Von Informationen' in line:
		return True
	return False
