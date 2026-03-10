data = [
    {
        "id": 1,
        "topic": "Machine Learning Overview",
        "content": "Machine learning is a subfield of artificial intelligence that enables computers to learn patterns from data without being explicitly programmed. It involves training algorithms on datasets so they can make predictions or decisions. Common applications include recommendation systems, fraud detection, computer vision, and natural language processing.",
        "tags": ["ml", "ai", "introduction"]
    },
    {
        "id": 2,
        "topic": "Supervised Learning",
        "content": "Supervised learning is a machine learning paradigm where models are trained on labeled datasets. Each training example includes both the input features and the correct output label. Common supervised learning tasks include classification and regression. Algorithms include linear regression, logistic regression, support vector machines, and random forests.",
        "tags": ["supervised learning", "classification", "regression"]
    },
    {
        "id": 3,
        "topic": "Unsupervised Learning",
        "content": "Unsupervised learning involves training machine learning models on datasets that do not have labeled outputs. The goal is to discover hidden patterns or structures in the data. Common tasks include clustering and dimensionality reduction. Algorithms include k-means clustering, hierarchical clustering, and principal component analysis (PCA).",
        "tags": ["unsupervised learning", "clustering", "pca"]
    },
    {
        "id": 4,
        "topic": "Reinforcement Learning",
        "content": "Reinforcement learning is a machine learning approach where an agent learns by interacting with an environment. The agent receives rewards or penalties depending on its actions and learns a policy that maximizes cumulative reward. Applications include robotics, game playing, and autonomous vehicles.",
        "tags": ["reinforcement learning", "agent", "policy"]
    },
    {
        "id": 5,
        "topic": "Classification",
        "content": "Classification is a supervised learning task where the goal is to predict a discrete category label. Examples include spam detection, image recognition, and medical diagnosis. Common algorithms include logistic regression, decision trees, random forests, and neural networks.",
        "tags": ["classification", "supervised learning"]
    },
    {
        "id": 6,
        "topic": "Regression",
        "content": "Regression is a supervised learning problem where the goal is to predict a continuous numeric value. Examples include predicting house prices, temperature forecasting, and sales prediction. Algorithms used include linear regression, ridge regression, and gradient boosting machines.",
        "tags": ["regression", "supervised learning"]
    },
    {
        "id": 7,
        "topic": "Model Evaluation",
        "content": "Model evaluation measures how well a machine learning model performs on unseen data. Common evaluation metrics include accuracy, precision, recall, F1-score, and ROC-AUC for classification problems. For regression tasks, metrics include mean absolute error (MAE), mean squared error (MSE), and R-squared.",
        "tags": ["evaluation", "metrics"]
    },
    {
        "id": 8,
        "topic": "Overfitting",
        "content": "Overfitting occurs when a machine learning model learns the training data too well, including noise and random fluctuations. This causes the model to perform poorly on new unseen data. Techniques to prevent overfitting include cross-validation, regularization, and using simpler models.",
        "tags": ["overfitting", "model generalization"]
    },
    {
        "id": 9,
        "topic": "Underfitting",
        "content": "Underfitting happens when a machine learning model is too simple to capture the underlying pattern in the data. As a result, the model performs poorly on both training and test datasets. Solutions include increasing model complexity, adding more features, or reducing regularization.",
        "tags": ["underfitting"]
    },
    {
        "id": 10,
        "topic": "Feature Engineering",
        "content": "Feature engineering is the process of transforming raw data into useful input features for machine learning models. It may involve scaling, encoding categorical variables, handling missing values, and creating new features from existing ones. Good feature engineering can significantly improve model performance.",
        "tags": ["feature engineering", "data preprocessing"]
    },
    {
        "id": 11,
        "topic": "Cross Validation",
        "content": "Cross validation is a technique used to evaluate machine learning models by splitting the dataset into multiple subsets. The model is trained on some subsets and tested on others. K-fold cross validation is one of the most common methods and helps estimate model performance more reliably.",
        "tags": ["cross validation"]
    },
    {
        "id": 12,
        "topic": "Random Forest",
        "content": "Random forest is an ensemble machine learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting. Each tree is trained on a random subset of the data and features. The final prediction is usually obtained by majority voting for classification or averaging for regression.",
        "tags": ["random forest", "ensemble"]
    },
    {
        "id": 13,
        "topic": "Gradient Boosting",
        "content": "Gradient boosting is an ensemble learning technique where models are trained sequentially, with each new model focusing on correcting the errors made by previous models. Popular implementations include XGBoost, LightGBM, and CatBoost.",
        "tags": ["gradient boosting", "ensemble"]
    },
    {
        "id": 14,
        "topic": "Neural Networks",
        "content": "Neural networks are machine learning models inspired by the human brain. They consist of layers of interconnected neurons that process data through weighted connections. Deep neural networks with many layers are commonly used in computer vision, speech recognition, and natural language processing.",
        "tags": ["neural networks", "deep learning"]
    },
    {
        "id": 15,
        "topic": "Natural Language Processing",
        "content": "Natural language processing (NLP) is a field of machine learning focused on enabling computers to understand and generate human language. Applications include chatbots, machine translation, sentiment analysis, and document summarization.",
        "tags": ["nlp", "language"]
    },
    {
        "id": 16,
        "topic": "Embeddings",
        "content": "Embeddings are dense vector representations of text, images, or other data types. In NLP, word or sentence embeddings capture semantic meaning so that similar words or sentences have similar vector representations. Embeddings are commonly used in search, recommendation systems, and retrieval augmented generation.",
        "tags": ["embeddings", "vector search"]
    },
    {
        "id": 17,
        "topic": "Vector Databases",
        "content": "Vector databases store high dimensional embeddings and allow efficient similarity search. They are commonly used in modern AI applications such as semantic search and retrieval augmented generation. Examples include Pinecone, Weaviate, and Milvus.",
        "tags": ["vector database", "rag"]
    },
    {
        "id": 18,
        "topic": "Retrieval Augmented Generation",
        "content": "Retrieval augmented generation (RAG) is a technique that combines information retrieval with large language models. Instead of relying only on the model's internal knowledge, relevant documents are retrieved from a knowledge base and provided as context to generate more accurate answers.",
        "tags": ["rag", "llm"]
    },
    {
        "id": 19,
        "topic": "Large Language Models",
        "content": "Large language models are deep learning models trained on massive text,datasets to understand and generate human language. Examples include GPT style models, BERT, and other transformer architectures. They are used for chatbots, summarization, translation, and question answering.",
        "tags": ["llm", "transformers"]
    },
    {
        "id": 20,
        "topic": "Transformers",
        "content": "Transformers are a neural network architecture introduced in 2017 that rely on self attention mechanisms instead of recurrent layers. They allow models to process text in parallel and capture long range dependencies, which made them the dominant architecture in modern NLP systems.",
        "tags": ["transformers", "attention"]
    }
]


# In[2]:


from minsearch import Index


# In[3]:


index = Index(
    text_fields = ['topic', 'content'],
    keyword_fields=['tags']
)


# In[4]:


index.fit(data)


# In[5]:




# In[6]:


import os
from groq import Client


# In[7]:


client = Client(api_key=os.environ.get("API_KEY"))


# In[63]:t


def build_prompt(query, search_result):
    prompt_template = """
You are a course teaching assistant bot.

You must answer ONLY using information from the CONTEXT below.

Rules:
1. If the QUESTION is related to Machine Learning and the answer exists in CONTEXT, return ONLY the exact sentence from CONTEXT that answers the question.
2. If the QUESTION is NOT related to Machine Learning, return exactly:
I don't have any info on that
3. Do NOT explain anything.
4. Do NOT add extra words.
5. Do NOT include reasoning.
6. Do NOT repeat the question.

Output must be ONLY the answer sentence OR:
I don't have any info on that

CONTEXT:
{context}

QUESTION:
{query}
""".strip()
 
    context = ""
    for topics in search_result:
        context += f"topic: {topics['topic']}\ncontent: {topics['content']}\n\n"

 
    prompt = prompt_template.format(context=context.strip(), query=query.strip())
    return prompt


def llm(prompt):
    response = client.chat.completions.create( 
        model='llama-3.1-8b-instant', 
        messages= [{ 'role': 'user', 'content':prompt }]
    )
    return response.choices[0].message.content


# In[23]:


def search(query):
    return index.search(query)


# In[24]:


def ask(query):

    search_result = search(query)[:3]

    prompt = build_prompt(query, search_result)

    response = llm(prompt)

    return response