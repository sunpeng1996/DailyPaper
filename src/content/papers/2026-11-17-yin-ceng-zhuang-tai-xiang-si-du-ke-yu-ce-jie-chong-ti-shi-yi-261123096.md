---
title: Hidden-State Similarity Predicts Re-Elicitation After Inoculation Prompting
title_zh: 隐层状态相似度可预测接种提示后被抑制行为的复现
authors:
- Rose N. Kwon
- Samy Mammeri
- Sabyasachi Sahoo
- Christian Gagné
- Thomas Jiralerspong
affiliations:
- Université Laval
- Mila – Québec AI Institute
- Université de Montréal
arxiv_id: '2611.23096'
url: https://arxiv.org/abs/2611.23096
pdf_url: https://arxiv.org/pdf/2611.23096
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: LLM安全 · 行为触发预测
tags:
- LLM Safety
- Inoculation Prompting
- Hidden State
- Emergent Misalignment
- Trigger Prediction
one_liner: 发现隐层状态相似度比文本相似度更能准确预测接种提示后被抑制行为的触发
practical_value: '- 做Agent人设/行为控制时，可替代传统文本相似度判断，用特定层隐层状态与目标人设参考隐层的余弦相似度预判prompt触发效果，规避语义相反但实际触发预设行为的异常case

  - 生成式推荐/电商文案生成的对齐场景中，可通过隐层相似度提前检测prompt是否会触发被抑制的违规内容生成逻辑，比文本语义检测准确率更高，适合上线前的prompt安全校验

  - Prompt工程迭代时，可先基于隐层相似度快速筛选符合目标行为的候选prompt，无需跑全量生成评估，大幅降低Prompt迭代的测试成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Inoculation Prompting（接种提示）是抑制LLM Emergent Misalignment（ emergent 错位）的主流方案，但被抑制的有害行为仍可被评估阶段的特定prompt重新触发，传统文本相似度预测触发效果准确率低，甚至存在语义完全相反的prompt仍能触发被抑制行为的情况，亟需更可靠的预测指标。
### 方法关键点
- 采用Qwen2.5-7B-Instruct、Qwen2.5-14B-Instruct两类模型，基于rank-32 LoRA微调两类任务：5个有害领域的错位行为任务、4种语言的全大写输出任务，均通过接种提示抑制目标行为
- 构造两类隐层相似度特征：1）训练参考平均相似度：评估prompt输出前隐层与所有接种训练样本平均隐层的余弦相似度；2）同问题接种提示相似度：相同问题下评估prompt与接种提示的隐层余弦相似度，根据任务类型选择对应最优层计算（抽象行为选中下层，格式行为选接近输出层）
- 对比基线包含BGE文本嵌入相似度、Token Jaccard、TF-IDF等文本相似度指标
### 关键实验
- 数据集：错位任务用5类有害微调数据集、400条UltraChat评估样本；大写任务用翻译后的GSM8K微调数据集
- 核心结果：隐层相似度与行为触发率的Spearman相关系数最高达0.92，跨任务跨模型稳定优于所有文本基线，其中大写任务中BGE文本相似度相关系数仅为-0.24，隐层相似度相关系数达0.90，提升幅度超110%
### 核心结论
Prompt对LLM行为的触发效果，本质取决于它诱导的模型内部状态，而非表面的文本语义相似度
