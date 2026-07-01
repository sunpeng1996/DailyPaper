---
title: Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations
title_zh: 面向可问责LLM判官评估的人在环核心信息标注方案
authors:
- Laura Dietz
affiliations:
- University of New Hampshire
arxiv_id: '2606.29033'
url: https://arxiv.org/abs/2606.29033
pdf_url: https://arxiv.org/pdf/2606.29033
published: '2026-06-27'
collected: '2026-06-30'
category: Eval
direction: LLM评估 · 人在环标注流程优化
tags:
- LLM-as-Judge
- Human-in-the-Loop
- Annotation
- RAG Evaluation
- Evaluation Pipeline
one_liner: 提出人标注核心信息点+LLM批量匹配的分工式标注方案，解决LLM判官评估的自循环与锚定偏差
practical_value: '- 搭建RAG/Agent生成内容的效果评估管线时，可复用「人独立标注核心校验点+LLM批量匹配」的分工逻辑，既降低人工标注成本，又彻底规避LLM自评估的循环偏差

  - 电商场景下生成式商品文案、智能客服回复的质量验收，可先由运营标注必达核心信息（如优惠规则、商品参数），再用LLM批量校验生成内容是否全部命中，大幅提升验收效率

  - 做LLM微调的效果对齐时，可基于该方法构建标准化nugget校验库，替代传统人工打分，避免标注者的锚定偏差，提升对齐训练的标注数据质量'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM-as-Judge评估存在三大核心缺陷：纯LLM自评估存在训练数据/偏见重叠的自循环问题，结果可信度低；人工先校验LLM判断的模式会触发锚定偏差，导致人工 rubber-stamping 失效；纯人工标注测试集成本极高、标注方差大，无法支撑业务高频迭代需求。
### 方法关键点
提出人-LLM分工的人在环标注原型工具，核心设计为：
1. 人工仅负责独立标注任务相关的核心信息点（nuggets），全程不预看待评估的LLM输出，彻底避免锚定偏差；
2. LLM承担高吞吐的匹配任务，批量校验待评估输出是否命中所有预设nuggets；
3. 导出的标准化nugget库可直接对接自动评估管线，实现可追溯、可问责的评估流程。
### 关键结果
目前已上线公开演示原型，相较于传统评估方案，在标注成本与评估可信度的平衡上有显著提升，同时完全消除LLM自评估的循环偏差与人工锚定误差。
