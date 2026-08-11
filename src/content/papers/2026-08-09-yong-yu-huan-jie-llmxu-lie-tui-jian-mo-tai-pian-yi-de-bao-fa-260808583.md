---
title: Structure-Preserving Projection for Mitigating Modality Bias in LLM-Based Sequential
  Recommendation
title_zh: 用于缓解LLM序列推荐模态偏倚的保结构投影方法
authors:
- Tzu-Wei Chiu
- Song-Duo Ma
- Hsin-Yu Lin
- Pu-Jen Cheng
affiliations:
- National Taiwan University
arxiv_id: '2608.08583'
url: https://arxiv.org/abs/2608.08583
pdf_url: https://arxiv.org/pdf/2608.08583
published: '2026-08-09'
collected: '2026-08-11'
category: GenRec
direction: 生成式推荐 · 多模态信号对齐
tags:
- Sequential Recommendation
- LLM4Rec
- Modality Bias
- Structure Preservation
- Projection Alignment
one_liner: 提出两种保结构投影损失，缓解LLM序列推荐中过度依赖文本忽略协同信号的模态偏倚
practical_value: '- 做LLM+协同信号融合的推荐时，可直接复用嵌入shuffle测试，快速验证模型是否真实利用了协同信号，避免伪融合

  - 投影层训练可叠加本文的两类保结构损失，优先使用序列级对比损失，比仅用语言建模损失提升HR@1 2-8pp

  - 训练可采用两阶段策略：先冻结LLM和协同编码器预训练投影层的保结构能力，再联合微调LoRA参数，避免协同结构被语言目标冲毁

  - 无需盲目追求协同嵌入全局结构完全对齐，面向任务的序列级对比对齐对推荐效果的提升更显著'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM-based序列推荐通常将传统协同模型的item嵌入投影到LLM输入空间，融合文本与协同信号，但存在严重模态偏倚：LLM因预训练偏好过度依赖文本信息，投影过程会扭曲协同嵌入的原有结构，导致模型几乎无法有效利用协同信号——实验显示shuffle协同嵌入后，基线模型HR@1波动不足0.01，说明协同嵌入仅充当无意义软提示，融合效果远低于预期。

### 方法关键点
- 设计两类保结构损失约束投影过程：① 余弦相似度保留损失：最小化投影前后item两两余弦相似度的MSE，保留全局几何关系；② 对比保留损失：让投影后的用户序列表征与正样本嵌入相似度高于负样本，保留序列级任务判别能力
- 两阶段训练：先冻结协同编码器与LLM，仅用保结构损失预训练MLP投影层，再联合优化投影层与LLM的LoRA参数，总损失为语言建模损失加加权保结构损失
- 可选动态权重调度：训练前期侧重余弦损失稳定投影结构，后期逐步切换为对比损失优化推荐效果

### 关键结果
在LastFM、MovieLens-100K数据集上对比GRU4Rec、TALLRec、LLaRA等基线，Contrastive-LM在LastFM上HR@1最高达0.5546，较LLaRA提升8.7pp；在MovieLens上HR@1最高达0.4993，较LLaRA提升2.5pp，嵌入shuffle测试验证模型对协同信号的依赖度提升3倍以上。

### 核心结论
无需完全保留协同嵌入的全局几何结构，任务相关的序列级判别能力对齐，比盲目追求全局结构保真更能提升推荐效果。
