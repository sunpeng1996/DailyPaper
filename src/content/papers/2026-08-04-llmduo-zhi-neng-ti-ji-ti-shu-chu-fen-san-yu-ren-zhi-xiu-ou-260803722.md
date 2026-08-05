---
title: When Outputs Disperse, Does Epistemic Revision Follow? A Black-Box Coupling
  Diagnostic for Machine Collectives
title_zh: LLM多智能体集体输出分散与认知修正耦合性的黑盒诊断
authors:
- Molood Arman
affiliations:
- Independent Researcher, Lyon, France
arxiv_id: '2608.03722'
url: https://arxiv.org/abs/2608.03722
pdf_url: https://arxiv.org/pdf/2608.03722
published: '2026-08-04'
collected: '2026-08-05'
category: MultiAgent
direction: 多智能体协作 · 认知修正评估
tags:
- Multi-Agent
- Collective Intelligence
- Black-box Evaluation
- Epistemic Revision
- LLM Evaluation
one_liner: 提出黑盒双维度诊断框架，验证LLM多智能体输出多样性不必然等价于认知可修正性
practical_value: '- 搭建多Agent导购/商品信息审核/舆情分析系统时，不能仅用输出多样性作为系统纠错能力的评估指标，需额外增加核心观点/事实立场的校验维度，避免表面多样但所有Agent都固守错误结论的无效优化

  - 可复用文中Coherence Index（CI）计算方法，快速监测多Agent对话的输出收敛程度，当输出过度收敛时触发差异化思考指令，可提升gpt-4o-mini等强耦合模型的错误修正率17个百分点以上

  - 针对不同LLM底座的多Agent系统，上线前必须先做耦合性校验：对gemini-2.5-flash这类弱耦合模型，仅靠要求输出差异化的干预无效，需直接引入外部事实校验模块而非单纯要求Agent提出不同观点

  - 多Agent系统评估可直接复用文中的两个统计指标：单干预立场偏移量Δs、前提保留率，替代单一的准确率/多样性指标，更全面衡量系统的纠错能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统集体智能研究默认输出多样性等同于认知多样性，可支撑后续立场修正，但这一假设在LLM多智能体系统中完全不成立——不同Agent可能输出表述完全不同的内容，但核心结论高度一致，表面多样性无法起到预期的纠错作用，此前缺乏可落地的黑盒方法诊断两者的关联程度。

### 方法关键点
- 「分散-修正耦合」双维度诊断框架完全黑盒无需访问模型内部权重：输出通道用固定外部编码器（text-embedding-3-small）计算Coherence Index（CI）衡量输出嵌入的聚类紧密度，CI越低输出越分散；认知通道用逐轮立场标注（-3到+3分）衡量集体是否真正修正错误前提
- Meta-Predictive Clarity System（MPCS）状态监测器可追踪输出收敛程度，当CI过高时触发Re-Differentiation Protocol（RDP），强制每个Agent提出1个独特的共识缺陷，作为可验证输出效果的干预探针
- 实验采用错误前提注入范式：5个Agent先围绕错误前提讨论4轮，再注入权威修正信息，衡量后续是否能拒绝错误前提

### 关键结果
- 在gpt-4o-mini多智能体系统中，基于CI触发的条件性异议相比无干预基线提升错误前提恢复率+17.7个百分点（p<1e-6），而固定persona的持续多样性反而降低恢复率-8.1个百分点（p=0.007）
- 在gemini-2.5-flash多智能体系统中，完全相同的RDP干预虽然验证到输出分散度显著提升，但错误前提恢复率无任何提升（26.1% vs 27.1%，p=0.84），94%的RDP后响应只是用不同机制重述错误前提，仅2%真正承认前提错误

最值得记住的一句话：多智能体系统的输出多样性不具备天然的纠错价值，只有当输出分散与认知修正强耦合时，多样性才能真正提升集体智能的事实准确性
