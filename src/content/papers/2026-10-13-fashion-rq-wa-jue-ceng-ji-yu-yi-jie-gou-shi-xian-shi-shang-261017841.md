---
title: 'FASHION-RQ: Mining Hierarchical Semantic Structure for Automated Evaluation
  of Fashion Retrieval'
title_zh: FASHION-RQ：挖掘层级语义结构实现时尚检索自动评估
authors:
- Tripti Shukla
- Shwetha Somasundaram
- Akshat Gupta
- Rohit Garg
- Paul Duff
- Ian Anderson
affiliations:
- Glance
arxiv_id: '2610.17841'
url: https://arxiv.org/abs/2610.17841
pdf_url: https://arxiv.org/pdf/2610.17841
published: '2026-10-13'
collected: '2026-10-15'
category: Eval
direction: 时尚检索 · 自动评估基准构建
tags:
- Fashion-Retrieval
- RQ-VAE
- Semantic-ID
- Benchmark
- Automated-Evaluation
- Attribute-Metric
one_liner: 基于RQ-VAE层级语义ID自动构建无人工标注的时尚检索多维度评估基准
practical_value: '- 垂类（时尚/家居等）检索/推荐场景下，可复用RQ-VAE+属性排他性损失方案自动生成层级聚类与分级relevance标签，大幅降低benchmark人工标注成本

  - 检索效果评估可引入加权属性匹配得分+分维度指标，替代单一nDCG/Recall，快速定位模型在材质、风格等难区分属性上的缺陷，指导迭代

  - 生成模拟用户query时，可参考「聚类属性分布+父/兄弟簇排他约束」的prompt设计，生成的query既自然又具备区分度，可用于训练数据增强或冷启动query构造

  - 基于RQ-VAE生成Semantic ID时，优先选择中等大小codebook（如64码/层），平衡聚类纯度与簇规模，避免过大导致簇碎片化、过小导致语义区分度不足'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有时尚检索基准依赖人工标注或预定义分类体系，扩展性差，且仅输出整体排序指标，无法拆解细粒度属性匹配效果，单目标相关性标签也不符合真实购物query对应多匹配结果的场景，难以定位模型实际业务缺陷。
### 方法关键点
- 基于RQ-VAE学习商品3层级Semantic ID，新增属性排他性损失，让不同量化层分别对应从粗到细的语义属性（大类→品类→组合属性），避免异构聚类
- 基于SID前缀划分聚类，过滤低质簇后结合父/兄弟簇的属性差异生成排他约束，用LLM自动生成符合用户习惯的检索query，相关性标签由SID前缀共享长度确定性生成，无需人工标注
- 设计4类互补评估任务（排序、分级相关性分类、兄弟簇区分、paraphrase鲁棒性），搭配加权属性相关性得分和分属性评估指标，同时衡量整体效果与细粒度属性匹配能力
### 关键实验
基于Myntra 4.4万件时尚商品构建FASHION-RQBENCH，包含588个聚类、5380条标注query。对比10个主流检索模型发现：dense编码器nDCG@10最高达0.87，显著优于BM25的0.77，但四分类相关性准确率仅0.51；模型在品类、性别属性得分超0.93，但材质、风格得分仅0.52、0.43；4B Qwen3编码器效果略优于8B版本，并非模型越大效果越好。人类验证显示生成的query自然度与真实用户query相当，意图清晰度更高。
### 核心结论
仅靠整体排序指标会掩盖模型在细粒度属性上的缺陷，基于层级语义结构自动生成的评估基准可低成本、可解释地衡量检索系统的真实业务效果
