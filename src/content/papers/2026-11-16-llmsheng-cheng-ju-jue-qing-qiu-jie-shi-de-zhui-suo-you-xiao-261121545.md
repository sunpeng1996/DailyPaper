---
title: 'Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied
  Requests'
title_zh: LLM生成拒绝请求解释的追索有效性评估
authors:
- Arunkumar V
affiliations:
- University College of Engineering, BIT Campus, Anna University
arxiv_id: '2611.21545'
url: https://arxiv.org/abs/2611.21545
pdf_url: https://arxiv.org/pdf/2611.21545
published: '2026-11-16'
collected: '2026-11-17'
category: Eval
direction: LLM解释生成质量评估与优化
tags:
- LLM
- Explanation Evaluation
- Recourse Validity
- Rule-based System
- LLM-as-Judge
one_liner: 提出追索有效性评估指标，揭示多规则拒绝场景下LLM解释的普遍失效问题及优化路径
practical_value: '- 电商/广告场景的拒绝类解释（如优惠券申领失败、活动报名驳回）生成，需增加追索有效性校验：仅给出单条正确拒绝理由会导致用户修改后仍被驳回，大幅降低体验

  - LLM自动解释类任务的评估，不能仅校验理由事实正确性，需新增「按解释修改后是否能改变决策」的判断逻辑，可复用本文hitting-set方法快速识别无效解释

  - 多规则校验场景的LLM解释生成，可强制要求输出全部触发的拒绝规则，能显著提升开源模型生成解释的可用性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM广泛用于生成规则系统（如福利申领、权限校验）的拒绝请求解释，但仅校验理由事实正确性的传统评估无法保障用户修改后可通过申请，用户体验极差。
### 方法关键点
1. 定义**recourse validity（追索有效性）**核心指标：仅修改解释提及的问题、不调整原始诉求即可反转决策的属性
2. 基于hitting-set理论可仅通过规则策略直接预判正确理由失效的场景
3. 对比20款LLM的解释生成质量，测试两种评估方案的有效性
### 关键结果
7个真实规则系统中6个在多规则同时触发拒绝时，单条正确理由几乎无追索有效性；仅校验理由正确性的评估（含LLM judge）识别失效解释的准确率接近随机；强制输出所有触发的拒绝规则可提升所有开源模型的解释可用性，强推理模型表现更优但在≥4条独立拒绝规则场景仍有大量失效。
