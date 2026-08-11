---
title: Scaling Inherently Interpretable Language Models
title_zh: 可扩展的内生可解释大语言模型
authors:
- Guide Labs Team
- Andreas Madsen
- Aya Abdelsalam Ismail
- Giang Nguyen
- Isaac Plant
- Muawiz Chaudhary
- Nathaniel Monson
- Saqib Azim
- Zhichen Guo
- Julius Adebayo
affiliations:
- Guide Labs
arxiv_id: '2608.07594'
url: https://arxiv.org/abs/2608.07594
pdf_url: https://arxiv.org/pdf/2608.07594
published: '2026-08-05'
collected: '2026-08-11'
category: LLM
direction: 大模型训练 · 内生可解释性
tags:
- Interpretable-LLM
- Inherent-Interpretability
- Concept-Bottleneck
- Diffusion-LM
- Scaling-Law
one_liner: 将可解释性约束加入预训练流程，实现性能与可解释性同步随计算规模提升
practical_value: '- 电商生成式推荐/文案生成场景可借鉴概念瓶颈架构：将品类、合规标签作为监督概念加入训练，无需重训即可调整概念权重干预生成内容，快速规避违规、不符合品牌调性的输出

  - 推荐系统可解释性优化可复用训练时加概念约束的思路：把用户兴趣标签、item类目作为预定义概念加入召回/排序模型训练，天然输出可信归因结果，无需额外开发事后解释模块

  - 电商导购Agent场景可借鉴归因设计：将Agent动作、决策维度作为预定义概念加入训练，实现决策路径可追溯，大幅降低badcase排查成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流大模型采用「先训黑盒再事后解释」的范式，事后解释方法可靠性差、无法保证归因和实际计算逻辑一致；业界普遍认为增加可解释性约束会损失模型性能，且没有大规模预训练级别的人类可理解概念库支撑内生可解释模型的训练。

### 方法关键点
- 全链路加可解释性训练约束：从数据标注、架构设计、损失函数、评估指标全流程嵌入可解释要求，而非事后补充
- 构建Atlas概念标注pipeline：从1.5万亿token多领域语料中提取33000+多粒度人类可理解概念，覆盖主题、风格、功能等维度
- 架构上加加法概念瓶颈层：在因果扩散LM的Transformer backbone和输出头之间插入轻量化概念模块，8B规模下仅占4%参数，输出logit可精确拆解为各概念贡献+残差
- 采用扩散掩码训练目标：让[MASK]作为天然的输入缺失基线，输入归因天然在分布内，无需额外设计OOD基线

### 关键结果
- 跨三个数量级计算规模的IsoFLOP实验显示：加可解释约束仅带来固定的小幅性能偏移，不会随规模扩大增加损失，且可解释性指标随模型规模同步提升
- 产出的Steerling-8B模型仅用同类开源模型1/2~1/16的计算量，性能达到同类模型平均水平的90%，同时支持输入、概念、训练数据三类可信归因，可直接调整概念权重干预输出无需重训

### 核心结论
可解释性不是性能的负担，将其作为训练约束加入全流程时，可解释性会和模型能力同步随规模提升
