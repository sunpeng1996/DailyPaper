---
title: Probing Transformer Representations Layer by Layer, Module by Module
title_zh: Transformer表征逐层逐模块探查分析与最优特征提取策略
authors:
- Ambroise Odonnat
- Theo Gnassounou
- Laetitia Chapel
- Romain Tavenard
- Ievgen Redko
affiliations:
- Noah's Ark Lab
- Inria
- EPFL
- IRISA
- Schneider Electric
arxiv_id: '2611.11531'
url: https://arxiv.org/abs/2611.11531
pdf_url: https://arxiv.org/pdf/2611.11531
published: '2026-11-07'
collected: '2026-11-13'
category: LLM
direction: Transformer表征探查 · 特征提取优化
tags:
- Transformer
- Probing
- Feature Extraction
- LLM
- VFM
one_liner: 系统分析Transformer各层各模块表征效果，给出零成本最优特征提取策略
practical_value: '- 电商Query理解、商品语义匹配、RAG召回等依赖LLM embedding的场景，无需微调，将默认的最后一层残差输出替换为60%深度的LN2层输出，平均可提升2.4pp的分类准确率，可直接省掉embedding微调成本

  - 多模态电商场景（商品图分类、素材审核、跨域内容召回等），使用视觉Foundation Model提取特征时，替换为最后一层FFN激活输出（Act@100），在预训练和下游数据分布差异大的任务上收益更明显，平均可拿到42%的最优探查增益

  - 若业务有少量标注数据，可仅遍历单个最优模块的不同层选择最佳输出，例如LLM场景遍历不同层的LN2输出，可回收接近100%的最优探查增益，成本远低于全层全模块遍历

  - 下游数据和预训练分布差异大的微调场景，可优先针对效果最优的模块所在层做LoRA微调，减少微调参数同时提升效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer特征提取默认取最后一层残差输出，过往探查研究仅关注层维度差异，将Transformer块视为原子单元，忽略块内不同模块（LN、Attention、FFN、激活层等）的表征差异，导致提取的特征远非最优，亟需系统性分析层与模块的联合影响，找到无额外成本的最优特征提取策略。

### 方法关键点
- 覆盖15个视觉基础模型（ViT、DINOv2/3、AIMv2，参数量22M~7B）和9个LLM（Qwen3、Llama3、Gemma3，参数量1B~12B），遍历每个层的8个模块输出做线性探查
- VFM侧在18个图像分类数据集完成9万次探查评估，LLM侧在MMTEB多语言benchmark的24个分类任务完成5.4万次探查评估
- 以最后一层残差输出（RC2@100）为基线，对比仅选最优层、仅选最优模块、层+模块联合最优的增益，同时验证无搜索成本的固定策略效果

### 关键结果
- 层与模块选择需联合考虑：联合最优的增益显著高于仅优化层或仅优化模块的增益
- 固定策略效果优异：VFM采用最后一层FFN激活输出（Act@100），平均可回收42%的联合最优增益，在分布偏移大的跨域任务上收益更高，89.3%的WILDS/DomainNet任务上有提升；LLM采用60%深度的LN2层输出（LN2@60），平均可回收86%的联合最优增益，87.5%的MMTEB任务上有提升，平均准确率涨2.44pp，可让Gemma3 4B的embedding效果匹配7B参数的SOTA embedding模型

### 核心结论
Transformer特征提取不要默认取最后一层残差输出，LLM用LN2@60、VFM用Act@100就能以零额外成本拿到大部分最优增益
