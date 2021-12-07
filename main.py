from funcverbnet.funcverbnet import FuncVerbNet
import spacy

FUNC_VERB_NET = FuncVerbNet()


class PreMA:
    def __init__(self, sentence):
        self.f_sentence = sentence
        self.f_category = self.find_f_category()
        self.f_verb = self.find_f_verb()

    def find_f_category(self):
        """
        tìm f_category tương ứng cho f_sentence sử dụng thư viện funcverbnet
        :param sentence:
        :return: category
        """
        category_id = FUNC_VERB_NET.find_category_by_any_sentence(self.f_sentence)
        cate = FUNC_VERB_NET.find_cate_by_id(category_id)
        return cate

    def find_f_verb(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.f_sentence)
        f_verb = None
        include_verb = self.f_category.included_verb
        for token in doc:
            if token.tag_ == 'VB' and token.text in include_verb:
                f_verb = token.text
                break
            if token.tag_ == 'VB':
                f_verb = token.text
                break
        return f_verb

    # def find_p_pattern(self):


if __name__ == "__main__":
    sentence = 'use this method to get the default sensor for a given type'
    finder = PreMA(sentence)

    # 4.1 phân loại f_sentence vào f_category
    print(finder.f_category.id, finder.f_category.name)
    # 4.2 phân tích p_pattern
    print('________________________________________________________________')



