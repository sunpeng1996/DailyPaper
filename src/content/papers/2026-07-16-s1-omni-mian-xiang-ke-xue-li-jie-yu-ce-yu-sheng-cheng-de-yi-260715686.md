---
title: 'S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding,
  Prediction, and Generation'
title_zh: S1-Omni：面向科学理解、预测与生成的统一多模态推理模型
authors:
- Jiahao Zhao
- Junyi Liu
- Lifeng Xu
- Nan Xu
- Qingli Wang
- Qingxiao Li
- Tianle Chen
- Xiaoyu Wu
- Yawen Zheng
- Zikai Wang
affiliations:
- ScienceOne AI
- Wenge AI
arxiv_id: '2607.15686'
url: https://arxiv.org/abs/2607.15686
pdf_url: https://arxiv.org/pdf/2607.15686
published: '2026-07-16'
collected: '2026-07-20'
category: Multimodal
direction: 多模态统一推理 · 科学大模型
tags:
- Multimodal
- Unified-Representation
- LLM
- Reasoning
- AI4S
one_liner: 提出统一多模态科学推理模型S1-Omni，多数基准性能超GPT-5.5、Gemini-3.1-Pro
practical_value: '- 核心为AI4S领域学术贡献，电商/推荐/Agent业务直接可复用性较低

  - 异构数据统一映射到共享表征空间的思路可参考用于跨域多模态商品特征融合

  - 知识对齐+任务特定解码的三段式架构可借鉴实现推荐多目标任务统一建模'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有AI4S领域模型能力高度碎片化，无法实现异构数据、科学规律、专家知识的联合建模，限制了跨任务通用科学推理能力落地。
### 方法关键点
架构包含三大核心模块：1）科学数据统一表征：将自然语言指令、CIF、SMILES、蛋白序列、光谱、科学图像等异构数据映射到共享表征空间；2）自然世界知识对齐：在数据构造与训练阶段融入科学规律与专家知识，支撑证据驱动的科学推理；3）领域任务特定解码：适配不同下游任务输出要求，覆盖预测、生成等多类应用。
### 关键结果数字
基于覆盖200类科学任务、百万级推理样本的S1-Omni-Corpus训练，在60+科学基准上测评，多数任务表现优于GPT-5.5、Gemini-3.1-Pro，部分基准持平或超越领域专用模型。
