---
title: 'Complete-SVD: A Functional Norm Approach to Low-Rank LLM Compression'
title_zh: Complete-SVD：基于泛函范数的大语言模型低秩压缩方法
authors:
- Alper Kalle
- Theo Rudkiewicz
- Mohamed-Oumar Ouerfelli
- Mohamed Tamaazousti
affiliations:
- Université Paris-Saclay
- CEA
- Inria
- CNRS
- LISN
arxiv_id: '2611.26059'
url: https://arxiv.org/abs/2611.26059
pdf_url: https://arxiv.org/pdf/2611.26059
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM低秩压缩 · 训练后无微调优化
tags:
- LLM Compression
- Low-Rank Factorization
- SVD
- Post-Training Optimization
- Kronecker Factorization
- Model Quantization
one_liner: 提出基于泛函范数的LLM低秩压缩方法，跨语料泛化性优于现有SVD类方案
practical_value: '- 部署垂域LLM（比如电商客服Agent、推荐文案生成模型）时，若业务涉及分布外query/物品，优先选用Complete-SVD压缩，跨域perplexity比现有SVD方案最高降44%，无需额外微调

  - 若模型仅在固定垂域使用，更看重零样本任务准确率，可选用同框架下的KL-SVD变体，校准集内效果优于Complete-SVD，适配封闭业务场景

  - Complete-SVD可与GPTQ量化组合使用，7B级模型可压缩至2GB以内，适合端侧推荐、端侧Agent等内存受限场景部署，推理效率提升显著

  - 可将加权SVD的思路迁移到推荐系统Embedding压缩场景：同时引入上游输入激活协方差、下游任务梯度信息做加权，降低Embedding低秩压缩后的排序掉点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM低秩压缩方法要么仅拟合权重Frobenius范数，要么仅优化校准集内观测token损失或预测分布，过度拟合校准域，在分布外数据上效果骤降；同时大词汇量下输出侧Jacobian矩阵计算成本与词汇量、序列长度正相关，落地门槛高。

### 方法关键点
- 核心优化目标为原始模型与压缩模型logits的L2距离，对所有logit变化均等加权，避免过度拟合校准集分布
- 基于Kronecker-factored近似将目标转化为加权SVD闭解，同时引入输入激活协方差Σ_input、logit Jacobian Gram矩阵Σ_grad做加权
- 提出无偏估计方法：先通过LM头分解将词汇维降至隐藏维，再用随机探针做广播反向传播，仅需K次反向传播即可算出Σ_grad，成本与词汇量、序列长度无关
- 同框架下推出KL-SVD变体，替换L2距离为KL散度，适配校准集内效果优先的场景

### 关键结果
在Mistral-7B、Llama3-8B、Qwen3-8B上测试，压缩比0.9时，Llama3-8B的PTB perplexity较SOTA基线IO-SVD从30.9降至23.0，所有设置下C4、PTB跨语料perplexity均为最低；结合3bit GPTQ量化，Llama2-7B可从13.5GB压缩至1.9GB，WikiText-2 perplexity仅16.7；IFEval指令跟随准确率优于所有现有SVD类方法。

### 核心结论
LLM低秩压缩时，对所有logit变化均等加权的泛函范数目标，相比仅拟合校准集分布的目标，能带来更优的分布外泛化性，且无需微调、兼容量化，适合工业落地
