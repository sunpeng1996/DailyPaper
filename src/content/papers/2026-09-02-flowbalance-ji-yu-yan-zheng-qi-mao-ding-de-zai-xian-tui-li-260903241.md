---
title: 'FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience'
title_zh: FlowBalance：基于验证器锚定的在线推理经验自优化方法
authors:
- Zixun Huang
- Kishan Panaganti
- Haitao Mi
- Leowei Liang
affiliations:
- Tencent HY LLM Frontier
- University of Pennsylvania
arxiv_id: '2609.03241'
url: https://arxiv.org/abs/2609.03241
pdf_url: https://arxiv.org/pdf/2609.03241
published: '2026-09-02'
collected: '2026-09-08'
category: Training
direction: LLM自训练 · 分布对齐与校准
tags:
- Self-Improvement
- Trajectory Balance
- RLVR
- Distribution Matching
- Privileged Guidance
one_liner: 结合稀疏验证器反馈与稠密自指导信号，通过轨迹平衡实现分布对齐的LLM自提升训练方法
practical_value: '- 电商/广告RAG Agent推理链优化可复用校准逻辑：用业务效果验证器（转化率、下单率）门控LLM内部自指导信号，避免模型过度拟合局部虚假偏好

  - 多候选召回/生成式推荐的多样性优化可借鉴分布对齐思路：不单独优化token级损失，通过轨迹平衡拟合包含多个高价值候选的归一化分布，兼顾效果与策略多样性

  - 推荐系统在线自迭代模块可参考符号门控设计：对负向反馈轨迹直接反转自指导信号权重，避免错误经验强化，提升训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM通过自生成在线经验迭代时存在两类核心痛点：一是验证器的终端反馈稀疏，无法覆盖长推理路径的细粒度信号；二是模型自身的稠密自指导信号不可靠，容易强化错误置信度、收敛到狭窄解空间，现有方法无法兼顾反馈的可靠性和信号密度。

### 方法关键点
- 对每条在线生成的推理轨迹，用冻结的同策略模型的特权后见视角（可访问训练侧参考答案等上下文）计算token级对数概率增益，聚合为轨迹级自指导得分
- 用验证器的组相对优势校准自指导得分：正向优势轨迹保留自指导权重，负向优势反转权重，无偏好时禁用自指导分支，避免错误自我确认
- 构造结合验证器优势与校准后自指导得分的轨迹能量，通过profiled轨迹平衡拟合归一化的目标响应分布，无单独的token级模仿损失

### 关键实验
在数学推理任务上测试Qwen3-4B、Qwen3-8B两个底座，对比GRPO、OPSD、RLSD、FlowRL基线：8B底座5项基准平均67.61，比GRPO高2.12点，比FlowRL高1.76点；达到AIME24 0.5验证准确率仅需100步，比GRPO快43%，400步训练无性能衰减，避免OPSD的响应长度坍缩问题；正确解的Simpson策略多样性达0.2194，是GRPO的2.16倍，保留更多异构正确路径。

**最值得记住的一句话**：自提升的核心不是最大化单步reward，而是学习一个锚定验证信号、兼顾效果与多样性的归一化轨迹分布。
