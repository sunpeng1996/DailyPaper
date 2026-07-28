---
title: 'FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models'
title_zh: FlowCTS：面向流模型的在策略连续轨迹监督方法
authors:
- Kaiyang Ye
- Yuan Ge
- Junxiang Zhang
- Bei Li
- Ziming Zhu
- Haishu Zhao
- Xiaoqian Liu
- Chenglong Wang
- Jingbo Zhu
- Zhengtao Yu
affiliations:
- Northeastern University
- NiuTrans Research
- Kunming University of Science and Technology
arxiv_id: '2607.24522'
url: https://arxiv.org/abs/2607.24522
pdf_url: https://arxiv.org/pdf/2607.24522
published: '2026-07-27'
collected: '2026-07-28'
category: Training
direction: 生成模型训练 · 流模型在策略蒸馏
tags:
- Flow Model
- On-policy Distillation
- Trajectory Matching
- Training Objective
- Generative Model
one_liner: 提出基于连续轨迹匹配的流模型在策略蒸馏目标，解决KL类方法时序监督错配问题，性能和收敛速度均优于基线
practical_value: '- 做生成式推荐/广告多专家模型能力蒸馏时，可直接用FlowCTS的轨迹匹配目标替换传统KL-based OPD，相同训练成本下可获得3%左右的生成质量提升，且收敛速度更快

  - 时序权重分配思路可迁移到所有序列/连续生成任务：优先给生成早期阶段分配更高监督权重，能有效提升全局结构、语义一致性，更符合电商商品图/营销文案的生成准确性需求

  - 多步监督的步长K无需盲目增大，建议优先试K=2，平衡轨迹信息增益和优化难度，避免不必要的训练成本上升

  - 做生成式内容（电商主图、商品文案）的模型后对齐时，该方法效果优于混合奖励RL基线，且无需额外偏好标注，降低对齐成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有On-policy Distillation（OPD）在大语言模型后训练中有效解决了稀疏奖励、暴露偏差问题，但流模型（如扩散、整流流）缺乏自然的下一步条件分布，传统KL-based OPD直接迁移存在严重时序监督错配：监督信号集中在生成后期，而学生与专家模型的实际差异最大的阶段是早期去噪阶段，导致效果差、收敛慢。

### 方法关键点
- 提出连续轨迹监督（CTS）范式，从同一学生访问的状态出发，匹配学生和专家的后续连续轨迹差异，替代原有单步KL匹配
- 基于轨迹和速度场的积分关系，推导带时序权重的速度匹配上界，权重随离起始状态的距离增大自动升高，符合误差累积规律
- 离散化得到可训练目标，由监督步长K参数化，K=1为单状态速度匹配，K>1为多步轨迹监督，同时支持在策略蒸馏（OPD）和离线SFT两种场景

### 关键实验
基于SD3.5-Medium开展实验，对比基线包括预训练模型、混合奖励Flow-GRPO、传统KL-based OPD：
- 单步FlowCTS-OPD（K=1）较Vanilla OPD，GenEval从0.90提升至0.93，OCR从0.90提升至0.92，PickScore从22.75提升至23.06，所有指标优于混合奖励RL基线
- 离线SFT场景下，FlowCTS-SFT（K=3）较Vanilla SFT，OCR从0.70提升至0.75，整体得分提升2.1%
- 时序分析验证传统KL-based OPD的监督信号80%集中在生成最后20%阶段，和实际差异分布完全错配，是其效果差的核心原因

### 最值得记住的结论
流模型在策略蒸馏的监督信号权重分配应匹配学生-专家的实际差异分布，优先强化早期生成阶段的监督，而非盲目依赖KL推导的固有权重。
