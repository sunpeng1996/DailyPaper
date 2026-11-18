---
title: 'OAK-Mind: Zero-Training Mental Health Change Inference from Passive Sensing
  via Knowledge-Grounded Multi-Agent LLMs'
title_zh: OAK-Mind：基于知识增强多智能体LLM的零训练被动感知心理健康推断
authors:
- Yishu Ji
- Zhihan Jiang
- Will Ke Wang
- Yuang Fan
- Anind K. Dey
- Xuhai "Orson" Xu
affiliations:
- University of Washington
- Columbia University
arxiv_id: '2611.22248'
url: https://arxiv.org/abs/2611.22248
pdf_url: https://arxiv.org/pdf/2611.22248
published: '2026-11-17'
collected: '2026-11-18'
category: MultiAgent
direction: 多智能体LLM · 零训练知识推理
tags:
- Multi-Agent
- Knowledge Grounding
- Zero-Training
- LLM
- Inference Pipeline
one_liner: 提出零训练知识增强多智能体框架OAK-Mind，无需标注即可从感知数据推断心理健康变化
practical_value: '- 跨领域零训练任务可借鉴「按维度拆分+领域专属Agent分工+知识对齐+结果融合」的通用多Agent架构，降低标注依赖

  - 结构化非文本数据（如用户行为埋点、设备传感数据）可先映射到语义维度，再输入LLM/Agent体系推理，大幅提升效果

  - 可解释推理任务可引入标准化量表/规则作为最终判定锚点，同步输出符合人类认知的归因依据'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统被动感知心理健康推断依赖有监督模型，需大量标注数据且可解释性差；现有LLM类方案仍需任务微调或传感器专属预训练，落地门槛高。
### 方法关键点
1. 零训练多Agent架构OAK-Mind，先将传感数据归类为睡眠、运动、出行、手机使用4个行为维度；
2. 每个维度配置基于心理健康文献对齐的专属Agent，解读纵向行为变化；
3. 融合多Agent结论后，基于标准化问卷症状评分规则，相对用户基线推断健康变化，同步输出可解释依据。
### 关键结果
无任务训练前提下，性能比肩甚至优于使用额外标注训练的最优有监督基线；在4种LLM backbone上，效果均显著优于直接prompt。
