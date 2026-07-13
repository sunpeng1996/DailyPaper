---
title: 'KronQ: LLM Quantization via Kronecker-Factored Hessian'
title_zh: KronQ：基于克罗内克分解海森的大语言模型后训练量化方法
authors:
- Donghyun Lee
- Yuhang Li
- Ruokai Yin
- Priyadarshini Panda
affiliations:
- University of Southern California
- Yale University
arxiv_id: '2607.07964'
url: https://arxiv.org/abs/2607.07964
pdf_url: https://arxiv.org/pdf/2607.07964
published: '2026-07-07'
collected: '2026-07-13'
category: LLM
direction: 大语言模型 · 后训练量化优化
tags:
- Post-Training Quantization
- Kronecker Factorization
- Low-bit LLM
- Hessian Approximation
- Efficient Inference
one_liner: 引入梯度协方差优化后训练量化，2bit量化LLaMA-3-70B时效果远超基线
practical_value: '- 低比特量化降本：业务中用LLM做生成式推荐文案、Agent推理、query改写的场景，可直接用KronQ做2bit/3bit量化，70B级大模型可压缩至单张A100部署，解码延迟降低20%-60%，推理成本大幅下降

  - 混合精度分配trick：原有量化流程中的混合精度策略可替换为tr(HG)*tr(HX)敏感度打分，能精准区分Q/K/V等共享输入子层的量化优先级，相同平均比特下精度提升显著

  - 工程落地兼容性：KronQ的双向非相干处理逻辑可无缝嵌入现有GPTQ/GPTAQ生产量化栈，仅需额外增加1次校准集反向传播计算梯度协方差，推理侧无额外overhead，落地成本极低

  - 稳定性优化：超低比特（2bit）量化场景下，KronQ可避免GPTQ/GPTAQ易发散的问题，适合端侧/边缘设备部署的轻量化推荐Agent场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有二阶后训练量化（PTQ）方法（如GPTQ）仅基于输入激活协方差构建优化目标，默认所有输出通道对量化损失的贡献一致，忽略了输出侧梯度的异质性，在2bit等超低比特场景下精度暴跌甚至完全发散，无法满足大模型落地的内存和延迟要求。

### 方法关键点
- 基于克罗内克分解海森（K-FAC）近似，将量化损失优化目标扩展为同时耦合输入激活协方差$H_X$和输出梯度协方差$H_G$，且$H_G$在权重补偿更新时会代数抵消，完全保留原有量化框架的计算效率
- 提出双向非相干处理（BiIP）：同时对输入、输出维度做随机Hadamard旋转和对角缩放，降低权重在两个维度的幅值方差，抑制量化误差
- 提出新的子层敏感度指标$\text{tr}(H_G) \cdot \text{tr}(H_X)$，解决Q/K/V等共享输入的子层无法区分量化优先级的问题，实现更优的层间混合精度分配

### 关键结果
在LLaMA-2/3、Gemma-3、DeepSeek-R1等主流大模型上验证，对比GPTQ、GPTAQ、AWQ、OmniQuant等SOTA基线：
- LLaMA-3-70B 2bit权重量化场景下，GPTQ/GPTAQ完全发散（WikiText-2 PPL>2000），KronQ PPL仅为7.93
- 2bit组量化（g=128）下，LLaMA-2-7B的GPTQ PPL达274，KronQ仅为7.61
- 量化后模型峰值VRAM比bf16降低3.5-7.5倍，解码延迟提升1.25-2.51倍，70B模型4bit量化可单张A100部署

### 核心结论
仅需在校准阶段额外计算一次梯度协方差，就能在几乎不增加推理开销的前提下，大幅提升超低比特LLM量化的精度和稳定性
