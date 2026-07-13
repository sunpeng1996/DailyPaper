---
title: Task-Specific Multimodal Question Answering Agents via Confidence Calibration
  and Incremental Reasoning for QANTA 2026
title_zh: 面向QANTA 2026的任务专属多模态问答Agent：置信度校准与增量推理
authors:
- Nirjhar Das
- Md. Al-Mamun Provath
affiliations:
- Chittagong University of Engineering & Technology
arxiv_id: '2607.09623'
url: https://arxiv.org/abs/2607.09623
pdf_url: https://arxiv.org/pdf/2607.09623
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 多模态问答任务优化
tags:
- Multimodal QA
- Confidence Calibration
- Agent Specialization
- Incremental Reasoning
- Human-AI Collaboration
one_liner: 提出双Agent多模态问答架构，通过置信度校准与任务专属推理策略登顶QANTA 2026竞赛榜首
practical_value: '- 多任务场景可采用任务专属Agent拆分设计：低延迟要求的实时任务用轻量模型（如实时召回、增量query推荐），高推理要求的离线/厚并发任务用大模型（如商品文案生成、多模态内容审核），平衡成本与效果

  - 置信度校准+门槛判断的思路可迁移到实时搜索提示、流式内容生成等增量输出场景，搭配领域专属规则防火墙（如数值、敏感内容校验），减少错误输出的业务损失

  - 多模态任务采用文本先生成候选、图像做二次校验的晚融合策略，比同步处理多模态输入算力成本低30%以上，可直接复用在电商图文商品分类、卖点抽取场景

  - 人机协作类输出（如广告创意审核、运营策略建议）需优化为「答案+置信度+精简佐证」的短结构，可提升人工采纳率20%以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
QANTA 2026多模态问答竞赛包含两类目标差异极大的任务：抢答类Tossup任务需边接收增量文本/图像线索边决策答题时机，答错会触发惩罚，对延迟和置信度校准要求极高；加分类Bonus任务需基于完整上下文做结构化推理，输出要适配人机协作场景，对准确率和可解释性要求更高。通用统一模型难以同时满足两类任务的效率、准确率、置信度约束，需要针对性设计。
### 方法关键点
- 双Agent拆分架构：Tossup任务采用轻量低延迟的GPT-4.1-mini，Bonus任务采用推理能力更强的GPT-4.1，分别优化任务目标
- Tossup Agent核心策略：设置0.9的置信度抢答阈值，搭配期望收益公式做抢答决策；新增数值防火墙规则，仅当孤立数字线索搭配命名实体/公式上下文/多线索佐证时，才允许提升置信度，避免过度自信
- Bonus Agent核心策略：先解析题干导语约束候选答案空间，采用文本先出候选、图像做交叉校验的晚融合多模态策略；输出格式简化为「答案+置信度+精简证据」，提升人工审核效率
### 关键结果
在QANTA 2026官方竞赛基准上，无额外检索或模型集成，仅靠任务专属策略获得总得分0.402，排名第1，领先第二名0.032；Tossup任务得分0.238，抢答精度72.5%，总推理成本仅0.14美元；Bonus任务得分0.164，单题部分准确率89.1%，置信度校准度88.2%，人工采纳率33.8%。
### 核心结论
高效多模态任务的收益核心来自任务专属推理策略、置信度校准、轻量化证据融合，而非复杂的prompt工程或更大的统一模型。
