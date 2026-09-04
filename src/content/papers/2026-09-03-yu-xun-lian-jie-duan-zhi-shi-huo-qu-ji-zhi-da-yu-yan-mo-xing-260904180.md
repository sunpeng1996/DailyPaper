---
title: Knowledge Acquisition During Pre-training? Large Language Models Learn Better
  With Auxiliary Views
title_zh: 预训练阶段知识获取机制：大语言模型借助辅助视图学习效果更优
authors:
- Joseph Lee
- Yidi Huang
- Dokyoon Kim
- Shu Yang
- Li Shen
affiliations:
- University of Pennsylvania
arxiv_id: '2609.04180'
url: https://arxiv.org/abs/2609.04180
pdf_url: https://arxiv.org/pdf/2609.04180
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM预训练 · 知识注入效率优化
tags:
- Pre-training
- Knowledge Acquisition
- Auxiliary View
- Data Augmentation
- Domain Adaptation
one_liner: 通过控制实验验证LLM预训练中知识辅助重述视图可显著提升知识获取效率，且不依赖生成教师强度
practical_value: '- 做垂直领域Agent（如电商导购、广告投放规则助手）的持续预训练时，同token预算下，将部分原始文档重复的配额替换为知识辅助视图（问答版、教程版、案例版），可提升10%+的知识掌握度，效果优于单纯paraphrase

  - 小batch微调场景（如垂直品类个性化推荐LLM微调）可采用paraphrase做数据增强，大batch（>256）预训练场景paraphrase增益消失，无需浪费算力生成

  - 生成辅助视图无需使用强LLM，小模型生成的视图效果与大模型差异不到2%，可大幅降低电商/广告长尾知识的数据制备成本

  - 若模型存在前置知识缺口（如面向下沉市场的导购Agent不了解基础商品参数），预训练时先补充前置知识视图，可显著提升知识推理任务表现'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有预训练数据优化多聚焦去重、过滤、质量等语料级属性，对知识本身的表示形式研究不足；垂直领域持续预训练的知识召回率普遍偏低（如70B模型仅能召回62.7%的预训练事实），缺乏可落地的知识表示优化方法，亟需明确不同知识表示形式对LLM学习效果的影响规律。

### 方法关键点
- 严格控制变量实验设计：所有对比组的知识相关token预算完全匹配，排除token数量干扰
- 定义三类知识表示：原始文档、paraphrase（语言层面同义改写）、辅助视图（概念层面重述，含博客、Stack Exchange风格问答、教材三种形式）
- 设计两类评估探针：factual探针考察事实记忆能力，inference探针考察知识理解推理能力
- 测试覆盖多尺度多模型家族：OLMo-2 1B/7B/13B/32B、Qwen-2.5-7B

### 关键实验结果
数据集覆盖计算机科学论文、法律判例、医疗病例三个垂直领域，共36份未出现在预训练语料的新文档，配套6435个factual探针、430个inference探针。对比基线为原始文档训练、9倍paraphrase训练，核心结果：
1. 同token预算下，加入辅助视图的32B模型factual MCQA提升8.3%，inference MCQA提升16.2%
2. 辅助视图增益随模型规模增大而提升，1B模型几乎无增益，32B模型增益是7B的2.1倍
3. 不同能力教师生成的辅助视图效果差异仅1.7%，几乎不依赖生成教师的强度
4. 小batch（64）场景下paraphrase可提升factual表现4.6%，大batch（256）场景下增益完全消失

> 最值得记住的结论：对同一知识的多视角概念重述，比单纯重复记忆更能提升LLM的知识掌握度，甚至能同时提升事实记忆和推理能力
