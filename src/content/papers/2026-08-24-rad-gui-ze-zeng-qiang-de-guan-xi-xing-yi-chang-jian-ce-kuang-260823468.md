---
title: 'RAD: Rule-Augmented Relational Anomaly Detection'
title_zh: RAD：规则增强的关系型异常检测框架
authors:
- Noah Dahle
- Anne Tumlin
- Ngoc Tran
- Xenofon Koutsoukos
- Tyler Derr
affiliations:
- Vanderbilt University
arxiv_id: '2608.23468'
url: https://arxiv.org/abs/2608.23468
pdf_url: https://arxiv.org/pdf/2608.23468
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: 关系型异常检测 · 符号规则与图学习融合
tags:
- Relational Anomaly Detection
- Heterogeneous Graph Learning
- Symbolic Rule Mining
- Anomaly Ranking
- Imbalanced Learning
one_liner: 结合异构图表示学习与符号规则信号，提升多表关系数据下的异常检测效果
practical_value: '- 电商多表用户行为（交易/浏览/会员）的异常检测（羊毛党、异常流失）场景，可采用异构图建模替代强制表打平，保留跨表多跳依赖

  - 可复用「随机森林路径提取可解释规则再注入图模型」的思路，同时兼顾风控场景要求的可解释性与模型识别精度

  - 类别极不平衡的异常识别任务，可引入pairwise-ranking监督替代单纯分类损失，提升异常样本的排序性能'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有关系数据库异常检测需将多表打平为特征矩阵，会丢失实体身份、schema结构、多跳依赖信息，且难以将符号行为规则融入学习到的关系表示中，限制依赖上下文的异常识别效果。
### 方法关键点
1. 从待评分实体的打平摘要中提取随机森林路径作为候选规则，精炼为紧凑可解释谓词
2. 将规则特征注入异构图表示学习模型，结合重建损失与pairwise-ranking监督学习异常分数
### 关键结果
在LANL安全检测、Amazon和H&M用户异常流失3个基准上，AUROC和AUPRC平均排名均为最优，优于打平表格检测与传统关系基线；消融实验显示规则注入、排序监督是性能核心贡献，边重建收益不统一
