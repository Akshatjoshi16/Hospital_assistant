from datasets import Dataset

def load_eval_dataset():
    data = {
        "question": [
            "Are employee electronic communications considered private?",
            "Can the Corporation monitor employee electronic communications without notice?",
            "Is personal use of company systems allowed?",
            "Can employees use company systems for offensive or obscene content?",
            "Can employees download software from the internet without permission?",
            
            
        ],
        "ground_truth": [
            "No. Electronic communications on company systems are not confidential or private.",
            "Yes. The Corporation may monitor, access, record, and disclose communications without further notice.",
            "Yes, incidental and occasional personal use is permitted if it does not interfere with work or violate policy.",
            "No. Employees may not use systems for insulting, obscene, offensive, or harmful content.",
            "No. Employees must obtain advance written permission from their supervisor before downloading software.",
            

        ]
    }

    return Dataset.from_dict(data)

