---
title: 'When Category Means Move: A Paired-Support Audit of Recommendation Logs with
  Random Insertions'
title_zh: 基于随机插入曝光的推荐日志配对支撑类目均值审计
authors:
- Yu Zhang
- Zhihan Wang
- Yuhang Lu
- Shuai Li
affiliations:
- AMap Alibaba Group
arxiv_id: '2611.05006'
url: https://arxiv.org/abs/2611.05006
pdf_url: https://arxiv.org/pdf/2611.05006
published: '2026-11-03'
collected: '2026-11-04'
category: RecSys
direction: 推荐系统评估 · 类目统计偏差审计
tags:
- Recommender System
- Log Audit
- Exposure Bias
- Random Insertion
- Metric Calibration
one_liner: 提出配对支撑审计框架，量化推荐类目统计偏差来源与校准效果
practical_value: '- 做电商/内容类目大盘指标核算时，可引入1%-5%的随机插入曝光作为无偏参考，先修正整体均值偏移再评估类目间相对表现

  - 类目指标偏差可复用论文拆解逻辑：72.4%来自同Item下的观众/上下文偏差，23.9%来自类目内Item曝光权重不均，仅3.6%来自支撑集差异

  - 生产环境做类目指标校准优先选分类目校准而非全局标量校准，实验显示前者可将MAE从0.0531降至0.0251，效果提升显著

  - 基于日志类目排名做流量倾斜、资源分配等top-k决策时，需额外做决策损失验证：本实验仅top-10有边际收益，top5/top20收益统计不显著'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统运营大盘常基于服务日志计算类目平均 engagement 做内容采购、流量分配等决策，但服务策略会扭曲用户、Item、上下文分布，导致类目均值失真，无法反映真实内容质量，现有方法多聚焦推荐模型去偏，缺乏针对运营类目指标的系统性审计方案。

### 方法关键点
- 基于KuaiRand公开数据集的随机插入曝光作为无偏参考基准，对齐两份日志的相同用户、Item集合构造配对支撑集，消除支撑集进出的影响
- 拆分三类偏差指标：绝对MAE（衡量整体水平偏移）、中心化MAE（衡量类目间相对形状偏差）、排名相关性（衡量类目排序偏差）
- 用Kitagawa分解将类目偏差拆分为同Item残差、类目内Item曝光mix两部分，再扩展到全支撑集加入出入项贡献拆分
- 设计无泄漏前瞻校准方案：用历史数据算用户基线，早期窗口算校准系数，冻结后在后期窗口验证效果

### 关键结果
用KuaiRand 17天数据，覆盖12472个用户、5486个视频、38个类目。原生服务日志类目均值相对无偏参考的绝对MAE为0.1935，中心化MAE为0.0491，排名相关性0.7833。用户去均值加随机全局均值锚定可降低80%绝对MAE，但中心化MAE仅降21%，排名无显著提升。分类目前瞻校准相对全局标量校准MAE从0.0531降至0.0251，但仅top10决策有边际收益，top5/top20收益统计不显著。

**最值得记住的结论**：不要被类目均值80%的绝对误差下降迷惑，它仅修正了整体水平偏移，对类目排序和top-k决策的提升非常有限。
