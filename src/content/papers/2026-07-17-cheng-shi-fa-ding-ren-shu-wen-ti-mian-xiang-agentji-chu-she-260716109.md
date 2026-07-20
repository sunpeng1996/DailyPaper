---
title: 'The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic
  Infrastructure'
title_zh: 诚实法定人数问题：面向Agent基础设施的认知拜占庭容错
authors:
- Jun He
- Deying Yu
affiliations:
- OpenKedge.io
arxiv_id: '2607.16109'
url: https://arxiv.org/abs/2607.16109
pdf_url: https://arxiv.org/pdf/2607.16109
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent基础设施容错机制设计
tags:
- Byzantine Fault Tolerance
- Agent Infrastructure
- Consensus
- Fault Tolerance
- Distributed System
one_liner: 针对Agent合规节点语义一致出错的故障场景，提出EBFT容错模型并推导多目标兼容的法定人数阈值条件
practical_value: '- 多Agent协同决策场景（如多LLM商品合规审核、广告素材准入）可复用EBFT双预算设计：不将语义出错的合规节点直接归为拜占庭节点，单独统计相干错误上限`eδ`和不可用支持上限`uϵ`计算投票阈值，比传统3f+1方案节省节点资源

  - Agent集群可靠性设计不要依赖名义多样性（不同模型/供应商/提示词），需实际校准语义错误的尾部分布：同基座微调的多模型即使来源不同，语义错误相关性高，堆节点无法降低common-mode故障的概率下限

  - 高风险Agent决策场景（如电商大促预算调整、广告投放策略自动变更）可直接复用EBFT阈值公式，在给定拜占庭节点上限、`eδ`、`uϵ`的前提下快速算出合法投票阈值区间，同时保证共识无冲突、错误决策不通过、合法决策不卡顿'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
经典Byzantine Fault Tolerance（BFT）共识假设非拜占庭节点一定能正确执行语义校验，但Agent作为校验节点时，即使完全遵守协议、不做恶、不宕机，也可能因为模型训练偏差、prompt共性、检索源重叠、工具链共享等原因，同时对同一个错误决策投赞成票，形成符合协议规则但语义错误的quorum，现有容错模型完全没有覆盖这类故障场景。
### 方法关键点
- 定义认知故障（epistemic fault）：合规节点的语义判断错误，分为相干故障（多节点同时支持同一错误决策，威胁语义安全）和分散故障（错误分散或节点弃权/超时，威胁系统活性）
- 提出双置信度预算指标：`eδ`为置信度1-δ下，合规节点对无效决策的最大相干赞成票上限；`uϵ`为置信度1-ϵ下，合规节点对有效决策的最大不可用支持（拒票、弃权、超时、语义分类分歧等）上限
- 推导三类阈值条件：语义安全要求`q > f + eδ`；共识一致性要求`q > (N + f)/2`；活性要求`q ≤ N - f - uϵ`，三者交集即为合法quorum阈值q的可行区间
- 给出集群可行性判定规则：集群规模N需同时满足`N > 2f + eδ + uϵ`和`N > 3f + 2uϵ`，才存在满足所有要求的q值
### 关键结果
本工作为理论性研究，无对比实验：当无认知故障时（`eδ=uϵ=0`），阈值条件退化为经典BFT的`N=3f+1`、`q=2f+1`，与现有结论完全兼容；保守降级方案可将eδ对应的相干错误节点直接计入拜占庭节点，沿用经典`3(f+eδ)+1`的集群规模要求，保证容错安全性。
### 核心结论
协议层的共识一致不等于语义层的决策正确，名义上的节点多样性不等于认知层面的故障独立性。
