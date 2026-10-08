---
title: 'SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery
  and Dynamic Routing'
title_zh: SLDR：基于选择性层恢复与动态路由的LLM恶意微调防御方法
authors:
- Hui Zhang
- Yachao Yuan
- Jiayun Wang
- Yuanzhuo Li
- Hongtao Wang
- Yali Yuan
affiliations:
- North China Electric Power University
- Southeast University
- Soochow University
- Engineering Research Center of Intelligent Computing for Complex Energy Systems,
  Ministry of Education
arxiv_id: '2610.10345'
url: https://arxiv.org/abs/2610.10345
pdf_url: https://arxiv.org/pdf/2610.10345
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM安全 · 恶意微调防御
tags:
- LoRA
- Fine-tuning Safety
- Dynamic Routing
- Layer-wise Diagnosis
- LLM Alignment
one_liner: 通过带符号层敏感度诊断训练特定层LoRA安全适配器，结合动态路由兼顾安全与下游性能
practical_value: '- 垂直场景LLM微调安全加固可复用带符号层敏感度诊断方法，仅在对安全影响最大的正负向两层训练LoRA适配器，算力成本远低于全层修复，且几乎不损失下游任务效果

  - 可借鉴表示驱动的动态路由机制，基于敏感层隐向量相似度判断query风险，仅对高危query激活安全适配器，避免正常业务query的效果损失，适配电商客服、内容生成等场景

  - 低资源安全修复可参考其仅需30条安全对齐数据即可抑制99%以上有害输出的结论，无需大规模标注安全数据，适合中小业务场景的轻量化安全加固'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Fine-tuning-as-a-Service模式下，攻击者可通过在微调数据中混入少量恶意样本，在保留下游任务性能的同时消除LLM的安全拒绝能力，现有防御要么泛化性差，要么修复时会严重损害业务效用，亟需兼顾安全与业务效果的后微调防御方案。

### 方法关键点
- 提出带符号层敏感度诊断方法，通过缩放单层权重观察拒绝率变化，识别出正向（增强拒绝）、负向（抑制拒绝）、无影响三类层，仅选择敏感度最高的正负向两层作为修复目标
- 仅在选中的两层上训练LoRA安全恢复适配器，其余层完全冻结，避免破坏下游任务所学知识
- 推理时基于最高正向敏感层的输出表示，计算query与恶意/良性参考集的相似度差得到恶意评分，超过阈值则激活安全适配器，否则直接使用微调后的业务模型

### 关键实验
在Llama3.1、Llama3、Qwen2.5、Mistral-v0.2四个模型，5个下游任务，4个有害基准集上测试，对比BDS、Antidote等7个SOTA基线。核心结果：Llama3.1/SST2场景下，平均有害得分从11.54降至0.08，下游准确率保持92.32与无防御SFT几乎一致；即使投毒比例高达0.9，有害得分仍接近0；仅需30条安全对齐数据即可达到最优防御效果。

### 最值得记住的一句话
LLM的安全拒绝能力仅由少数几层控制，针对性修复这几层即可在几乎不损失业务性能的前提下实现高效安全加固。
