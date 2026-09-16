---
title: 'Root-Cause Attribution Is a Search Problem: Continual Search for Long-Horizon
  Agent Failures'
title_zh: 长周期Agent故障根因归因：基于持续搜索的迭代诊断框架
authors:
- Harsh Raj
- David Lee
- Anas Mahmoud
- Renxiong Wang
- Razvan-Gabriel Dumitru
- Chenguang Wang
- Tong Zhao
- Yunzhong He
- Darvin Yi
- Vipul Gupta
affiliations:
- Scale AI
arxiv_id: '2609.13463'
url: https://arxiv.org/abs/2609.13463
pdf_url: https://arxiv.org/pdf/2609.13463
published: '2026-09-10'
collected: '2026-09-16'
category: Agent
direction: Agent故障根因归因 · 长轨迹迭代诊断
tags:
- Root Cause Attribution
- Long-Horizon Agent
- LLM Judge
- Continual Search
- RCA Benchmark
one_liner: 提出迭代式持续搜索框架，解决长周期Agent故障根因归因精度低的问题，F1最高提升超40%
practical_value: '- 搭建电商Agent、推荐系统badcase溯源系统时，可复用持续搜索框架替代单轮LLM判断，每轮强制诊断模型探索未读的用户行为路径、策略执行日志等证据，相比自一致性、多评委投票等方案成本更低、诊断准确率更高

  - 长文本诊断场景优先分配算力到多轮搜索而非提升单轮推理规格，低阶LLM搭配持续搜索可超过更高阶LLM的单轮诊断效果，最高可降低24%左右的推理成本

  - 短轨迹（<10K token）的诊断场景不要盲目使用多轮迭代，避免LLM受prompt压力翻转正确结论，直接使用单轮判断即可'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期Agent在复杂任务中的落地越来越广泛，执行日志可达百万token规模，故障根因归因（RCA）是保障Agent可靠性的核心环节。现有单轮LLM Judge方法容易过早锁定表面故障，漏看分散在长轨迹中的关键证据，人工审核成本极高，且现有基准缺少超大规模长轨迹的RCA评测样本，亟需更高效的自动化诊断方案。

### 方法关键点
- 对比单轮判断、被动重判、自一致性、多评委面板等现有方案，提出**Continual Search**迭代框架：每轮强制Judge挑战当前诊断结论，主动探索未读证据、未排查的失败步骤、未考虑的根因分类
- 发布MegaRCA-Mix基准数据集：包含50个人工标注的长周期Agent失败案例，中位日志长度286K token，覆盖软件研发、科研、安全等多领域的全量执行证据

### 关键实验
在5个公开RCA基准上验证效果，对比单轮判断、被动重判、自一致性、多评委面板等baseline：
- 长轨迹场景下效果提升显著：在MegaRCA-Mix上，GPT-5.5的F1从0.349提升42.7%至0.498，Opus-4.8的F1从0.478提升至0.62
- 低阶模型收益更高：Sonnet-5搭配持续搜索仅用76%的算力即可达到高阶模型Fable-5的同等诊断效果
- 短轨迹（<10K token）场景下持续搜索反而会因prompt压力导致效果下降，最多降低18%的准确率

### 核心结论
长周期根因归因核心是搜索受限而非推理受限，扩容搜索轮次的收益远高于提升单轮推理算力。
