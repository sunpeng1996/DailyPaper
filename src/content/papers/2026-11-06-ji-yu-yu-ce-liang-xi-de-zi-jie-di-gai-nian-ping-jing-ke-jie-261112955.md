---
title: Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable
  Time Series
title_zh: 基于预测惊喜的自接地概念瓶颈可解释时间序列分类方法
authors:
- Sachith Abeywickrama
- Emadeldeen Eldele
- Min Wu
- Xiaoli Li
- Chau Yuen
affiliations:
- Nanyang Technological University, Singapore
- Institute of Advanced Intelligence and Computing (IAIC), A*STAR, Singapore
- Department of Computer Science, Khalifa University, UAE
- Singapore University of Technology and Design, Singapore
arxiv_id: '2611.12955'
url: https://arxiv.org/abs/2611.12955
pdf_url: https://arxiv.org/pdf/2611.12955
published: '2026-11-06'
collected: '2026-11-12'
category: Other
direction: 可解释时间序列分类 · 自监督概念瓶颈
tags:
- Time Series Classification
- Predictive Surprise
- Self-Supervised Learning
- Concept Bottleneck
- Interpretable AI
one_liner: 提出ConceptTime框架，基于自监督预测惊喜信号实现高精度可解释可弃权的时间序列分类
practical_value: '- 电商用户行为序列（浏览/点击/加购）建模可复用预测惊喜信号做无监督分段，替代固定滑窗，提升行为模式挖掘精准度

  - 可借鉴自监督构造概念瓶颈的思路，无需专家标注即可生成可解释的用户/物品行为标签，降低生成式推荐可解释性落地成本

  - 冷启动低标注场景可复用仅1%标注达到近SOTA精度的半监督训练范式，适配新用户/新物品的行为分类需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
高风险场景下的时间序列分类需同时满足高精度、可解释、弱证据下弃权三个要求，现有方法依赖固定滑窗或专家标注词表，无法同时覆盖三类特性，核心瓶颈是时序片段边界与模式识别的循环依赖问题。
### 方法关键点
用冻结的概率预测器逐时间步输出下一观测的预测分布，将预测与真实值的偏差定义为预测惊喜，该信号可同时定位片段边界、表征片段特征；聚类片段特征得到动态机制词表作为概念，轻量分类头基于概念序列输出结果，样本与最近概念的距离天然提供置信度判断能力。
### 关键结果
17个公开基准上精度与SOTA黑盒模型相当，优于所有可解释基线；癫痫检测任务仅用1%标注仍保持近98%精度；OOD检测、可信度指标优于现有可解释方法，全程无需人工标注、LLM调用或领域专家介入。
