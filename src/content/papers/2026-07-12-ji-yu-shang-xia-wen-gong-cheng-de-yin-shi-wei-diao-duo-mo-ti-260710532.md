---
title: 'Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework
  for Multimodal Entity Alignment'
title_zh: 基于上下文工程的隐式微调：多模态实体对齐课程学习框架
authors:
- Yunpeng Hong
- Chenyang Bu
- Di Wu
- Yi He
- Xindong Wu
affiliations:
- 合肥工业大学大数据知识工程教育部重点实验室
- 西南大学计算机与信息科学学院
- 威廉与玛丽学院数据科学系
arxiv_id: '2607.10532'
url: https://arxiv.org/abs/2607.10532
pdf_url: https://arxiv.org/pdf/2607.10532
published: '2026-07-12'
collected: '2026-07-14'
category: LLM
direction: LLM上下文工程 · 多模态实体对齐
tags:
- Multimodal Entity Alignment
- Context Engineering
- Curriculum Learning
- Fine-tuning
- LLM
one_liner: 证明多模态实体对齐中上下文工程等价于微调，提出渐进提示框架降本提效
practical_value: '- 电商同款商品匹配、跨模态实体对齐场景可直接复用三阶段渐进推理范式，优先用简单特征（如商品名）对齐高置信样本，低置信样本再补充属性/图片/关联商品特征，平均token消耗可降80%以上

  - 上下文工程与微调等价的结论可复用，无需调整LLM参数，仅通过结构化提示编排就能达到接近微调的效果，大幅降低小模型在实体匹配场景的落地成本

  - 自适应置信度阈值机制可迁移到LLM重排序、RAG问答等场景，动态判断是否需要注入额外上下文，平衡推理效率与效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态实体对齐（MMEA）的上下文工程策略多为黑盒启发式，高度依赖大参数LLM性能，既缺乏理论可解释性，又存在token消耗高、推理慢的问题，同时缺乏将成熟微调策略转化为提示设计的统一框架。

### 方法关键点
- 理论证明MMEA任务中LLM的softmax注意力计算与微调的线性注意力层数学等价，提示各组件对应隐式微调步骤，为提示设计提供理论依据
- 设计三阶段渐进推理流程：Stage I仅输入实体名做匹配，高置信结果直接输出；Stage II为低置信样本补充实体邻域结构信息；Stage III再引入多模态特征、知识图谱三元组做精细推理
- 自适应难度调制机制，基于历史预测的平均置信度动态调整当前阶段的置信阈值，避免固定阈值带来的误判

### 关键结果
在5个公开MMEA数据集上达到SOTA，ICWIKI数据集上，Qwen2.5-72B与14B的H@1差距仅0.6%；相比SOTA基线MM-ChatAlign，Qwen2.5-72B推理耗时从21小时降至1小时，token消耗从2200-300降至200-400，降幅超80%。

**最值得记住的一句话**：无需微调，仅通过符合课程学习逻辑的提示编排，即可显著降低LLM任务对参数规模的依赖，同时大幅压缩推理成本。
