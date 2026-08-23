---
title: 'HARP: Hierarchical Adaptive Ranking with Preference-Adaptive Fusion for Query-Based
  CVE Prioritization'
title_zh: HARP：面向查询式CVE优先级排序的分层自适应排序框架
authors:
- Haochen Liu
- Zhengzhang Chen
- Haoyu Wang
- Yanchi Liu
- Jundong Li
- Haifeng Chen
affiliations:
- University of Virginia
- NEC Laboratories America
arxiv_id: '2608.19430'
url: https://arxiv.org/abs/2608.19430
pdf_url: https://arxiv.org/pdf/2608.19430
published: '2026-08-19'
collected: '2026-08-23'
category: Other
direction: 自适应排序 · 隐式偏好多视角融合
tags:
- Ranking
- Implicit Preference
- Knowledge Graph
- Multi-view Fusion
- LLM
one_liner: 基于历史标注案例与多视角融合实现无需显式偏好的查询式CVE优先级排序
practical_value: '- 隐式偏好适配可复用：无需用户显式输入偏好prompt，通过历史标注样本自动学习多视角融合权重，可迁移到电商大促/日常等不同运营场景的排序策略适配，降低规则配置成本

  - 多信号融合架构可借鉴：全局+业务域+用户三层分层打分逻辑，可直接复用在搜索/广告/推荐的多源排序信号融合模块，替代人工指定的固定权重融合方案

  - 冷启动排序思路可参考：基于历史样本库支撑的检索增强排序模式，适合业务冷启动场景下的排序策略快速迭代，无需重新微调大模型'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有CVE优先级排序方法依赖固定评估准则，而不同组织的运营偏好是隐式的，难以转化为显式prompt描述，查询本身也不携带偏好信息，已标注的历史分诊案例是更易获取的信号。
### 方法关键点
提出HARP分层自适应排序框架：1）从漏洞知识图谱检索候选CVE的关联证据；2）基于策略约束从全局、企业、用户三个独立视角分别为候选打分；3）从采样的历史支撑样本中自动拟合多视角分数的融合权重，无需显式偏好文本即可完成查询驱动的排序。
### 关键结果
在3种不同偏好场景、多款主流LLM backbone上的实验显示，HARP效果全面优于所有基线方法
