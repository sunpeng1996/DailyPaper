---
title: Graphical Design of Interpretable Architectures
title_zh: 可解释AI架构的图形化设计方法
authors:
- Pietro Barbiero
affiliations:
- IBM Research, Zurich
arxiv_id: '2608.18936'
url: https://arxiv.org/abs/2608.18936
pdf_url: https://arxiv.org/pdf/2608.18936
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: 可解释AI · 架构图形化表示
tags:
- Interpretability
- Tensor Notation
- PyTorch
- Einsum
- Architecture Design
one_liner: 提出适配Penrose张量记法的可解释AI架构图形表示，可1:1映射为PyTorch einsum代码
practical_value: '- 设计可解释召回/排序模型时，可用该图形记法梳理张量操作逻辑，降低跨团队架构沟通成本

  - 自研业务侧可解释LLM/推荐模型时，可参考1:1映射einsum代码的思路，把架构设计直接转化为可运行代码，减少实现误差

  - 分析黑盒预测异常时，可借鉴该方法拆解张量操作节点，快速定位逻辑问题，提升问题排查效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有可解释架构的表示方法存在两类缺陷：符号方程无法快速获取架构全局视图，概率图模型/流程图不描述实际张量操作，隐藏关键实现细节、降低复现性。

### 方法关键点
1. 基于Penrose张量记法适配设计可解释AI架构的图形表示，既提供架构全局视图，又可1:1映射为PyTorch einsum代码
2. 覆盖概念瓶颈、稀疏探针、原型网络、神经加性模型、线性模型混合等多种原生可解释架构的表示
3. 针对前沿可解释LLM Steerling-8B做核心架构组件可视化

### 关键结果数字
Steerling-8B的可视化直接揭示其残差架构属性，每个操作可对应明确几何解释，且能直接翻译成仅33行的PyTorch可运行代码
