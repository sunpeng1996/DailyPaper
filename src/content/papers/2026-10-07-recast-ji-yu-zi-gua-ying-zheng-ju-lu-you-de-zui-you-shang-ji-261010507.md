---
title: 'RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing'
title_zh: 《RECAST：基于自适应证据路由的最优上下文计算框架》
authors:
- Yilun Hao
- Krishna Sayana
- Isabella Ye
- James S Ren
- Sukhdeep Sodhi
- Craig Boutilier
- Chuchu Fan
affiliations:
- MIT
- Google Research
arxiv_id: '2610.10507'
url: https://arxiv.org/abs/2610.10507
pdf_url: https://arxiv.org/pdf/2610.10507
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 自适应证据路由上下文构建
tags:
- RAG
- Agent
- Tool Use
- GRPO
- SFT
- Context Construction
one_liner: 提出结合检索与计算的多轮证据路由框架，轻量化RouterLM动态构建上下文，性能超最强基线15.9%
practical_value: '- 电商RAG场景可复用「检索+计算双操作」架构，处理用户需聚合/计算类查询（如'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统RAG仅能召回已存在的源内容，无法处理需要跨源聚合、数值计算、多条件筛选等需推导证据的场景（如计算品类同比增速、筛选高性价比商品），现有Agent工具调用框架多直接生成答案，缺乏专门的证据构建与充分性判定环节，在异构数据源下准确率低、token成本高。

### 方法关键点
- 框架分三层：仅轻量化RouterLM需训练，负责多轮决策，可选调用词汇/语义/关系检索三类原语，或请求冻结的CompilerLM生成自定义可执行代码，判定证据足够时将结果传给冻结的AnswerLM输出最终答案
- 训练分两阶段：先基于筛选后的成功轨迹做SFT冷启，再用GRPO做策略优化，奖励函数按9:0.8:0.2权重兼顾答案正确性、答案F1、动作结构合法性
- 异构源预处理统一转为标准化记录，生成精简源概要供RouterLM感知，无需传入全量源数据，大幅降低token消耗

### 关键实验
在6个异源基准（含表格、金融报告、维基文本、用户画像）上平均成功率75.6%，超最强基线Interact-RAG 15.9%；SFT+GRPO训练后的Qwen3.5-9B RouterLM，比无训练的Gemini 3.5 Flash路由效果高5%；3个零样本跨域基准上平均成功率79.3%，超最强基线15%。

### 最值得记住的一句话
上下文构建不只是召回，更是基于任务需求动态推导证据的过程，检索和计算是互补的证据获取手段。
