from rake_nltk import Rake

rake_nltk_var = Rake()

text = """ I am a passionate python programmer and competitive coder from India."""

rake_nltk_var.extract_keywords_from_text(text)

keyword_extracted = rake_nltk_var.get_ranked_phrases()

print(keyword_extracted)
