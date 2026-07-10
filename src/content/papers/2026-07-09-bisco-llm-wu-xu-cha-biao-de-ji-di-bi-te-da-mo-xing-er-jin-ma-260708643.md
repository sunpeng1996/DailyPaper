---
title: 'BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language
  Model Compression'
title_zh: BiSCo-LLM：无需查表的极低比特大模型二进制球面编码压缩框架
authors:
- Yuantian Shao
- Peisong Wang
- Zhilei Liu
- Chuangyi Li
- Yuanteng Chen
- Pengcheng Xie
- Yiwu Yao
- Zhihui Wei
- Jian Cheng
affiliations:
- 南京理工大学
- 中国科学院自动化研究所
- 华为
arxiv_id: '2607.08643'
url: https://arxiv.org/abs/2607.08643
pdf_url: https://arxiv.org/pdf/2607.08643
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: 大语言模型 · 极低比特无码表压缩
tags:
- LLM-Compression
- Low-Bit-Quantization
- Codebook-Free
- Binary-Coding
- Post-Training-Optimization
one_liner: 无码表二进制球面编码压缩框架，实现2比特级LLM压缩且精度损失低于现有方案
practical_value: '- 端侧Agent、边端垂域LLM部署可直接复用该压缩框架，2比特级压缩无码表查表开销，内存占用仅为FP16的1/8，精度损失远低于现有同比特量化方案，适合端侧电商导购Agent、离线推荐场景的小模型部署

  - 敏感通道分精度压缩的思路可迁移到所有LLM量化场景，仅筛选1%左右的高敏感通道保留8bit精度，其余通道走低比特压缩，可在几乎不增加存储开销的前提下降低10%以上的量化损失，对推荐场景的用户理解、文案生成小模型优化性价比极高

  - 类别级蒸馏恢复策略可复用在LLM压缩/微调后的精度对齐环节，按Transformer模块类别（注意力、MLP等）替换后统一蒸馏，无需逐层局部优化，可减少30%以上的蒸馏成本，同时避免局部优化导致的全局误差累积'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型尤其是MoE架构参数规模飙升至千亿/万亿级，部署时内存、带宽、存储瓶颈突出，现有低比特压缩方案存在明显缺陷：标量/组量化在2比特以下表达能力不足，向量量化需要存储显式码表、引入查表开销，极致压缩下精度损失大，部署成本高。

### 方法关键点
- 无码表二进制球面编码：将权重块映射到单位超球后二值化，仅存储符号流，无需显式VQ码表，避免查表开销
- 二阶残差BSQ编码：针对基础球面编码的重建误差单独做编码，提升比特利用率，无需盲目扩大单阶段编码长度
- 敏感通道保护：筛选1%左右的激活敏感、大权重通道单独用8bit存储，其余走2bit压缩，大幅降低量化损失
- 类别级恢复蒸馏：按Transformer模块类别（注意力投影、MLP门控/上/下投影等）替换压缩后统一蒸馏，搭配LoRA做精度补偿，避免逐层局部蒸馏的全局误差累积

### 关键实验
在Qwen3-8B上测试，对比GPTQ、AWQ、AQLM、QuIP#等主流低比特压缩方案，2比特压缩下WikiText-2困惑度为10.18，仅比FP16基线9.73高0.45；7项下游任务平均准确率68.05，仅比FP16基线69.92低1.87个百分点，效果优于所有对比基线。

值得记住的一句话：极致低比特LLM压缩的核心不是单纯压低比特宽度，而是通过结构化编码、敏感权重保护、全局对齐的组合，在存储开销和精度损失之间找到最优平衡。
