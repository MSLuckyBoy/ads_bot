import gettext
import os
import threading


class I18N:
    context_lang = threading.local()

    def __init__(self, translations_path, domain_name):
        super().__init__()
        self.update_types = self.process_update_types()
        self.path = translations_path
        self.domain = domain_name
        self.translations = self.find_translations()
    
    def gettext(self, text, lang=None):
        if lang is None:
            lang = self.context_lang.language

        if lang not in self.translations:
            return text
        
        translator = self.translations[lang]
        return translator.gettext(text)
    
    def get_user_language(self, obj):
        raise NotImplementedError
    
    def process_update_types(self) -> list:
        raise NotImplementedError

    def pre_process(self, message, data):
        self.context_lang.language = self.get_user_language(obj=message)

    def post_process(self, message, data, exception):
        pass
    
    def find_translations(self):
        if not os.path.exists(self.path):
            raise RuntimeError(f"Translations directory by path: {self.path!r} was not found")
        
        mo_files = gettext.find(self.domain, self.path, all=True, languages=os.listdir(self.path))
        result = {}
        
        for mo_file in mo_files:
            language = mo_file.split("/")[1]
            
            with open(mo_file, "rb") as file:
                result[language] = gettext.GNUTranslations(file)
        
        return result
