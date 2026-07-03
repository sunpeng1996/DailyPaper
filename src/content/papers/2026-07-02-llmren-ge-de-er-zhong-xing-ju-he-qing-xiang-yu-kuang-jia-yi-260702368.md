---
title: 'The Dual Nature of LLM Persona: Aggregated Tendencies and Frame-Dependent
  Geometry'
title_zh: LLM人格的二重性：聚合倾向与框架依赖的几何结构
authors:
- Yuan Yuan
affiliations:
- Independent Researcher
arxiv_id: '2607.02368'
url: https://arxiv.org/abs/2607.02368
pdf_url: https://arxiv.org/pdf/2607.02368
published: '2026-07-02'
collected: '2026-07-03'
category: LLM
direction: LLM人格建模与特性评估
tags:
- LLM Persona
- Psychometric Evaluation
- SPD Manifold
- Frame Dependency
- Big Five
one_liner: 发现LLM人格包含框架鲁棒的聚合特征与框架依赖的几何特征两类可分离组件
practical_value: '- 做用户仿真Agent时，区分稳定人格聚合特征和场景框架依赖的几何特征，可提升用户行为模拟准确度

  - 个性化推荐的用户画像可引入双维度建模：长期稳定偏好对应聚合特征，上下文依赖的偏好波动对应几何特征

  - LLM驱动的导购/客服Agent人格设定时，可固定核心特质的同时通过上下文框架调整交互风格适配不同场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM人格的心理测量评估仅依赖聚合得分，丢弃实例内相关结构，无法明确人格几何结构是内在固有还是框架依赖的。
### 方法关键点
基于IPIP-50问卷回复构建实例内相关矩阵，在SPD流形上分析GPT-4o模拟美国/华裔美国人格时，不同问题排序（框架操纵）下的特征变化。
### 关键结果
- 聚合特征（大五人格得分）框架鲁棒性强，随机化下仅下降21%
- 几何特征在框架错位时下降42%，共享框架下可恢复到84%，优于聚合特征76%的恢复率
- 人格几何是框架依赖的协调模式，包含聚合得分无法捕捉的隐式信息
