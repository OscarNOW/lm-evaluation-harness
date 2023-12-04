def process_docs(dataset):
    def _helper(doc):
        # Create a more difficult question without warmup
        difficult_question = {
            "warmup": "",
            "question": doc["question"],
            "choices": doc["answers"],
            "answer": doc["answer"]
        }

        # Create a less difficult question with warmup
        easy_question = {
            "warmup": doc["warmup"],
            "question": doc["question"],
            "choices": doc["answers"],
            "answer": doc["answer"]
        }

        return [difficult_question, easy_question]

    return dataset.map(_helper).flatten()