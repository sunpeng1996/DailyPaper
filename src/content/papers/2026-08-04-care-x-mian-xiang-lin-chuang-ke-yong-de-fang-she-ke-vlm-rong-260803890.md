---
title: 'CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision,
  Reward-Aligned Learning, and Tool-Augmented Measurement'
title_zh: CARE-X：面向临床可用的放射科VLM，融合辅助监督、奖励对齐与工具增强
authors:
- Mercy Prasanna Ranjit
- Anirban Porya
- Sathvik Joel
- Niharika Vadlamudi
- Nikhilesh Chowdary Eathamukkala
- Prasanth V
- Abhyuday Kumara Swamy
- Pranay Narhari Umredkar
- Pradeep Narayan
- Vivek Rajagopal
affiliations:
- Microsoft Research India
- Medha AI, Narayana Health, India
- RTIICS, Narayana Health, India
arxiv_id: '2608.03890'
url: https://arxiv.org/abs/2608.03890
pdf_url: https://arxiv.org/pdf/2608.03890
published: '2026-08-04'
collected: '2026-08-06'
category: Multimodal
direction: 多模态大模型 · 垂直领域落地优化
tags:
- VLM
- Reward Alignment
- Tool Calling
- Multi-task Learning
- Multimodal
one_liner: 提出融合辅助监督、奖励对齐、工具增强的胸片VLM，多维度匹配临床放射科实际需求
practical_value: '- 多任务联合训练可采用「生成主干+分类/定位专用头」共训方案，结构化预测与生成任务可互相增益，可复用到多模态商品理解、内容审核、广告素材质检场景

  - 可借鉴DAPO思路设计任务专属奖励对齐策略，直接优化业务核心指标，可迁移到生成式推荐的用户满意度对齐、广告文案生成的转化效果优化

  - 大模型原生工具调用结合确定性工具的混合推理方案，可解决需精确数值计算的业务场景如电商尺码推荐、物流时效预测、营销预算分配'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有放射科VLM仅聚焦报告生成，无法同时满足临床所需的可调阈值分类、病灶空间定位、解剖数值测量需求，多任务割裂的设计与临床实际要求存在明显差距。

### 方法关键点
1. 在生成主干上额外新增focal-loss分类头、复合损失定位头，与语言建模目标联合训练，同时兼顾结构化预测与生成能力；
2. 提出DAPO策略优化，基于报告生成、VQA、空间定位的任务专属奖励信号，直接对齐临床核心评价指标；
3. 基于Qwen3-VL原生工具调用能力，耦合确定性测量工具，用混合推理解决数值测量类诊断需求。

### 关键结果
在4个报告生成基准的多数指标上达到SOTA，ReXVQA数据集VQA准确率达94.0%，超次优基线6pp；空间生成解码性能接近专用检测头；5类测量依赖的诊断任务平均F1较纯感知基线提升43.6pp。
