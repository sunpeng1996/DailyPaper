---
title: Music-to-Dance Generation via Atomic Movements
title_zh: 基于原子动作的音乐驱动舞蹈生成方法
authors:
- Xinhao Cai
- Yixuan Sun
- Minghang Zheng
- Qingchao Chen
- Xin Jin
- Song-chun Zhu
- Yang Liu
affiliations:
- Wangxuan Institute of Computer Technology, Peking University
- School of Electronics Engineering and Computer Science, Peking University
- National Institute of Health Data Science, Peking University
- State Key Laboratory of General Artificial Intelligence, Peking University
- Beijing Institute for General Artificial Intelligence
arxiv_id: '2607.13978'
url: https://arxiv.org/abs/2607.13978
pdf_url: https://arxiv.org/pdf/2607.13978
published: '2026-07-15'
collected: '2026-07-17'
category: Multimodal
direction: 多模态生成 · 语义原子单元结构化建模
tags:
- Multimodal Generation
- Motion Synthesis
- LLM Annotation
- Structured Generation
- Semantic Unit
one_liner: 提出基于语义可解释原子动作的两阶段音乐舞蹈生成框架，提升结构连贯性与可控性
practical_value: '- 可复用LLM对无监督聚类结果做语义重标注的方法，迁移到推荐系统Semantic ID构建、用户行为原子单元建模、商品属性体系自动梳理等场景

  - 两阶段生成（先规划符号序列再补全细节）的架构可复用在生成式推荐的物品序列生成、广告文案/商品短视频脚本生成等任务，大幅提升生成结果的可控性

  - 基于语义原子单元的结构化表示思路，可用于优化生成式内容的可解释性，支持用户自定义编辑需求，适配电商个性化内容生成、直播话术生成等场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有音乐驱动舞蹈生成方法将动作建模为连续信号，忽略舞蹈的组合特性，存在生成结果结构不连贯、可控性差、难以编辑的问题。
### 方法关键点
1. 预处理阶段：对大规模舞蹈数据做动作分割与无监督聚类，再调用LLM对聚类簇做语义重标注与精炼，构建可解释、可复用的原子动作词汇表；
2. 两阶段生成架构：第一阶段为原子动作规划，基于输入音乐预测原子动作的类型、时长、时序，生成符号化舞蹈编排结构；第二阶段为动作补全，用过渡感知生成器基于规划结构合成平滑、风格统一的完整动作序列。
### 关键结果
相比现有基线方法，生成舞蹈的结构连贯性、节奏对齐度、感知自然度均显著提升，同时通过显式结构表示实现了更强的可解释性与可控编辑能力。
