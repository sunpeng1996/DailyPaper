---
title: 'MoRoute: Dynamic Routing for In-Context Multimodal Video Generation'
title_zh: MoRoute：面向上下文多模态视频生成的动态路由方法
authors:
- Chong Gao
- Jie Ma
- Zhan Peng
- Chongxiao Wang
- Haoxue Wu
- Jun Liang
- Guanbin Li
- Jing Li
affiliations:
- Sun Yat-sen University
- HUJING Digital Media & Entertainment Group
- Huazhong University of Science and Technology
arxiv_id: '2607.29545'
url: https://arxiv.org/abs/2607.29545
pdf_url: https://arxiv.org/pdf/2607.29545
published: '2026-07-31'
collected: '2026-08-04'
category: Multimodal
direction: 多模态视频生成 · 动态专家路由
tags:
- Dynamic Routing
- Multimodal Generation
- Video Diffusion
- VLM
- DiT
- In-Context Learning
one_liner: 通过动态层路由连接异构预训练VLM与视频DiT，实现多模态输入下高质量可控视频生成
practical_value: '- 跨异构预训练模型的特征对接可复用动态路由思路：预训练LLM与召回/排序模型特征融合时，无需人工选层，用轻量块级路由器自适应匹配每层最优特征源，降低异构模型复用成本

  - 多模态条件注入可参考in-context拼接思路：电商商品短视频/广告生成场景下，参考图/样例视频直接拼接进DiT token序列，比单独特征注入保留更多视觉细节，精准还原商品外观、风格

  - 冻结预训练主干+轻量模块适配的训练策略可复用：大幅降低大模型落地的训练成本，适合业务侧快速迭代多模态生成类功能'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态视频生成方案对接预训练VLM与视频DiT时，要么仅注入少量人工指定VLM层的特征，要么要求理解与生成流架构匹配后联合训练，异构预训练主干复用难度高，无法灵活支持文本/图像/视频混合输入的生成需求
### 方法关键点
1. 提出MoRoute框架，将冻结的异构预训练VLM、视频DiT作为异质专家，通过轻量块级路由模块，为每个DiT块自适应选择最匹配当前生成阶段的VLM层特征，建立多模态理解与视频生成的自适应对应关系
2. 采用统一上下文条件注入机制，将参考图、源视频直接拼接进DiT token序列，保留细粒度视觉细节
### 关键结果
在IntelligentVBench、OpenVE-Bench、RefVIE-Bench三个基准上均超过SOTA，1-5分制下平均分分别提升0.15、0.18、0.34
