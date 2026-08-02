---
title: Windowed thinning and query complexity for the bouncy particle and Zigzag samplers
title_zh: 弹性粒子采样器与Zigzag采样器的窗口化抽稀及查询复杂度
authors:
- Jianfeng Lu
- Yinchen Luo
arxiv_id: '2607.28413'
url: https://arxiv.org/abs/2607.28413
pdf_url: https://arxiv.org/pdf/2607.28413
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 采样算法复杂度理论研究
tags:
- Sampling
- Gradient Query Complexity
- Markov Process
- BPS
- Zigzag Sampler
one_liner: 为弹性粒子和Zigzag两类采样器提出窗口化抽稀方法，给出高斯冷启动下的梯度查询复杂度边界
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
BPS、Zigzag两类事件驱动采样器无时间离散误差，但长期缺乏梯度查询次数的量化复杂度保证，无法准确评估实际运行的计算成本。
### 方法关键点
1. 提出windowed thinning精确模拟方法，将采样轨迹划分为确定性窗口，每个窗口起始处做一次梯度评估，构建事件率的可解局部包络；
2. 结合定量混合估计、弹跳/翻转次数的有限时间边界，推导高斯冷启动下的查询复杂度保证。
### 关键结果
总变差误差为$ε$时，BPS预期梯度查询复杂度为$O(κ^{1/2}d(d\logκ + \log\frac{1}{ε}))$；Zigzag的全梯度等价查询复杂度为$O(κ d^{1/4}(d\logκ + \log\frac{1}{ε}))$，其中d次坐标偏导查询等价1次全梯度查询。
