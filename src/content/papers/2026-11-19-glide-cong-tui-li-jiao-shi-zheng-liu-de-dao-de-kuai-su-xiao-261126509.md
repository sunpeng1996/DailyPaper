---
title: 'GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers'
title_zh: GLiDE：从推理教师蒸馏得到的快速校准决策模型
authors:
- Sahibzada Allahyar
- Julia White
- Dhruv Atreja
- George Hurn-Maloney
- Urchade Zaratiana
affiliations:
- Fastino Labs
arxiv_id: '2611.26509'
url: https://arxiv.org/abs/2611.26509
pdf_url: https://arxiv.org/pdf/2611.26509
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent决策 · 推理能力蒸馏优化
tags:
- Knowledge Distillation
- Decision Model
- Low Latency
- Calibration
- Reasoning
- LLM
one_liner: 基于Qwen混合架构蒸馏推理能力，实现单前向传播的高性能低延迟决策模型
practical_value: '- 电商智能客服、Agent工具调用/意图分类场景可直接复用蒸馏范式：用带CoT推理的大模型作为教师，将推理后软目标蒸馏到单前向传播的小模型，在线推断无需生成推理过程即可获得推理级精度，同时满足<100ms的低延迟要求

  - 推荐/广告系统的候选粗排、多目标分类场景可借鉴混合注意力改造方案：保留低复杂度因果层处理长序列用户行为上下文，去掉全注意力层的因果掩码，让query、候选item、上下文双向交互，提升匹配精度的同时控制计算量

  - 高风险业务场景（售后退款决策、广告合规审核）可复用校准训练trick：采用黄金标签+多教师软目标加权的损失函数训练，无需后处理温度缩放即可得到ECE<2%的高可靠置信度，方便基于置信度阈值做人工拦截路由'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
决策模型仅需单前向传播即可输出候选得分，延迟远低于生成式推理，但推理能力缺失导致精度瓶颈；带CoT的大模型虽然决策精度更高，但逐token生成推理过程的延迟无法满足电商、推荐、Agent等在线业务的低延迟要求，如何在保留单步推断效率的同时获得推理级精度是核心痛点。

### 方法关键点
- 架构改造：基于Qwen3.8混合大模型优化，去掉16层全注意力层的因果掩码，实现上下文、query、候选答案的双向交互；保留48层Gated DeltaNet的因果结构，控制长序列计算复杂度；新增255路专用读出层，输出归一化的候选概率
- 蒸馏训练：分四阶段渐进训练，先微调得到带CoT推理能力的教师模型，再按教师直接预测置信度加权混合推理后软目标与直接预测软目标作为监督信号，结合多教师任务特定加权、递归checkpoint平均提升泛化性与校准度
- 推理优化：支持无参数循环深度，推理时重复调用中间层，无需新增参数量即可进一步提升效果

### 关键实验
在Hugging Face Decision Index v0.4.1的225个参评模型中，GLiDE V1.2（27B）以71.52分位列第一，超第二名1.77分，预期校准误差（ECE）仅2.0%，单RTX PRO 6000 GPU上延迟仅92.9ms；加入权重平均与无参数循环深度后，GLiDE 27B得分提升至73.37，ECE仍保持2.1%，延迟122ms；0.4B-27B全尺寸模型均处于性能-参数量帕累托前沿，同尺寸下领先其他参评模型3.2-10.9分。

### 核心结论
推理的计算成本可在训练阶段一次性支付，通过蒸馏将推理能力内化到单前向传播的模型中，在线推断无需生成CoT即可同时获得推理级精度、高校准置信度与低延迟。
