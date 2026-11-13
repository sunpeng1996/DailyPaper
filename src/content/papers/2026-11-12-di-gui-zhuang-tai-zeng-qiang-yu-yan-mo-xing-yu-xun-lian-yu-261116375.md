---
title: 'Recursive State-Augmented Language Models: Persistent Latent-State Adaptation
  of Pretrained Language Models'
title_zh: 递归状态增强语言模型：预训练语言模型的持久潜态适配
authors:
- Omer Haq
affiliations:
- Independent Researcher
arxiv_id: '2611.16375'
url: https://arxiv.org/abs/2611.16375
pdf_url: https://arxiv.org/pdf/2611.16375
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: LLM 持久潜态适配架构优化
tags:
- LoRA
- State-Augmented LLM
- Persistent Latent State
- Context Compression
- Parameter-Efficient Fine-Tuning
one_liner: 提出读-转换-写架构的递归潜态适配框架，仅用64维状态实现媲美全上下文LoRA的多轮推理性能
practical_value: '- 多轮电商客服/导购Agent可复用该读-转换-写潜态记忆架构，用低维持久状态替代超长上下文KV缓存，大幅降低长交互下的推理内存和算力成本

  - 生成式推荐、动态用户偏好适配场景的LLM适配可优先选用Gated LoRA或Soft Prompt接口，同等参数量下效果优于FiLM、Prefix Tuning等方案

  - 召回、排序类任务训练早停规则不要仅依赖token级NLL，需补充候选排序准确率等业务指标，避免出现NLL升高但排序效果仍提升的错配问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
自回归LLM依赖有限token上下文窗口，长交互场景下KV缓存容量随上下文长度线性增长，截断上下文又会丢失关键历史信息；现有长上下文扩展、RAG等方案要么推理成本高，要么依赖外部检索，缺乏轻量的跨上下文边界持久信息传递机制。

### 方法关键点
- 采用模块化读-转换-写架构：读模块用冻结骨干LLM编码历史观测，转换模块用GRU更新64维潜态，写模块将潜态映射为LLM适配信号，支持LoRA、Soft Prompt、FiLM、Prefix Tuning等多种适配接口，骨干LLM全程冻结
- 支持确定性/随机两种潜态建模，确定性版本仅用单低维潜态即可完成推理，无需存储任何历史上下文token
- 训练时仅优化读、转换、写模块参数，通过状态回传梯度学习编码关键历史信息

### 关键实验结果
基于冻结GPT-2 small（124M参数）验证：
1. 四轮假设推理任务：Gated LoRA版本准确率达89.1±4.1%，媲美全上下文LoRA基线的88.0±0.9%；零化/打乱潜态后准确率降至31%左右，证明预测完全依赖潜态记忆
2. 两轮未见code召回任务：Soft Prompt版本候选排序准确率达44.8±13.0%（随机水平1.6%），但准确生成率仅2.6%，说明潜态可支撑候选排序但难以直接生成完全未见过的词汇

> 最值得记住：轻量持久潜态适配可在不保留历史上下文的前提下实现媲美全上下文的多轮推理性能，是平衡长交互能力和推理成本的可行路径
