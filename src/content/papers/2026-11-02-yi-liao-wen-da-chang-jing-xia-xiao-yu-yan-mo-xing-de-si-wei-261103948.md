---
title: Balancing Chain-of-Thought and Answer Supervision for Small Language Models
  on Medical Question Answering
title_zh: 医疗问答场景下小语言模型的思维链与答案监督平衡方法
authors:
- Le Zhou
- Xiao Luo
- Chinmay Chandra
- Zhan Zhang
affiliations:
- Pace University
- Southern Methodist University
arxiv_id: '2611.03948'
url: https://arxiv.org/abs/2611.03948
pdf_url: https://arxiv.org/pdf/2611.03948
published: '2026-11-02'
collected: '2026-11-04'
category: Training
direction: 小语言模型 · CoT监督微调策略优化
tags:
- SLM
- Chain-of-Thought
- Supervised Fine-Tuning
- Loss Weighting
- Medical QA
one_liner: 对比两种CoT与答案联合微调损失策略，为医疗QA场景下的SLM微调提供适配指导
practical_value: '- 做Agent推理类SFT时，可根据任务类型选择损失加权策略：封闭域分类/多选择任务用Segment-weighted (SwS)
  策略，开放域生成任务用Uniform-across-Sequence (UaS) 策略，无需多组实验即可拿到较优效果

  - 针对通用基座做领域适配SFT时，优先用SwS策略并将答案损失权重λ设为0.4-0.8区间，可快速弥补基座的领域知识短板，效果增益远高于已做领域预训练的基座

  - SFT过程中可加入软CoT长度惩罚，针对生成CoT过长且效果下降的模型-任务组合，限制过长推理输出，避免不必要的性能损耗'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
小语言模型（≤9B参数）可满足医疗QA本地部署需求，兼顾数据隐私与低延迟，但现有Chain-of-Thought（CoT）监督微调未解决推理过程与最终答案的损失平衡问题，通用策略无法适配不同任务格式与基座特性。
### 方法关键点
- 设计两种联合微调损失策略：Uniform-across-Sequence（UaS）对CoT+答案全序列做均等token级损失加权；Segment-weighted（SwS）分别计算CoT和答案段的归一化平均损失，通过可调参数λ控制答案损失权重，不受两段长度差异影响。
- 覆盖3款通用SLM（Llama-3.2-3B、Qwen3.5-4B/9B）和3款医疗领域SLM（BioMistral-7B、Lingshu-7B、Meerkat-8B），所有实验基于LoRA微调，控制变量保证效果差异仅来自损失策略。
### 关键结果
在3个基准数据集（多选MedQA、EMS-MCQA，自由文本Med-O1）上验证：① 多选任务上SwS效果最优，Qwen3.5-4B在MedQA上较零-shot基线提升44.8%，通用基座增益远高于领域预训练基座；② 自由文本任务上UaS效果最优，3B Llama-3.2效果接近7B医疗领域模型；③ 过长CoT生成会导致部分模型性能下降，λ取0.4-0.8区间普遍能得到最优或次优效果。
### 核心结论
CoT与答案监督的平衡策略没有通用最优解，需根据任务格式（封闭/开放域）和基座已有的领域知识储备做适配，而非统一套用单一微调策略
