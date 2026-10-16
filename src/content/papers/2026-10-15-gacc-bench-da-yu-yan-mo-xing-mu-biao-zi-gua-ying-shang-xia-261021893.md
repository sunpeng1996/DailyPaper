---
title: 'GACC-Bench: Benchmarking Goal-Adaptive Context Compression Ability across
  Large Language Models'
title_zh: GACC-Bench：大语言模型目标自适应上下文压缩能力评测基准
authors:
- Weiting Liu
- Zhiyu Pan
- Shuhong Wang
- Zhenquan Yao
- Jungang Li
- Li Zhao
- Jian Jiang
- Jianfeng Feng
- Ai Han
- Wenlian Lu
affiliations:
- 复旦大学
- 华中科技大学
- 京东
- 哈尔滨工业大学
- 香港科技大学（广州）
arxiv_id: '2610.21893'
url: https://arxiv.org/abs/2610.21893
pdf_url: https://arxiv.org/pdf/2610.21893
published: '2026-10-15'
collected: '2026-10-16'
category: Eval
direction: LLM上下文压缩 · 基准评测
tags:
- Context Compression
- Benchmark
- LLM
- Agent Memory
- RAG
one_liner: 首个面向高层目标引导、下游问题未知场景的LLM上下文压缩多领域评测基准
practical_value: '- 长周期电商导购Agent、客服Agent的会话记忆压缩可直接复用目标引导逻辑：提前识别用户当前会话的高层目标（如选购游戏本、咨询售后政策）再压缩历史，实验显示匹配目标的压缩比无目标压缩准确率高13~30pp，远优于错配目标的效果

  - RAG召回后上下文压缩可引入目标自适应机制：电商搜索/推荐场景下，根据用户查询对应的高层意图（如侧重性价比、功能参数）压缩召回的商品详情、评价文本，可在相同token预算下提升下游生成内容的准确率

  - 业务侧对比不同压缩方案时可复用compressor-reader-judge固定评估框架：固定统一的reader和judge避免评估偏差，同时可参考Macro指标衡量压缩结果对同目标下多轮交互的支撑能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有上下文压缩技术多面向查询已知或完全无目标的场景，不符合实际长会话、Agent交互的真实场景：压缩时仅获知高层目标（如用户要选购家电），具体后续问题未知，且需支撑同目标下的多个后续查询，此前缺乏针对性的统一评测基准。
### 方法关键点
- 数据集构造：基于7个长文本、Agent轨迹基准生成281个跨领域上下文、500个高层目标、2571个关联问题，所有实例经人工审核，压缩阶段完全看不到下游问题
- 评估框架：采用compressor-reader-judge三段式结构，固定reader和judge模型，仅替换压缩器，消除其他变量干扰；指标设为Micro准确率（单问题回答正确率）和Macro准确率（目标下所有问题全对的比例）
- 支持可配置的token保留预算，可模拟不同业务的算力、延迟约束场景
### 关键结果
- 全上下文场景下Micro准确率达99.38%、Macro达96.8%，10% token保留预算下最优模型GPT-6-Astra的Micro准确率仅57.41%、Macro仅14.8%，仍有巨大优化空间
- 匹配目标的压缩比无目标压缩Micro准确率高13~30pp，比错配目标的压缩高20~37pp，20%预算下带目标的Macro准确率是无目标的3倍
### 核心结论
目标适配的上下文压缩可大幅提升token利用效率，但错配目标的引导反而会劣于无目标压缩，当前压缩能力距离支撑同目标下全量查询的需求仍有明显差距
