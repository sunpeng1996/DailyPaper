---
title: Robust Explanatory Analysis for Structured Optimization Networks (REASON) in
  Learning
title_zh: 面向学习场景的结构化优化网络鲁棒解释性分析框架REASON
authors:
- Vahid Jebraeeli
- Hamid Krim
- Keisuke Fujii
affiliations:
- North Carolina State University
- Nagoya University
arxiv_id: '2610.19378'
url: https://arxiv.org/abs/2610.19378
pdf_url: https://arxiv.org/pdf/2610.19378
published: '2026-10-13'
collected: '2026-10-20'
category: Reasoning
direction: 双系统认知 · 自适应推理优化
tags:
- System1-System2
- Adaptive Computation
- Distribution Shift
- Epistemic Uncertainty
- Two-loop Model
one_liner: 受双系统认知启发提出嵌套双循环推理框架，在分布偏移下兼顾性能与计算效率
practical_value: '- 推荐/搜索排序场景可复用双循环架构：常规请求走快循环做浅层推理，残差超阈值时触发慢循环调用LLM/补全复杂特征，兼顾吞吐与准确率

  - 大促、新客冷启动等分布偏移场景下，可基于认知残差判断是否需要主动拉取额外特征（如用户实时行为、商品上下文），降低无效计算

  - 线上推理集群资源调度可参考该框架逻辑，仅对高不确定性请求分配高计算资源，提升集群整体资源利用率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有ML推理多为关联式，泛化性不足，在分布偏移、数据扰动场景下性能退化明显，缺少自适应的推理资源调度机制。
### 方法关键点
受System1/System2认知范式启发，设计嵌套双循环推理架构：
1. 类System1快循环：基于现有证据快速推理，消解可处理残差；
2. 若剩余认知残差超过阈值，触发类System2中速循环，主动获取额外证据，通过残差下降幅度衡量新信息价值；理论证明中速循环最优解不劣于快循环。
### 关键结果
双循环模型性能始终优于单独快循环，计算量仅为单独中速循环的1/2；同等计算成本下，效果超过staged分类器和learning-to-defer方法，未见扰动场景下仍保持性能优势。
