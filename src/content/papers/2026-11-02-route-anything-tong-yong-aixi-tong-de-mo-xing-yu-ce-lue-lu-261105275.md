---
title: 'Route Anything: A Study of Model and Policy Routing for General-Purpose AI
  Systems'
title_zh: Route Anything：通用AI系统的模型与策略路由研究
authors:
- Pengfei Zhou
- Yixing Ma
- Hexin Wang
- Weidong Tang
- Zhenglin Wan
- Wangbo Zhao
- Yang You
affiliations:
- National University of Singapore
- InfRec, Cardinal AI Lab
- University of California, Berkeley
- Hong Kong University of Science and Technology
arxiv_id: '2611.05275'
url: https://arxiv.org/abs/2611.05275
pdf_url: https://arxiv.org/pdf/2611.05275
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent 多模型调度路由优化
tags:
- Model Routing
- Cost-Efficiency
- Multimodal AI
- Agent Orchestration
- LLM Deployment
one_liner: 提出跨模态统一模型与策略路由框架，量化收益并给出路由落地最佳实践
practical_value: '- 做多模型路由时优先训练回归每个候选的输出效果，不要训练分类最优候选的winner标签，后者会因平局/成本tie-break引入大量噪声，效果远差于回归方案

  - 多候选对比必须在相同输入集上评估，不能因少数输入结果缺失淘汰强模型，否则会导致基线偏低，错误高估路由收益

  - 质量可控的降本路由收益远高于提优：允许<0.5分质量损失时平均效率提升8.82倍，电商客服、商品文案生成等场景可直接复用这套质量约束+效率优化的路由方案

  - 路由潜在收益90%以上来自任务类型内部的输入级差异，仅靠粗粒度任务类型路由只能拿到8%的收益，需要做更细粒度的输入特征感知'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用AI系统依赖异构专业模型、工具、策略协同完成跨域跨模态任务，单模型无法兼顾所有场景的效果与成本。现有路由研究多集中在LLM领域，跨模态场景下路由的潜在收益、最优实现方案、质量管控方法尚未形成系统性结论。

### 方法关键点
- 建立统一路由理论框架，基于价值-成本加权目标建模最优路由策略，定义信息阶梯量化不同观测粒度（任务类型、输入特征、全输入）下的路由性能上限
- 构建覆盖25个基准的全模态轨迹矩阵，包含文本理解、音视频生成、代码、机器人操作等场景，共452个候选配置的374401次带评分运行记录
- 对比三类路由实现方案，明确训练目标、评估方法、质量校验的最佳实践

### 关键结果
- 输入级理想oracle比各场景最优固定候选平均高5.4分，视频生成、机器人操作场景提升达18-19分
- 学习到的路由模型比最优固定候选平均高0.3分，视频生成场景高2.1分，机器人操作场景高1.1分同时减少24%推理时间
- 在允许<0.5分质量损失的约束下，路由相比基准模型平均效率提升8.82倍，代码场景达25.5倍，文本QA场景达7.1倍

> 最值得记住的结论：路由的核心价值是可控质量损失下的效率优化，优先做单候选效果回归、同输入集对比、独立集质量校验是落地三大原则。
