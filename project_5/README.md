# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 5: LangChain: Q&A

## Overview
ChatGPT has had a significant impact on various domains such as natural language understanding, content generation, medical diagnosis, language translation, and education. Its ability to generate high-quality responses to natural language queries has revolutionized the way we interact with machines and has enabled faster and more efficient information retrieval. This has led to the development of several applications such as chatbots, virtual assistants, and intelligent tutoring systems that are powered by ChatGPT, contributing to advancements in artificial intelligence, machine learning, and natural language processing.

## Contents:
- [Problem Statement](#Problem-Statement)
- [Conclusions](#Conclusions)
- [Future Work](#Future-Work)

## Problem Statement
The goal of this project is to build a system that can answer natural language questions based on the content of a given set of documents. The system will be powered by ChatGPT, a language model that is trained on a large corpus of text and can generate coherent responses to questions in natural language. The project will involve the use of LangChain, a framework for developing applications powered by language models.

## Conclusions
We have successfully created a ChatGPT Powered Question Answering Over the books Romeo & Juliet and The Great Gatsby. The two books were added into the same vectorstore to find out if it might cause any confusion to the LLM as compared to if only one book was added. It turns out that the OpenAI LLM still works fine. We have used OpenAIEmbeddings to embed our documents.

## Future Work
In future work, we plan to explore the use of "memory" to take into account chat history, which can potentially improve the accuracy and relevance of responses generated by our question-answering system. By considering previous interactions with the user, the system can adapt its responses to better meet the user's needs and preferences. Additionally, we aim to investigate the use of prompt engineering techniques to fine-tune ChatGPT for specific domains or tasks, which can enhance the system's performance in specialized areas. We also plan to extend the system's multilingual capabilities to support a wider range of languages, enabling communication with users from different linguistic backgrounds.