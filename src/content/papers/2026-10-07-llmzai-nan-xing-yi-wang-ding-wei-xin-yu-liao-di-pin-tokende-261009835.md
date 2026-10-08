---
title: 'A Deafening Silence: Catastrophic Forgetting Lives in the Output Embeddings
  of Tokens the Data Never Speaks'
title_zh: LLM灾难性遗忘定位：新语料低频token的输出嵌入是核心重灾区
authors:
- Jonghyun Han
- Younghoon Song
- Jongyoul Park
affiliations:
- Seoul National University of Science and Technology
- Korea Institute of Land & Infrastructure Safety Technology
arxiv_id: '2610.09835'
url: https://arxiv.org/abs/2610.09835
pdf_url: https://arxiv.org/pdf/2610.09835
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM训练 · 灾难性遗忘缓解
tags:
- CatastrophicForgetting
- AdamOptimizer
- ContinualTraining
- LLMFineTuning
- LoRA
one_liner: 定位LLM灾难性遗忘集中于低频token输出嵌入，单步优化器调整无损失降67.9%遗忘
practical_value: '- 做电商/垂域LLM微调、Agent工具调用微调时，直接给输出嵌入层的Adam ε单独设为1e-4，零计算/内存开销，可在不损失新任务效果的前提下降低39%~68%的灾难性遗忘

  - 垂域微调前先统计新语料token频率，若低频（出现次数<1000）token占比高（如小语种电商、垂域黑话多的场景），该方法收益最高

  - 用LoRA微调时若需放开输出头训练，必须开启该ε调整，可避免输出头放开带来的23倍遗忘暴增问题

  - 不要试图事后修复输出嵌入层的参数漂移，现有后处理方法最多只能恢复<5%的遗忘，所有干预必须在训练阶段执行'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM持续预训练/微调不可避免出现灾难性遗忘，主流缓解方案replay需访问原预训练数据，绝大多数业务场景无法满足；现有无数据缓解方法盲目约束整体参数漂移，会严重牺牲新域学习效果，且过往遗忘位点研究结论冲突，无明确因果定位指导优化。

### 方法关键点
1. 采用训练时逐参数组冻结的因果定位方法，排除相关性指标干扰，准确定位遗忘发生位点
2. 发现遗忘集中于新语料中出现次数<1000的低频token输出嵌入层：这类token会持续收到softmax单侧负梯度，Adam二阶矩归一化会将极小梯度放大成全量更新，默认ε（1e-8）无法抑制该漂移
3. 提出仅给输出投影层的Adam ε单独调高至1e-4，无额外开销，无需原数据或提前统计token频率，利用输出层与主体层二阶矩的天然分布差实现选择性抑制漂移

### 关键结果
在160M~12B共4个模型族、8种实验设置下，该方法移除39.4%~67.9%的灾难性遗忘，完全不降低新域学习效果；与1%比例的replay结合，最高可降低79.8%的遗忘；可解决LoRA放开输出头时出现的23倍遗忘暴增问题；事后修复漂移的输出嵌入最多仅能恢复<5%的遗忘，干预必须在训练阶段执行。

> 最值得记住的一句话：无数据场景下LLM域适应的灾难性遗忘防御，优先调整优化器配置，成本远低于数据增广或参数约束方案
