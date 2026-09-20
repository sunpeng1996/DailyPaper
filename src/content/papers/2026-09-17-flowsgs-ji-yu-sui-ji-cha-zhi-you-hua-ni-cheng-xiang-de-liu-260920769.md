---
title: 'FlowSGS: Improving Flow Matching Priors for Inverse Imaging with Stochastic
  Interpolants'
title_zh: FlowSGS：基于随机插值优化逆成像的流匹配先验
authors:
- Tianao Li
- Xinhui Qian
- Emma Alexander
affiliations:
- Northwestern University Department of Computer Science
- Northwestern University Department of Statistics and Data Science
- NSF-Simons AI Institute for the Sky (SkAI)
arxiv_id: '2609.20769'
url: https://arxiv.org/abs/2609.20769
pdf_url: https://arxiv.org/pdf/2609.20769
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 流匹配生成模型 · 逆问题采样优化
tags:
- Flow Matching
- Stochastic Interpolants
- Posterior Sampling
- Generative Model
- Inverse Imaging
one_liner: 提出拆分吉布斯采样的流后验采样方法FlowSGS，首次实现流基逆求解器适配非线性问题
practical_value: '- 拆分吉布斯采样分解后验为似然+先验步的思路，可迁移到GenRec多约束生成场景，同时满足用户兴趣先验与业务规则约束

  - 随机插值框架集成预训练流模型的方法，可复用在生成式推荐任务中降低大模型推理的网络调用开销

  - 反向SDE时间步校正技术的设计思路，可参考优化流匹配类GenRec的采样效率，减少KV cache占用'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有流基逆求解器默认依赖线性前向模型假设，后验采样存在简化近似误差，且推理阶段网络评估次数多、效率低，无法适配非线性逆问题场景。
### 方法关键点
1. 基于Split Gibbs Sampling将后验采样拆分为似然步、先验步两个独立步骤：似然步采用朗之万动力学采样，先验步通过Stochastic Interpolants框架集成预训练流模型，基于SI反向SDE实现采样
2. 结合流先验的直概率路径特性，提出反向SDE时间步校正技术，大幅降低先验步的网络评估次数
### 关键结果
在多类逆成像任务上取得SOTA性能，首次实现流基逆求解器在非线性逆问题（傅里叶相位恢复）上的有效验证，先验步网络评估次数远低于即插即用扩散采样器
