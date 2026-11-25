---
title: 'BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure
  of Scientific Articles'
title_zh: BioLoom：利用科学文献结构训练规模化生物医学视觉语言模型
authors:
- Yuwei Yang
- Xiaoxiao Sun
- Alejandro Lozano
- Yuan-Sen Ting
- Yuhui Yuan
- Liang Zheng
- Serena Yeung-Levy
affiliations:
- Australian National University
- Stanford University
- The University of Sydney
- The Ohio State University
- Canva
arxiv_id: '2611.33151'
url: https://arxiv.org/abs/2611.33151
pdf_url: https://arxiv.org/pdf/2611.33151
published: '2026-11-24'
collected: '2026-11-25'
category: Multimodal
direction: 生物医学多模态预训练 · 样本构造优化
tags:
- VLM
- Contrastive Learning
- Multimodal Pre-training
- Negative Sampling
- Biomedical AI
one_liner: 利用科研文献结构构造多粒度正负样本对，训练性能更优的生物医学VLM
practical_value: '- 多模态对比学习训练时，可利用内容天然结构（如商品详情页主/副图、详情文案、关联评论）构造弱正样本对，无需新增数据即可提升表征质量

  - 负样本筛选可引入加权策略：同品类跨主体的负样本提升权重，强化模型细粒度区分能力，适配电商同款识别、广告素材去重场景

  - 多模态样本扩增时，可融合关联上下文（如商品参数、用户提问内容）丰富文本描述，减少单图文配对的信息损失'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有生物医学VLM对比预训练仅将文献图文作为独立配对，忽略了文献本身的结构关联信息，限制了表征质量提升，无需新增数据即可从现有样本中挖掘更多监督信号。
### 方法关键点
1. 保留精确图文匹配对的同时，引入同图不同子面板、兄弟面板对应文案等弱正样本监督；
2. 对同内容类型的跨文章负样本加权，强化细粒度区分能力；
3. 融合视觉内容、原始图注、正文提及段落丰富子面板文本描述，构建52.4M规模的Loom52M数据集。
### 关键结果
67个零样本分类任务域平衡平均准确率达56.82%，较MedPMC-CLIP提升8.05pct；BioLoomBench、BioMedFlickr双向Recall@1分别达63.20%、10.59%，较对应最优基线分别提升16.83pct、3.04pct。
