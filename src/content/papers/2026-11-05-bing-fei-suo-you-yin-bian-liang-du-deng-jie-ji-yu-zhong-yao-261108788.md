---
title: 'Not All Latents Are Equal: Importance-Weighted Latent Graph Generation'
title_zh: 并非所有隐变量都等价：基于重要性加权的隐空间图生成方法
authors:
- Biraaj Rout
- Jay Revolinsky
- Han Liu
- Harry Shomer
affiliations:
- University of Texas at Arlington
- Michigan State University
arxiv_id: '2611.08788'
url: https://arxiv.org/abs/2611.08788
pdf_url: https://arxiv.org/pdf/2611.08788
published: '2026-11-05'
collected: '2026-11-09'
category: Training
direction: 图生成 · 隐空间训练优化
tags:
- Latent Graph Generation
- Importance Reweighting
- Autoencoder
- Training Optimization
- Diffusion Model
one_liner: 无额外参数的LIR隐维度重加权方法，可提升隐空间图生成性能并加快训练收敛
practical_value: '- 电商推荐的用户/物品隐向量建模场景可参考LIR思路，对隐向量不同维度按下游排序/召回任务贡献加权，无需给所有维度同等损失权重，减少无关信息的优化开销

  - 生成式推荐的Semantic ID生成、用户兴趣路径图生成等隐空间生成类任务，可复用该无额外参数的重加权方案，无需修改模型结构即可提升性能并加快收敛

  - 计算隐维度重要性时可直接复用雅可比矩阵相对影响统计的方案，无需额外引入超参数，工程落地成本极低'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离散图扩散模型随节点数量增长复杂度呈二次方上升，难以适配大图场景；隐空间图生成虽可扩展性更优，但性能显著落后于离散扩散方案，根因为不同隐维度对图重建的贡献差异极大，现有损失函数对所有隐维度同等加权，导致模型浪费算力优化大量下游无关信息。
### 方法关键点
隐变量重要性重加权（LIR）机制通过解码器对隐向量的雅可比矩阵计算单个隐单元对图重建的相对影响，以此为权重对不同隐维度的损失赋值；方法完全模型无关，无需新增模型参数或调整超参数。
### 关键结果
在多类基准数据集上对两种不同自编码器应用LIR后，图生成性能稳定提升，同时训练收敛速度显著加快。
