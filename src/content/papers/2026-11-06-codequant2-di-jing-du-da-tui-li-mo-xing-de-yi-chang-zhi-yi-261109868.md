---
title: 'CodeQuant2: Enhanced Outlier Mitigation and Adaptive Clustering for Low-Precision
  LRMs'
title_zh: CodeQuant2：低精度大推理模型的异常值抑制与自适应聚类框架
authors:
- Xingyu Liu
- Xiangyang Yin
- Tianhua Xia
- Haiyu Wang
- Sai Qian Zhang
affiliations:
- New York University Tandon School of Engineering
- New York University Courant Institute of Mathematical Sciences
arxiv_id: '2611.09868'
url: https://arxiv.org/abs/2611.09868
pdf_url: https://arxiv.org/pdf/2611.09868
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM低精度量化 · 推理模型部署优化
tags:
- Quantization
- Large Reasoning Model
- Low-Precision Inference
- Clustering Quantization
- CUDA Kernel
one_liner: 针对大推理模型低比特量化精度损失问题，提出兼顾精度与效率的聚类量化框架，较BF16最高提速2.85×
practical_value: '- 做推荐/Agent侧LLM推理部署时，可复用「重点校准推理前N步激活」的策略，针对多步导购、商品属性计算等场景大幅降低低比特量化的精度损失

  - 可借鉴自适应聚类分配思路，对大模型不同层权重分配差异化量化位宽，在整体latency预算不变的前提下最大化模型精度，适合边缘端/端侧LLM部署

  - 定制LUT CUDA kernel可直接复用到现有推理框架，无需重建聚类权重即可执行矩阵乘，在L40s/A100等硬件上可获得稳定2x+推理提速'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大推理模型（LRM）依赖长推理链实现数学计算、代码生成、工具调用等复杂任务，但长生成过程显著推高推理成本，低比特量化是核心降本手段。现有量化方法未适配LRM推理阶段的激活特性：前30步解码激活波动比普通生成高20%，早期量化误差会沿推理链累积，导致推理任务精度骤降，现有方案难以兼顾精度与推理效率。

### 方法关键点
- 推理感知校准：校准集混合通用文本与推理任务前256步激活样本，重点匹配早期高波动激活分布，降低早期量化误差
- 微调旋转+缩放变换：联合优化正交旋转矩阵与层级缩放矩阵，平滑激活异常值，降低量化误差
- 自适应聚类分配：根据每层权重对量化的敏感度与推理latency，动态分配8/16/32个聚类中心，在4bit平均位宽约束下平衡精度与效率
- 定制LUT CUDA kernel：直接基于聚类索引与量化激活查表计算，无需重建权重，减少内存开销与计算延迟

### 关键实验
在Qwen3-4B-Thinking、Qwen3-8B、Phi-4-Reasoning三个主流LRM上测试，对比QuaRot、SqueezeLLM、CodeQuant等SOTA量化方案，A4W4设置下Qwen3-4B-Thinking的推理任务平均精度较CodeQuant提升10.6个百分点，推理速度较BF16最高提升2.85×，AIME25 pass@8从0.667提升到0.8。

### 核心结论
大推理模型的量化优化不能只关注通用分布拟合，必须针对性优化推理早期的高波动激活，才能在低比特下保留完整推理能力。
