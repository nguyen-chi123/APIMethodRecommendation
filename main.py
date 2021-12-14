from funcverbnet.funcverbnet import FuncVerbNet
import spacy    # sử dụng để tạo vector từ vựng, gắn thẻ

FUNC_VERB_NET = FuncVerbNet()


class PreMA:
    def __init__(self, f_sentence):
        self._f_sentence = sentence
        self._f_category = self.find_f_category()
        self._f_verb, self._vector_doc = self.find_f_verb()

    def find_f_category(self):
        """
        tìm f_category tương ứng cho f_sentence sử dụng thư viện funcverbnet
        :param: sentence
        :return: category
        """
        category_id = FUNC_VERB_NET.find_category_by_any_sentence(self._f_sentence)
        cate = FUNC_VERB_NET.find_cate_by_id(category_id)
        return cate

    def find_f_verb(self):
        if self._f_category.id == -1:
            return None
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self._f_sentence)
        f_verb = None
        include_verb = self._f_category.included_verb
        for token in doc:
            if token.tag_ == 'VB' and token.text in include_verb:
                f_verb = token.text
                break
        # khi ko tìm thấy verb thuộc f_category
        if f_verb is None:
            for token in doc:
                if token.tag_ == 'VB':
                    f_verb = token.text
                    break
        return f_verb, doc

    def find_p_pattern(self):
        for token in self._vector_doc:
            if token.tag_ != 'VB':
                continue
            # đệ quy chuyển đổi sang cấu trúc SP


if __name__ == "__main__":
    # sentence = 'Attempt to compute for the specified key and its current mapped value \
    #             (or null if there is no current mapping)'
    sentence = 'use this method to get the default sensor for a given type'
    finder = PreMA(sentence)

    # 4.1 phân loại f_sentence vào f_category
    print('phân loại vào f_category: ', finder._f_category.name)
    # 4.2 phân tích p_pattern
    print('____Phân tích p_pattern____')
    print('xác định f_verb: ', finder._f_verb)







