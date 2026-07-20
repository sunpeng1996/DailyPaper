---
title: 'Language Identification via Compositional Data Analysis: A Linear-Time Classifier
  Based on Log-Ratio Geometry'
title_zh: 基于成分数据分析与对数比几何的线性时间语言识别分类器
authors:
- Paul-Andrei Pogăcean
- Sanda-Maria Avram
affiliations:
- Babeș-Bolyai University, Cluj-Napoca, Romania
arxiv_id: '2607.15238'
url: https://arxiv.org/abs/2607.15238
pdf_url: https://arxiv.org/pdf/2607.15238
published: '2026-07-16'
collected: '2026-07-20'
category: Other
direction: 低资源语言识别 · 线性时间分类
tags:
- n-gram
- CLR Transformation
- Language Identification
- Linear-time Algorithm
- Compositional Data Analysis
one_liner: 采用CLR变换处理n-gram特征，提出低资源高可解释的线性时间语言识别方案
practical_value: '- 跨境电商多语言场景的用户query、评论语种识别可直接复用该pipeline，线性时间复杂度适配高QPS需求，无需GPU即可部署，推理成本比大模型低1~2个数量级

  - 推荐/搜索场景中对用户行为频率、query term频率这类成分类特征建模时，可借鉴CLR变换替代直接归一化，避免传统欧氏距离度量带来的效果损失

  - 端侧Agent的语种识别模块可直接落地该方案，无需训练、可解释性强，便于线上bad case排查'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语言识别技术分为两类：神经方案准确率高但计算资源需求大，推理复杂度随序列长度平方级增长；传统n-gram统计方案是线性时间效率，但采用的距离度量不适配频率类成分数据的分布特性，效果存在瓶颈。
### 方法关键点
将unigram、bigram的频率分布建模为单纯形约束的成分向量，通过centered log-ratio (CLR)变换双射映射到(D-1)维零和子空间，使子空间内的欧氏距离等价于适配成分数据的Aitchison距离；搭配Laplace平滑解决n-gram特征稀疏问题，整套pipeline推理为线性时间复杂度。
### 关键结果
在6种语言的测试集上实现跨文本长度的稳定准确率，长序列表现尤为突出，推理速度、资源消耗远优于神经方案，具备完全可解释性。
