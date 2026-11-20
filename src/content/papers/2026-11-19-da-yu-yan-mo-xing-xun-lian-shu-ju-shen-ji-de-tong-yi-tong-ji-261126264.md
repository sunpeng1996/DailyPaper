---
title: A Statistical Framework for Training Data Auditing of Large Language Models
title_zh: 大语言模型训练数据审计的统一统计框架
authors:
- Shengjie Niu
- Yeheng Ge
- Jian Huang
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2611.26264'
url: https://arxiv.org/abs/2611.26264
pdf_url: https://arxiv.org/pdf/2611.26264
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM训练数据审计 · 成员推断
tags:
- TrainingDataAuditing
- MembershipInference
- LLM
- MultipleTesting
- StatisticalFramework
one_liner: 提出统一统计框架实现LLM训练数据的单文档推断、全局审计与可疑子集识别
practical_value: '- 业务侧微调LLM做推荐/文案生成时，可复用该框架检测测试集是否混入训练数据，避免评估结果虚高

  - 自有版权的商品文案、用户问答数据被第三方LLM违规使用时，可借鉴Cauchy组合chunk证据的方法做侵权举证，提升长文档核验准确率

  - 构建Agent调用的私有知识库时，可用该框架审计预训练LLM是否已包含知识库内容，减少冗余RAG调用成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
LLM训练语料通常不公开，存在版权侵权、用户隐私泄露、benchmark测试集污染等风险；现有审计方法处理长文档时易稀释仅存在于局部片段的成员归属信号，且缺乏从单文档到全数据集的统一审计能力。

### 方法关键点
1. 采用Cauchy组合规则融合不同chunk的成员推断证据，构造文档级得分，避免局部信号被稀释
2. 对文档得分校准得到p值，通过多重检验实现目标数据集全局审计、可疑文档子集识别
3. 理论上证明了有限样本下p值有效性、全局审计I类错误可控、子集识别错误发现率（FDR）可控

### 关键结果
在BookTection、Pile-arXiv、Cosmopedia、HealthCareMagic四个公开数据集上，验证了该框架在预训练、微调阶段数据审计的有效性与可靠性。
