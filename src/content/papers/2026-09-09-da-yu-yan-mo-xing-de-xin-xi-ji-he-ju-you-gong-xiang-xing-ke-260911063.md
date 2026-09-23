---
title: The information geometry of large language models is shared, learned, and controllable
title_zh: 大语言模型的信息几何具有共享性、可学习性与可控性
authors:
- Dario Picozzi
affiliations:
- University College London (UCL)
- London Centre for Nanotechnology
arxiv_id: '2609.11063'
url: https://arxiv.org/abs/2609.11063
pdf_url: https://arxiv.org/pdf/2609.11063
published: '2026-09-09'
collected: '2026-09-23'
category: LLM
direction: LLM信息几何 · 低扰动模型控制
tags:
- Information Geometry
- Fisher-Rao Metric
- LLM Steering
- Knowledge Editing
- Low-perturbation Fine-tuning
one_liner: 基于Fisher-Rao输出几何构建跨架构LLM的统一分析与低扰动干预框架
practical_value: '- 做LLM驱动的电商推荐文案生成、Agent工具调用微调时，可替换欧几里得正则为Fisher-Rao拉回度量，同等目标效果下可降低60~250倍的离群输出扰动，避免模型通用推荐能力退化

  - 电商领域的商品知识、营销规则植入可采用文中的低扰动知识编辑方案，相比传统编辑方法可降低10倍以上的其他token输出偏差，减少无关营销内容生成

  - 做LLM可解释性分析、推荐召回特征重要度评估时，可采用Fisher加权输出敏感度替代激活值大小，与特征消融后的实际KL散度相关性达0.997，评估准确度大幅提升

  - 跨LLM的语义特征迁移时可利用文中验证的跨架构共享输出几何，语义分类探针跨模型迁移准确率可达0.66，接近单模型内的0.72水平，减少重复标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大语言模型行为相似性的底层结构不明确，传统基于激活欧氏距离的分析、干预方法受重参数化影响不稳定，难以实现改变目标行为的同时不干扰其他通用能力，且跨架构模型的共性规律难以统一度量。

### 方法关键点
- 基于Fisher-Rao度量构建LLM输出概率分布的正则几何框架，将输出度量拉回至干预层得到与坐标无关的行为度量，不受内部激活重参数化影响
- 提出基于语料n-gram统计的事实获取时间预测方法，以及阻尼自然梯度的低扰动干预方案，支持跨prompt复用的模型控制
- 实验覆盖Transformer、状态空间、循环架构共11个LLM系列，参数规模从70M到7B

### 关键结果
- 跨架构模型的输出几何秩一致性达0.88，远高于中间层激活的0.62；语义分类探针跨模型迁移准确率达0.66，接近单模型内的0.72水平
- 低扰动干预相比欧氏控制方法，知识编辑的其他token偏差降低10.57倍，LoRA微调的离群变化降低60~250倍，steering的离靶KL降低最高72.7倍
- 语料n-gram统计可预测新事实的学习轨迹，R²达0.775~0.792，深层证据的事实获取时间是浅层的4.3倍

### 核心结论
LLM的输出几何是与内部坐标无关的统一基准，既可以解释跨模型的行为共性，也能指导所有低扰动模型操作。
