---
title: 'ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition
  Gaps'
title_zh: ActiveEvidence：具备可验证获取缺口的决策导向证据图框架
authors:
- Miaobo Hu
- Shuhao Hu
- Xiaobo Guo
- Xin Wang
- Bokun Wang
- Peng Zhang
- Daren Zha
- Jun Xiao
affiliations:
- University of Chinese Academy of Sciences
- Institute of Information Engineering, CAS
arxiv_id: '2610.20532'
url: https://arxiv.org/abs/2610.20532
pdf_url: https://arxiv.org/pdf/2610.20532
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: 多模态Agent · 资源受限证据采集
tags:
- Multimodal Agent
- Evidence Retrieval
- Decision Certification
- Resource Bounded Reasoning
- Active Learning
one_liner: 提出反事实证据交互图框架，实现资源约束下可验证的多模态证据主动采集
practical_value: '- 多模态商品检索/审核场景可复用CEIG的二阶证据交互建模，避免重复调用视觉模型，降低推理成本，比如相似商品图、重复资质图的联合收益建模，减少冗余调用

  - 决策导向的间隙引导精炼策略可迁移到LLM工具调用路由场景，仅评估可能改变当前最优决策的交互项，将平均交互评估量从191.4降至19.6，大幅降低推理延迟

  - 可复用epsilon决策证书机制对高风险Agent决策（比如电商品控、广告合规审核）做一致性校验，保证决策可追溯、可复现，符合监管要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多模态Agent执行任务时需要按需获取视觉证据，但现有自适应采集方案要么全量调用视觉服务浪费资源，要么无法保证未评估的证据不会改变决策，缺乏可验证的决策边界，且无法严格区分免费元数据与付费观测的信息边界，难以落地到资源受限、合规要求高的生产场景。

### 方法关键点
- 反事实证据交互图（CEIG）：对证据的一元价值、二阶符号交互、定向条件损害分别建模，同时为未解析的交互项保留显式的分数上下界
- 决策加权边界优化：对可能改变决策的边缘收紧界的范围，大幅降低不必要的计算开销
- 间隙引导精炼策略：仅评估可能替换当前最优决策的交互项，当未解析项的最大上界与当前最优分数差小于𝜖时停止计算，输出可验证的决策证书，保证未评估项不会改变决策
- 独立轨迹认证机制：严格执行决策前元数据免费、决策后标签冻结的信息边界，保证决策可追溯、可审计

### 关键实验
在640个多模态任务案例（384训练/128验证/128测试）上，对比VisionThink、AdaptVision等18个基线，ActiveEvidence达到任务得分0.842、grounding F1 0.816、证据召回0.873，平均仅调用1.74次视觉服务，消耗286.5K视觉token，p95延迟742ms，对比最优基线任务得分提升1.4%，视觉token消耗减少4.3%，仅需要评估19.6个交互项（对比全量评估的191.4个），决策证书与全量计算的一致性达0.992。

### 核心结论
资源受限的多模态Agent决策优化的核心不是追求全局最优的证据组合，而是在可验证的决策边界下，用最小的计算成本保证决策不会因未评估的证据发生改变。
