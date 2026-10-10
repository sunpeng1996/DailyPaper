---
title: 'Frozen Models, Evolving Expertise: Model-Agnostic Learning from Deployment
  Experience for Multimodal Medical AI'
title_zh: 无需微调的模型无关框架：让冻结LLM/VLM从部署经验持续进化
authors:
- Yexiao He
- Yucheng Tang
- Pengfei Guo
- Yufan He
- Andriy Myronenko
- Can Zhao
- Ang Li
- Daguang Xu
- Dong Yang
affiliations:
- University of Maryland, College Park
- NVIDIA
arxiv_id: '2610.09146'
url: https://arxiv.org/abs/2610.09146
pdf_url: https://arxiv.org/pdf/2610.09146
published: '2026-10-05'
collected: '2026-10-10'
category: LLM
direction: 冻结LLM优化 · 无参数持续学习
tags:
- Frozen LLM
- External Memory
- Multimodal RAG
- Continual Learning
- Model Agnostic
one_liner: 无需修改模型参数，通过三类外部知识库+动态验证策略让冻结LLM/VLM持续提升性能
practical_value: '- 电商/广告生成式推荐Agent可复用三类外部知识库设计：Skill库沉淀通用推理规则（如大促优惠计算、品类搭配逻辑），Knowledge
  Memory存储合规/商品属性等确定性事实，Multimodal Knowledge Base保存高转化商品图、爆款文案参考案例，无需微调底座即可适配业务变化

  - 可直接复用其更新验证策略：所有Skill/知识库更新必须同时在新流量batch和历史case buffer上达标（新流量收益>0、老流量无负向），避免规则迭代导致的业务波动，适配推荐系统线上灰度迭代需求

  - 电商多模态搜索/推荐RAG系统可参考MMKB使用逻辑：不直接拼接召回的多模态结果，额外引导LLM对比参考案例与当前query/user的匹配点、差异点，大幅降低多模态RAG的信息干扰'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM/VLM部署后通常冻结参数，无法从实际部署的交互反馈中持续迭代能力；微调需要模型权重权限、算力成本高，现有无参数更新方法要么易过拟合固定验证集，要么多模态场景下仅存文本丢失视觉细节，在知识迭代快的医疗、电商等领域痛点尤其突出。

### 方法关键点
- 维护三类外部异构知识库：① Skill库：沉淀可复用的推理、工具调用规则，每批次基于高分轨迹全量重写而非追加，避免规则冲突与上下文膨胀；② Knowledge Memory：存储带可信证据的确定性事实，调用时自动校验与当前任务的匹配性；③ Multimodal Knowledge Base（MMKB）：存储带标注的多模态历史案例，通过图文联合embedding召回，引导模型主动对比参考案例与当前输入的异同。
- 动态更新校验机制：每批次知识库更新必须同时在新case批次和历史case buffer上满足：新case平均收益>0且胜场≥负场，历史case平均收益≥0且胜场≥负场，才会正式上线，避免过拟合。

### 关键实验
在6个覆盖临床诊断、多模态推理的基准上测试4款开源/闭源底座模型，对比Base、ACE、SkillOpt等基线，医疗任务性能最高提升34.2%，非医疗多模态任务最高提升81.9%；冻结后泛化到unseen case平均提升20.7%，沉淀的知识跨模型零样本迁移平均提升20.0%。

最值得记住的一句话：无需微调模型参数，仅通过结构化外部知识沉淀与严格的更新校验，就能让冻结模型在特定任务上获得持续的性能提升。
