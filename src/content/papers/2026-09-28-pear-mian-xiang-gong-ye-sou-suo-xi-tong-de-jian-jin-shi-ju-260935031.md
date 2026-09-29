---
title: 'PEAR: Progressive Evidence-Based AutoResearch for Industrial Search Systems'
title_zh: PEAR：面向工业搜索系统的渐进式证据驱动自动研究框架
authors:
- Yifan Wang
- Shipeng Zhu
- Fei Xiong
- Yuqin Yang
- Yonghui Huang
- Kunyao Wu
- Yue Wang
- Weichao Meng
- Yu Gong
affiliations:
- Global E-Commerce Agentic Search Team
arxiv_id: '2609.35031'
url: https://arxiv.org/abs/2609.35031
pdf_url: https://arxiv.org/pdf/2609.35031
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent驱动搜索系统自动迭代优化
tags:
- AutoResearch
- LLM Agent
- Industrial Search
- A-B Testing
- Multi-fidelity Evaluation
one_liner: 提出证据驱动状态管理与四级置信度门控验证阶梯结合的工业搜索AutoResearch框架
practical_value: '- 可直接复用四级多保真评估链路：L1离线回放→L2影子流量→L3快速在线→L4决策级在线，搭配置信度门控晋升规则，大幅降低无效高成本在线实验的开销，适配电商搜索/推荐的策略迭代场景

  - 证据驱动的研究状态管理方法可迁移：每个策略任务独立维护假设、候选空间、上下文和历史证据，通过Plan-Execute-Evaluate-Update四步流转，解决非稳态流量下的
  transient 收益误判问题，避免迭代走偏

  - 统一置信度晋升规则可复用：基于95%置信区间的PROMOTE/RETAIN/STOP三分类规则，适配不同评估阶段的统计校验需求，不需要为每个阶段单独设计晋升逻辑

  - 附录提供的假设更新、跨轮记忆更新等prompt模板可直接用到业务的Agent化迭代工作流中，降低自定义Agent的prompt开发成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业搜索/推荐系统的策略迭代高度依赖人工设计实验、分析结果，现有AutoResearch方案存在两大核心痛点：一是非稳态流量下的 transient 收益容易被误判为长期增益，导致迭代方向走偏、知识积累不可靠；二是不同保真度的评估信号（离线/影子流量/在线）缺乏统一的晋升逻辑，要么离线优化效果无法转化为在线收益，要么全量在线实验成本过高、风险大，亟需适配工业生产环境的自动迭代框架。
### 方法关键点
- 证据驱动AutoResearch模块：每个策略任务独立维护研究状态（包含优化目标、干预范围、当前假设、候选空间、历史证据与上下文），通过Plan-Execute-Evaluate-Update四步流转，结合贝叶斯优化思想平衡已知有效区域的打磨和未知区域的探索，解决非稳态流量下的实验结果不可比问题。
- 置信度门控验证阶梯：将评估分为四级递增保真度的阶段：L1离线回放、L2影子流量评估、L3小流量快速在线评估、L4决策级全周期在线评估，所有阶段共用统一的置信度晋升规则：只有当指标提升的95%置信区间完全大于0时才晋升到下一阶段，否则保留重测或直接淘汰。
### 关键结果
在真实电商搜索系统落地测试，对比基线策略，两个优化后的策略在L4决策级A/B实验中分别将主订单/DAU提升2.7336%、3.2957%，同时ASN、SKU订单/DAU等辅助指标也均有统计显著提升；L2影子流量的订单proxy信号与最终在线效果方向一致性较高，相对误差仅-3.49%。
### 核心结论
工业级AutoResearch的核心不是快速找到局部最优解，而是通过多保真评估的置信度过滤和上下文关联的证据积累，在非稳态环境下稳定积累可复用的优化知识，大幅降低无效实验的成本与风险
