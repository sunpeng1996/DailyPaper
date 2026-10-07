---
title: 'Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents'
title_zh: 基于选择的结构化推理：实现高效多模态搜索智能体
authors:
- Feiyu Gavin Zhu
- Xiaoyu Zhu
- Jiqi Yang
- Rui Yang
- Arnab Kumar Mondal
- Yancheng Wang
- Xinke Deng
- Jean Oh
- Reid Simmons
- Joerg Liebelt
affiliations:
- Apple
- Carnegie Mellon University
arxiv_id: '2610.01892'
url: https://arxiv.org/abs/2610.01892
pdf_url: https://arxiv.org/pdf/2610.01892
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: Agent 多模态搜索推理效率优化
tags:
- Multimodal Agent
- Search Agent
- Efficient Reasoning
- Structured Reasoning
- Inference Optimization
one_liner: 将多模态搜索Agent的开放推理改为候选选择，推理延迟降90%+且性能持平
practical_value: '- 端侧/低算力Agent推理优化：电商导购、商品搜索等场景的端侧多模态Agent，可将高频推理逻辑（搜同款、查参数、看评价、直接回答）封装为固定候选库，替代开放推理生成，大幅降低推理延迟，提升用户体验

  - 工程落地低改造成本：无需给LLM加额外分类头，复用现有推理框架的KV cache、teacher forcing能力即可实现候选并行打分，SGLang等现有推理引擎可直接适配

  - 小模型Agent训练参考：SSR无需SFT warmup即可直接用RL训练，2B/4B小模型即可达到接近8B零-shot模型的效果，适合成本敏感的大规模线上推荐/搜索Agent场景

  - 推理候选库构建方法：可从业务历史成功Agent轨迹中聚类抽取高频推理逻辑构建候选库，效果随库大小单调提升，无需一开始就覆盖全场景，可快速迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多模态搜索Agent传统ReAct架构每次决策前需自回归生成自由形式推理，小模型推理能力有限易生成无效长文本，既浪费算力又带来极高延迟，无法满足端侧或高并发场景需求；现有推理压缩方法仍未摆脱自回归解码的本质瓶颈，而搜索场景的高层推理逻辑高度重复，无需遍历全自然语言空间。
### 方法关键点
- 提出SSR框架，将推理从开放生成改为从预定义可复用自然语言候选库选择，候选覆盖高频推理逻辑（如图搜识别实体、文本查参数、放大图片、直接回答等）
- 并行推理解码：用原生LLM对所有候选做长度归一化的log似然打分，共享上下文KV cache，候选内、候选间全并行计算，无需额外分类头，完全消除推理token自回归生成成本
- 兼容SFT、GRPO/GSPO/SAPO等多种训练范式，无需SFT warmup，推理选择和动作生成共享模型参数端到端优化
### 关键结果
在7个多模态搜索基准上测试，采用2B/4B Qwen3-VL模型，对比freeform推理、Chain-of-Draft等多个高效推理基线：
- 4B SSR平均成功率61.37%，与同规模SOTA搜索Agent持平；2B SSR成功率51.26%，接近零-shot 8B模型效果
- 单轮推理延迟降低90%以上，单问题总推理延迟降低28-54%，有效推理吞吐量提升35倍以上
- p95推理延迟仅0.071s，远低于基线的0.798s以上，延迟稳定性大幅提升
### 核心结论
小搜索Agent不需要每一步都在全语言空间推理，将高频重复的推理逻辑封装为可复用候选库，即可在不损失效果的前提下大幅提升推理效率
