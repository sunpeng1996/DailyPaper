---
title: Do Probing and Steering Favor the Same Directions Within and Across Language
  Models?
title_zh: 大语言模型内部概念探测与引导方向的一致性对比研究
authors:
- Afshin Sadeghi
- Daniel Becker
affiliations:
- Fraunhofer IAIS, Sankt-Augustin, Germany
arxiv_id: '2611.19499'
url: https://arxiv.org/abs/2611.19499
pdf_url: https://arxiv.org/pdf/2611.19499
published: '2026-11-13'
collected: '2026-11-20'
category: LLM
direction: 大语言模型表示工程 · 概念探测与引导
tags:
- Probing
- Steering
- Representation Engineering
- LLM
- Hallucination Mitigation
one_liner: 证实大语言模型中概念的最优探测与引导方向不重合，探测方向跨模型迁移性更强
practical_value: '- 做LLM驱动的电商营销文案生成、Agent可控回复时，不要直接复用概念探测方向做activation steering，优先选择类间均值差Δμ方向，引导效果更优

  - 跨模型迁移概念校验能力（比如用户评论情绪识别、商品内容合规探测）时，用逆映射转置迁移探测方向即可保留81%-91%的性能，大幅降低标注成本

  - 构建问答类Agent的幻觉兜底机制时，引导模型朝向「未知」方向干预，可使不确定错误的拒答率提升18-44pp，仅使高置信错误拒答率提升2-5pp，对正确答案影响极小

  - 对比不同steering方向的业务效果时，统一用中性文本的KL散度固定副作用预算，避免因干预强度不同导致的结果偏差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有表示工程实践常直接复用概念探测方向做模型引导，但最优探测方向仅需最大化类间区分度，最优引导方向需最小化干预副作用，二者优化目标存在本质差异，跨模型迁移规律也不明确，需系统对比来优化可控生成、幻觉抑制等落地场景的效果。
### 方法关键点
- 构造从协方差调整的Fisher判别方向（探测最优候选）到类间均值差Δμ（当前主流引导方向）的连续单参数方向族，统一在中性文本KL散度固定的副作用预算下对比两类任务的性能，避免干预强度差异干扰结果
- 跨模型迁移分别适配两类方向的映射规则：探测方向用逆映射的转置迁移，引导方向用前向线性映射迁移，映射均在无标注中性文本上拟合
- 实验覆盖3个不同家族的指令微调模型（LLaMA-3.1-8B、Qwen3.5-9B、Gemma-3-12B），测试真实性、情绪、未知三类概念的表现
### 关键结果
- 同模型内6组模型-概念组合中，最优探测方向与最优引导方向完全不重合，引导最优方向更接近Δμ；情绪场景下中间方向比Δμ的引导效果高27%-56%
- 跨模型迁移时，探测方向可保留81%-91%的目标模型高于随机的性能，11/12的模型对中引导方向的迁移效果弱于探测方向
- 引导模型输出「未知」时，不确定错误的拒答率提升18-44pp，高置信错误仅提升2-5pp，对正确答案的影响小于7pp
### 核心结论
探测与引导是LLM概念表示的两个独立优化目标，不要直接将探针方向复用为引导方向，二者各自有最优方向和迁移规律
