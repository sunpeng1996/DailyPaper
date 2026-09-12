---
title: The Eloquence submission for Task 2 of the Interspeech 2026 MLC-SLM challenge
title_zh: Interspeech 2026 MLC-SLM挑战赛任务2 Eloquence团队参赛方案
authors:
- Jordi Luque
- Lorenzo Concina
- Marco Matassoni
- Alessio Brutti
- Filippo Vella
affiliations:
- Telefónica Innovación Digital
- Fondazione Bruno Kessler
- Consiglio Nazionale delle Ricerche
arxiv_id: '2609.11724'
url: https://arxiv.org/abs/2609.11724
pdf_url: https://arxiv.org/pdf/2609.11724
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: 多语种口语问答 · Speech LLM优化
tags:
- Speech-LLM
- LoRA
- In-Context-Learning
- RAG
- Data-Augmentation
- Multilingual
one_liner: 针对21语种口语多选问答任务提出三类优化方案，最优Macro准确率达0.81
practical_value: '- 跨语言业务场景（如多语种电商客服、跨境推荐）可复用「LoRA微调+跨语言数据增强+ASR转录增强」组合trick，用小模型低成本实现多语言能力提升

  - 模型推理存在标签偏置问题时，可尝试用冻结大模型+多模态ICL的方式修正，无需额外训练即可获得明显效果提升

  - 垂类小场景冷启动可参考三层锚定记忆检索架构，不用训练即可实现基线以上效果，落地成本极低'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
Interspeech 2026 MLC-SLM挑战赛任务2要求覆盖21种语言的多语种口语多选问答，现有Speech LLM在多语种真实对话场景下存在训练资源分布不均、标签偏置、深层语义推理准确率不足等问题。
### 方法关键点
1. 基于Voxtral-Mini-3B做LoRA微调，配套跨语言数据增强、ASR转录增强、时间戳感知音频裁剪三类预处理优化
2. 冻结Voxtral-24B大模型，采用多模态ICL缓解数据集自带的强标签偏置问题
3. 训练免检索系统，基于融合声学身份、语义内容、知识图谱的三层语音锚定记忆架构实现推理
### 关键结果数字
微调小模型Phase2评测Macro准确率0.72，多模态ICL大模型达0.81（最优成绩），无训练检索系统达0.68，三类方案均大幅超过官方基线
