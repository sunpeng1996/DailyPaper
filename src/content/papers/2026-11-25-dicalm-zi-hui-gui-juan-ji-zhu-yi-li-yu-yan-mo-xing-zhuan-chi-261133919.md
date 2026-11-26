---
title: 'DiCALM: Converting Autoregressive Convolution-Attention Language Models into
  Discrete Diffusion Language Models'
title_zh: DiCALM：自回归卷积-注意力语言模型转离散扩散模型方案
authors:
- Phong Le
- Ngoc-Quan Pham
- Dat Quoc Nguyen
affiliations:
- Qualcomm AI Research
- Qualcomm Vietnam Company Limited
arxiv_id: '2611.33919'
url: https://arxiv.org/abs/2611.33919
pdf_url: https://arxiv.org/pdf/2611.33919
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM推理优化 · 扩散模型转换
tags:
- Discrete Diffusion LLM
- Hybrid LLM
- Inference Acceleration
- Autoregressive Conversion
- On-device LLM
one_liner: 提出LFM2混合架构自回归转离散扩散方案，性能可比原AR模型，平均推理提速超1.4倍
practical_value: '- 可复用混合架构LLM转扩散加速的框架：端侧电商导购、推荐文案生成场景下，采用双向卷积扩展+联合AR-扩散训练的思路，可在精度损失极小的前提下提升推理速度，适配端侧低延迟需求

  - 可直接复用联合AR-扩散训练的loss平衡与warm-up策略：生成式推荐场景下调整解码置信度阈值可灵活控制质量-速度trade-off，高流量场景可适当降低阈值到0.5可获得最高2.18×的推理提速

  - 块级扩散+KV cache兼容的设计：可应用于LLM驱动的推荐Agent实时响应场景，比如实时生成商品推荐理由、导购话术，兼顾低延迟和生成质量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自回归LLM转离散扩散模型的方案多针对全注意力架构，而卷积+注意力混合架构（如LFM2系列）具备更优的端侧推理效率、更低显存占用，但缺乏适配的扩散转换方案，行业需要在精度损失极小的前提下进一步提升混合架构LLM的推理速度，适配端侧生成场景部署需求。
### 方法关键点
- 架构改造：为LFM2的因果门控短卷积新增前向分支，支持双向局部上下文捕获，仅增加少量权重，可灵活切换因果/双向处理模式；GQA层改造成当前块内双向注意力+上文因果注意力，兼容KV cache更新逻辑。
- 训练策略：采用联合AR-扩散训练，动态加权平衡两类任务loss量级，新增边际正则项提升掩码预测置信度，适配阈值解码；GQA注意力掩码逐步预热，稳定训练过程。
- 解码策略：采用阈值解码+PARD策略，每次解码最长左段置信度达标的掩码位置，平衡并行度与生成质量。
### 关键实验结果
基于2M指令微调数据集，以同初始化、同训练数据的LFM2.5 AR微调模型为基线，覆盖350M、1.2B两个参数量级下：
1. 精度：生成类任务精度下降最多不超过1.82个点，多选类任务精度平均提升3~4个点，整体性能与基线相当；
2. 速度：平均推理提速1.42×~1.43×，峰值最高达1.79×；若调低解码置信度阈值到0.5，最高可获2.18×提速，质量-速度trade-off清晰可控。
### 核心结论
混合架构LLM转离散扩散模型可在几乎不损失通用能力的前提下获得稳定推理提速，是端侧低延迟生成场景的高性价比方案
