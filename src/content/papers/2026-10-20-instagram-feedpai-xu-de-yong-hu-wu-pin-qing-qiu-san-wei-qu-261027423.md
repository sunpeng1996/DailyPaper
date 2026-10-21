---
title: 'Baseline and Incremental: User, Item, and Request Debiasing in Instagram Feed
  Ranking'
title_zh: Instagram Feed排序的用户、物品、请求三维去偏：基线与增量拆分方案
authors:
- Hsin-Chiang Chen
- Hao Wang
- Gedi Zhou
- Mingze Gao
- Abhishek Kumar
- Yiben Yang
- Haoyu Wang
- Hongjing Xia
- Bo Chen
- Zhengyu Su
affiliations:
- Meta
arxiv_id: '2610.27423'
url: https://arxiv.org/abs/2610.27423
pdf_url: https://arxiv.org/pdf/2610.27423
published: '2026-10-20'
collected: '2026-10-21'
category: RecSys
direction: Feed排序 · 多维度去偏优化
tags:
- debiasing
- feed-ranking
- value-model
- online-experiment
- popularity-bias
one_liner: 将排序预测拆为基线与独立加权增量项做三维去偏，在Meta全场景落地提升留存指标
practical_value: '- 无需修改模型结构，直接在Value Model层将原始预测和增量项（预测减基线）拆为两个独立加权特征，配置上线成本极低，可快速AB测试验证效果

  - 三类基线计算可直接复用：用户基线取历史行为率、物品基线取跨用户历史点击率/时长/格式分桶均值、请求基线取当前候选池预测分p75/均值

  - 离线信号筛选规则可复用：预测分与基线的分位数相关系数≥0.5、方差占比≥20%的信号优先拆分，弱相关稀疏特征不要直接丢弃，降低无效实验量

  - 去偏方案选型规则：物品流行度偏用VM层加项，媒体格式偏用去偏标签训练，右偏信号用sigmoid门控、对称信号用线性hinge，减少试错成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界排序的Value Model通常直接加权多任务预测分，但每个预测分混杂了用户习惯、物品流行度、请求上下文的基线噪声；传统去偏直接移除基线，浪费了基线本身承载的真实信号（如高活跃度用户的真实engagement、优质热门内容的价值），单一系数无法权衡基线与增量的价值。

### 方法关键点
1. 改造Value Model公式：保留原始预测分的加权项，新增增量项Δ（预测分相对基线的偏差，可选sigmoid门控/线性hinge形式）独立加权，无需重新训练排序模型
2. 三类基线计算逻辑：用户基线取用户历史行为率，物品基线取物品跨用户历史指标/格式分桶均值，请求基线取当前请求候选池预测分的p75/均值
3. 落地流程：离线用分位数相关系数+方差占比筛选需要拆分的信号，线上用四臂AB实验（无项/仅原始/仅增量/双项）验证最优配置

### 关键结果
在Instagram Feed全流量上线6个去偏项，四臂AB测试显示13个（项×指标）对中有11个双项配置的点估计优于仅原始或仅增量配置；26组直接对比中17组显著正收益，仅1组负收益。方案已在Meta全产品线（Reels/Threads/Facebook）落地，最高提升DAU 0.042%、Feed时长0.359%。

### 最值得记住的一句话
去偏不是要完全消除基线，而是把基线和增量拆为两个独立信号让调参器自动权衡，用极低的配置改动成本就能拿到核心指标收益。
