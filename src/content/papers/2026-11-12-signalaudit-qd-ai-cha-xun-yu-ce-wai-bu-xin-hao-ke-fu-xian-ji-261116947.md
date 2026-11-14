---
title: 'SignalAudit-QD: A Reproducible Audit Resource for External Signals in AI-Query
  Forecasting'
title_zh: SignalAudit-QD：AI 查询预测外部信号可复现审计资源
authors:
- Amir Rafe
- Iman Jamshidi
- Gourab Sil
- Subasish Das
affiliations:
- Texas State University
- Indian Institute of Technology Indore
arxiv_id: '2611.16947'
url: https://arxiv.org/abs/2611.16947
pdf_url: https://arxiv.org/pdf/2611.16947
published: '2026-11-12'
collected: '2026-11-14'
category: QueryRec
direction: 查询预测 · 外部信号审计
tags:
- Query_Forecasting
- External_Signal
- Reproducible_Audit
- Google_Trends
- Temporal_IR
one_liner: 构建可复现审计资源验证外部信号对AI查询预测的实际增量价值
practical_value: '- 做搜索query趋势预测、下拉推荐优化时，新增外部信号前必须做严格增量价值审计，避免无效特征拉高训练/推理成本

  - 可复用论文中planted-signal assay方法验证新增特征真实贡献，排除伪相关、数据泄露导致的虚高收益

  - 时序预测任务新增外部信号时，需匹配严格的时间窗口控制，优先做伪原点检测规避回溯数据污染问题'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前查询趋势预测任务中，外部信号的增量价值易被高估，缺乏可复现的审计框架验证信号真实贡献，常出现伪相关、数据泄露导致的特征误用。
### 方法关键点
构建SignalAudit-QD审计资源，对齐2020-2023年20个美国AI领域查询的Google Trends存档、8个USPTO AI专利公开流，配套可执行测试、来源追溯、防篡改运行清单，采用伪原点检测方法排除回溯数据泄露问题。
### 关键结果数字
1个月预测窗口下，加入专利信号后MAE仅波动+0.0012 Trends点，95%置信区间[-0.0363,+0.0387]，无统计显著增益；非线性模型加入信号后甚至出现性能劣化；植入信号检测仅能识别最大量级的注入信号，验证了小增益外部信号的检测难度。
