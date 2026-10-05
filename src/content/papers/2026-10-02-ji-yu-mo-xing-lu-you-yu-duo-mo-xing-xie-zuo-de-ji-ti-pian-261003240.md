---
title: Collective Bias Mitigation via Model Routing and Collaboration
title_zh: 基于模型路由与多模型协作的集体偏见消解框架
authors:
- Mingzhe Du
- Luu Anh Tuan
- Xiaobao Wu
- Yichong Huang
- Yue Liu
- Dong Huang
- Huijun Liu
- Bin Ji
- Jie M. Zhang
- See-Kiong Ng
affiliations:
- Nanyang Technological University
- National University of Singapore
- Harbin Institute of Technology
- King's College London
arxiv_id: '2610.03240'
url: https://arxiv.org/abs/2610.03240
pdf_url: https://arxiv.org/pdf/2610.03240
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM公平性 · 多模型协作去偏
tags:
- LLM Debiasing
- Model Routing
- Multi-LLM Collaboration
- Fairness
- Ensemble Learning
one_liner: 通过模型路由选择适配LLM搭配协作拓扑，实现更优偏见消解并兼顾推理成本
practical_value: '- 电商/广告推荐场景可复用CBM思路：无需微调单模型，通过路由选择多台不同偏好的小模型，搭配Voting/Committee拓扑生成更公平的推荐结果，避免单模型刻板印象偏见放大，降低合规风险

  - 模型路由设计可直接迁移：训练时用匿名ID替代模型名避免过拟合，路由拆分为风险类型检测+适配资源选择两步，可用于推荐场景query风险识别、召回源动态选择等任务

  - 多模型拓扑可按业务要求选型：在线低延迟场景选Voting拓扑，效果稳定成本低；离线高要求场景（如内容审核、营销文案生成）选Committee拓扑，比Debating节省30%左右算力

  - 多模型推理优化方法可复用：采用并行推理+批量推理策略，可将多模型调用延迟降至接近单模型水平，满足在线业务的性能要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有单模型自去偏方案依赖模型固有知识，难以消解训练数据中根深蒂固的刻板印象偏见；而LLM在电商、金融、公共服务等落地场景对公平性要求极高，偏见输出会导致对特定群体的歧视，影响业务合规与用户体验，亟需更有效的去偏方案。
### 方法关键点
- 构建CrowdEval数据集：覆盖年龄、性别、种族、社会经济地位等8个社会维度的偏见诱导问题，收集50+开源LLM的响应，标注每个模型的细粒度偏见行为，支撑模型路由训练
- 设计LLM-based模型路由器：训练时用匿名ID替代模型名避免过拟合，同时完成两个核心任务：识别输入的偏见类型，为当前query选择偏见最低的Top-K适配模型
- 提出5种多模型协作拓扑：Single（单模型基线）、Sequential（串行传递响应）、Voting（并行输出多数表决）、Debating（多轮辩论达成共识）、Committee（指定协调员汇总意见表决），适配不同效果与成本要求
### 关键实验
基于BBQ偏见基准数据集评测，对比单模型自去偏基线：Top-7配置下Committee拓扑将年龄偏见得分从0.25降至0.10；Debating拓扑偏见得分最低，但推理成本是单模型的27倍，Committee拓扑成本仅为Debating的70%；32B参数的模型路由器偏见类型检测准确率达0.851，模型选择精度达0.941。
### 核心结论
多模型协作去偏的效果显著优于单模型自去偏，合理选择路由策略与协作拓扑可以在效果、成本之间找到适合业务的平衡点。
