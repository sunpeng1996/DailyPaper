---
title: Certified Parallel-in-Time Sinkhorn for Dynamic Entropic Optimal Transport
title_zh: 带精度保障的动态熵最优传输时间并行Sinkhorn算法
authors:
- Xinyang Wen
arxiv_id: '2607.24741'
url: https://arxiv.org/abs/2607.24741
pdf_url: https://arxiv.org/pdf/2607.24741
published: '2026-07-27'
collected: '2026-07-29'
category: Other
direction: 最优传输加速 · 分布式迭代算法优化
tags:
- Sinkhorn
- Optimal Transport
- Parallel Computing
- Flow Matching
- Distributed Training
one_liner: 提出带确定性精度校验的时间并行Sinkhorn执行器，大幅提升动态最优传输任务运算速度
practical_value: '- 电商推荐跨域分布对齐、用户兴趣分布匹配等用到Sinkhorn的场景，可复用TemporalSinkhorn时间并行思路提升运算效率

  - 分布式迭代类算法的精度保障可借鉴「安全前缀校验+事后残差检查」设计，在提速的同时避免精度损失

  - 流数据下最优传输求解（如实时Flow Matching生成推荐样本）可复用其动态调度、审计里程碑设置的trick'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
动态最优传输类任务（如Flow Matching）需反复求解熵最优传输问题，传统分布式Sinkhorn按序列处理帧、每轮迭代后全局同步，算力利用效率低。
### 方法关键点
研发TemporalSinkhorn时间并行执行器，批量处理未来候选及修正计算；设计中心行分片证书仅接收确定性安全前缀，剩余候选共享打包Sinkhorn更新；引入在线投影遗忘率设置审计里程碑，搭配事后残差检查规避深度低估问题，全程保障输出精度无偏差。
### 关键结果
4卡A100 n=2048场景下，相比逐打包迭代审计方案耗时降低1.15x-1.47x；相比序列软c变换热启动方案在6个合成流上提速1.42x-3.55x，无精度违规；Flow Matching小批量流场景下提速3.054x-3.632x；RTX 4060笔记本GPU固定核测试几何平均提速4.315x。
