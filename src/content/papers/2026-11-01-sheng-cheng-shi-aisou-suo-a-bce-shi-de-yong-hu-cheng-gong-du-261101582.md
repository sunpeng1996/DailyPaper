---
title: 'Measuring User Success in Randomized Search Experiments: Interpreting Good
  Abandonment in Generative AI Search'
title_zh: 生成式AI搜索A/B测试的用户成功度量：识别良性无点击
authors:
- Minha Hwang
- Shavak Agrawal
- David Chen
- Carto Wong
- Xin Du
- Tiannan Wang
- Georg Buscher
- Zheng Chen
affiliations:
- Microsoft
- Simplex AI
arxiv_id: '2611.01582'
url: https://arxiv.org/abs/2611.01582
pdf_url: https://arxiv.org/pdf/2611.01582
published: '2026-11-01'
collected: '2026-11-03'
category: Eval
direction: 搜索A/B测试 · 良性无点击度量
tags:
- A-B Testing
- Good Abandonment
- Generative Search
- User Success Metric
- Online Experimentation
one_liner: 提出人类标注对齐的SSR度量，解决生成式搜索下良性无点击的A/B测试评估难题
practical_value: '- 做生成式搜索/智能导购的A/B测试时，不要只依赖点击率判断效果，可加入无点击场景的停留时长、滚动深度、后续query语义相似度等特征，识别良性无点击，避免误判无点击等于效果差

  - 指标设计可参考SSR的分层逻辑：先做query级的点击/无点击分支独立建模，再加权聚合到会话级，兼顾可解释性和准确率，方便后续归因排查实验异动原因

  - 生产实验评估可复用SSR的敏感性优化思路：人类标注对齐的弱监督指标相比纯行为指标（如人均会话数）可提升2.5倍的实验检测灵敏度，降低单实验流量需求，提升实验吞吐量'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式AI搜索场景下，传统点击、停留等行为指标无法准确反映用户满意度：用户点击后可能依旧不满意，而无点击也可能是生成式结果直接满足了需求（良性无点击），导致A/B测试效果评估出现偏差，过往无点击识别方法缺乏上下文行为关联，准确率低，无法直接用于线上实验度量。

### 方法关键点
- 标注流程：分层采样跨设备、会话长度、query频率的搜索会话，由标注员结合脱敏交互数据、会话完整录屏标注用户满意度，仅用标注做离线训练，线上不依赖录屏数据
- 特征体系：融合三类信号：query时序、点击、下游engagement等事件信号；页面停留、可视比例、滚动行为等页面交互信号；后续query语义改写是否属于挣扎类修改的语义旅程信号
- 模型结构：分点击、无点击两个独立分支建模query级成功率，再用所有query的平均成功率作为会话级SSR，放弃复杂控制变量以保留可解释性和鲁棒性

### 关键实验
离线数据集包含6904条标注query、3216条标注会话，其中53.2%的无点击query属于良性无点击，6.5%的点击query实际未满足用户需求；离线效果上，query级平衡准确率0.75，无点击场景平衡准确率0.68，会话级平衡准确率0.68，远优于多数类基线和过往无点击规则；线上验证覆盖12个A/B测试，SSR和人均会话数的方向一致性达7/12，仅1例冲突；4000个生产实验中，SSR的统计显著性检测灵敏度是人均会话数的2.5倍，可降低单实验流量需求、提升实验吞吐量。

### 最值得记住的一句话
生成式搜索/导购场景下的效果评估不能唯点击率论，无点击不等于用户不满意，结合上下文行为的人类对齐指标才能更准确反映真实用户体验。
