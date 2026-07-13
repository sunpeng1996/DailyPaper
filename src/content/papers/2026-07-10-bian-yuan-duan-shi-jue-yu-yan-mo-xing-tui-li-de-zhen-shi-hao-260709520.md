---
title: 'Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in
  Edge VLM Inference'
title_zh: 边缘端视觉语言模型推理的真实能耗瓶颈定位与分析
authors:
- Junfei Zhan
- Haoxun Shen
- Mingang Guo
- Zixuan Huang
- Tengjiao He
affiliations:
- University of Pennsylvania
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Jinan University
arxiv_id: '2607.09520'
url: https://arxiv.org/abs/2607.09520
pdf_url: https://arxiv.org/pdf/2607.09520
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 多模态大模型 · 边缘推理能耗优化
tags:
- VLM
- Edge Inference
- Energy Profiling
- Autoregressive Decoding
- On-device AI
one_liner: 通过系统性能耗剖析揭示边缘VLM推理核心能耗瓶颈是输出token长度而非视觉处理
practical_value: '- 端侧多模态Agent（如AR导购、端侧商品识别推荐）优化能效时，优先通过prompt约束+max_tokens硬限制减少输出长度，收益是视觉token剪枝的2~24倍

  - 端侧VLM选型参考：需高分辨率商品图输入时优先选固定token架构VLM（如InternVL3、Gemma-3），避免动态分辨率模型的prefill能耗随分辨率暴涨

  - 端侧应用能耗预算可直接用论文给出的通用线性公式估算，仅需模型大小、输入token数、输出token数3个核心特征，无需单模型额外校准'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有边缘VLM能效优化默认视觉处理是能耗核心，普遍聚焦视觉token剪枝，但端侧VLM的实际能耗分布从未被系统性量化，导致优化方向可能偏离真实瓶颈；而端侧Agent（如实体导购机器人、AR眼镜导购）电池容量有限，能耗是核心运营约束，亟需明确真实能耗来源。

### 方法关键点
- 覆盖3类VLM架构、5个1B~4B参数量模型、4种输入分辨率、2种边缘硬件平台（RTX 3070、Jetson Orin NX）做全维度能耗 profiling
- 拆解VLM推理为prefill、decode两个阶段，分别量化单token能耗成本，建立跨模型通用能耗预测模型
- 推导视觉token剪枝的能耗优化理论上限，对比输出长度控制的实际优化收益

### 关键结果
- 平均推理功率是模型固有属性，与输入分辨率、图像复杂度、prompt类型无关，波动<5%，能耗差异完全来自推理时长差异
- 单输出token能耗是单输入token的11~39倍，decode阶段占总能耗的86%~97%；完全移除所有视觉token最多仅能节省10%能耗，而控制输出长度最多可节省97%能耗
- 图像复杂度通过影响输出长度可带来最高4.1倍的能耗差异，通用能耗预测模型仅用5个特征即可解释98.6%的能耗方差，无需单模型校准

最值得记住的结论：边缘VLM推理的真实能耗瓶颈不是「看到什么」，而是「说多少」，输出侧优化的收益远高于输入侧视觉处理优化
