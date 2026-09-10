---
title: 'A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free
  Hold-Out'
title_zh: 延后测试集并非新领域：无污染留出集下预训练熟悉度仍存在
authors:
- Mahdi Naser Moghadasi
- Faezeh Ghaderi
affiliations:
- BrightMind AI
- University of Texas at Arlington
arxiv_id: '2609.10357'
url: https://arxiv.org/abs/2609.10357
pdf_url: https://arxiv.org/pdf/2609.10357
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: 时序大模型评估 · 预训练数据污染验证
tags:
- Time Series Foundation Model
- Evaluation
- Data Contamination
- Domain Familiarity
- Hold-out Set
one_liner: 构建全晚于模型发布的无污染时序评估集，证明时间留出无法消除预训练领域熟悉度优势
practical_value: '- 做电商销量、流量等时序类预测业务选预训练大模型时，优先选预训练语料覆盖自身业务领域的模型，不要盲目追通用SOTA

  - 内部评估自研大模型时，除时间留出集外必须加与预训练语料完全无重叠的领域留出集，才能真实衡量泛化能力

  - 做推荐/搜索场景的时序用户行为建模时，预训练阶段可多覆盖业务域内历史数据，新时间窗口预测效果会明显更好'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时序基模评估普遍使用早于模型发布的公开数据集，无法区分性能来自真泛化还是预训练见过测试集，行业默认用晚于模型发布的时间留出集解决该问题，但方案有效性未被验证。

### 方法关键点
构建无API依赖、所有观测数据均晚于参评模型发布时间的评估集，覆盖5个领域7个数据组，对比13种预测方法（4种经典方法、3种单数据集训练模型、6种预训练基模）的性能，定位性能差异的核心影响因素。

### 关键结果数字
预训练模型在7组测试中赢下5组，在预训练语料覆盖的维基百科周浏览量场景下MASE比最优经典方法低28%；TimesFM在其预训练主域维基百科数据上比Chronos排名高0.53，其他域仅高0.09，Mann-Whitney p < 1e-5；时间留出集仅能消除窗口记忆，无法消除领域熟悉度带来的性能优势。
