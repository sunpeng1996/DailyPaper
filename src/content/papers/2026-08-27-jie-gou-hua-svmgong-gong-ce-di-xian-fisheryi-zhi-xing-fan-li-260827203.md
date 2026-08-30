---
title: 'Common Geodesics Do Not Guarantee Fisher Consistency of the Structured SVM:
  Minimal Counterexamples and a Tree-Metric Classification'
title_zh: 结构化SVM公共测地线Fisher一致性反例与树度量分类
authors:
- Jintao Fei
- Jiangying Luo
affiliations:
- JD.com
- Tsinghua University
arxiv_id: '2608.27203'
url: https://arxiv.org/abs/2608.27203
pdf_url: https://arxiv.org/pdf/2608.27203
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 结构化SVM Fisher一致性理论分析
tags:
- Structured_SVM
- Fisher_Consistency
- Geodesic_Metric
- Tree_Metric
- Learning_Theory
one_liner: 构造结构化SVM Fisher一致性反例，给出树度量下argmax一致性的充要分类
practical_value: '- 设计多标签/序列推荐等结构化预测任务的SSVM损失时，若用树结构度量loss，优先选择路径型树度量，可保证argmax一致性

  - 输出空间为分支树度量时，仅边界分布下会出现一致性失效，全支撑分布的业务场景下可正常使用SSVM

  - 验证结构化预测损失的一致性时，不能仅依赖公共测地线条件，需额外校验与解码器的匹配性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
此前研究提出结构化SVM Fisher一致性的必要条件为任务损失是度量且任意三个输出存在公共测地线，但未验证该条件是否充分。
### 方法关键点
构造严格非贝叶斯最优的得分向量反例，对输出空间为正权树度量的场景做完全分类，所有最优性结论均附带精确原对偶证书。
### 关键结果
1. 4输出星型树是满足公共测地线条件的最小反例
2. 树度量下argmax一致性的充要条件为树是路径型
3. 分支树仅在边界分布下失效，全支撑分布下一致性保留
4. 满足公共测地线条件的全支撑反例最小需要5个输出，$K_{2,3}$是最小二分图反例，三维汉明立方也存在全支撑反例
