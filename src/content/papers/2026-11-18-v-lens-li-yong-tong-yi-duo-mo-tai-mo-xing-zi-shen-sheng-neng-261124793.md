---
title: 'The Elephant in the Question: Unified Models Picture the Concepts Behind Their
  Answers'
title_zh: V-LENS：利用统一多模态模型自身生成能力可视化推理中间概念
authors:
- Tobias Braun
- Marcus Rohrbach
- Lorenzo Cavallaro
affiliations:
- Technische Universität Darmstadt
- University College London
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.24793'
url: https://arxiv.org/abs/2611.24793
pdf_url: https://arxiv.org/pdf/2611.24793
published: '2026-11-18'
collected: '2026-11-19'
category: Multimodal
direction: 多模态可解释性 · 隐藏态可视化
tags:
- Multimodal
- Interpretability
- Hidden State
- Unified Model
- LoRA
one_liner: 无需额外解码器，用统一多模态模型自身图像生成器可视化文本推理中间隐藏态，可通过视觉监督提升模型表现
practical_value: '- 多模态电商推荐/搜索场景可复用V-LENS思路，无需额外训练解码器，即可用模型自身生成能力校验query理解、召回排序阶段的中间隐藏态是否和用户意图的隐含概念对齐，快速排查bad
  case根因

  - 模型微调阶段可借鉴lens tuning范式，用业务侧已有的图像标注（如正确商品图、场景图）监督中间隐藏态，无需直接监督输出token即可提升文本回答/推荐匹配准确率，降低标注成本

  - 多模态Agent开发中可集成V-LENS类工具，可视化推理链路的隐含概念，定位Agent在用户意图理解、工具调用决策阶段的错误，提升推理可解释性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多模态大模型推理过程为黑盒，回答推理依赖的中间隐含概念（如回答“最大陆生动物所在洲”时的“大象”）不会显式输出，传统隐藏态解释方法仅能转换为文本，无法直观还原视觉语义；而统一多模态模型同时具备文本理解和图像生成能力，存在利用自身能力可视化中间态的可能性。

### 方法关键点
- V-LENS：先为每个模型校准最优插入层R，对任意层ℓ提取的目标token隐藏态做中心化、坐标缩放，对齐到插入层的统计分布后，替换绘图prompt中的占位符token，直接调用模型自身图像生成器输出对应概念的图片，无需训练额外解码器。
- Lens tuning：仅在文本层插入LoRA，用目标图像通过V-LENS的扩散损失监督选中的隐藏态，无需直接监督文本输出token，即可强化隐藏态和对应概念的关联。

### 关键实验
在6款主流统一多模态模型（含扩散式、自回归式架构）上测试：未显式提及的中间概念可视化准确率比最优基线高32%；Lens tuning后，代词指代对象的可视化准确率从2%-11%提升至86%-94%；仅用视觉监督的情况下，模型文本回答准确率最高提升13.3个百分点，且无通用能力下降。

### 核心结论
统一多模态模型的自身生成能力可直接用于内部隐藏态的可解释性校验与弱监督训练，无需额外引入外部解码器或文本标注。
