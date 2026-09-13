---
title: 'Augustinian BabyLM: What Ostensive Definition Can and Cannot Teach a Small
  Language Model'
title_zh: 奥古斯丁式BabyLM：示教定义对小语言模型的作用边界研究
authors:
- Lisa Bylinina
affiliations:
- Utrecht University
- Institute for Language Sciences
arxiv_id: '2609.11870'
url: https://arxiv.org/abs/2609.11870
pdf_url: https://arxiv.org/pdf/2609.11870
published: '2026-09-10'
collected: '2026-09-13'
category: LLM
direction: 小语言模型 · 多模态词嵌入初始化
tags:
- BabyLM
- Visual Grounding
- Word Embedding Initialization
- Masked Language Model
- Low-resource LLM
one_liner: 用视觉特征初始化小LM词嵌入，验证示教学习仅对实体属性知识任务有增益，对语法类任务无影响
practical_value: '- 电商商品属性匹配、多模态召回场景可复用视觉初始化词嵌入方案，定向提升实体属性关联类任务效果

  - 低资源场景下小LM训练可针对业务相关的特定词做定制化预初始化，精准优化目标任务，不影响通用语法能力

  - LLM业务效果评估需区分任务类型，通用语法类benchmark无法检测特定语义/属性类优化的实际效果，需定制业务相关评测集'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
常规小语言模型词嵌入从随机初始化开始训练，低数据量下语义学习效率低，人类儿童通过示教绑定语音与实物完成词汇学习，可验证该机制对小LM训练的增益边界。
### 方法关键点
基于10M词语料训练小DeBERTa模型，将有视觉对应实体的token用对应图像区域特征做初始化，其余token随机初始化；在多类BabyLM benchmark上验证效果，补充定制化视觉属性交换评测集做因果验证。
### 关键结果数字
- 视觉初始化的词嵌入特征会保留到训练结束，held-out mask-prediction损失平均下降3%-5%
- 通用语法类benchmark无显著效果提升，仅实体属性知识任务（COMPS、视觉属性交换）准确率提升8%-12%，增益仅覆盖初始化过的词汇
- 函数词、抽象词的视觉初始化也能保留到训练结束，但无对应评测集可检测增益
