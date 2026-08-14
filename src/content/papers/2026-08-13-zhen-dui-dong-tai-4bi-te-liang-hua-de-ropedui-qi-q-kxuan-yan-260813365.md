---
title: 'When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for
  Dynamic 4-Bit Quantisation'
title_zh: 针对动态4比特量化的RoPE对齐Q/K旋转性能研究
authors:
- Shuhan Wang
- Yilin Luo
- Nan Xu
- Chi Wang Cheung
affiliations:
- University College London (UCL)
arxiv_id: '2608.13365'
url: https://arxiv.org/abs/2608.13365
pdf_url: https://arxiv.org/pdf/2608.13365
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM低比特量化 · RoPE优化
tags:
- LLM Quantization
- RoPE
- 4-bit Quantization
- Dynamic Quantization
- KV Cache
one_liner: 证明头共享RoPE对齐成对旋转在动态W4A4KV4量化下性能弱于全头Hadamard变换，明确混合支持度与量化误差的关联
practical_value: '- 业务侧部署低比特LLM做推荐/Agent推理时，优先选择全头Hadamard变换做Q/K旋转，不要盲目使用RoPE对齐的成对旋转，避免PPL升高导致生成内容/推荐结果质量下降

  - 做动态W4A4KV4量化的角度估计时，优先从K流单独统计特征，相比Q/K混合统计可降低0.1~0.5PPL的性能损失

  - 低比特KV cache优化时，优先保证混合支持度≥64，可同时降低K值范围、量化误差和推理PPL，适配电商/推荐场景的长上下文用户行为序列处理需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
低比特训练后量化是LLM落地部署的核心降本技术，旋转类量化方法通过正交变换重分布激活离群点降低量化误差，而RoPE将注意力头天然划分为二维频率对，此前学界不清楚基于RoPE成对结构设计的变换是否优于全头混合变换，同时局部方差最优的变换是否能真正降低端到端量化误差也有待验证，直接关系到低比特LLM部署的性能与成本平衡。

### 方法关键点
- 理论证明：当RoPE频率互异时，与RoPE可交换的单头正交变换只能是各频率对内部的独立平面旋转，排除了其他单头可交换映射的可能
- 闭式解推导：针对头共享参数化设置，推导得到最小化池化协方差、位置平均代理目标下的最优旋转角闭式解，可实现局部方差最优
- 对照实验设计：设置三组对照变换：全头Hadamard变换（基线）、仅成对RoPE对齐旋转、成对旋转+Hadamard组合变换，在动态W4A4KV4量化下对比性能

### 关键实验
在Llama-3.2-1B/3B、Llama-3.1-8B、Mistral-7B-v0.3四个 checkpoint上测试，短上下文基于WikiText-2，长上下文覆盖Proof-Pile、PG19到128K长度。结果：仅成对旋转相比全头Hadamard基线PPL升高0.05~1.33，K流单独统计角度可降低0.1~0.5PPL的损失但仍高于基线；混合支持度从2提升到128时，K范围、相对量化误差、PPL损失均单调下降，当支持度≥64时PPL差距可控制在±0.05以内。

### 核心结论
结构对齐本身不能决定旋转变换是否降低量化误差，结构化变换的优化目标和混合支持度必须与量化器的尺度设置规则匹配才能提升性能
