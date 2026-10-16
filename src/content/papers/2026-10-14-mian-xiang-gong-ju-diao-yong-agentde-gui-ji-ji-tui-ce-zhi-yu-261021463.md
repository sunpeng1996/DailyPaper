---
title: Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents
title_zh: 面向工具调用Agent的轨迹级推测执行与语义验证框架SpecAgent
authors:
- Zilin Wang
- Yinhong Liu
- Chao Chen
- Qun Liu
- Zhijiang Guo
affiliations:
- LARK, HKUST (GZ)
- Yinwang
- University of Cambridge
- HKUST
arxiv_id: '2610.21463'
url: https://arxiv.org/abs/2610.21463
pdf_url: https://arxiv.org/pdf/2610.21463
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent工具调用 · 强弱模型协作
tags:
- Tool-using Agent
- Speculative Execution
- Weak-Strong Collaboration
- Semantic Verification
- Edge-Cloud Deployment
one_liner: 提出强弱模型协作的SpecAgent框架，大幅降低工具Agent的时延与显存带宽消耗
practical_value: '- 可复用强弱模型分工范式：将大模型从每步生成者转为验证者，仅在订单修改、券发放等不可逆操作前做校验，其余步骤由小模型执行，适合电商客服Agent、售后自动化等场景降本提效

  - 语义验证逻辑可迁移：放弃要求小模型输出与大模型精确匹配，只要语义朝向任务目标就算有效，可大幅提升小模型草稿接受率，降低大模型调用量

  - 工程侧可复用代价模型：基于LLM推理显存带宽绑定特性，优先将大模型算力用在批量prefill的验证场景，而非逐step的 autoregressive 生成场景，单位算力产出更高

  - 边缘云部署可直接套用：小模型在边缘侧执行查询订单、库存等只读操作，大模型在云端仅校验关键操作，既能降低API成本，又可减少隐私数据外传风险，适合电商敏感业务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前工具调用Agent普遍采用单一大模型生成每一步，时延、成本随交互轮次线性上升，但多数常规操作（查订单、搜库存）小模型完全可胜任；现有强弱协作方案仍要求大模型生成每步参考结果，未从根本上降低大模型开销。

### 方法关键点
- 操作分类执行：只读操作小模型直接执行，首个修改环境的不可逆操作（如退款、改地址）先挂起，等待大模型验证
- 语义前缀校验：大模型一次prefill读取整段小模型生成的轨迹，返回最长语义合法前缀，仅修复第一个错误步骤，无需逐token生成完整轨迹
- 轻量修复设计：常见错误直接在验证结果中返回修复方案，仅复杂修复才需要大模型单独生成一步

### 关键结果
在τ2-Bench、AutomationBench、VitaBench、MCP-Atlas四个基准上对比单模型、AgentCollab等基线：
- τ2-Bench零售场景下，成功率和397B大模型基线仅差0.9个百分点，显存带宽消耗降至53-57%，时延降至54%
- 边缘云部署场景下，填补53-75%的强弱模型质量差，大模型输出token量仅为基线的36-50%，API成本降至59-81%

> 最值得记住：大模型不需要生成Agent的每一步，只要做grounded草稿的审核者，就能保留大部分质量的同时大幅降低时延和成本。
