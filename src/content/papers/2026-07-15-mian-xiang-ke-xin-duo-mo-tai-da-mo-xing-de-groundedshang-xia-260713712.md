---
title: 'Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal
  LLMs'
title_zh: 面向可信多模态大模型的Grounded上下文偏好优化方法Groc-PO
authors:
- Zhixiao Zheng
- Zheren Fu
- Zhiyuan Yao
- Chunxiao Liu
- Dongming Zhang
- Zhendong Mao
affiliations:
- University of Science and Technology of China
- Xiaomi Corporation
- State Key Laboratory of Communication Content Cognition, People's Daily Online
arxiv_id: '2607.13712'
url: https://arxiv.org/abs/2607.13712
pdf_url: https://arxiv.org/pdf/2607.13712
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 多模态大模型 · 偏好优化对齐训练
tags:
- Multimodal-LLM
- DPO
- Preference-Optimization
- Hallucination-Mitigation
- Faithful-Reasoning
one_liner: 通过多阶段grounded上下文偏好监督，降低多模态大模型幻觉并提升复杂推理能力
practical_value: '- 电商多模态商品理解/审核场景，可复用「实体识别→属性关联→推理判断」分层偏好优化思路，降低多模态LLM的商品属性幻觉、推理错误

  - 偏好优化训练可复用model-centric采样策略：负样本用待优化模型自身生成的错误case，相比通用负样本对齐效率提升更显著

  - 可复用Groc-PO的双权重自适应损失：阶段权重随任务复杂度递增，难样本加权，在不显著增加训练overhead的前提下提升对齐效果

  - 多轮对话式推荐Agent的对齐，可复用渐进式上下文监督方案，提升多轮交互下的上下文一致性和推理准确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）广泛存在视觉幻觉、内容捏造、推理不忠实问题，严重限制落地价值。标准Direct Preference Optimization（DPO）仅在最终答案层施加偏好监督，无法解决早期grounding阶段的错误沿推理链路传播的核心痛点，间接的监督信号难以抑制grounding漂移和上下文不一致导致的错误累积。
### 方法关键点
- 构建3阶段Grounded Context Preference Dataset（GCPD）：按「物体grounding→上下文grounding→ grounded推理」的人类认知路径组织偏好对，每阶段prompt强制包含前序所有正确上下文，保障信息传递连续性
- 采用model-centric负采样策略：负样本优先使用待优化模型自身生成的错误结果，相比通用外部负样本，大幅缩小训练数据与模型原生错误分布的gap，提升对齐效率
- 设计自适应Groc-PO损失：融合阶段感知权重（越靠后的复杂推理任务权重越高）和难度感知权重（模型难区分的样本权重越高），动态分配训练优先级
### 关键结果
在LLaVA-v1.5 7B/13B、Qwen2.5-VL 7B上验证，对比标准DPO、RLHF-V等基线：MM-Hal幻觉率相对降低19%-23%，复杂推理任务准确率相对提升最高45%，训练开销仅比DPO增加3%的单样本处理时间、0.03%的峰值显存。
### 核心结论
多模态模型对齐不能只关注最终输出，对早期grounding等中间阶段的显式分层监督，能以极低overhead大幅降低幻觉并提升复杂推理能力。
