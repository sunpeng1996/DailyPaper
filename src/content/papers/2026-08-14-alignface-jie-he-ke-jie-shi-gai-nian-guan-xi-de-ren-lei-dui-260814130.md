---
title: 'AlignFace: Human-Aligned Face Similarity Metric with Interpretable Concept
  Relations'
title_zh: AlignFace：结合可解释概念关系的人类对齐人脸相似度度量
authors:
- Ying Huang
- Wencan Zhang
- Brian Y. Lim
affiliations:
- National University of Singapore
arxiv_id: '2608.14130'
url: https://arxiv.org/abs/2608.14130
pdf_url: https://arxiv.org/pdf/2608.14130
published: '2026-08-14'
collected: '2026-08-21'
category: Other
direction: 可解释计算机视觉 · 感知对齐度量
tags:
- Interpretable AI
- Perceptual Alignment
- Concept Bottleneck Model
- Vision-Language Model
- Computer Vision
one_liner: 基于认知心理学原理构建对齐人类感知的可解释人脸相似度度量，配套FACETS数据集
practical_value: '- 电商虚拟人、人脸编辑类工具的生成效果评估，可借鉴「认知先验+可解释概念瓶颈」范式，替代黑箱度量，更对齐C端用户感知

  - 做人群差异化的内容推荐/生成优化时，可参考其对不同群体感知偏置的建模思路，适配细分用户群的偏好差异

  - 搭建可解释AI系统时，可复用「属性级门控交叉注意力提特征+广义加性模型建模非线性影响」架构，输出可解释决策依据'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有生成人脸内容的相似度度量仅做行为级建模，未实现认知对齐，默认统一观察者假设忽略人群固有感知差异，易导致评估结果失真、生成模型调试方向误导。
### 方法关键点
1. 引入认知心理学先验规则：人脸相似度依赖特征/结构属性、非线性心理物理响应、自有群体感知偏置；
2. 用VLM编码人脸对和文本属性，门控交叉注意力提取属性级人脸差异表征；
3. 结合概念瓶颈模型（CBM）约束推理过程可解释，神经广义加性模型（GAM）建模各属性的非线性影响；
4. 配套发布FACETS数据集。
### 关键结果
相比LPIPS、SSIM等基线度量，AlignFace在三元组比较任务中与人类子群体感知的对齐度实现显著提升。
