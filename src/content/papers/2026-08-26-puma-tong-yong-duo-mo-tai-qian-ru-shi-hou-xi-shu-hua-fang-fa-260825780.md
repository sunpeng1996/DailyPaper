---
title: 'PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient
  Retrieval'
title_zh: PUMA：通用多模态嵌入事后稀疏化方法实现高效检索
authors:
- Matteo Attimonelli
- Alessandro De Bellis
- Franco Maria Nardini
- Claudio Pomo
- Cosimo Rulli
- Rossano Venturini
- Tommaso Di Noia
affiliations:
- Politecnico di Bari, Italy
- Sapienza University of Rome, Italy
- ISTI–CNR, Pisa, Italy
- University of Pisa, Italy
arxiv_id: '2608.25780'
url: https://arxiv.org/abs/2608.25780
pdf_url: https://arxiv.org/pdf/2608.25780
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 多模态检索 · 嵌入事后稀疏化
tags:
- Multimodal Retrieval
- Sparse Embedding
- Autoencoder
- Retrieval Efficiency
- Post-hoc Optimization
one_liner: 无需重训多模态骨干，将稠密嵌入转为稀疏检索码，降本提效同时效果比肩稠密检索
practical_value: '- 电商多模态商品检索场景可直接复用PUMA流水线，无需重训已上线的多模态嵌入大模型，仅对已缓存的稠密嵌入做稀疏化转换，就能大幅降低向量存储成本、提升召回速度，可先在垂类商品域做小流量验证

  - 训练稀疏自编码器的三个核心trick可直接复用：跨模态对齐损失保证图文激活特征重叠、AuxK特征复活机制解决字典原子死亡问题、先预训练保留稠密点积几何再用对比损失微调适配检索任务，组合使用可避免稀疏化后的效果掉点

  - 可根据业务对 latency/效果的平衡需求灵活调整k值（活跃特征数），比如组合检索场景k=48时就能保留96%的稠密检索效果，存储仅为FP32稠密的1/33，适合低算力边缘场景或大促峰值降本需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
通用多模态嵌入器支持文本、图像、图文混合查询的统一检索，是电商多模态商品搜索、穿搭推荐等场景的核心基建，但高维稠密嵌入存在存储成本高、大候选池下检索速度慢的痛点，现有稀疏化方案要么需要重训骨干模型成本高，要么针对单模态文本设计，多模态事后稀疏化的落地路径未被充分探索。

### 方法关键点
- 三阶段无骨干重训流水线：第一阶段缓存冻结多模态骨干输出的所有稠密嵌入，训练过程不触碰骨干，大幅降低训练成本
- 第二阶段预训练TopK稀疏自编码器，损失组合包含重构损失、跨模态对齐损失、稠密点积蒸馏损失、AuxK特征复活损失、轻量对比损失，同时引入k渐进退火策略，早期用更高k保证训练信号，后期退火到目标稀疏度
- 第三阶段用检索场景的InfoNCE对比损失微调稀疏编码器，仅保留重构和蒸馏损失作为正则项，让稀疏表示完全适配检索排序目标

### 关键结果
在5个多模态检索基准（涵盖文本到图像检索、图文组合检索）上测试，基于Qwen3-VL-Embedding-2B骨干，PUMA在4/5数据集上效果与稠密检索持平甚至更高，CIRR数据集nDCG@10从0.424提升到0.436；存储成本较FP32稠密嵌入降低8-16倍，542K候选池下精确检索速度较稠密检索提升25倍，效果远超Raw TopK剪枝、PCA、同存储预算稠密自编码器等基线。

事后稀疏化是多模态检索降本提效的高性价比路径，无需重训大模型即可实现存储和速度的数量级提升，仅需保证预TopK激活特征充足且与检索目标对齐即可避免效果掉点。
