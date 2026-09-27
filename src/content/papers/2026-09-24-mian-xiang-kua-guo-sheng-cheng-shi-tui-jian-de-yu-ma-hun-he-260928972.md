---
title: Cross-Country Code-Mixing for Generative Recommendation
title_zh: 面向跨国生成式推荐的语码混合增强框架CMRec
authors:
- Yuan Gao
- Hao Deng
- Haibo Xing
- Yi Xu
- Lingyu Mu
- Jinxin Hu
- Yu Zhang
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.28972'
url: https://arxiv.org/abs/2609.28972
pdf_url: https://arxiv.org/pdf/2609.28972
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · 跨国知识迁移
tags:
- Generative Recommendation
- Cross-Country Recommendation
- Code-Mixing
- Data Augmentation
- Semantic Codebook
one_liner: 通过双约束语码混合在数据层面注入跨国监督信号，同步提升大小市场推荐效果
practical_value: '- 跨市场/跨域生成式推荐可复用共享语义码本构建方案：融合多模态内容+跨域行为i2i信号训练统一码本，解决ID空间不重叠的语义对齐问题

  - 跨域序列增强可直接复用双约束替换逻辑：静态语义相似度+动态属性（价格/受众/热度分桶归一化）双筛选，相比单靠内容/协同的增强噪声降低30%以上

  - 生成式推荐的增强样本训练可借鉴上下文感知重加权：用模型在原序列上的置信度动态调整增强样本权重，自动过滤上下文不兼容的噪声样本，无需额外标注

  - 生产落地可直接参考默认超参：替换比例p=10%、单样本替换占比k=10%、损失权重λ=0.5在工业数据上达到近最优，可作为初始调优基准'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
跨境电商各市场用户/物品ID空间完全独立，传统跨域推荐依赖的共享ID/实体锚点不存在；现有生成式跨域推荐仅在参数层面做知识迁移，数据层面不同市场的行为序列完全隔离，大市场的丰富交互信号无法有效迁移到小市场，稀疏市场效果提升瓶颈明显。

### 方法关键点
- 构建共享语义码本：用跨市场统一的多模态预训练模型编码物品内容，联合跨市场i2i双塔训练注入行为共现信号，再通过RQ-VAE量化为统一token序列，同时作为GR的分词器和跨市场替换的语义空间
- 双约束语码混合：对每个物品，先匹配跨市场语义token汉明距离小于阈值的候选，再要求动态属性（价格、受众、热度经分桶归一化）的余弦相似度达标，按10%比例抽取训练样本，每个样本替换10%的位置生成混合序列
- 上下文感知损失重加权：用原序列下模型对原目标和替换后目标的预测概率比作为混合样本的权重（stop-gradient避免影响主模型训练），动态降低上下文不兼容的噪声样本权重

### 关键实验
在阿里内部6国10亿级交互广告数据集、公开Amazon M2多语言6站点数据集（大小市场数据量差达10倍）上，对比SASRec、HSTU、GenCDR等基线，工业数据集6国平均Recall@10提升3.01%、NDCG@10提升1.98%，小市场Recall@10提升达5.32%；在线A/B测试获+1.77%广告收入、+2.64%订单量提升。

### 核心结论
跨市场生成式推荐的知识迁移不能只靠参数共享，在数据层面通过低噪声的跨域序列混合注入监督信号，能同时实现大小市场的效果正向提升。
