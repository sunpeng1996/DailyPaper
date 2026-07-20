---
title: RecGPT-V3 Technical Report
title_zh: RecGPT-V3 技术报告：工业级高效有状态大模型推荐系统
authors:
- Bowen Zheng
- Chao Yi
- Dian Chen
- Gaoyang Guo
- Han Zhu
- Jiakai Tang
- Jian Wu
- Mao Zhang
- Wen Chen
- Yifan Lu
affiliations:
- Taobao
arxiv_id: '2607.15591'
url: https://arxiv.org/abs/2607.15591
pdf_url: https://arxiv.org/pdf/2607.15591
published: '2026-07-16'
collected: '2026-07-20'
category: GenRec
direction: 生成式推荐 · 工业级LLM4Rec落地
tags:
- GenRec
- LLM4Rec
- Semantic ID
- Memory Augmented
- Latent Reasoning
one_liner: 提出有状态混合模态大模型推荐架构，在淘宝落地实现效果与推理效率双提升
practical_value: '- 可直接复用Memory Hub架构：将用户长序列行为蒸馏为可增量更新的结构化记忆单元，减少每次请求的长序列重计算，实测降低用户建模算力55.8%，适合大流量推荐场景

  - 混合模态LLM设计可落地：将Semantic ID作为独立模态加入LLM词表，通过两阶段预训练对齐文本与SID语义，解决文本标签到物品的信息瓶颈，大幅提升意图到召回的匹配效率

  - 潜意图推理Trick可复用：将长CoT蒸馏为少量可解码的latent token，降低推理token成本200×，同时保留可解释性，解决CoT推理延迟过高的工业落地痛点

  - RL优化方案可借鉴：用下游排序模型的CTR分作为RL奖励，解决传统HitRate奖励稀疏、与线上Pipeline不一致的问题，直接对齐业务目标'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工业级LLM推荐系统落地面临三大核心瓶颈：无状态行为建模导致每次请求重处理全量用户历史，算力冗余严重；文本标签作为意图到物品的中介，存在信息损失无法对齐ID级召回需求；显式Chain-of-Thought推理token成本高、延迟大，无法支撑亿级用户高QPS场景。
### 方法关键点
- 部署Memory Hub：将用户长周期行为蒸馏为结构化、可溯源、可增量更新的记忆单元，单次推理仅需输入记忆单元+近期行为序列，避免全量历史重计算
- 混合模态推荐基座：将Semantic ID（SID）作为独立模态加入LLM词表，通过多模态对比学习+残差量化生成物品SID，两阶段预训练对齐文本与SID语义，打通意图推理到物品召回的高带宽通道
- Latent Intent Reasoning：将数千token的显式CoT蒸馏为少量可学习latent token，推理token成本降低200×，同时支持latent token反向解码为可读CoT，兼顾效率与可解释性；后续采用下游排序模型CTR分作为RL奖励，直接对齐线上业务目标
### 关键结果
在淘宝首页「猜你喜欢」场景大流量A/B测试，对比RecGPT-V2基线：主Feed场景IPV+1.28%、CTR+1.00%、TC+1.97%、GMV+3.97%，端到端服务资源消耗降低52.4%；用户建模算力降低55.8%，推理token成本降低200倍。
最值得记住的结论：LLM完全可以作为工业级业务系统的智能核心，同步实现推荐精度与服务效率的提升，而非二者只能取其一
