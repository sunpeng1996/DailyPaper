---
title: Learning to Defer under Expert Drift
title_zh: 专家能力漂移场景下的学习拒判（L2D）优化方法
authors:
- Ziyao Mou
- Andrea Wynn
- Eric Nalisnick
affiliations:
- Johns Hopkins University
arxiv_id: '2611.26440'
url: https://arxiv.org/abs/2611.26440
pdf_url: https://arxiv.org/pdf/2611.26440
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 人机协同 · 动态拒判策略优化
tags:
- Learning to Defer
- Expert Drift
- Human-AI Collaboration
- Sequence Modeling
- Adaptive Policy
one_liner: 提出基于专家历史表现序列建模的EDA-L2D框架，动态适配能力漂移优化人机决策分配
practical_value: '- 电商内容审核、违规商品判别场景可复用该框架，基于审核员近期错误率/效率序列建模动态分配审核任务，降低人工成本同时提升准确率

  - Agent+人工兜底的业务流程（比如大模型客服转人工、个性化推荐合规审核）可引入该时序建模思路，替代固定阈值转人工策略，适配人工坐席状态波动

  - 众包标注场景可通过该方法动态分配标注任务，对标注质量波动大的标注员分配更简单的任务或及时质检，提升标注数据集质量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有学习拒判（L2D）框架默认人类专家能力固定，未考虑疲劳、认知偏差等因素导致的专家表现时序波动，无法适配医疗、内容审核、众包标注等实际人机协同场景的动态需求。
### 方法关键点
提出EDA-L2D自适应拒判框架，通过序列模型对专家近期决策结果历史建模，将专家表现时序特征输入拒判头，动态调整人机决策分配策略，主动预判专家可靠性波动。
### 关键结果
在图像分类、医疗诊断、仇恨言论检测三类任务上开展实验，覆盖不规则漂移、周期性漂移等多种专家能力变化模式，相比传统静态假设的L2D方法，适配性显著更优，系统整体决策准确率和拒判合理性均有明显提升，已开源相关代码。
