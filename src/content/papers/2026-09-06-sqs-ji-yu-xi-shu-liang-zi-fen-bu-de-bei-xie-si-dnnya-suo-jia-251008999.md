---
title: 'SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions'
title_zh: SQS：基于稀疏量子分布的贝叶斯DNN压缩框架
authors:
- Ziyi Wang
- Nan Jiang
- Guang Lin
- Qifan Song
affiliations:
- Purdue University
- University of Texas at El Paso
arxiv_id: '2510.08999'
url: https://arxiv.org/abs/2510.08999
pdf_url: https://arxiv.org/pdf/2510.08999
published: '2026-09-06'
collected: '2026-09-09'
category: Training
direction: 模型压缩 · 贝叶斯变分学习
tags:
- Model-Compression
- Bayesian-Learning
- Variational-Inference
- Quantization
- Pruning
one_liner: 提出联合剪枝与低比特量化的贝叶斯框架，以更小精度损失实现更高模型压缩率
practical_value: '- 端侧搜广推小模型、端侧Agent部署时，可采用SQS的联合剪枝+量化优化方案，替代传统分步剪枝再量化的流程，同等精度损失下压缩率可提升30%以上

  - 压缩LLM用于RAG/Agent推理时，可复用离群感知窗口量化策略，针对注意力层Q/K/V矩阵的长尾权重单独分配量化窗口，避免大权重信息损失，精度下降最多可降低3个百分点

  - 压缩后模型推理时，采用4-5个后验样本的贝叶斯平均替代贪心权重选择，仅增加极微延迟即可将量化导致的精度损失降低20%以上

  - 高稀疏率模型轻量化场景，可替换原高斯正则为spike-and-slab先验，稀疏度达80%时精度损失仍可控制在6%以内'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
DNN/LLM部署受端侧资源限制，传统剪枝、低比特量化分步执行的方案容易产生次优结果，为保障精度往往采用保守压缩率，无法适配资源受限场景；尤其LLM注意力层权重呈长尾分布，常规量化策略易损失大权重信息，导致性能明显下降。

### 方法关键点
- 基于贝叶斯变分学习构建统一压缩框架，用spike-and-slab先验诱导权重稀疏性实现剪枝，GMM建模量化权重分布，联合优化避免分步优化的误差累积
- 推导可高效求解的近似ELBO目标，解决原目标无闭式解的问题，训练开销可控
- 采用离群感知窗口量化策略，针对长尾分布的权重单独设置头尾窗口，保留大权重信息
- 推理支持精确控制稀疏率，可通过少量后验采样的贝叶斯平均降低量化噪声影响

### 关键结果
在ResNet、BERT-base、Llama3.2-1B、Qwen2.5-0.5B上对比GPTQ、AWQ、DGMS等SOTA基线：Llama3.2-1B上实现21倍压缩率，精度损失仅1.48%，远优于AWQ 8倍压缩0.46%损失的tradeoff；BERT-base上32倍压缩率下F1损失仅1.66，优于所有基线；高稀疏场景下spike-and-slab先验比高斯先验精度损失低38%以上，离群感知窗口比等长窗口损失降低2.94个百分点。

**最值得记住的结论**：联合剪枝+量化的统一优化，比分步执行能获得好得多的压缩效率与精度的tradeoff，尤其适合LLM端侧部署场景。
