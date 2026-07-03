---
title: Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning
title_zh: 基于非对称互变分学习的多模态连续推理方法
authors:
- Shijie Li
- Yilin Gao
- Siyuan Yang
- Tieyuan Chen
- Chaofan Gan
- Zhihao He
- Zicheng Zhao
- Yuyu Guo
- Weiyao Lin
- Hang Yu
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2607.00461'
url: https://arxiv.org/abs/2607.00461
pdf_url: https://arxiv.org/pdf/2607.00461
published: '2026-06-30'
collected: '2026-07-03'
category: Reasoning
direction: 多模态大模型 · 连续潜推理
tags:
- Multimodal LLM
- Continuous Reasoning
- Variational Learning
- KL Divergence
- Train-Inference Alignment
one_liner: 提出非对称互变分学习框架解决多模态潜推理的训练推理不匹配问题，大幅提升多模态推理性能
practical_value: '- 搭建LLM/多模态Agent的潜推理模块时，可直接复用AMVL的双向KL校准思路：正向KL对齐推理先验与训练后验，反向KL正则后验避免答案泄露，无需手工设计潜变量监督信号即可解决训练推理不匹配问题

  - 电商多模态场景（商品图文理解、穿搭推荐推理、商品问答等）要规避离散CoT的语言空间瓶颈时，可参考论文最优配置插入8个d=512的连续latent占位符，加轻量变分头实现连续推理，比离散CoT精度更高、幻觉更少

  - 变分训练可复用非对称KL调度策略：先预热正向KL权重，延迟引入且设置更小的反向KL权重，避免早期先验能力不足导致的过正则，训练稳定性更好'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多模态大模型（MLLM）的离散Chain-of-Thought（CoT）推理存在天然语言空间瓶颈，强制高维连续视觉信号映射到离散词表会丢失细粒度感知信息，易引发推理漂移、幻觉问题。变分连续潜推理虽能绕过该瓶颈，但其训练时后验可访问真实答案，存在严重答案泄露问题：传统ELBO单目标训练会让推理阶段使用的目标无关先验继承后验的答案依赖偏差，造成训练推理不匹配，推理性能骤降。
### 方法关键点
- 提出非对称互变分学习（AMVL）框架，通过双向KL目标双向校准先验与后验：正向KL采用stop-gradient固定后验，训练推理用的目标无关先验匹配后验分布；反向KL采用stop-gradient固定先验，正则训练用的目标感知后验不偏离先验高密区域，从两端缩小分布gap，缓解答案泄露。
- 架构改造极轻量化：仅需在MLLM输入序列与答案之间插入k个<latent>占位符，加轻量变分头分别基于输入（推理）、输入+答案（训练）生成对角高斯先验/后验分布，重参数化采样后替换占位符嵌入用于解码。
- 训练采用非对称KL调度：先预热正向KL权重，延迟引入反向KL且设置更低权重，避免早期先验能力不足导致的过正则。
### 关键结果
基于Qwen2.5-VL-7B实现，在V*、HRBench4K/8K细粒度视觉感知基准上平均得分74.97，较基线提升+5.57；在BLINK复杂视觉推理基准上平均提升+10.83，其中Jigsaw拓扑推理任务提升达+32.00，优于所有离散CoT和现有连续潜推理基线。
> 最值得记住：变分连续潜推理的核心瓶颈是答案泄露导致的训练推理不匹配，双向非对称KL校准可在无手工潜变量监督的前提下，同时兼顾潜空间的训练表达性和推理可用性。
