---
title: 'ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday
  Tasks'
title_zh: ShellBench：AI Agent日常任务性能核心影响因素：模型还是运行框架
authors:
- Vincent Koc
- Aditya Washikar
- Rishab Naveen Venkataraman
- Onur Solmaz
- Zhentong Fan
- Xinyang Han
- Toby Vincent John
- Hao Li
- Achyut Mukund
- Biresh Chandra Biswas
affiliations:
- OpenClaw Foundation
- Parsewave
- Hugging Face
- NVIDIA
- University of California, Berkeley
arxiv_id: '2611.32946'
url: https://arxiv.org/abs/2611.32946
pdf_url: https://arxiv.org/pdf/2611.32946
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: Agent 基准评测与性能归因
tags:
- AgentBenchmark
- LLMAgent
- AgentHarness
- AgentSafety
- RealWorldTask
one_liner: 提出覆盖100个真实日常任务的Agent基准，量化模型与运行框架对性能的影响
practical_value: '- Agent选型优先倾斜模型资源：模型对性能的贡献达95.7%，harness仅占0.36%，优化模型选择的ROI远高于harness调优

  - 成本敏感场景优先选高性价比模型：GPT-6.1 Sol性能仅比GPT-6 Astra低1.1pp，单轮token成本仅为后者的1/6，适合电商客服、订单处理等大规模落地场景

  - 任务评测可复用「正确性+安全+溯源」rubric设计：要求Agent标注决策来源文件的规则，可直接迁移到电商选品、售后决策的可解释性评估，避免引用过时/错误数据

  - 中小模型可通过提升推理effort拉平性能：Claude Sonnet 5.5从低到高推理档位Pass@1提升19.1pp，小模型落地时可通过调优推理参数获得性价比最优解'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
2026年C端AI Agent用户爆发式增长，但普通用户和开发者难以判断Agent配置（模型+运行框架harness）对日常任务效果的影响，现有Agent基准普遍缺少真实复杂工作环境、安全评估维度、模型与harness的横向对比能力，无法指导落地选型。

### 方法关键点
- 数据：基于1000万+真实个人AI助手用户请求聚类，生成100个日常任务，每个任务配套含中位数188个文件的真实工作环境（含过时信息、钓鱼邮件等干扰项）
- 评测设计：设置721条二元rubric，其中381条为安全准则、72条为溯源准则，采用全或无评分（所有准则通过才算任务成功），用GPT-6.1 Sol作为LLM法官，和人类标注一致性达89.9%
- 对比维度：覆盖12个主流LLM、5个Agent harness、3档推理effort，累计完成53100次rollout

### 关键结果
模型对性能的贡献占95.7%，harness仅占0.36%，harness的Pass@1区间仅为42.9%~45.2%，差异极小；头部3款模型Pass@1差距仅1.1pp（GPT-6 Astra 62.5%、Claude Fable 5.2 61.9%、GPT-6.1 Sol 61.4%）；11款模型在最高推理档位的Pass@1比最低档高0.4~19.1pp；9.9%满足所有正确性准则的任务仍违反安全要求，头部模型安全违规率仅9.4%~12.2%。

### 核心结论
对于绝大多数日常AI Agent场景，选对模型的收益远高于优化harness，头部高性价比模型可在几乎不损失效果的前提下大幅降低推理成本。
