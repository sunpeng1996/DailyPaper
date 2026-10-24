---
title: 'RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting'
title_zh: RLSplat：面向前馈3D高斯泼溅的资源线性预算控制框架
authors:
- Injae Kim
- Minseok Joo
- Jihwan Park
- Sehyung Kim
- Minseong Bae
- Hyunwoo J. Kim
affiliations:
- KAIST
- Korea University
arxiv_id: '2610.27712'
url: https://arxiv.org/abs/2610.27712
pdf_url: https://arxiv.org/pdf/2610.27712
published: '2026-10-19'
collected: '2026-10-24'
category: Other
direction: 3D场景重建 · 高效推理资源控制
tags:
- 3DGS
- Resource Control
- Efficient Inference
- Novel View Synthesis
- Budget Allocation
one_liner: 实现资源线性可控的前馈3D高斯泼溅框架，低预算下性能、速度、显存均大幅优于基线
practical_value: '- 资源线性调度的思路可迁移到多算力环境下的LLM推理/生成式推荐服务，按请求优先级动态分配计算预算，实现成本与效果的线性tradeoff

  - 放弃「先全量生成再剪枝」的低效逻辑，改用按粒度直接按需分配预算的策略，可复用到推荐候选生成/Query改写场景，低峰时段直接减少生成量降本

  - 仅关联局部近邻元素做注意力优化的思路，可优化LLM长上下文推理的KV cache占用，降低搜推场景下长尾用户长会话请求的延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有可控预算的前馈3D高斯泼溅（FF3DGS）方法采用先稠密预测再剪枝的逻辑，推理 latency 和峰值显存几乎不随目标高斯数降低而减少，未实现真实的资源可控，无法适配AR/VR、边缘设备等资源受限场景。

### 方法关键点
1. 学习高斯分配策略，直接按局部场景区域分配预算，精确生成请求数量的高斯，避免全量预测的冗余开销；
2. 采用资源线性的高斯解码机制，仅通过高效层级近邻搜索关联局部高斯做注意力优化，解码成本随高斯数线性下降。

### 关键结果数字
零样本评估下全预算区间性能优于现有基线，高斯数减少4倍时仍超过最强基线；低预算下推理速度最高提升4.1倍，峰值显存最高降低9.6倍。
