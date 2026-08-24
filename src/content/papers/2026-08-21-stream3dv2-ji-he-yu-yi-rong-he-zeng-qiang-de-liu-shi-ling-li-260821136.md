---
title: 'Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene
  Understanding'
title_zh: Stream3Dv2：几何语义融合增强的流式零样本3D场景理解
authors:
- Jie Xu
- Na Zhao
arxiv_id: '2608.21136'
url: https://arxiv.org/abs/2608.21136
pdf_url: https://arxiv.org/pdf/2608.21136
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent 具身3D场景感知能力增强
tags:
- Zero-Shot
- 3D Perception
- Geometric-Semantic Fusion
- LLM Agent
- Streaming Perception
one_liner: 提出免训练几何语义融合流式3D感知框架，可对接LLM Agent实现语言驱动场景理解
practical_value: '- 做电商AR导购、仓储具身巡检Agent的场景感知模块时，可复用几何-语义融合机制降低3D感知噪声，提升流式输入处理效率

  - 需对接3D场景输入的LLM Agent可直接集成该免训练框架，快速实现语言驱动的3D场景理解能力，减少训练成本

  - 多模态语义融合的流式处理架构可迁移到实时AR商品推荐的场景感知链路，优化多视角一致性对齐效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有开集零样本3D场景理解方案无法高效处理流式RGB-D输入，且对带噪2D分割掩码鲁棒性差，难以落地真实场景。

### 方法关键点
1. 采用免训练架构，通过嵌套局部-历史结构处理序列数据，兼顾多视角一致性与低计算开销，支持实时响应；
2. 核心为几何-语义融合机制，通过显式语义引导、将3D分割建模为点集合并/划分问题，解决几何噪声与语义歧义；
3. 提出流形距离点云优化策略，用局部流形图优化边界识别效果，通过几何包围盒动态更新历史实例，实现快速迭代优化。

### 关键结果
在公开数据集上开集流式3D分割、检测性能稳定超过现有基线，对接LLM Agent可实现语言驱动的3D场景理解，适配开放世界具身智能需求。
