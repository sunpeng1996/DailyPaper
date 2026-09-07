---
title: 'ReLViC: Loss-Resilient Learned Video Coding with Dispersed Packetization and
  Controllable Packet Dependencies'
title_zh: ReLViC：抗丢包鲁棒学习型视频编码框架
authors:
- Xuyang Chen
- Daquan Feng
- Xianfu Chen
- Xiang-Gen Xia
arxiv_id: '2608.30202'
url: https://arxiv.org/abs/2608.30202
pdf_url: https://arxiv.org/pdf/2608.30202
published: '2026-08-31'
collected: '2026-09-07'
category: Other
direction: 学习型视频编码 · 丢包鲁棒优化
tags:
- Learned Video Coding
- Packet Loss Resilience
- Transformer
- Error Propagation Control
- Progressive Training
one_liner: 提出兼具隐态编码和丢包恢复的学习型视频编码框架，严重丢包下效果优于H.265+FEC及GRACE基线
practical_value: '- 双用途Transformer设计思路可复用：单个模型同时承担编码（特征预处理）和解码（缺失特征补全）任务，降低多任务链路的推理和维护成本，适合电商推荐多模态特征处理链路

  - 三阶段渐进训练策略可迁移：先训练基础任务能力，再叠加时序/上下文建模，最后注入噪声模拟真实故障（特征缺失、请求抖动）优化鲁棒性，可用于提升大促等极端流量下推荐系统的稳定性

  - 无重训参数化权衡机制可借鉴：通过可配置参数直接调整模型在效果、鲁棒性、开销之间的平衡，无需重新训练，可用于快速适配推荐/广告系统不同流量等级的服务要求'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
丢包尤其是突发丢包会破坏学习型视频编码的隐态token，导致空间重建失效、时序预测误差传播，现有方案在严重丢包下重建稳定性差，无法满足实时视频交互的低时延高可靠要求。
### 方法关键点
1. 空间相邻隐态token打散分配到不同数据包，降低单包丢失对局部区域的影响；
2. 双用途Transformer同时实现编码端熵模型参数估计、解码端缺失隐态token重建；
3. 周期性重置的包上下文拓扑，通过段长参数调整压缩效率与错误传播范围的权衡，无需重训；
4. 三阶段渐进训练：先训单帧编码、再学时序上下文熵建模、最后模拟丢包优化掩码隐态的恢复能力。
### 关键结果
采用真实突发丢包轨迹测试，严重丢包场景下重建稳定性优于带RS前向纠错的H.265、GRACE抗丢包学习型编码基线。
