---
title: Hardware-Aware FP4 FlashAttention-4
title_zh: 面向Blackwell GPU的硬件感知FP4 FlashAttention-4优化
authors:
- Robert Hu
affiliations:
- Graphcore Research
arxiv_id: '2609.04105'
url: https://arxiv.org/abs/2609.04105
pdf_url: https://arxiv.org/pdf/2609.04105
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 大模型训练推理 · FP4低精度算子优化
tags:
- FlashAttention
- FP4 Quantization
- Blackwell GPU
- Transformer Training
- Low Precision Inference
one_liner: 针对Blackwell GPU的FP4 attention瓶颈，提出Direct-P实现2.13倍BF16前向吞吐，训练提速1.14倍
practical_value: '- 推荐/Agent场景部署大模型推理时，可复用Direct-P的FP4概率量化思路，在可接受精度损失下大幅提升GB200/B300的attention吞吐，降低服务成本

  - 训练电商场景大尺寸推荐Transformer（如长序列用户建模、多模态召回模型）时，可采用前向量化状态直接回传的设计，配合FP8梯度operand，无收敛损失前提下单卡训练提速14%

  - 低精度量化选型可直接复用论文结论：推理用MXFP4作为P/V operand可获最高速度，训练必须改用FP8 P/V避免发散，无需额外做ablation验证'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
NVIDIA Blackwell系列GPU的FP4张量核心理论算力远高于BF16，但attention算子中softmax转换、片上依赖等中间环节成为瓶颈，无法发挥FP4的算力优势，现有FP4 FlashAttention实现未能解决临界路径延迟与概率值量化范围的矛盾，亟需硬件感知的针对性优化。

### 方法关键点
- 提出Direct-P方法，将归一化后的attention分数直接映射为MXFP4格式的E2M1概率编码，省去冗余的指数计算与精度转换步骤，缩短前向临界路径
- 采用与PV矩阵乘法完全一致的量化值计算归一化分母，避免数值偏差；仅对极端logit层增加轻量采样guard，无需全局扫描
- 训练阶段将前向量化得到的Q/K、缩放因子、softmax归一化值直接传入反向传播，复用低精度状态重构概率，梯度采用FP8 operand，避免额外的BF16分数路径开销

### 关键结果
- 非因果前向推理：在NVIDIA GB200上对比BF16版FlashAttention-4，Direct-P最快达到2.13倍吞吐，几何平均加速2.02倍，ViT/BERT等任务下精度损失极小，与BF16预测一致性超过95%
- 训练场景：单GB200上8B参数Llama模型完整更新步最高加速1.14倍，FP8 P/V配置可稳定完成100B token预训练，MXFP4 P/V配置会出现训练发散

**最值得记住的一句话**：FP4低精度优化不能只关注矩阵乘法加速，必须针对硬件架构解决算子中间环节的临界路径瓶颈，训练场景下盲目追求全FP4会引发收敛性问题，FP8是当前更稳妥的概率/值operand选型
