---
title: Do speech foundation models really learn words?
title_zh: 语音基础模型是否真的学到了词层面的语义表征
authors:
- Robin Huo
- Ewan Dunbar
affiliations:
- University of Toronto
arxiv_id: '2609.10434'
url: https://arxiv.org/abs/2609.10434
pdf_url: https://arxiv.org/pdf/2609.10434
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: 语音大模型可解释性与表征分析
tags:
- speech foundation model
- interpretability
- HuBERT
- wav2vec2.0
- probing
one_liner: 通过残差法分离音素信息，验证HuBERT与wav2vec2.0高层学到独立于语音内容的词表征
practical_value: '- 搭建语音交互类Agent（电商语音导购、语音搜索）时，可复用残差法提取语音模型高层纯词表征，降低语音特征噪声

  - 语音关键词识别、语音query理解场景，可通过残差法剥离音素扰动，提升高阶语义信息召回准确率

  - 语音预训练模型微调时，可优先操作高层网络（已具备独立词语义编码能力），降低微调算力成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有自监督语音基础模型的词判别能力常被归因于音素编码效果，无法证明其学到了独立于语音形式、包含句法/语义属性的词表征，传统探测方法无法区分这两种机制。

### 方法关键点
引入残差化方法剥离表征中的音素信息，对HuBERT、wav2vec 2.0的各层表征做纯词编码能力探测，验证是否存在形式无关的词表征。

### 关键结果
1. 两类模型的高层网络均能以较高保真度编码独立于局部语音内容的词信息；
2. 该简单解耦方法可在词发现任务中增强高阶语言信息，有效提升下游任务效果。
