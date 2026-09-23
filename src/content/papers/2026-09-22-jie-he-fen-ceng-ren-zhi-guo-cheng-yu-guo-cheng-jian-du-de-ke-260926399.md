---
title: Combining Hierarchical Cognitive Process with Process Supervision for Interpretable
  Scene Safety Understanding
title_zh: 结合分层认知过程与过程监督的可解释场景安全理解
authors:
- Zhiyun Jiang
- Hanyong Wang
- Binbin Liang
- Yu Xie
- Zhengjie Wang
- Menglong Yang
- Wei Li
arxiv_id: '2609.26399'
url: https://arxiv.org/abs/2609.26399
pdf_url: https://arxiv.org/pdf/2609.26399
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: 大语言模型 · 过程监督推理优化
tags:
- LLM
- Process Supervision
- LoRA
- MoE
- Hierarchical Cognition
- Interpretability
one_liner: 构建带过程标签的分层认知安全数据集，提出融合LoRA与MoE的LLM过程监督框架提升场景理解性能与可解释性
practical_value: '- 多步推理类业务（如Agent决策、内容合规审核）可复用分层认知+过程监督范式，给中间推理步骤打标签做监督，同时提升效果与可解释性

  - LLM微调时可借鉴LoRA+MoE的模块化设计，针对推理链不同子任务训练专属专家模块，在降低微调成本的同时实现能力 specialization

  - 高风险业务场景（如电商广告审核、平台内容安全管控）可复用中间推理步骤的信息流+显著性分析方法，快速定位bad case根因'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统场景安全理解方法直接学习场景到安全等级的映射关系，可解释性极差，无法满足高风险关键场景的可靠性要求，需要对齐人类认知过程优化推理链路的可解释性。
### 方法关键点
1. 构建分层认知安全结构，基于多步推理链路标注过程标签，生成高质量场景安全理解数据集，支持中间推理步骤的细粒度分析；
2. 提出模块化过程监督框架，以LLM为核心底座，融合LoRA与MoE策略，每个专家模块独立负责推理链的特定子过程，完全对齐人类分层认知逻辑。
### 关键结果
实验验证相较于传统端到端方法，该框架在场景安全理解任务上的可解释性与综合性能均实现显著提升。
