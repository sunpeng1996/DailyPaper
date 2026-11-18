---
title: 'TempQuant: Learning Adaptive Temperatures for Quantized Language Models'
title_zh: TempQuant：为量化大语言模型学习自适应温度参数
authors:
- Mukund Athmaram
- Liang Ma
- Manoj Rao
affiliations:
- AMD
- Cornell University
arxiv_id: '2611.22128'
url: https://arxiv.org/abs/2611.22128
pdf_url: https://arxiv.org/pdf/2611.22128
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大语言模型量化 · 解码参数自适应优化
tags:
- Quantization
- Temperature Scaling
- LLM Decoding
- LLM Compression
- Knowledge Distillation
one_liner: 无标注调整量化LLM的采样温度与top-p，无需重训即可大幅恢复精度损失
practical_value: '- 业务部署低比特量化LLM时，不要直接复用全精度模型的温度和top-p参数，可先用全局TempQuant的网格搜索方案找最优参数，零部署成本就能提升推理准确率

  - 对于3比特等低比特量化模型容易出现的重复生成、推理崩溃问题，优先选择forward KL作为优化目标调整温度，可大幅降低重复率、恢复推理精度

  - 做生成式推荐/Agent回复的低延迟部署时，若用轻量量化模型，可根据业务场景选优化目标：长推理场景选forward KL，短文本生成选reverse KL，轻量化场景选JSD'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前量化LLM部署普遍直接复用全精度模型的采样温度、top-p参数，而量化会扭曲下一词概率分布，导致推理精度下降、重复生成等问题，传统重训量化权重成本高，调整解码参数的优化方案缺乏系统性研究。

### 方法关键点
- 分两个粒度优化解码参数：全局TempQuant针对每个请求温度，网格搜索温度+top-p组合最小化与全精度模型的分布散度，零部署开销；逐步TempQuant通过两个轻量MLP头，基于量化logit的42维特征（32个最大logit+10个分布统计量）实时预测每步的温度修正系数和top-p，仅训练小头部无需改动LLM权重
- 针对两类量化误差设计优化目标：排序保留的token适合降温缩小分布偏差，排序翻转的token适合升温提升正确token概率，可选择forward KL（优先修复翻转token）、reverse KL（优先修复保留token）、JSD（平衡两者）三类散度作为损失

### 关键实验
在3比特GPTQ量化的Qwen3-4B上测试，MATH数据集上全局TempQuant对比官方推荐配置，准确率从34%提升到51%；逐步TempQuant在τ=1.0场景下精度超过全局方案，同时降低与全精度模型的行为差异；4比特MXFP4轻量量化场景下，JSD优化的TempQuant可降低1/3与全精度模型的答案不一致率，精度几乎无损失。

### 核心结论
量化LLM的最优解码参数与全精度模型存在显著差异，仅调整温度和top-p即可恢复大部分量化损失，无需额外重训成本
