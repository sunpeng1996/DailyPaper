---
title: A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications
  in AI Governance
title_zh: 训练后模型适配技术六维度分类框架及其在AI治理中的应用
authors:
- Fardin Afdideh
- Fernando Seoane
- Farhad Abtahi
affiliations:
- Karolinska Institutet
- Karolinska University Hospital
- University of Borås
- KTH Royal Institute of Technology
arxiv_id: '2608.06246'
url: https://arxiv.org/abs/2608.06246
pdf_url: https://arxiv.org/pdf/2608.06246
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 训练后模型适配 · 分类框架与治理对齐
tags:
- Post-Training Adaptation
- Taxonomy
- AI Governance
- PEFT
- RAG
one_liner: 提出覆盖48种适配技术的六维度分类体系，解决术语歧义并对齐AI监管要求
practical_value: '- 可直接复用六维度框架梳理团队常用的LoRA、RAG、Prompt Tuning等适配技术的边界，统一内部术语定义，降低跨角色协作成本

  - 针对出海电商/广告等合规要求高的场景，可通过框架的监管映射能力快速判定不同适配操作是否触发EU AI Act等法规的「重大修改」申报义务，规避合规风险

  - LLM驱动的推荐/Agent系统选型时，可通过D3（数据要求）、D4（持久性）、D5（修改范围）三个维度快速过滤适配方案：短期临时需求优先选RAG/提示词（无参数修改、会话级生效），长期领域适配优先选LoRA（局部参数修改、版本级持久化）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前训练后适配技术（从全量微调、PEFT到RAG、模型编辑、对齐等）碎片化严重，存在三大核心问题：一是术语歧义，同一术语（如Fine-Tuning）对应完全不同的技术实现；二是现有单/双维度分类无法覆盖技术的多属性本质，易混淆技术边界；三是未考虑模型类型差异（传统ML到MLLM）导致的适配方案适用性差异，同时无法对齐EU AI Act、FDA PCCP等AI监管要求，给技术选型、变更管控、合规申报带来极大障碍。
### 方法关键点
- 提出六维度分类框架：5个特征维度分别为D1（修改机制：参数更新/上下文注入/激活操纵等）、D2（适配目标：漂移修复/领域适配/安全对齐/知识更新等）、D3（数据要求：标注数据量/偏好对/零样本等）、D4（生效持久性：永久/版本级/会话级/临时等）、D5（修改范围：全模型/局部模块化/输入层无参数修改等），第6个调制维度D6为目标模型类型，用来过滤适配方案的可行性。
- 覆盖48种主流训练后适配技术，每个技术对应明确的六维度坐标，梳理技术间的继承、替代、混合、分层部署关系。
- 额外提供监管映射能力，将六维度属性对齐NIST AI风险管理框架、EU AI Act、FDA PCCP等主流监管要求。
### 关键结果
相比现有适配技术综述，本框架覆盖技术数量从最多15种提升至48种，分类维度从最多3个提升至6个，是首个同时覆盖从传统机器学习到多模态大模型全谱系、同时关联AI监管要求的分类体系。
### 核心洞见
任何适配技术都不是单属性的，选型时需要结合业务目标、数据可用性、生效时长要求、修改范围约束、合规要求综合判断。
