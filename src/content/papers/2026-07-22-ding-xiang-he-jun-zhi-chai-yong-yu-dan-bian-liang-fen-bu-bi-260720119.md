---
title: 'Directional Kernel Mean Difference: A Fast Signed Statistic for Univariate
  Distribution Comparison'
title_zh: 定向核均值差：用于单变量分布比较的快速带符号统计量
authors:
- Shijie Zhong
- Jiangfeng Fu
affiliations:
- Northwestern Polytechnical University
arxiv_id: '2607.20119'
url: https://arxiv.org/abs/2607.20119
pdf_url: https://arxiv.org/pdf/2607.20119
published: '2026-07-22'
collected: '2026-07-24'
category: Other
direction: 基础统计·分布差异度量
tags:
- Distribution Comparison
- MMD
- A-B Testing
- Outlier Robust
- Efficient Statistic
one_liner: 提出保留分布偏移方向的带符号单变量分布比较统计量DKMD，低开销支持百万级样本
practical_value: '- 电商/推荐系统A/B测试中可替换均值差/MMD做指标分布偏移检测，能识别正向/负向偏移，过滤无业务意义的对称波动，降低误判率

  - 特征漂移监控场景下用DKMD判断CTR、用户时长等单变量特征的偏移方向，可快速定位推荐/广告系统性能涨跌根因

  - 自带O(N log N)低复杂度、O(N)内存优化，无需额外适配即可直接落地大流量业务的实时监控场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分布比较方法（如平方MMD）丢失偏移方向信息，均值差易被重尾异常值翻转符号，传统核方法O(N²)复杂度无法适配大规模业务数据。
### 方法关键点
1. 对核均值嵌入差值乘固定奇权重函数积分，得到带符号的DKMD统计量，具备反对称性、对称分布差异免疫、随机占优下方向单调性三大特性
2. 推导数据驱动的黎曼估计器保证渐进一致性，保留带符号统计量的理论特性
3. 设计O(N log N)前缀后缀扫描算法，仅需O(N)内存，大幅降低算力开销
### 关键结果
合成实验显示DKMD可从对称扰动中正确分离定向偏移，对能翻转均值差符号的重尾异常值鲁棒，可秒级处理百万级样本。
