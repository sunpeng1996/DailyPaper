---
title: 'Wasserstein-Barycentric Interaction Fields for Spatial Factor Models: Evidence
  from Language-Model Representations'
title_zh: 面向空间因子模型的Wasserstein重心交互场：基于LLM表征的实证
authors:
- Marcus Gawronsky
- Chun-Sung Huang
affiliations:
- Department of Finance and Tax, University of Cape Town
arxiv_id: '2608.29669'
url: https://arxiv.org/abs/2608.29669
pdf_url: https://arxiv.org/pdf/2608.29669
published: '2026-08-29'
collected: '2026-09-06'
category: Other
direction: LLM表征 · 空间因子交互场构建
tags:
- Wasserstein Barycenter
- LLM Embedding
- Spatial Factor Model
- Text Representation
- Interaction Field
one_liner: 基于LLM文本表征用Wasserstein重心重构构建无带宽空间交互场，提升空间因子模型表现
practical_value: '- Wasserstein重心重构方法可直接迁移至多源异构用户/物品embedding分布融合任务，无需人工设定核函数带宽，鲁棒性更强

  - 无带宽交互场构建思路可用于跨域推荐的全局相似度矩阵生成，替代传统人工定义的RBF、等权重相似度计算方案

  - 反馈映射为错位惩罚比的校准思路，可迁移到推荐系统负反馈归因，量化推荐结果与用户真实偏好的错位程度'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有空间因子模型依赖人工预设交互矩阵，未解释反馈的实际含义，嵌入分布融合通常需人工设定带宽参数，适配性和鲁棒性不足。

### 方法关键点
1. 基于企业新闻文本的LLM embedding分布，采用目标锚定的Wasserstein重心重构方法，构建无带宽的空间交互场；
2. 设计二次暴露调整问题，将模型反馈映射为同行错位惩罚比，量化模型对真实关联的适配度。

### 关键结果
基于2018-2022年新闻冻结构建的交互场，在2023-2026年52家企业样本上惩罚比达3.46（95%置信区间[2.89, 4.17]），条件拟似然显著优于等权重同行支持、同距离RBF加权方法；联合重心场与新闻共提及场的惩罚比分别为2.33和0.86，边界校准测试均拒绝两个场的排他性假设（p=0.0005）。
