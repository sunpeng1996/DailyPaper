---
title: Toward Recursive Self-Improvement in Physical AI
title_zh: 面向实体AI的递归自我改进（RSI）研究综述与框架梳理
authors:
- Meng Luo
- Zechen Bai
- Shanqing Xu
- Yanlin Li
- Kaixin Li
- Mengchen Qian
- Weifeng Lu
- Ran Zhang
- Yingtian Zou
- Ziyang Luo
affiliations:
- National University of Singapore
- Huazhong University of Science and Technology
- Shanghai Jiao Tong University
- Nanyang Technological University
- Hong Kong Baptist University
arxiv_id: '2610.29677'
url: https://arxiv.org/abs/2610.29677
pdf_url: https://arxiv.org/pdf/2610.29677
published: '2026-10-20'
collected: '2026-10-25'
category: Agent
direction: 实体AI Agent 递归自我改进研究
tags:
- RSI
- Agent Self-Improvement
- Robot Learning
- Physical AI
- Evaluation Framework
one_liner: 梳理实体AI递归自我改进的路径、约束条件，给出评估原则与未来研究方向
practical_value: '- RSI增益可延续判断逻辑可迁移到推荐系统自迭代模块：仅保留适配业务目标、可被下游组件复用、跨场景有效的迭代结果，大幅降低无效迭代开销。

  - RSI安全可控评估原则可复用到广告/推荐自优化链路：上线前校验迭代收益的普适性、不可逆风险，避免业务故障。

  - 分层迭代架构可套用到电商Agent自主优化设计：按执行策略/用户画像知识/学习流程分层管控迭代粒度，降低全链路变更风险。'
score: 4
source: huggingface-daily
depth: abstract
---

**动机**：现有数字Agent的递归自我改进（RSI）依赖代码可修改、测试可并行、变更可逆的前提，无法适配高试错成本、部分可观测、存在不可逆风险的实体AI场景，缺乏系统性落地框架。
**方法关键点**：1 定义实体AI RSI的四层迭代落点：执行策略、世界模型、外部知识、学习流程；2 明确RSI增益可延续的4个必要条件：反馈匹配待解决的学习需求、变更可被下游组件消费、收益跨任务/硬件可迁移、迭代过程安全且成本可控；3 系统综述机器人操控领域的相关研究。
**关键结果**：现有实体AI研究仅验证了行为优化、后续学习效率提升、流程优化的可行性，尚未分离出递归迭代带来的独有增益，最终输出实体RSI的评估原则与核心研究方向。
