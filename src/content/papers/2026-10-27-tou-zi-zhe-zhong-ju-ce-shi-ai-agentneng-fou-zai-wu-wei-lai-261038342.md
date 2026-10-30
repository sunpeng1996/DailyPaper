---
title: 'Investor''s Last Exam: Can AI Agents Do Equity Investment Without Seeing the
  Future?'
title_zh: 投资者终局测试：AI Agent能否在无未来信息条件下完成股权投资
authors:
- Huangfei Jiang
- Anning Hu
- Kai Sheng
- Yuchen Cai
- Rui Ge
- Xiangyu Kong
- Jianghao Lin
- Shuzi Chen
- Jiyi Weng
- Junchi Yan
affiliations:
- Prophetlab
- RethinkLab
- Antai College of Economics and Management, SJTU
- USTC
- Foresight Fund
arxiv_id: '2610.38342'
url: https://arxiv.org/abs/2610.38342
pdf_url: https://arxiv.org/pdf/2610.38342
published: '2026-10-27'
collected: '2026-10-30'
category: Agent
direction: 金融Agent 投研能力全链路评测
tags:
- Agent
- Evaluation Benchmark
- Financial Agent
- Decision Making
- LLM
one_liner: 推出由专业买方投资者主导的股权投资AI Agent全链路可追溯评测基准ILE
practical_value: '- 可复用「带严格时间戳的版本化知识库+依赖图打分」框架，解决电商大促/营销Agent评测中未来数据泄露的问题

  - 「从孤立能力评测转向证据-假设-决策全链路评测」的思路，可迁移到电商选品、广告投放Agent的效果评估体系搭建

  - 专业领域Agent落地可参考「行业专家定义任务taxonomy+对齐职业交付物」的模式，降低对齐业务需求的成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有金融Agent评测仅覆盖单点知识、工作流或预测能力，缺乏严格冻结的信息边界与专业评估标准，无法衡量完整投研链路的真实决策效果，还容易出现未来数据泄露问题。
### 方法关键点
1. 构建带校验时间戳的版本化金融数据库，覆盖3.43万份文档、9类数据源，配套结构化行情数据，严格限制检索计算的信息范围；
2. 对齐专业分析师交付物设计任务分类体系；
3. 推出专家主导的金融依赖图打分框架，将评分标准与数据源、计算逻辑、假设条件关联。
### 关键结果
86项任务综合评测显示，GPT-6 Astra、Claude Opus 5.5总分分别为68.1、66.9（满分100），但前者在预测建模模块得分仅52.5，说明当前SOTA模型无法将整体研究能力转化为预测表现。
