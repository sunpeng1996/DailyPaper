---
title: 'Memory Tax: Dissecting the Net Value of Agent Memory'
title_zh: 记忆税：拆解Agent记忆系统的净价值
authors:
- Xuan He
- Sining Zhoubian
- Ruozhen Yang
- Yuhao Wen
- Zhineng Wang
- Yuyang Hu
- Ke Yang
- Yuyu Zhang
- Ping Nie
- Jiawei Han
affiliations:
- University of Illinois Urbana Champaign
- Tsinghua University
- Renmin University of China
- Verdent.ai
- University of Waterloo
arxiv_id: '2610.34073'
url: https://arxiv.org/abs/2610.34073
pdf_url: https://arxiv.org/pdf/2610.34073
published: '2026-10-24'
collected: '2026-10-28'
category: Agent
direction: Agent 长时记忆净价值评估与优化
tags:
- Agent Memory
- RAG
- Memory Tax
- Long-Horizon Agent
- LLM Agent
one_liner: 提出记忆税概念，量化拆解Agent记忆系统相对朴素RAG的净价值与损耗来源
practical_value: '- 业务落地Agent记忆系统时，优先以朴素分块RAG为基线，不要盲目引入复杂记忆架构，多数检索友好场景（如电商用户对话记忆、商品咨询历史召回）下RAG的性价比远高于复杂记忆系统

  - 优化现有记忆系统可直接复用文中的轻量化改造方案：记忆检索结果与原始历史召回结果联合重排，实测可降低30%以上的记忆税，无需重构记忆架构

  - 评估自研/第三方记忆系统时，必须对齐Retrieval Scope（召回给LLM的总token量），避免不公平的配置夸大复杂记忆架构的效果

  - 针对电商用户画像、个性化推荐等偏好抽象需求，可仅对高置信度的长期偏好做结构化记忆，短期交互信息保留原始格式减少信息丢失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长horizon LLM Agent记忆系统架构日益复杂，但多数方案仅在同类记忆系统间做对比，普遍忽略朴素RAG基线，其相比直接检索原始历史的实际净价值长期不明确，大量场景下复杂记忆系统甚至出现负收益。

### 方法关键点
- 以朴素分块RAG为统一参照，将记忆系统的净价值拆解为**记忆收益**（解决RAG答错的Query）与**记忆税**（答错RAG答对的Query），二者均源于记忆处理对原始历史信息的双向偏移
- 从三个维度定位记忆税来源：忠实度（信息留存完整度）、可及性（存储信息的检索难度）、鲁棒性（跨LLM backbone的性能波动）
- 覆盖会话记忆、经验记忆、世界模型记忆三类主流记忆场景，验证记忆税概念的普适性

### 关键结果
在LongMemEval-s、PersonaMem-v2、MINT-Eval三个主流Agent记忆基准上，测试10+主流开源记忆系统，对齐Retrieval Scope的公平配置下，多数系统相对2轮RAG的准确率低1.2%~40.4%，仅极个别系统在特定任务上实现最高3.9%的准确率增益；加入原始历史回溯通路的轻量化优化，可将记忆税降低4%~6.8%。

### 最值得记住的一句话
Agent记忆系统的核心价值是相对朴素RAG的净收益，任何记忆处理操作的偏移都同时存在收益与损耗，优先保证有害偏移可恢复。
