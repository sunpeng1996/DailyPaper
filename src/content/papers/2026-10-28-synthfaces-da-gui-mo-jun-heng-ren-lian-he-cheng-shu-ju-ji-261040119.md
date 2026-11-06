---
title: 'SynthFaces: Balanced Large Scale Human Dataset'
title_zh: SynthFaces：大规模均衡人脸合成数据集
authors:
- Sergey Karpukhin
- Denis Bobkov
- Kirill Morozov
- Aibek Alanov
affiliations:
- FusionBrain Lab
- HSE University
- MSU
arxiv_id: '2610.40119'
url: https://arxiv.org/abs/2610.40119
pdf_url: https://arxiv.org/pdf/2610.40119
published: '2026-10-28'
collected: '2026-11-06'
category: Other
direction: 合成数据集 · 公平人脸生成
tags:
- Synthetic Dataset
- Face Generation
- Flow Matching
- Fair AI
- Privacy Preservation
one_liner: 基于Arc2Face扩展流匹配生成模型，构建无隐私风险、身份均衡的大规模合成人脸数据集
practical_value: '- 可复用可控人脸生成pipeline生成电商虚拟模特素材，完全规避真人肖像权合规风险

  - 身份嵌入流空间匹配的方法可迁移到个性化数字人推荐场景，提升不同人群生成效果均衡性

  - 身份分布均衡构建思路可复用在用户画像训练数据集补全场景，解决subgroup偏置导致的模型公平性问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
真实人脸数据集普遍存在身份分布不均衡、敏感隐私信息泄露风险，训练出的人脸生成模型在不同人群上表现差异大，身份保留生成场景的公平性问题尤为突出。
### 方法关键点
1. 扩展Arc2Face diffusion模型，在身份嵌入流形上新增flow matching生成模块，支持可控生成多样化身份的人脸数据；
2. 设计最近邻非泄露指标验证身份分离度，确保合成数据不包含真实用户的人脸信息。
### 关键结果
生成的SynthFaces数据集同时达到现有真实人脸数据集不具备的高生成保真度、高标签多样性两个目标，所有合成身份均无隐私风险，用其微调adapter-based个性化生成模型可有效提升下游任务公平性。
