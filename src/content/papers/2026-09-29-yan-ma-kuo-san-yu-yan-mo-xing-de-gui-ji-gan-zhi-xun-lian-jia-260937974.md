---
title: On Trajectory-Aware Training for Masked Diffusion Language Models
title_zh: 掩码扩散语言模型的轨迹感知训练框架PUMBA
authors:
- Manuel Madeira
- Amitis Shidani
- Alice Bizeul
- Victor Turrisi
- Louis Béthune
- Bhavika Devnani
- Dan Busbridge
- Pierre Ablin
- João Monteiro
affiliations:
- Apple
- EPFL
- Georgia Institute of Technology
arxiv_id: '2609.37974'
url: https://arxiv.org/abs/2609.37974
pdf_url: https://arxiv.org/pdf/2609.37974
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: 掩码扩散LLM · 训练推理对齐优化
tags:
- Masked Diffusion Language Model
- Train-Inference Alignment
- BPTT
- SFT
- NFEs Optimization
one_liner: 提出统一轨迹感知训练框架PUMBA，弥合掩码扩散LLM训练推理gap，降低推理步数
practical_value: '- 生成式推荐MDM落地可复用PUMBA的渐进式掩码训练思路，适当调大训练时每步揭示token数规避局部过拟合，无需强行完全对齐训练推理掩码分布即可获得收益

  - 长文案生成、多轮Agent推理等多步生成任务可复用跨步骤连续隐状态传递+截断BPTT的设计，效果优于离散梯度估计器，同时可降低推理函数调用次数

  - LLM SFT优化可在标准SFT后加入短周期PUMBA Post-SFT训练，无需翻倍训练时长即可获得2+的效果提升，同时降低推理NFEs达22%~26%，性价比极高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
掩码扩散语言模型（MDM）训练时采用随机掩码，推理时采用模型预测引导的渐进式揭字轨迹，二者存在掩码分布差异、跨步骤信息无法复用两大核心gap，现有优化方案零散未形成统一框架，无法最大化训练效率与推理性能的平衡。

### 方法关键点
- 提出PUMBA统一框架，覆盖轨迹感知训练三个核心轴：推理策略诱导的训练轨迹构造、跨步骤连续隐状态（carry）传递、跨W步的截断BPTT联合优化
- 针对小u（每步揭字数量）训练时的局部过拟合问题，采用训练时u大于推理时u的宽松对齐方案，既降低掩码分布差异又避免过拟合
- 用连续隐状态传递替代离散梯度估计器，梯度仅在W步窗口内回传，平衡训练开销与优化效果

### 关键实验
- 可控实验用125M Transformer在TinyGSM训练，GSM8K零样本评估，W=8时精度达55.6%，追平同规模AR模型效果
- 8B LLaDA SFT场景下，仅用4000步Post-SFT训练，效果提升是标准SFT翻倍时长的3倍；相同性能下，全画布生成NFEs降低22%，块扩散生成NFEs降低26%

最值得记住的一句话：掩码扩散模型训练无需追求与推理的完全对齐，平衡轨迹对齐度与训练样本多样性才能获得最优的性能-推理效率tradeoff
