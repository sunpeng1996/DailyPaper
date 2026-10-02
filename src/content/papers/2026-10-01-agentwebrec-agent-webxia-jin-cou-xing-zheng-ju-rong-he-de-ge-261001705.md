---
title: 'AgentWebRec: Compact Evidence Fusion over the Agent Web for Personalized Recommendation'
title_zh: AgentWebRec：Agent Web下紧凑型证据融合的个性化推荐框架
authors:
- Haoran Qiang
- Guannan Liu
- Liang Zhang
- Junjie Wu
affiliations:
- Beihang University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.01705'
url: https://arxiv.org/abs/2610.01705
pdf_url: https://arxiv.org/pdf/2610.01705
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent 跨源协作个性化推荐
tags:
- LLM Agent
- Agent Web
- Personalized Recommendation
- Evidence Fusion
- Multi-Agent Collaboration
one_liner: 面向用户Agent组成的Agent Web新范式，提出渐进式跨源证据融合的个性化推荐框架
practical_value: '- 用户侧私域Agent偏好建模可复用「语义+时序加权的TopK记忆检索」方案，避免长历史噪声，比全量记忆输入推理成本低、效果更稳定

  - 冷启动/低置信度推荐场景可借鉴「置信度门控的邻域Agent协作」逻辑，基于用户行为共现/画像相似度选协作对象，补充本地偏好不足的问题，无需中心化聚合用户数据，符合隐私合规要求

  - 电商Item侧语义增强可复用「候选Item + TopK语义邻居的抽象增强」方法，控制语义邻居数量在3-7个区间（参数实验最优区间），避免语义漂移

  - 跨Agent信息交互无需传递原始行为数据，仅返回任务相关的紧凑型模式摘要，降低通信成本同时保护用户隐私'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM个人Agent成为用户语义的持久载体，传统用户-平台的推荐范式演进为「用户-Agent Web-平台」的新路径，分布式用户侧信息可补充平台侧信息，但现有推荐方法无法适配该范式下的三个核心挑战：证据分散在互不可见的Agent中仅能通过有限查询获取、绝大多数证据与当前任务无关、不同Agent返回的内容语义异构无法直接拼接使用。

### 方法关键点
- 将Agent Web下的推荐定义为有限预算下的任务时证据获取融合问题，所有Agent记忆保留本地，无需中心化聚合训练
- 三层渐进式证据获取融合：1）先向平台Agent查询候选Item的增强语义（候选+TopK语义邻居抽象生成）作为任务锚点；2）用增强语义作为Query，从目标用户Agent本地记忆中加权检索（语义相似度+时序衰减权重）TopK相关记录，投影为任务特定偏好状态，生成本地决策及置信度；3）置信度低于阈值时，向邻域用户Agent发送协作Query，各邻域Agent返回本地抽象的偏好模式，目标Agent融合后输出最终决策
- 邻域Agent基于Item共现关系构建，优先选择行为相似的用户Agent，降低协作噪声

### 关键实验结果
在4个InstructRec数据集（Books/Goodreads/MovieTV/Yelp）上对比SASRec、LightGCN、LLMRank、AgentCF、MemRec等基线，全指标领先：Books数据集H@1达0.525，比最优基线MemRec高74%；Goodreads数据集H@1达0.686，比最优基线AFL高137%。

### 核心结论
Agent Web下的推荐核心不是聚合更多全局数据，而是为当前决策精准获取并融合分布式的任务相关紧凑型证据，平衡个性化效果与数据隐私要求
