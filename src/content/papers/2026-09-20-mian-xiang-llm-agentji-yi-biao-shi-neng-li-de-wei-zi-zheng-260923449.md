---
title: 'PSD: Pseudo Self-Distillation of Memory Representation Capabilities for LLM
  Agents'
title_zh: 面向LLM Agent记忆表示能力的伪自蒸馏框架PSD
authors:
- Pirzada Suhail
- Menglin Xia
- Xuchao Zhang
- Mayukh Das
- Chetan Bansal
- Saravan Rajmohan
affiliations:
- Microsoft Research
- M365
arxiv_id: '2609.23449'
url: https://arxiv.org/abs/2609.23449
pdf_url: https://arxiv.org/pdf/2609.23449
published: '2026-09-20'
collected: '2026-09-23'
category: Agent
direction: Agent 记忆能力蒸馏优化
tags:
- Distillation
- LLM-Agent
- Memory-System
- SLM
- Black-Box-Distillation
one_liner: 无需访问黑盒大模型内部参数，将其记忆构建能力蒸馏到小模型，部署成本大幅降低
practical_value: '- 闭源大模型能力下沉可直接复用PSD范式：无需获取大模型logits/隐状态，仅需将大模型输出作为特权参考加入prompt，让同个小模型分教师/学生角色做分布对齐，适合电商客服Agent、用户行为记忆抽取等场景的小模型落地

  - 结构化输出任务可复用两阶段训练流程：先做SFT对齐输出格式、解决小模型JSON错误/字段缺失问题，再做PSD蒸馏提升质量，适配商品结构化信息抽取、用户标签生成等场景

  - 多阶段Pipeline任务优先选off-policy PSD变体：避免学生自身生成的错误在多阶段传播，效果比on-policy高10%+，适合电商全链路Agent的记忆同步、跨环节用户意图传承等场景

  - 跨领域迁移需求优先停在SFT阶段：PSD会让模型拟合训练域分布，降低OOD性能，跨品类/跨场景的记忆构建任务无需额外做PSD优化即可拿到较好的迁移效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent分层记忆系统依赖闭源大模型做多阶段记忆构建，调用成本极高，难以大规模落地；直接用小模型替代会出现JSON格式错误、字段缺失、记忆抽取质量差等问题；传统蒸馏方法需要访问大模型的logits、隐状态等内部参数，闭源模型不开放，无法落地。

### 方法关键点
- 两阶段训练范式：第一阶段先用大模型生成的记忆构建样本做LoRA SFT，对齐小模型的输出格式和大模型的生成风格，解决结构错误问题；第二阶段做伪自蒸馏（PSD），同个小模型分两个角色：教师侧输入带大模型输出的特权prompt，学生侧输入普通任务prompt，冻结教师参数，训练学生对齐教师的输出分布，实现黑盒大模型能力的迁移
- 三种PSD变体：on-policy用学生生成的轨迹计算分布差，off-policy用特权教师生成的轨迹计算分布差，混合模式插值两者的损失

### 关键结果
- 在LoCoMo长对话记忆基准上，PSD训练的Qwen3-4B的LLM-judge得分达0.8699，超过GPT-4.1-mini版MEMORA的0.849，部署成本仅为后者的数十分之一；0.6B小模型的LLM-judge得分也达0.8211，超过RAG、Mem0等所有非MEMORA基线
- off-policy PSD效果最优，比on-policy的LLM-judge得分高11个百分点，避免学生错误在多阶段传播
- 仅在LoCoMo训练的PSD模型在未见过的LongMemEval OOD基准上得分达77%，超过Full Context和Nemori基线，有较强的跨域迁移能力

最值得记住的结论：无需访问闭源大模型内部参数，仅靠文本层面的特权提示就能实现能力蒸馏，是低成本落地Agent记忆系统的可行路径
