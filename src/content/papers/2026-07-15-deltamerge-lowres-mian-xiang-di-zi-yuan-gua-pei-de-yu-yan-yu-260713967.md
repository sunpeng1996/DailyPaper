---
title: 'DeltaMerge-LowRes: Composing Language and Task Deltas for Low-Resource Adaptation'
title_zh: DeltaMerge-LowRes：面向低资源适配的语言与任务Delta组合方法
authors:
- Son Ha Xuan
- Xuan-Bach Le
- Phat T. Tran-Truong
affiliations:
- RMIT University Vietnam
- Ho Chi Minh City University of Technology (HCMUT)
arxiv_id: '2607.13967'
url: https://arxiv.org/abs/2607.13967
pdf_url: https://arxiv.org/pdf/2607.13967
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 低资源NLP · 模型Delta合并适配
tags:
- LoRA
- model merging
- low-resource NLP
- parameter-efficient fine-tuning
- TIES-merging
one_liner: 提出4种语言与任务Delta组合规则，低资源场景下无需联合微调即可适配新语言新任务
practical_value: '- 跨域适配可复用Delta合并思路：电商场景下可分别训练语种/垂域Delta和排序/生成任务Delta，无需联合微调即可快速适配小语种/新垂域业务，大幅降低训练成本

  - 不同任务匹配对应合并规则：生成类任务（商品标题生成、营销文案生成）优先用跨轴TIES合并，分类任务（商品类目预测、用户意图识别）优先用sparsity-aware合并提升校准度，减少预测置信度偏差

  - 低资源冷启动场景可复用框架：新市场/新业务仅有少量标注数据时，先用无标注语料训练垂域/语种Delta，再用通用标注数据训练任务Delta，合并后快速上线，降低冷启动标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有低资源场景下将多语言编码器适配到新语言+新任务的方案，通常需要针对每个语言-任务对单独做端到端微调，依赖小样本标注集的泛化能力，训练成本高、复用性差。此前模型合并研究多针对同语言下的多任务Delta组合，未探索语言、任务两个独立轴的Delta组合方案。

### 方法关键点
- 框架设计：独立训练两类LoRA式Delta：语言Delta∆L用目标语言无标注单语文本做继续预训练得到，任务Delta∆T用英文标注数据做任务微调得到，两类Delta训练完成后仅需无数据的权重空间合并即可得到适配目标语言-任务对的模型，无额外推理开销。
- 对比4种合并规则：1）加法合并：全局加权相加两类Delta；2）激活引导合并：基于50条探针句的层激活偏移量做逐层加权；3）稀疏感知合并：保留两类Delta联合幅度前20%的参数，其余置零；4）跨轴TIES：将原TIES合并的修剪、符号选举、合并步骤适配到语言-任务Delta对，过滤两类Delta符号冲突的参数。

### 关键结果
基于XLM-R和mT5底座，在4类任务（分类、NER、抽取式QA、摘要）、4种非洲低资源语言上测试，所有任务Delta仅用256条英文标注数据训练。核心结果：跨轴TIES在摘要任务上比仅用任务Delta的baseline提升4.79 chrF，3/4语言提升4-7 chrF；QA任务F1提升2.32、EM提升2.91；稀疏感知合并在分类任务上保持macro-F1持平的同时，ECE相对降低36%，大幅提升校准度。

最值得记住的结论：Delta合并的效果核心取决于规则与任务特性的匹配度，当任务需要语言和任务信号在每一步输出紧密配合时，跨轴TIES的冲突过滤机制收益最高。
