---
title: 'MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval
  and Verification-Guided Refinement'
title_zh: MathForm：结合知识检索与验证引导优化的数学自动形式化框架
authors:
- Lushi Pu
- Weiming Zhang
- Xinheng Xie
- Zixuan Fu
- Bingxiang He
- Hengyu Zhao
- Hongya Lyu
- Xin Li
- Jie Zhou
- Yudong Wang
affiliations:
- ModelBest Inc.
- Tsinghua University
arxiv_id: '2608.14221'
url: https://arxiv.org/abs/2608.14221
pdf_url: https://arxiv.org/pdf/2608.14221
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: 大语言模型 · 数学自动形式化
tags:
- RAG
- Autoformalization
- SFT
- Reinforcement Learning
- Dataset
one_liner: 提出结合RAG与验证引导迭代优化的数学自动形式化框架，8B模型效果超32B专用基线
practical_value: '- 面向电商合规文案生成、商品属性标准化等领域LLM生成任务，可复用「生成前检索领域库定义+生成后用系统诊断+语义一致性反馈迭代修正」的流程，提升输出准确率

  - 构建业务领域微调数据集时，可采用验证引导的自动标注流水线，降低人工标注成本，提升标注数据质量

  - 小参数模型通过「SFT+RL+检索增强」的组合优化路径，可超过大参数专用模型效果，适合业务侧降本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有数学自动形式化方法高度依赖模型参数记忆知识库的层级定义，单遍生成后仅做过滤，缺乏反馈迭代修正机制，输出准确率低、语义一致性差。
### 方法关键点
1. 提出MathForm框架，生成前由检索规划器从Mathlib召回相关定义、已有形式化结果引导生成；
2. 生成后引入编译器诊断、语义一致性反馈做多轮迭代修正；
3. 基于该框架构建含367K跨领域验证样本的Lean4数据集FormalVerse，先SFT再RL训练得到MathForm-8B模型。
### 关键结果
6个基准测试平均Pass@8：语法检查（SC）88.06%、一致性检查（CC）72.37%，性能超过多个32B专用自动形式化模型；FATE-H、FATE-X难例子集CC通过率分别达63%、37%，均优于SOTA基线。
