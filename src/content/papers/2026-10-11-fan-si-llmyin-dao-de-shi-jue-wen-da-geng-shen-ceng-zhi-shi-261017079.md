---
title: 'Rethinking LLM-Guided Visual Question Answering: Does Deeper Knowledge Integration
  Really Help?'
title_zh: 反思LLM引导的视觉问答：更深层知识整合真的更有效吗？
authors:
- Aneerban Saha
- Vijay Kumar
- Sameer Madhav D.
- Priyam Srivastava
- Dhruv Bansal
affiliations:
- Independent Researchers, India
arxiv_id: '2610.17079'
url: https://arxiv.org/abs/2610.17079
pdf_url: https://arxiv.org/pdf/2610.17079
published: '2026-10-11'
collected: '2026-10-16'
category: Multimodal
direction: 多模态VQA · LLM知识融合策略
tags:
- VQA
- LLM Knowledge Integration
- Multimodal Fusion
- Late Fusion
- Data Augmentation
one_liner: 对比LLM引导的VQA知识整合策略，发现少数据场景下浅层晚融合效果更优，提供10倍数据增强pipeline
practical_value: '- 多模态商品问答/搜索场景下，训练数据不足时优先选择决策层晚融合方案，无需修改底层模型注意力逻辑，开发成本低且效果更优

  - 可直接复用LLM生成结构化辅助信息+问题paraphrase的数据增强pipeline，快速扩充小样本场景的训练数据集

  - 做LLM能力融合时需匹配数据规模：数据稀缺时优先用浅融合方案，数据充足后再尝试深层融合架构，避免无效研发投入'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
知识型VQA需调用超出图像内容的外部常识与事实知识，现有方案普遍将LLM作为知识源，但LLM引导信息的最优整合深度缺乏系统验证，业界默认深层整合效果更优。
### 方法关键点
基于Llama 3.3 70B生成结构化推理引导、视觉焦点概念、干扰项、外部知识四类辅助信息，在统一冻结ViT + FLAN-T5框架下对比两种整合策略：决策层晚融合、注意力矩阵注入；同时推出LLM问题改写数据增强pipeline，可将训练数据扩充10倍以上。
### 关键结果
少样本微调场景下，浅层晚融合Exact Match达39.4%，较无引导基线提升10.0个百分点，效果优于深层注意力修改方案的31.8%，验证融合深度需匹配数据量级。
