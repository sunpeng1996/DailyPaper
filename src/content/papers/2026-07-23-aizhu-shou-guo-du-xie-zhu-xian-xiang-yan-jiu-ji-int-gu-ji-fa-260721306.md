---
title: AI Assistants Overassist
title_zh: 《AI助手过度协助现象研究及Int-Bench评估基准发布》
authors:
- Verona Teo
- Raghav Jain
- Tobias Gerstenberg
- Max Kleiman-Weiner
affiliations:
- Stanford University
- University of California, San Diego
- University of Washington
arxiv_id: '2607.21306'
url: https://arxiv.org/abs/2607.21306
pdf_url: https://arxiv.org/pdf/2607.21306
published: '2026-07-23'
collected: '2026-07-25'
category: Eval
direction: LLM助手行为评估 · 基准构建
tags:
- LLM Assistant
- Int-Bench
- Intervention Evaluation
- Human-AI Alignment
- Evaluation Benchmark
one_liner: 提出评估LLM学习场景干预决策的Int-Bench基准，揭示LLM过度干预、偏好直接给答案的共性问题
practical_value: '- 搭建电商导购Agent、用户学习类助手的干预策略设计可参考研究结论：避免过早/过频介入用户自主决策过程，优先输出定向提示而非完整方案，平衡短期任务完成率与长期用户留存

  - 可复用Int-Bench的「观察者-执行者」双角色模拟框架，评估自家Agent的干预时机、干预粒度是否符合用户预期，优化交互策略

  - 面向商家的AI运营助手、客服助手场景可根据用户层级（新手/熟手）定制干预阈值，新手多给引导提示，熟手减少不必要干预，避免打扰用户自主操作'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM作为AI助教、思考伙伴的应用愈发广泛，但干预时机、干预方式的设计缺乏统一评估标准，过早/过频干预会阻碍用户自主思考与长期学习效果，现有研究对LLM干预决策的行为规律认知不足。
### 方法关键点
1. 提出Int-Bench模拟评估基准，构建「学生解题-教师监控」双角色交互范式，覆盖代码调试、数学、脑筋急转弯3个领域；
2. 从干预频率、干预时机、干预内容类型3个维度评估LLM教师的干预行为，同时对比人类教师的行为差异。
### 关键结果
- 相比人类教师，LLM干预频率更高、干预时机更早；
- 多数LLM倾向直接输出完整解决方案，而人类教师更偏好给出定向提示；
- 当前LLM助手普遍优先优化短期任务成功率，而非支持用户深度思考以提升长期泛化能力。
