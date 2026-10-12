---
title: On the Design Space of Continuous Diffusion Language Models
title_zh: 连续扩散语言模型（CDLM）的设计空间优化研究
authors:
- Oscar Davis
- Daan Roos
- Alice Bizeul
- Amitis Shidani
- Victor Turrisi
- Louis Béthune
- Pierre Ablin
- Marco Cuturi
affiliations:
- Apple
- University of Oxford
- University of Amsterdam
arxiv_id: '2610.13834'
url: https://arxiv.org/abs/2610.13834
pdf_url: https://arxiv.org/pdf/2610.13834
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: 连续扩散语言模型 训练与架构优化
tags:
- Continuous Diffusion
- CDLM
- Self Conditioning
- Flow Matching
- Text Generation
one_liner: 提出无额外前向开销的DoubleCat与SemiCat，让连续扩散语言模型性能追平离散扩散
practical_value: '- 做生成式推荐的文案生成、Semantic ID生成、query补全任务时，可直接替换原生self-conditioning为DoubleCat方案，无需额外前向传播即可降低训练推理分布mismatch，训练算力开销不变的前提下可将生成准确率提升3倍以上

  - 扩散式生成item、query等离散序列时，可复用SemiCat的随机token reveal机制，解决高维噪声下的token识别误差问题，减少生成的无效ID、错词等问题，生成有效率可提升近40%

  - 训练嵌入式CDLM时，不要仅用交叉熵损失训练嵌入层，需加入MSE项联合更新所有嵌入的几何结构，避免出现与one-hot方案一致的高解码错误率，同时可将嵌入维度降低1-2个数量级减少显存开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
连续扩散语言模型（CDLM）具备采样速度快、生成可控的优势，可适配文本生成、序列生成等多类场景，但当前对其训练核心影响因子的认知远不如图像等连续模态的扩散模型；现有self-conditioning等优化方案需要额外前向传播，训练开销高，嵌入式CDLM的训练机理不清晰，性能始终落后于离散扩散模型，亟需系统性探索设计空间提升性能、降低落地开销。
### 方法关键点
- DoubleCat双层插值方案：通过在输出simplex上新增一层corruption过程，模拟self-conditioning的训练推理分布对齐效果，无需额外前向传播即可降低训练开销
- SemiCat混合扩散方案：针对token可识别性问题（高斯噪声范数远大于token嵌入范数导致的识别误差），在DoubleCat基础上加入随机离散token reveal机制，进一步提升生成准确率
- 嵌入式CDLM训练机理：纯交叉熵训练会将token嵌入推至类似one-hot的几何结构，解码错误率与one-hot方案一致，需联合更新所有嵌入的几何结构优化效果
### 关键实验
在TinyGSM数学题生成任务上，DoubleCat将基础one-hot流的准确率从4.42%提升3倍到16.00%；SemiCat搭配调优采样器准确率可达49.94%，追平离散扩散基线；1.7B参数规模下，SemiCat在6个似然基准测试中4个超过离散扩散模型，无条件生成效果优于one-hot流。
### 核心结论
连续扩散语言模型的性能短板主要源于训练推理分布 mismatch与token可识别性问题，通过低成本的分布对齐与离散reveal机制即可追平甚至超过离散扩散模型的性能
