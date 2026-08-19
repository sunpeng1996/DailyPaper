---
title: 'Deep Academic Survey: Stateful Agentic Closed-Loop Paradigm for Academic Survey
  Automation'
title_zh: DAS：面向学术综述自动化的有状态智能体闭环生成范式
authors:
- Zhikai Xu
- Zhucun Xue
- Teng Hu
- Yabiao Wang
- Yong Liu
- Jiangning Zhang
affiliations:
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2608.18034'
url: https://arxiv.org/abs/2608.18034
pdf_url: https://arxiv.org/pdf/2608.18034
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: 智能体长文本生成 · 闭环状态管理
tags:
- LLM Agent
- Long-form Generation
- Closed-loop Optimization
- Evaluation Benchmark
- Retrieval Augmentation
one_liner: 提出首个有状态智能体学术综述生成框架，配套200万论文元数据湖与专用评测基准，效果超现有方案
practical_value: '- 可复用元数据湖+主题态生成的拆分架构可直接迁移到电商种草文案、商品详情页生成场景，提前预处理商品/内容的结构化属性，避免不同生成任务重复调用LLM解析物料，降本提效

  - 反向物料-模块路由机制可用于多素材组装类生成任务，提前将召回的商品/内容素材匹配到对应文案模块，从根源减少生成内容与物料不匹配的幻觉问题

  - 分粒度闭环修复策略可复用到生成式推荐、广告文案的质检环节，根据缺陷类型选择修改单句、重写段落或重构整个模块，平衡生成质量与token消耗'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
学术文献指数级增长，手动撰写综述需消耗大量专家精力，现有深度调研和自动综述生成系统要么缺乏学术规范性、引用匹配不准，要么各环节独立无共享状态，导致内容不一致、重复计算成本高，无法生成符合出版要求的标准化综述。

### 方法关键点
- 预构建DAS-2M动态元数据湖，存储200万篇2020-2026年arXiv论文的面向综述的8类结构化表示，支持BM25+稠密检索的混合召回，避免不同任务重复解析论文
- 全程维护文献、结构、写作、终稿四类可追溯状态，通过候选文献驱动的大纲规划、反向论文-章节路由、层级化论点-引用规划实现从素材到内容的全链路对齐
- 设计范围化语义评审+确定性校验闭环，仅激活缺陷对应的状态节点修复，支持直接改句、重写段落、重构章节三种修复策略，降低返工成本
- 构建包含30个主题的DAS-Bench评测基准，配套DAS-Eval从引用质量、大纲合成、层级论述、手稿可靠性4维度共16个指标做标准化评估

### 关键结果数字
在30个主题评测中DAS总得分4.34，优于最强基线Naive RAG的4.03；盲测中专家在27/30个主题偏好DAS优于Naive RAG，19/21个CS主题偏好DAS优于AutoSurvey；自适应修复策略实现74.59%的评审通过率，单篇综述仅消耗0.79M token，修复成本低于所有单策略方案。

### 最值得记住的一句话
把长文本生成拆分为可复用的物料预处理、有状态的层级规划、分粒度的闭环修复三个阶段，是同时提升生成质量、降低计算成本的核心路径。
