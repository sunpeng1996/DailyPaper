---
title: 'When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable
  Capability Retrieval'
title_zh: 可执行能力检索的源风格坍塌问题与源感知路由优化
authors:
- Yiqi Liu
- Joseph James
- Yang Wang
- Chenghao Xiao
- Chenghua Lin
affiliations:
- University of Manchester
- University of Sheffield
- Shanghai University of Finance and Economics
arxiv_id: '2608.16502'
url: https://arxiv.org/abs/2608.16502
pdf_url: https://arxiv.org/pdf/2608.16502
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: Agent 可执行能力检索可靠性优化
tags:
- Tool Retrieval
- Agent
- Source Style Collapse
- RAG
- Routing
- Fine-tuning
one_liner: 发现工具检索的源风格坍塌失效模式，提出基于TF-IDF的路由方案大幅提升多源场景覆盖率
practical_value: '- 多源query场景（如电商搜索/客服/导购多渠道query、多团队维护的工具库RAG）不要仅在单源数据上fine-tune
  dense retriever，避免跨源召回率暴跌的源风格坍塌问题

  - 检测跨源匹配度无需复杂语义模型，基于query侧TF-IDF质心与训练源质心的余弦距离即可实现低成本判断，效果优于BGE-M3等语义embedding检测

  - 可直接复用路由方案：匹配源流量用垂直fine-tune的检索器保证效果，非匹配源路由到全源训练检索器，仅需20条左右匹配样本做增量fine-tune即可快速修复坍塌场景

  - 工具/API检索fine-tune时优先选择检索混淆的语义硬负样本，效果优于同品类负样本、随机负样本，能显著提升召回准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大模型Agent依赖RAG检索外部工具/API获取可执行能力，检索层是前置瓶颈：若召回不到正确工具，下游规划/重排完全无法修复。现有检索适配方案大多假设语料库变化，忽略了**工具库完全固定时，单源fine-tune的检索器在其他来源query上会静默失效**的问题，这对部署了多来源工具、多渠道query的生产系统影响极大。

### 方法关键点
- 定义「源风格坍塌」失效模式：同一工具库下，单源训练的dense retriever在其他来源query上召回率暴跌，且无法用query与工具的词法重叠解释
- 低成本源匹配检测：计算query的TF-IDF质心与训练源TF-IDF质心的余弦距离，检测效果优于语义embedding、query长度等指标
- ToolScout路由机制：距离在安全阈值内用垂直fine-tune检索器，否则路由到全源训练检索器；积累20条左右匹配样本后做增量fine-tune快速修复坍塌
- 验证了该失效与API格式无关，将工具统一转为技能卡片后问题仍然存在

### 关键结果
在ToolRet数据集（44k+工具、4996条混合源query）上测试：
1. 单源fine-tune的FT-1100检索器在APIGen源上top20覆盖率从训练源的91.8%暴跌至0.7%，完全失效
2. TF-IDF路由将混合源流量的覆盖率从22.3%提升至86.1%
3. 5个坍塌源上，仅用20条匹配样本增量fine-tune，覆盖率加权的全局top1准确率从1.3%提升至53.9%

### 核心结论
工具RAG的检索可靠性不能仅看单源测试指标，低成本的TF-IDF源匹配+路由是解决多源场景源风格坍塌的性价比最高方案
