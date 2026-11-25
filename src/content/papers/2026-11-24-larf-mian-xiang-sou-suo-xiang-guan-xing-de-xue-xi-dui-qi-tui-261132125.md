---
title: 'LARF: Learning-aligned Reasoning Framework for Search Relevance'
title_zh: LARF：面向搜索相关性的学习对齐推理框架
authors:
- Tian Tang
- Guo Chen
- Reed Li
- Hao Wang
- Yu Lu
- Haijin Liang
- Haibo Shi
affiliations:
- Tencent Yuanbao Team
- Southwest University
arxiv_id: '2611.32125'
url: https://arxiv.org/abs/2611.32125
pdf_url: https://arxiv.org/pdf/2611.32125
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: 搜索相关性优化 · LLM 推理蒸馏
tags:
- Search Relevance
- LLM Distillation
- GRPO
- Chain-of-Thought
- Reranking
- Margin Loss
one_liner: 提出三阶段训练框架，将LLM推理能力蒸馏为低延迟工业级搜索相关性模型
practical_value: '- 可直接复用三阶段训练流水线：训练阶段用CoT+GRPO强化学习注入领域判断逻辑，推理阶段蒸馏丢弃生成头仅保留分类头，适配电商搜索/推荐精排等延迟敏感场景，latency降幅可达80%以上

  - 多维度奖励+终端token margin loss的优化方法可直接迁移到电商商品分级、相关性判断等场景，解决相邻标签（如部分相关/基本相关）边界模糊、难区分的问题，硬样本准确率提升明显

  - 冷启动SFT阶段的分层主题采样+硬样本挖掘策略，仅用1/3标注数据即可达到全量数据训练效果，大幅降低标注成本，适合标注资源有限的业务场景

  - 多Agent自动生成分维度CoT rationale的方法，可低成本构造推理类训练样本，无需人工标注思考过程，降低数据制作成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM应用于搜索相关性任务存在三大痛点：常规SFT仅监督标签输出，缺乏领域判断逻辑的细粒度监督；标准轨迹级RL优化无法显式拉大相邻相关性标签的决策边界；CoT推理的自回归生成延迟过高，无法满足线上实时排序的latency要求，亟需兼顾效果与效率的工业级落地方案。

### 方法关键点
- 冷启动SFT阶段：通过分层主题覆盖+相关性类别密度采样+硬样本挖掘筛选1/3高价值训练样本，采用多Agent协作生成语义、质量、权威、时效性分维度的CoT推理依据，对齐人类标注逻辑
- 判别式GRPO优化阶段：设计属性维度、列表级排序、规则一致性三类组合奖励，新增终端相关性token的margin loss，显式拉大地真值标签与最强竞争类别的概率差，解决相邻标签混淆问题
- 双头知识蒸馏阶段：共享Transformer backbone，同时训练辅助生成推理头和多维度分类头，推理时完全丢弃生成头，仅通过分类头做单步非自回归预测，大幅降低推理延迟

### 关键实验
基于30万训练、1.6万测试的人工标注网页搜索相关性数据集，对比Qwen3系列reranker与基座模型：LARF-8B六分类准确率较Qwen3-8B-Instruct提升5.78pp，NDCG提升5.05；分类头推理路径延迟较自回归方案降低82.9%，速度提升5.86倍；1.7B蒸馏版线上A/B测试高满意度率提升1.77%，低满意度率降低3.22%。

### 核心结论
推理能力可作为训练阶段的监督信号注入模型，通过蒸馏保留在小模型的分类头中，无需在线生成推理过程即可获得推理带来的准确率收益，完美平衡效果与推理latency。
