---
title: 'PACT: Certifying What Is Written in Parallel Decoding of Diffusion Language
  Models'
title_zh: PACT：扩散语言模型并行解码的生成内容校验方法
authors:
- Yanchao Li
- Yusu Zhang
- Jiaqing Xie
- Yi Ban
- Ben Gao
- Zhongyu Huang
- Tianfan Fu
- Yuqiang Li
affiliations:
- Nanjing University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2611.04152'
url: https://arxiv.org/abs/2611.04152
pdf_url: https://arxiv.org/pdf/2611.04152
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: 扩散大语言模型 · 并行解码加速
tags:
- Diffusion LLM
- Parallel Decoding
- Training-free
- Inference Optimization
- Sampling
one_liner: 训练免的扩散语言模型并行解码提交规则，先采样token再校验，兼顾解码速度与生成质量
practical_value: '- 电商场景用扩散LLM生成商品文案、营销话术时，可直接复用PACT先采样再校验+位置间隔的trick，相同生成质量下降低推理成本

  - Agent调用扩散LLM做多轮推理时，可通过PACT的阈值τ灵活调整速度-质量平衡，低延迟场景调低τ，高准确率场景调高τ

  - 扩散LLM做推荐理由、商品标题生成时，PACT的位置间隔策略可大幅降低重复词、语序错误概率，减少后处理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有扩散语言模型并行解码的commit规则仅基于预测分布选择要填充的token位置，未考虑实际采样token的可靠性，采样温度升高时生成质量骤降，还容易出现相邻重复词等错误，解码速度和质量的平衡不佳。

### 方法关键点
- 核心设计PACT，完全训练免，仅修改解码阶段的commit规则，无额外前向传播开销
- 先采样得到每个掩码位置的token，按采样token的对数概率排序，选择最长前缀满足总对数概率≥logτ，保证提交token集的可靠性
- 新增位置间隔策略，同一步提交的token位置至少间隔g（默认8），降低同一步提交token间的依赖，减少联合概率偏差
- 理论证明相同可靠性约束下，PACT是提交token数最多的规则，在任意采样温度下校验都生效

### 关键实验
在LLaDA-8B、LLaDA-MoE、Dream-7B等4个扩散模型上测试，覆盖HumanEval、MBPP、GSM8K等5个基准，对比Fast-dLLM、EB-Sampler等5个SOTA解码规则：相同质量下PACT比现有SOTA最多提速12倍，平均提速2-5倍；相同速度下现有规则的重复词率最高达52%，PACT仅为0.9%；采样温度升高到1.0时，基于top选择的规则准确率损失达90%以上，PACT仅损失不到2%。

### 最值得记住的一句话
扩散语言模型并行解码的速度提升不能只看每步提交的token数量，更要保证提交的实际采样token的可靠性。
