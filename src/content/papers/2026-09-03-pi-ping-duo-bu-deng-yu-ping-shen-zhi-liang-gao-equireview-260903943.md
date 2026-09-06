---
title: 'More Criticism Does Not Make a Better Review: EquiReview-R'
title_zh: 批评多不等于评审质量高：EquiReview-R智能评审优化框架
authors:
- Zexing Zhang
- Jichao Li
- Tianyang Lei
- Yude Fu
- Yang Kewei
affiliations:
- National University of Defense Technology
arxiv_id: '2609.03943'
url: https://arxiv.org/abs/2609.03943
pdf_url: https://arxiv.org/pdf/2609.03943
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: LLM辅助决策 · 双风险管控与证据对齐
tags:
- LLM-assisted decision making
- risk control
- evidence alignment
- review optimization
- corpus release
one_liner: 提出证据引导的AI评审框架EquiReview-R，双控漏判与过度批评风险，提升评审效率与准确性
practical_value: '- 做Agent决策/内容审核时，可复用「先校验存量结论证据对齐、再做新增召回」的流程，避免无效召回带来的误判，可落地于广告素材合规审核、评论负向标签校验场景

  - 双风险独立管控的思路可迁移到推荐系统bad case治理：分别对齐漏召回、误召回的优化目标，避免单一指标（如召回率）提升带来的负向体验，可落地于电商低俗内容拦截、虚假评价识别场景

  - 可复用「stop/continue/defer三级输出」逻辑做LLM推理的算力动态调度，对高置信度结果提前终止推理，降低大模型调用成本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI评审系统盲目追求批评数量，混淆「遗漏重要缺陷（漏判）」「无证据指控（过度批评）」两类方向完全相反的错误，单一聚合评估指标无法区分两类问题，导致评审有效性不足。
### 方法关键点
将AI辅助评审重构为证据引导的结构化关注点集合优化任务，对漏判、过度批评两类风险独立管控；提出EquiReview-R框架，先基于局部证据校验已有批评的合理性，再从独立、评审条件依赖双视角搜索遗漏问题，最终输出停止/继续/延迟三类决策；构建证据关联的评审轨迹语料ReviewTrace开源。
### 关键结果
在未见过的论文测试集上，满足重大漏判非劣效标准，重大过度批评率从15.5%降至8.1%，漏判单侧上限为9.9%，可对52.4%的论文直接终止评审；消融实验证明增益来自证据校验环节，而非额外推理或短输出。
