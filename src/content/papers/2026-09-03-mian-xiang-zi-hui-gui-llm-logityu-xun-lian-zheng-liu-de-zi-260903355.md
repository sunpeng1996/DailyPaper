---
title: 'ALRA: Adaptive Local Relational Alignment for Logit-Based Pre-training Distillation
  of Autoregressive Language Models'
title_zh: 面向自回归LLM logit预训练蒸馏的自适应局部关系对齐方法
authors:
- Quang Hoang Trung
- Quang Huu Hieu
- Nguyen Van Hoang Phuc
- Vo Nguyen Le Duy
affiliations:
- VJ Technologies
- AJ Technologies
- Vietnam National University, Ho Chi Minh City
- University of Information Technology, Ho Chi Minh City
arxiv_id: '2609.03355'
url: https://arxiv.org/abs/2609.03355
pdf_url: https://arxiv.org/pdf/2609.03355
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: LLM预训练 · 知识蒸馏优化
tags:
- Knowledge Distillation
- Autoregressive LLM
- Logit Distillation
- Pre-training
- ALRA
one_liner: 提出ALRA自适应局部关系对齐框架，提升自回归LLM预训练蒸馏的小模型零样本性能
practical_value: '- 垂直域小参数LLM蒸馏（如电商客服、商品文案生成模型）可复用ALRA的「学生候选+教师top1锚定」token选择机制，既避免漏掉学生易混淆token，又缓解训练早期学生排名不准的问题

  - 蒸馏损失设计可借鉴Adaptive Local Divergence思路，将词汇表拆分为局部高概率区+剩余区，两个区域的条件KL均采用单位权重，避免长尾语义的监督信号被过度压制，适配商品属性识别、小众Query理解等长尾场景

  - 业务中需要做相对偏好对齐的场景（如推荐排序pairwise蒸馏、广告文案优劣偏好学习），可直接复用SWPRA加权策略，给高概率、小差异pair更高权重，提升难分样本的对齐效果'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
传统自回归LLM的logit蒸馏要么对齐全词汇表分布，忽略高概率候选间的相对偏好且计算开销大；要么局部token选择仅依赖教师或学生单方，要么漏掉学生易混淆token，要么训练早期学生排名不准效果差，同时固定局部token数无法适配不同上下文的不确定性，亟需更自适应的蒸馏方案。
### 方法关键点
- 教师锚定自适应局部token选择：每个预测位先取学生top-dmax候选，强制加入教师top1 token作为锚，再根据候选集内教师分布的有效支持度相对batch均值的比值，动态调整该位置的局部token数，最终选候选集内教师概率最高的d_u个作为局部集
- 自适应局部散度（ALD）：将全词汇表KL拆解为区域质量匹配、局部集条件KL、剩余集条件KL三部分，两个条件KL均采用单位权重，避免低概率区域的监督信号被教师质量系数压低
- 学生加权pairwise关系对齐（SWPRA）：给局部集内总概率高、学生概率差小的token对更高权重，强化学生对难分候选的相对偏好学习
### 关键结果
以Qwen1.5-1.8B为教师，在The Pile数据集上训练200M、500M参数量的随机初始化学生，对比8个主流蒸馏基线，9个零样本benchmark上平均准确率分别达36.62%、37.40%，比最强基线高0.94、0.83个百分点，比无蒸馏预训练高2.31、2.91个百分点。
### 核心结论
LLM蒸馏不需要硬对齐全词汇表分布，结合学生当前状态+教师引导的自适应局部对齐，既能降低计算开销，还能获得比全量对齐更好的下游效果
