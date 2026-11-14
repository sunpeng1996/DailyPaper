---
title: Shortcuts or Memorisation? Revisiting Data Corruption in Natural Language Understanding
  with Large Language Models
title_zh: 《捷径还是记忆？重新审视大语言模型自然语言理解中的数据扰动问题》
authors:
- Aarne Talman
- Stergios Chatzikyriakidis
affiliations:
- University of Helsinki
- Institute of Language and Speech Processing, Athena Research Centre
arxiv_id: '2611.16843'
url: https://arxiv.org/abs/2611.16843
pdf_url: https://arxiv.org/pdf/2611.16843
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: 大语言模型 · 基准鲁棒性分析
tags:
- LLM
- Natural Language Understanding
- Benchmark
- Robustness
- Data Perturbation
one_liner: 通过扰动实验证明LLM在NLI基准上的鲁棒性源于数据集捷径而非预训练记忆
practical_value: '- 落地LLM相关任务时，避免使用带明显模式捷径的标注数据集做效果验证，否则上线后泛化性会大幅低于测试表现

  - 电商/搜索场景的Query理解、语义匹配模型优化时，可通过词类消融、语序扰动等方法排查模型是否学到真实语义而非数据集捷径

  - 搭建LLM驱动的Agent推理模块时，优先加入CoT等前置推理步骤，可显著降低模型依赖任务模式捷径盲答的概率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
此前研究发现微调编码器在NLI等语言理解任务上，输入被扰动（如移除名词、打乱语序）后仍能保持较高准确率，但LLM是否存在相同特性、背后原因是预训练记忆了benchmark还是数据集捷径尚不明确。
### 方法关键点
对8款LLM及微调编码器在GLUE、三轮ANLI数据集上开展扰动实验（移除名词/功能词、语序打乱），同时检测预训练数据n-gram重合度，额外构造368条全新人工验证、无预训练曝光的样本做对照验证。
### 关键结果数字
- 直接作答的LLM在MNLI数据集移除名词后仍保留36-72%的超随机性能，同条件下ANLI数据集仅保留14-29%
- 新增无曝光样本中，带MNLI风格提示的样本移除名词后性能保留率远高于无提示样本，移除功能词后该优势反转
- 未发现预训练数据暴露和扰动鲁棒性的关联，仅加入前置推理步骤的模型不受上述模式影响
