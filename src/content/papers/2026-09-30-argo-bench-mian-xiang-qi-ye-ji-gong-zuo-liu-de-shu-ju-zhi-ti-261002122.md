---
title: 'Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows'
title_zh: Argo-Bench：面向企业级工作流的数据智能体评测基准
authors:
- Gabriel Tomitsuka
- Arman Raayatsanati
- Emma Xing
- Duke Gand
- Joseph J Ma
affiliations:
- TextQL
arxiv_id: '2610.02122'
url: https://arxiv.org/abs/2610.02122
pdf_url: https://arxiv.org/pdf/2610.02122
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: 智能体评测 · 企业级数据工作流
tags:
- Agent
- Benchmark
- Enterprise-Data
- Text-to-SQL
- Simulation
one_liner: 构建含75亿行ERP数据的仿真外卖平台基准，端到端评测数据Agent的决策落地效果
practical_value: '- 业务Agent评测可复用「仿真环境+隐状态打分」架构：决策类任务无需人工标注黄金答案，直接基于决策在仿真环境中的实际收益判分，解决标注准确率低的问题

  - 企业级多表数据Agent的任务设计可参考：将数仓表探索、多工具调用（SQL+Python）、决策落地全链路纳入评测，避免仅验证单步SQL生成的片面性

  - 电商反欺诈、预算分配、销量预测类Agent开发可复用失败经验：优先做多源数据校验避免读错表/字段，对齐业务真实目标避免优化错指标，预测任务需做置信度校准降低过自信问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数据Agent评测大多仅覆盖text-to-SQL单步任务，依赖的人工标注答案错误率超50%，且多基于零散公开数据集，无法复现企业ERP场景下单个业务事件跨数十张表、需结合SQL+ML/优化方法输出决策并落地的真实工作流，也无法衡量决策的实际业务收益。
### 方法关键点
- 仿真还原2024年纽约市外卖平台全量业务，包含8100万订单、340万活跃用户，真实复现薪资政策调整、欺诈模式、市场激励规则，完全对齐官方披露的经济数据
- 导出为符合Oracle EBS规范的ERP数仓，共235张表、74.9亿行，隐去仿真器底层真实状态，Agent仅可通过数仓查询+Python沙箱工具完成任务
- 设计210个覆盖反欺诈封禁、预算分配、销量预测、财报核对、增长效果分析的业务任务，直接对Agent的最终决策结果打分，而非中间SQL
### 关键结果
测试14款前沿闭源/开源模型，最强的Claude Opus 5.5仅能在34.8%的任务上得分≥95，平均得分仅59.5，9款模型平均得分低于35；模型输出的80%置信度预测区间实际覆盖率仅44.8%，普遍存在目标理解错误、多表关联错误、过自信的问题。
### 核心结论
现有大模型在企业级数据工作流上的落地能力远未成熟，评测不能只看单步SQL准确率，需重点关注端到端决策的业务收益。
