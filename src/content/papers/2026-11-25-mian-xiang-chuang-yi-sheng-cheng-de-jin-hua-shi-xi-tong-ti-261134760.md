---
title: 'One Model, Many Modes: Evolving System Prompt Ensembles for Creative Generation'
title_zh: 面向创意生成的进化式系统提示词集成优化框架
authors:
- Daiwei Chen
- Anda He
- Binwei Yao
- Junjie Hu
- Ramya Korlakai Vinayak
affiliations:
- University of Wisconsin–Madison
arxiv_id: '2611.34760'
url: https://arxiv.org/abs/2611.34760
pdf_url: https://arxiv.org/pdf/2611.34760
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM推理优化 · 提示词集成
tags:
- Prompt Optimization
- Ensemble Learning
- Creative Generation
- Inference Optimization
- LLM
one_liner: 无需训练的SEPO框架，可平衡LLM创意生成的质量、多样性与新颖性
practical_value: '- 电商营销文案、商品标题生成场景可直接复用SEPO框架，无需微调模型，通过优化系统提示词集成提升内容多样性与新颖性，配合质量阈值控制内容达标率

  - 推荐系统的个性化解释生成、Agent脑暴模块可复用贪心max-min选择策略，基于生成结果的JS divergence筛选行为差异最大的提示词，避免同质化输出

  - 可复用「小模型搜索提示词、大模型部署」的迁移策略，用小参数量模型完成提示词迭代优化，迁移到大模型推理，大幅降低优化成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
经过偏好对齐的LLM易出现模式崩溃，生成内容集中在窄范围的高奖励响应，现有测试时间优化方法无法同时兼顾质量、多样性、新颖性三个创意生成核心维度，难以满足电商文案、创意脑暴等场景既要内容优质又要差异化的需求。

### 方法关键点
- 训练无关的SEPO框架将创意生成建模为多目标分布优化问题，基于系统提示词集成的均匀混合分布实现多样生成
- 候选生成阶段：通过聚类+LLM进化生成候选提示词，经过质量阈值过滤后保留合格候选
- 候选选择阶段：采用贪心max-min策略，基于生成响应分布的JS divergence筛选与已选提示词、默认提示词行为差异最大的候选加入集成
- 推理阶段：每次生成均匀采样一个优化后的系统提示词调用模型，无需修改模型参数

### 关键实验结果
在发散思维、创意写作、逻辑推理4类任务，Qwen3-1.7B、Llama 3.1 8B、Mistral 7B三个开源模型上测试，对比base采样、min-p采样等5个基线：
- 12个模型-数据集组合中，SEPO在8个取得质量、多样性、新颖性调和均值第一，其余基线最多仅2个第一
- 相比base采样，LLM评判的多样性从1.92提升到3.43，新颖性从1.00提升到3.34，质量仅从3.72微降到3.30（仍高于合格线3分）
- 小模型搜索的提示词可直接迁移到大模型，在Qwen3-30B MoE上仍能提升多样性2.62、新颖性2.97，质量仅下降0.45

### 核心结论
无需微调模型的系统提示词集成优化，是平衡生成质量、多样性、新颖性的低成本高效方案，生成行为层面的分布差异比提示词本身的语义差异更能有效提升生成多样性
