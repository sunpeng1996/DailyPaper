---
title: 'Spoken Function Calling: A New Perspective on Spoken Language Understanding
  for Large Audio Language Models'
title_zh: 面向大音频语言模型口语理解的新范式：口语函数调用
authors:
- Yuezhang Peng
- Yuxin Liu
- Changfeng Gao
- Zhifu Gao
- Xiangang Li
- Xie Chen
affiliations:
- Shanghai Jiao Tong University
- Token Foundry, Alibaba Group
- Shanghai Innovation Institute
arxiv_id: '2608.05126'
url: https://arxiv.org/abs/2608.05126
pdf_url: https://arxiv.org/pdf/2608.05126
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 口语语义理解与Function Calling
tags:
- SLU
- Function Calling
- LALM
- Multi-Agent
- Synthetic Dataset
one_liner: 提出口语函数调用SFC范式，结合结构化规则与合成数据集，显著提升大模型开放域口语语义提取精度
practical_value: '- 落地语音导购/智能客服Agent时，可复用SFC结构化规则定义思路替代传统封闭域SLU，提升开放域用户意图解析准确率

  - 低资源场景构造语音语义数据集时，可借鉴多Agent自动合成方案，大幅降低人工标注成本

  - 大音频语言模型适配任务型语音交互场景时，可采用post-tuning注入SFC能力，性价比高于全量SFT'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统SLU依赖域内SFT适配封闭集任务，规则定义模糊，无法支持开放域任务的in-context learning，是人机语音交互规模化落地的核心瓶颈。
### 方法关键点
1. 提出SFC（Spoken Function Calling）新范式，基于结构化规则定义优化口语语义理解，突破传统封闭域SLU的能力边界
2. 基于传统SLU数据集扩展通用口语函数库，搭建多Agent协作系统自动合成SFC-Bench评测数据集
3. 采用轻量化post-training方案为LALM注入SFC能力，大幅降低模型适配成本
### 关键结果
SFC范式效果显著优于传统SLU，可大幅提升LLM与LALM的口语语义提取准确率
