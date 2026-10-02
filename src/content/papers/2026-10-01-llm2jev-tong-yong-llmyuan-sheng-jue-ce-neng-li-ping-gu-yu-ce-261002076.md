---
title: 'LLM2Jev: LLMs Are Already Jev-Style Decision Models -- When and How to Fine-Tune
  Them'
title_zh: LLM2Jev：通用LLM原生决策能力评估与微调最优策略框架
authors:
- Yinheng Li
- Justin Wagle
affiliations:
- Microsoft
arxiv_id: '2610.02076'
url: https://arxiv.org/abs/2610.02076
pdf_url: https://arxiv.org/pdf/2610.02076
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM决策适配 · 结构化输出优化
tags:
- LLM4Decision
- LoRA
- KL Regularization
- Zero-shot
- Jev-style Model
one_liner: 提出架构无损的Jev式决策抽取框架，明确LLM决策能力边界与微调适用场景
practical_value: '- 电商客服意图识别、推荐候选排序、Agent工具选择等决策类任务，可直接复用零-shot前缀-free编号提示模板，无需微调就能实现任意量级候选的决策抽取，比单字母logit读取上限更高，完全不用修改基座架构

  - 做LLM业务决策任务微调时，必须加KL锚定正则（大模型默认λ=1，小模型可降至0.1），防止模型通用生成能力退化，同时优先选用LoRA而非全量微调，大幅降低负迁移概率

  - 微调训练集必须完全匹配线上分布，必须包含fallback选项、长文本、二元校验等场景，不能仅喂高置信简单样本，否则会出现明显的heuristic shortcut导致跨域性能暴跌

  - 所有决策类任务先跑零-shot基线验证效果，仅当小模型部署、高基数路由等明确短板场景再启动微调，不要盲目微调大模型浪费算力与数据资源'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Jev风格决策模型直接输出预定义选项的概率分布，无需解析自由文本，可被下游系统直接调用，是连接LLM与自动化系统的核心范式。但当前社区Jev类模型普遍存在两类问题：要么修改基座架构新增分类头/保留token，适配新模型成本极高；要么盲目微调，既浪费资源又容易出现负迁移，同时缺乏对通用LLM原生决策能力的系统性评估，没有明确微调的适用边界与最优策略。

### 方法关键点
- 零推理方案：将选项用前缀-free的带括号数字编号（如[1][2][12]），统一prompt模板固定助手回复前缀为「Best answer: [」，并行计算各候选后缀的联合log概率，softmax归一化得到决策分布，无需修改模型、词表，支持任意数量候选
- 微调方案：采用树因子化列表式损失优化决策准确率，同时引入3种KL锚定正则（合法token质量、非法token分布、非决策位置分布）对齐原基座分布，支持全量微调或LoRA，微调后模型仍保留原生生成与多模态能力
- 训练优化：训练时随机打乱选项顺序消除位置偏置，严格过滤训练测试重叠样本，仅需数百梯度步即可收敛

### 关键结果
在Qwen3.5-4B、Qwen3-0.6B上验证，对比社区SOTA Jev模型：
1. 零-shot Qwen3.5-4B在JevBench公共数据集准确率达81.4%，与同基座微调的社区Jev模型持平，ECE仅0.057，校准效果优于多数微调模型，原生支持77分类的Banking77任务，零-shot多模态决策在MMBench上达82.4%
2. 微调仅对小模型、高基数意图路由等明确短板场景有效：0.6B模型微调后Banking77准确率从22.2%提升至59.8%，但4B大模型全量微调在通用JevBench上无收益甚至下降，仅LoRA微调可提升2.6个点至84.0%
3. KL锚定可完全避免微调后的生成退化，λ=1对大模型最优，小模型可放宽到0.1

### 核心结论
通用LLM本身已经是合格的Jev风格决策模型，微调仅能带来针对性收益而非通用提升，盲目全量微调大模型反而会导致负迁移
