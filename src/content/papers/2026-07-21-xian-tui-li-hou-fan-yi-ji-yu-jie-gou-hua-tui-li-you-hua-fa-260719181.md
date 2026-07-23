---
title: 'Reasoning Before Translation: Enhancing Legal Machine Translation with Structured
  Reasoning'
title_zh: 先推理后翻译：基于结构化推理优化法律领域机器翻译
authors:
- Aixiu An
- Michael Jungo
- Eloi Eynard
- Mark Drenhaus
- Andreas Fischer
- Jean Hennebert
- Sébastien Rumley
affiliations:
- iCoSys, University of Applied Sciences and Arts Western Switzerland
- AIBEX, University of Fribourg
- Neur.on, Fribourg
- Human-IST, University of Fribourg
arxiv_id: '2607.19181'
url: https://arxiv.org/abs/2607.19181
pdf_url: https://arxiv.org/pdf/2607.19181
published: '2026-07-21'
collected: '2026-07-23'
category: LLM
direction: 大语言模型 · 垂直领域微调优化
tags:
- Legal NMT
- Supervised Fine-Tuning
- Reinforcement Learning
- Small Language Model
- Model Evaluation
one_liner: 对比多类微调范式对小模型法律翻译的优化效果，验证可验证奖励RL性能优于SFT
practical_value: '- 电商跨语种合规文案生成、商品参数多语言对齐等高精度要求的垂直生成任务，可优先采用可验证奖励的RL微调，效果优于普通SFT

  - 中小参数模型适配垂直业务场景时，重训范式的收益远高于大模型，可优先优化小模型降低部署推理成本

  - 垂直场景LLM选型时，可先验证「小模型+针对性微调」方案，效果接近前沿大模型时可直接落地，平衡成本与业务效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
法律领域机器翻译对术语准确性、逻辑一致性要求极高，通用NMT方案难以满足专业场景的精度要求，亟需适配高约束垂直场景的LLM优化路径。
### 方法关键点
以瑞士多语种法律文本为测试基准，对比SFT、可验证奖励RL等重训范式在Qwen3.5 4B/9B、Gemma3 12B三类小模型上的优化效果，同时与前沿推理大模型做性能对齐。
### 关键结果
1. 可验证奖励RL微调的翻译效果显著优于SFT，是最优重训方案；
2. 经重训优化的小模型性能接近前沿推理大模型，仅存在极小差距；
3. 重训范式的收益随模型尺寸增大快速递减，大模型重训的投入产出比远低于中小模型。
