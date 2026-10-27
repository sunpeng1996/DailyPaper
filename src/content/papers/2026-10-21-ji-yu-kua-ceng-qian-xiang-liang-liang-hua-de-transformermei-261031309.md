---
title: Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization
title_zh: 基于跨层潜向量量化的Transformer每层嵌入极致压缩方法
authors:
- Jiacheng Liu
- Yaxin Luo
- Xiaohan Zhao
- Peng Sun
- Xinyi Shang
- Jiacheng Cui
- Yonina C. Eldar
- Zhiqiang Shen
affiliations:
- 穆罕默德·本·扎耶德人工智能大学
- 西湖大学
- 浙江大学
- 伦敦大学学院
- 魏茨曼科学研究所
arxiv_id: '2610.31309'
url: https://arxiv.org/abs/2610.31309
pdf_url: https://arxiv.org/pdf/2610.31309
published: '2026-10-21'
collected: '2026-10-27'
category: LLM
direction: LLM嵌入压缩 · 向量量化
tags:
- EmbeddingCompression
- VectorQuantization
- LLMInference
- ModelCompression
- Gemma
one_liner: 提出OPTIC跨层共享压缩方案，实现Gemma 4 PLE百倍压缩几乎无损
practical_value: '- 电商/推荐场景海量用户/物品Embedding可迁移跨共享编码思路：用统一向量加场景/任务专属仿射变换，大幅降低千亿级向量的存储成本，适配召回层大库容需求

  - 部署带PLE结构的大模型（如Gemma 4系列）搭建Agent时，可直接复用OPTIC压缩方案，显存降低30%仅增0.4%延迟，适配端侧/边缘侧部署约束

  - Embedding压缩优化不要仅对齐向量本身MSE，要对齐下游实际使用路径的误差（如推荐排序层输出损失），可大幅提升压缩后业务指标保留率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
近年大模型将嵌入容量作为独立缩放维度，Gemma 4的Per-Layer Embeddings（PLE）占总参数量35.2%，成为部署显存瓶颈；传统量化方法为每个token-层向量单独编码，高压缩比下性能损失极高。

### 方法关键点
- 提出OPTIC压缩框架：每个token仅存1组跨层共享的编码tuple，每层用专属仿射解码器生成对应层的PLE向量，消除编码存储的层维度冗余
- 拟合目标对齐PLE实际输出路径，最小化门控+投影后的输出误差，而非PLE向量本身的重建误差
- 采用交替优化策略：连续更新码本/解码器与离散更新token编码交替进行，配合PCA初始化、未使用码本重置等trick提升压缩质量

### 关键实验结果
在Gemma 4 E4B上测试，对比PQ、RVQ、AQLM等6种传统量化基线：100× BF16 PLE压缩下，7个基准任务平均性能保留97.8%，最强基线仅66.3%；594×、1002×压缩下性能仍保留90.5%、84.1%；搭配W4A16量化主干，100×压缩下性能保留96.9%；推理时固定KV cache大小，BF16 E4B显存降低29.7%，推理延迟仅增加0.4%。

高压缩比下，共享编码+对齐下游使用路径的优化，远优于对每个向量单独做传统量化的效果
