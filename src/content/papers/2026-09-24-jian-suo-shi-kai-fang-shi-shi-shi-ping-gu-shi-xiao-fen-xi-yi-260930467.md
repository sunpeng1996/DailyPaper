---
title: Where Does Retrieval-Based Open-Ended Evaluation Fail? Automatic Taxonomy Induction
  from Long-Form Medical Answer Factuality Verification
title_zh: 检索式开放式事实评估失效分析：医疗长回答核验的自动错误分类体系
authors:
- Heyuan Huang
- Jirui Dai
- Alexandra DeLucia
- Sonal Joshi
- Mahsa Yarmohammadi
- Jie Gao
- Bernal Jiménez Gutiérrez
- Mark Dredze
affiliations:
- Johns Hopkins University
arxiv_id: '2609.30467'
url: https://arxiv.org/abs/2609.30467
pdf_url: https://arxiv.org/pdf/2609.30467
published: '2026-09-24'
collected: '2026-09-28'
category: Eval
direction: RAG错误诊断 · 医疗场景事实核验
tags:
- RAG
- Factuality Verification
- Error Taxonomy
- LLM-as-Judge
- Medical NLP
one_liner: 提出无金标依赖的检索+验证两阶段错误分类体系，揭示医疗场景检索验证范式的结构性局限
practical_value: '- 高风险业务（如电商医疗健康类商品推荐合规审核、RAG问答事实校验）可直接复用这套检索+验证两阶段错误分类框架，通过LLM-as-Judge无需金标即可规模化定位系统瓶颈，避免仅靠F1等聚合指标误判

  - 优化业务RAG系统时，不要盲目堆大模型、扩检索库：检索侧除相关性外，需补充适用范围匹配、信息极性、来源可信度多维度评估；验证侧拆解推理步骤排查错误，可有效降低线上事实错误率

  - LLM选型不要唯基准榜论：如论文中小模型Mistral Small3召回率更高但推理错误率高，业务中可先用小模型做初筛召回风险case，再用大模型做精细校验，平衡效果与成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索式事实核验系统仅输出F1等聚合指标，无法定位失效根因；主流RAG诊断方案依赖金答案或金证据标注，在医疗等高风险开放式场景下这类标注不存在，检索-验证范式在开放式场景性能暴跌的根本原因缺乏系统性分析。
### 方法关键点
- 构建无金标依赖的两阶段错误分类体系：检索侧错误拆分为实体匹配、适用范围匹配、来源可信度、证据极性、分片问题5个维度；验证侧错误拆解为证据选择、理解、推理、置信度校准、一致性、grounding 6个连续步骤
- 采用LLM-as-Judge自动标注错误模式，可规模化开展错误分析，无需人工标注金答案/金证据
- 跨4种检索器、6款主流验证LLM、3类知识库做对照实验，覆盖1个开放式医疗数据集MedExpert + 4个封闭式医疗基准数据集
### 关键结果
- 最优配置（Qwen3检索+GPT-5.4验证）在开放式医疗数据集MedExpert-gold上F1仅35.2%，远低于封闭式数据集0.7~0.8的水平
- 升级检索器、将知识库扩容到谷歌权威来源、使用更大/医疗微调的验证模型、增加推理步数均无法解决核心失效问题，属于检索-验证范式的结构性局限
- 端到端指标易误导选型：小模型Mistral Small3召回率最高达34.9%，但推理步骤正确率仅66%，高召回是错误推理导致的偶然结果
### 核心结论
仅依赖端到端聚合指标的RAG系统评估会掩盖真实失效模式，多维度的中间过程评估才能准确定位系统瓶颈。
