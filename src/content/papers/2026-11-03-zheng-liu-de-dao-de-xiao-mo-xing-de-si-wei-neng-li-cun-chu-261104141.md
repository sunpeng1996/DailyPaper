---
title: Where Do Distilled Students Store Thinking?
title_zh: 蒸馏得到的小模型的思维能力存储在权重的哪个子空间？
authors:
- Taeyeong Kim
- Jaemin Jung
- Ahhyun Kim
- Unggi Lee
affiliations:
- Chosun University
- Korea University Sejong Campus
arxiv_id: '2611.04141'
url: https://arxiv.org/abs/2611.04141
pdf_url: https://arxiv.org/pdf/2611.04141
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM推理蒸馏 · LoRA子空间编辑
tags:
- LoRA
- Knowledge Distillation
- Chain-of-Thought
- Model Editing
- Reasoning
one_liner: 定位LoRA蒸馏的小推理模型中存储类思维行为的共享权重子空间
practical_value: '- 做电商/搜索Agent的小模型部署时，可删除LoRA中的思维子空间关闭长输出，推理速度提升2~5倍（对应输出长度从几千token降到几百），满足实时响应要求

  - 如需给导购Agent注入多步需求探询的类思维行为，可单独蒸馏对应LoRA子空间后嫁接进目标模型，无需全量微调，迭代周期从周级降到天级

  - 可复用本文的子空间分析方法，定位业务小模型中特定行为（如营销话术生成、合规拒绝）对应的LoRA方向，实现定向编辑无需重新训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前将大推理模型(LRM)的长链思考能力蒸馏进小模型时，小模型在长推理任务上性能退化明显。现有研究通过插值LRM和短答案指令模型调整教师输出长度优化蒸馏效果，但仅从输出层面分析，无法明确小模型权重中哪部分存储了类思维行为，也无法实现思维能力的定向开关。
### 方法关键点
- 采用插值教师方案：将LRM（λ=0）和同基座短答案指令模型（λ=1）按比例λ线性插值得到不同教师，随λ增大教师逐步停止思考
- 以LoRA为可观测的更新载体，对3组教师对、3款0.5B~1B参数的学生模型，在不同λ下蒸馏得到LoRA适配器，对比不同适配器的更新子空间重叠度
- 提取教师停止思考前所有适配器共享的权重子空间，通过删除、嫁接、放大三类干预实验验证其与类思维行为（反思标记、独白格式、长输出）的关联
### 关键结果
- 该共享子空间占LoRA 16个更新方向中的5~8个，存储了47%~72%的更新能量
- 删除该子空间可将所有实验组的类思维标记降低到原有水平的0.2%~10%，推理精度平均提升8.6pp，效果优于删除其他等能量方向
- 给短答案模型嫁接2倍权重的该子空间，可开启早期反思标记，但模型完成完整推理的概率不足15%

> 最值得记住的一句话：蒸馏小模型的类思维行为并非分散在全量权重中，而是集中存储在LoRA的一个低秩共享子空间内，可通过定向编辑实现快速开关。
