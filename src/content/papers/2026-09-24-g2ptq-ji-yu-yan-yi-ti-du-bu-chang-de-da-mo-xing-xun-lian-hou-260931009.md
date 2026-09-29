---
title: 'G^2PTQ: Improving LLM Post-Training Quantization with Generalized Gradient
  Compensation'
title_zh: G²PTQ：基于广义梯度补偿的大模型训练后量化优化
authors:
- Ruikang Liu
- Haoli Bai
- Yuxuan Sun
- Qian Zhang
- Wenzheng Cai
- Yanqi Hao
- Feiyu Wang
- Weidong Zhong
- Zhuang Wang
- Tong Yang
affiliations:
- ZTE Corporation
- The Chinese University of Hong Kong
- Northwestern Polytechnical University
- Peking University
- Nanjing University of Aeronautics and Astronautics
arxiv_id: '2609.31009'
url: https://arxiv.org/abs/2609.31009
pdf_url: https://arxiv.org/pdf/2609.31009
published: '2026-09-24'
collected: '2026-09-29'
category: LLM
direction: 大模型压缩 · 训练后量化(PTQ)
tags:
- PTQ
- LLM Quantization
- GPTQ
- Gradient Compensation
- Model Compression
one_liner: 结合一阶二阶信息与块级全局监督，实现精度优于SOTA的低开销LLM训练后量化方案
practical_value: '- 业务侧LLM服务（智能导购、推荐文案生成、Agent推理等）可直接复用G2PTQ做3bit/4bit量化，推理时延下降的同时精度损失远小于传统GPTQ，8B模型仅需12.54GB显存即可完成量化，适配端侧、边缘侧LLM部署需求

  - 量化优化思路可迁移：块级监督+单块反向传播刷新梯度/Hessian的设计，比固定全局Hessian的方案精度更高，同时比全量反向传播成本低70%以上，可复用到业务垂类小模型的量化流程

  - 信任域缩放机制解决了一阶梯度补偿的权重爆炸问题，无需额外标注数据做量化感知训练（QAT）即可稳定低比特量化效果，适合业务侧标注资源不足的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前GPTQ类训练后量化（PTQ）是LLM部署的核心压缩手段，但现有方案存在两类互补缺陷：层级局部优化缺乏全局监督易陷入局部最优，全局优化方案又固定初始Hessian估计、忽略一阶梯度，随量化推进指导信号逐渐失效，导致低比特（2bit/3bit）量化精度损失过大，无法满足业务侧LLM服务的效果要求。
### 方法关键点
- 采用块级优化目标：中间Transformer块优化量化前后输出MSE，最后一个块优化输出分布KL散度，兼顾计算效率与全局监督
- 每个块量化前单独执行反向传播，刷新梯度与Hessian估计，避免固定Hessian的过时问题，计算复杂度与原生GPTQ持平
- 引入信任域缩放机制动态限制一阶梯度补偿步长，解决了直接使用精确一阶梯度导致的权重更新爆炸问题，量化过程无需微调
- 实现了块级Hessian近似、梯度补偿的高效算子，支持稠密模型与MoE模型量化
### 关键实验
覆盖0.6B~125B共15款稠密/MoE模型，对比GPTQ、GuidedQuant、GPTAQ等SOTA基线：W2A16量化下平均QA准确率比GPTAQ高6.45%，W4A16量化下LLaMA3-70B QA准确率比GPTAQ高4.56%；8B模型量化仅需2.24小时、12.54GB单卡显存，部署门槛极低。
### 核心结论
低比特LLM量化的精度收益，核心来自于更贴近真实量化状态的动态监督信号，而非固定的全局先验。
