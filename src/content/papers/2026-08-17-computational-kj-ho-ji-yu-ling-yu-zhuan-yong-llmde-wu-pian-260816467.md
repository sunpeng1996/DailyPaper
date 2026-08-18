---
title: 'Computational KJ-Ho: An Analyst-Bias-Free Insight Extraction Framework from
  Large-Scale Qualitative Data Using Domain-Specialized LLMs'
title_zh: Computational KJ-Ho：基于领域专用LLM的无偏差洞见提取框架
authors:
- Kasumi Ban
affiliations:
- Sophia University Graduate School, Graduate Program in Applied Data Sciences
arxiv_id: '2608.16467'
url: https://arxiv.org/abs/2608.16467
pdf_url: https://arxiv.org/pdf/2608.16467
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: 领域专用LLM · 消费者洞见提取
tags:
- Domain-Specific LLM
- Consumer Insight
- Continued Pre-Training
- Supervised Fine-Tuning
- Qualitative Analysis
one_liner: 基于领域专用LLM复现KJ法逻辑，实现大规模定性数据无分析师偏差的洞见自动化提取
practical_value: '- 挖掘用户评论、客服对话等非结构化定性数据时，可复用「CPT+SFT训练领域专用LLM」范式，相比通用LLM降低人工偏差，提升洞见准确率

  - 可复用三层架构落地端到端用户洞察系统：先做非结构化数据结构化聚类，再提取用户需求标签，最后关联可落地运营动作

  - 做领域LLM效果评估时，可参考自定义业务指标思路，比如针对电商场景设计需求识别F1、运营策略有效性QA等专属评估维度，替代通用LLM评测指标'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统KJ法、扎根理论等定性消费者洞察方法受限于人类分析师认知上限，无法处理大规模用户数据，且存在分析师主观偏差；现有自动化方案依赖通用LLM，缺乏领域知识沉淀，无针对性评估指标，输出难落地为可执行策略。

### 方法关键点
提出Computational KJ-Ho三层架构，先对营销调研语料做**Continued Pre-Training (CPT)**，再用专家标注的洞见对做**SFT**得到领域专用LLM；架构分为三层：数据结构化层、洞见提取层、策略生成层，无需分析师预设立场即可让结构从数据中自动涌现。

### 关键结果
日本营销场景预实验验证了基于CPT的领域专用LLM效果优于通用方案；配套提出**InsightExtraction-F1**、**MarketingQA**两个专属评估指标，可量化洞见质量与落地可行性。
