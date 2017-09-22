NLP Programming Tutorial
========================

* [Intro Words](#intro-words)
* [Olde Schedule](#old-schedule)
* [New Tentative Schedule](#new-tentative-schedule)
* [Dataset](#dataset)

### Intro Words

This is an NLP and ML practical programming course delivered by [Graham Neibig](http://www.phontron.com/) which is very awesome, and covers many classic basics of natural language processing and the machine learning methods applied. This fork from Neubig is to adapt to his materials to our [Evening Tea Party](https://epsilon-lee.github.io/party/) here at Harbin Institute of Technology. I hope this course of study would be relaxing, joyful and rewarding. 

### Old Schedule

This is a tutorial to learn the basics of natural language processing and machine learning through programming exercises using Python.
The tutorial files are in the "download" directory, so please open up this directory and view the PDF there.

Currently, this tutorial covers the following material:

  * **Tutorial 0:** Programming Basics
  * **Tutorial 1:** Unigram Language Models
  * **Tutorial 2:** Bigram Language Models
  * **Tutorial 3:** Word Segmentation
  * **Tutorial 4:** Part-of-Speech Tagging with Hidden Markov Models
  * **Tutorial 5:** The Perceptron Algorithm
  * **Tutorial 6:** Advanced Discriminative Training
  * **Tutorial 7:** Neural Networks
  * **Tutorial 8:** Recurrent Neural Networks  
  * **Tutorial 9:** Topic Models
  * **Tutorial 10:** Phrase Structure Parsing
  * **Tutorial 11:** Dependency Parsing
  * **Tutorial 12:** Structured Perceptron
  * **Tutorial 13:** Search Algorithms 
  * **Bonus 1:** Kana-Kanji Conversion for Japanese Input

### New Tentative Schedule

A more tentative schedule would be the following: 

- N-gram Language Models (LMs)
  - Math concepts of statistical/probabilistic model, likelihood, maximum likelihood estimation (MLE), entropy and perplexity.
  - Statistical LMs and its estimation (Uni-gram/Bi-gram models).
  - Smoothing techniques.
- Word Segmentation
  - Viterbi algorithm and forward-backward stages.
  - Word segmentation based on an estimated bi-gram language model.
- Part-of-speech Tagging with Hidden Markov Models
  - The concept of generative models, and Hidden Markov models (HMM).
  - MLE for estimating parameters of HMM.
  - The concept of decoding in probabilistic models (probabilistic graphical models).
  - Using Viterbi algorithm to perform decoding in HMM.
- The Perceptron Algorithm and other Discriminative Models
  - Perceptron and its on-line learning algorithm.
  - Stochastic gradient descent and logistic regression.
  - The concept of margin and support vector machine.
  - Margin based perceptron and L1, L2 regularization based perceptron.
- Neural Networks and Deep Learning for NLP
  - TBD [Tentative: PyTorch/Tensorflow basics, and a sentiment classification use case.]
- Topic Models
  - Review the concept of supervised and unsupervised learning.
  - Topic modeling as an unsupervised learning, Latent Dirichlet Allocation (LDA).
  - MLE for LDA.
  - Gibbs sampling and the learning of LDA.
- Parsing Techniques
  - Phrase structure tree parsing.
    - Phrase structure grammar (Context-free grammar).
    - Probabilistic modeling of phrase structure grammar and probabilistic context-free grammar.
    - The concept of hypergraph.
    - Viterbi algorithm for finding highest scored graph and inside-outside algorithm for finding highest scored hypergraph.
    - CKY algorithm.
  - Dependency tree parsing.
    - Shift-reduce based method.
    - Spanning tree based method.
- Structured Perceptron and Search Algorithms
  - Structured perceptron training for HMM.
  - The concept of intractable search problems; Beam search for intractable decoding.

### Dataset

Since Neubig is giving tutorials to his group used to be in NAIST, Japan. So some of the dataset he prepared for his students for training and testing are in Japanese, which is not so suitable for us Chinese. So some of the dataset would be augmented to include Chinese ones which is easy for experiment analysis and making sense to us. 
