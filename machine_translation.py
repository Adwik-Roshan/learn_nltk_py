from translate import Translator

#create Translator object
translator = Translator(to_lang='es') # es= spanish

#Text to be translated
text= "Hello how are you? \
My name is Adwik Roshan, I am twenty years old and looking to make a\
trip to Spain, what would you recommend for sixty nine days?"

#translate
translation= translator.translate(text)
print("Translated to Espa\u00f1ol : ",translation)
