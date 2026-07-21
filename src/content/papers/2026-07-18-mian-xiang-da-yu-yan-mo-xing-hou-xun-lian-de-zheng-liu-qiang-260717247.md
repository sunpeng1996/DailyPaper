---
title: Distilled Reinforcement Learning for LLM Post-training
title_zh: 面向大语言模型后训练的蒸馏强化学习框架
authors:
- Chen Wang
- Zhaochun Li
- Jionghao Bai
- Yining Zhang
- Hexuan Deng
- Ge Lan
- Yue Wang
affiliations:
- Nankai University
- Zhongguancun Academy
- Beijing Institute of Technology
- Zhejiang University
- Institute of Automation, CAS
arxiv_id: '2607.17247'
url: https://arxiv.org/abs/2607.17247
pdf_url: https://arxiv.org/pdf/2607.17247
published: '2026-07-18'
collected: '2026-07-21'
category: Training
direction: LLM后训练 · 强化学习与蒸馏融合
tags:
- Reinforcement Learning
- Knowledge Distillation
- LLM Post-training
- GRPO
- Cross-family Distillation
one_liner: 将教师模型监督融入RL目标，解决RL信用分配差与OPD跨族蒸馏失效问题
practical_value: '- 做垂直场景小模型蒸馏时，可替换原有KL蒸馏+RL的混合方案，用Distilled RL避免OPD的早熟收敛，尤其适配跨模型族（从通用大模型蒸馏行业小模型）的场景，提升小模型推理/决策准确率

  - 做Agent的RL训练时，可复用负样本重置+序列几何归一化的trick：仅在正收益轨迹上引入专家/大模型的token级偏好加权，负收益轨迹保留原生RL惩罚，避免错误引导同时解决信用分配问题

  - 做生成式推荐的item生成/文案生成对齐训练时，可借鉴Distilled RL的框架，把人工标注的优质样本作为教师信号融入RLHF流程，减少对大规模标注数据的依赖'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM后训练两大范式存在固有缺陷：RL依赖粗粒度序列级奖励，信用分配难度大，难以学习学生当前策略外的新知识；OPD通过KL散度无条件匹配教师logits，同模型族蒸馏收益有限，跨模型族时分布 mismatch 导致引导失效，且容易早熟收敛限制后续RL优化空间。

### 方法关键点
- 核心思路：不单独添加KL蒸馏损失，直接将教师偏好加权融入RL梯度，实现选择性知识迁移
- 反向重要性采样：计算每个token的教师/旧学生策略概率比，裁剪比值范围避免梯度不稳定
- 负样本重置：仅对优势为正的响应应用教师加权，负优势样本权重重置为1，避免在错误轨迹上模仿教师
- 序列级几何归一化：对每个响应内的token级比值做归一化，确保几何均值为1，消除师生似然的全局尺度差异，仅保留教师对token的相对偏好

### 关键结果
在DAPO-17K数据集上训练，对比OPD、RL（GRPO）、OPD+RL三个基线，覆盖同/跨模型族三类学生模型：跨模型族场景下平均Pass@1比OPD高4.73个点，比RL高3.14个点；同模型族场景下平均Pass@1比OPD高2.99个点，比RL高1.56个点，Pass@16指标也有稳定提升。

### 核心结论
不要把教师蒸馏作为独立损失和RL加权混合，而应该让教师作为细粒度指导者，仅在正向轨迹上重新分配RL的学习信号，才能同时保留RL的持续优化能力和蒸馏的知识迁移效率。
