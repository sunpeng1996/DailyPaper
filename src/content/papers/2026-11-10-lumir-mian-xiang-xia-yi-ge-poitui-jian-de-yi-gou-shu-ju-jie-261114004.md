---
title: 'LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data
  for Next-POI Recommendation'
title_zh: LUMIR：面向下一个POI推荐的异构数据解耦多模态表示学习
authors:
- Zehui Wang
- Wolfram Höpken
- Dietmar Jannach
affiliations:
- University of Applied Sciences Ravensburg-Weingarten
- University of Klagenfurt
arxiv_id: '2611.14004'
url: https://arxiv.org/abs/2611.14004
pdf_url: https://arxiv.org/pdf/2611.14004
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 多模态推荐 · 解耦式表示学习
tags:
- Multimodal Representation
- Contrastive Learning
- Sequential Recommendation
- POI Recommendation
- LLM
one_liner: 提出解耦式多模态POI表示学习框架，无需耦合下游模型即可生成高复用性语义嵌入
practical_value: '- 多模态异构特征统一方案可复用：将结构化属性、文本、视觉特征全部通过LLM转成统一文本语义嵌入，避免不同模态特征对齐的繁琐开发

  - 解耦式预训练范式可迁移到电商商品表示：无需和下游排序/召回模型绑定训练，一次预训练生成的商品嵌入可适配GRU4Rec、SASRec等多种序列推荐架构，降低多模态特征迭代成本

  - 小batch下对比学习优化技巧：用memory bank存储历史embedding作为负样本，解决多模态高维embedding训练时batch size受限导致的负样本不足问题

  - 序列信号弱监督思路：用用户交互序列中相邻item的共现关系作为无监督监督信号，无需标注即可让表示学习贴合业务场景的序列依赖特性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐的表示学习模块与下游模型深度耦合，学到的嵌入泛用性差，更换下游架构需重新训练多模态融合模块，计算成本高；且下游任务目标的监督会让融合过程偏向任务最优解，忽略模态间固有语义关联，POI场景下异构数据（文本、图片、结构化属性）的噪声还会进一步降低表示质量。

### 方法关键点
- LLM语义统一层：将POI的结构化元数据、用户评论、图片三类异构模态信息全部转换为结构化文本，用可微调的LLM编码器映射到共享语义空间，生成各模态独立嵌入
- 解耦式对比预训练：设计两个自监督损失，①模态压缩损失$L_{MC}$：通过随机掩码模态生成增强视图，用memory bank扩充负样本，让融合表示对齐不同模态的互补信息，提升抗噪性；②序列对齐损失$L_{SA}$：将用户交互序列中的相邻POI作为正样本对，让嵌入贴合场景的序列转移规律
- 下游适配：预训练好的POI嵌入直接替换下游序列推荐模型的ID embedding层，冻结嵌入仅训练下游模型即可

### 关键实验
在Yelp多模态POI数据集上验证，对比ID基线、特征拼接、模态加权、FLAVA、CoMM共5种基线方案，适配BERT4Rec、SASRec、GRU4Rec三类主流序列推荐架构；在BERT4Rec上效果最优，相比最强基线NDCG@10提升20.2%、HR@20提升28.9%，同时覆盖度、惊喜度等非精度指标也有明显提升。

### 核心结论
多模态表示学习与下游推荐任务解耦的范式，不仅能降低多模态特征的迭代维护成本，还能同时提升推荐精度与多样性。
