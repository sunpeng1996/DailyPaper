---
title: 'PAA: The Probabilistic Allen Algebra: A Generative and Complete Probabilistic
  Extension of Allen''s Interval Relations'
title_zh: 概率艾伦代数：艾伦区间关系的生成式完备概率扩展
authors:
- Julian Eggert
arxiv_id: '2609.20634'
url: https://arxiv.org/abs/2609.20634
pdf_url: https://arxiv.org/pdf/2609.20634
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 时序关系建模 · 概率代数扩展
tags:
- Temporal Reasoning
- Probabilistic Algebra
- Generative Model
- Uncertainty Modeling
- Open Source
one_liner: 提出生成式完备的概率艾伦代数PAA，基于区间边界分布推导时序关系概率
practical_value: '- 可复用PAA的高斯区间建模方法，处理电商用户行为时序、会话时间边界的不确定性，优化浏览时段、活动周期的模糊匹配效果

  - 可借鉴分级时序语义划分逻辑，提升搜索推荐中"最近浏览""刚结束的活动"等模糊时间query的召回与排序准确率

  - 官方开源Python包可直接集成到Agent时序推理模块，实现自然语言中模糊时间表述的精准语义解析'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统Allen区间代数的13种基础时序关系是基于精确区间边界的硬谓词，无法适配自然语言、用户行为数据、业务数据库中时序边界、时长普遍存在的不确定性，无法建模“刚在之前”“大致期间”这类带分级语义的时序表述。
### 方法关键点
1. 时序点采用高斯分布建模，区间采用高斯中点+截断高斯时长建模，所有关系概率从边界分布直接推导而非人工预设打分
2. 接触类关系（meets、starts、finishes、equals）通过容忍带获得正度量，13种关系形成完备划分，容忍度归0时可退化为原始硬Allen代数
3. 代数具备尺度不变性，可区分“不久前”“很久以前”这类分级表述与接触类关系的语义差异
### 关键结果
所有推导结论经蒙特卡洛验证，已发布经过测试的开源Python包可直接落地使用
