---
title: 'Backbone-Specific LoRA Geometry: Orthogonality, Superposition, and Provenance'
title_zh: 面向不同基座的LoRA几何特性：正交性、叠加性与溯源
authors:
- Kazuhiko Kawamoto
- Keigo Watanabe
- Hiroshi Kera
affiliations:
- Chiba University
- National Institute of Informatics
arxiv_id: '2611.27201'
url: https://arxiv.org/abs/2611.27201
pdf_url: https://arxiv.org/pdf/2611.27201
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: LoRA训练优化 · 跨模型适配与溯源
tags:
- LoRA
- Model Merging
- Provenance
- Attention Symmetry
- Fine-tuning
one_liner: 基于注意力对称性推导跨基座LoRA正交边界，实现无对齐LoRA溯源与多基座共享
practical_value: '- 多基座LLM/MoE推荐/广告推理服务场景，可直接复用LoRA叠加方案，7个基座仅需存1份16秩压缩LoRA，存储成本降为1/7，精度仅损失0.79pp

  - 针对LoRA资产盗用溯源需求，无需额外嵌入水印，直接用全量更新的余弦相似度即可100%准确识别LoRA训练所属基座，跨任务也生效

  - LoRA合并时可省略坐标对齐步骤，利用不同基座LoRA天然正交的特性降低合并干扰，可优化TIES/DARE等现有合并方法效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多基座大模型部署场景（如电商多场景推荐、多模态内容理解）中，同个业务任务需为每个基座单独训练适配LoRA，存储、运维成本高；LoRA合并复用存在干扰，且LoRA来源溯源需额外嵌入水印或坐标对齐，开销大，现有方案无法兼顾低损耗、低成本解决跨基座LoRA共享与溯源需求。
### 方法关键点
- 基于Transformer注意力的符号排列对称性，推导跨基座同任务LoRA更新的余弦相似度二阶矩上界，证明不同基座训练的同任务LoRA天然近乎正交，跨基座相似度均值仅为1.78×10⁻⁴
- 通过梯度流模型解释同一基座同任务多次训练的LoRA存在正相关特性，可作为基座专属签名
- 落地三类应用方案：①多基座同任务LoRA直接叠加共享，SVD截断降存储；②基于余弦相似度匹配识别LoRA所属基座，无需坐标对齐、无需推理数据；③内积检测叠加后的混合LoRA是否包含指定注册权重
### 关键实验
基于7个ViT-B/16 CLIP基座、8个公开图像分类数据集验证：
- 单基座单独LoRA精度90.34%，7个同任务LoRA直接叠加后精度90.06%，仅损失0.28pp；SVD压缩到16秩（与单个LoRA存储一致），精度89.55%，仅损失0.79pp
- 基座识别任务中，余弦匹配法在任务匹配、跨任务场景下Top-1准确率均为100%，无需训练额外编码器
- 注册LoRA检测任务中，普通负例下AUROC达100%
### 核心结论
不同基座训练的同任务LoRA天然近乎正交，无需额外约束即可实现精度损失可接受的多基座LoRA共享与无水印溯源检测
