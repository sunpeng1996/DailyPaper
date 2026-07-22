---
title: 'DAIS: Dependency-Aware Intermediate QA Supervision for Complex Reasoning'
title_zh: DAIS：面向复杂推理的依赖感知中间QA监督框架
authors:
- Yu Wang
- Ming Fan
- Xicheng Zhang
- Zhiyong Li
- Zhihu Wang
- Caiyue Xu
- Dahai Hu
- Ting Liu
affiliations:
- Xi'an Jiaotong University
- Huawei Technologies Ltd.
arxiv_id: '2607.19088'
url: https://arxiv.org/abs/2607.19088
pdf_url: https://arxiv.org/pdf/2607.19088
published: '2026-07-21'
collected: '2026-07-22'
category: Reasoning
direction: 大模型复杂推理 · 中间监督优化
tags:
- Chain-of-Thought
- Supervised Fine-Tuning
- Intermediate Supervision
- Complex Reasoning
- LLM
one_liner: 将教师CoT拆解为带依赖的中间QA监督信号，无需推理时改动即可提升LLM复杂推理准确率
practical_value: '- 电商/广告合规审核类Agent可直接复用DAIS的SFT构造流程：把合规判断的多步逻辑拆解为带依赖的中间QA对，小模型SFT后无需改动推理链路即可提升准确率，政策类任务最高可提5.6个点

  - 多步决策类推荐Agent（如长路径导购、复杂用户需求满足场景）可参考DAIS思路，把决策链拆为带依赖的中间监督信号，比平层CoT-SFT效果更好，且不需要增加推理时的外部控制器/分解模块

  - 垂类低资源场景下的小模型训练可借鉴DAIS的数据增强逻辑：10%的训练数据即可达到平层CoT全量数据的效果，大幅降低垂类标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有平层CoT监督将推理过程作为单一序列优化，无法显式建模局部结论对后续决策的支撑关系，导致CoT增益容易和目标长度、风格、模板模仿等噪声混淆，中间监督的价值未被充分挖掘，且现有方案往往需要推理时新增额外组件，落地成本高。

### 方法关键点
- 纯训练侧框架，推理时完全兼容原生任务范式，无需额外输入、中间标注、控制器或架构修改；
- 先过滤匹配金标的教师CoT，将其拆解为2-5个决策相关的局部子任务，聚类归纳得到数据集级子任务Schema；
- 每个子任务转为中间QA记录，后续子任务的输入拼接前置子任务的问答结果作为支撑上下文，最终答案记录保留原生任务格式，不接入任何中间状态；
- 所有中间QA记录和原生最终任务记录统一用标准自回归SFT目标训练，损失仅作用在输出侧。

### 关键结果
在GDPR/AIACT政策合规、MedQA医疗问答、FOLIO逻辑推理4个基准上测试，覆盖4款Qwen系列 backbone，对比Answer-only、平层CoT-SFT、无依赖中间QA等基线：政策合规任务上较最强基线最高提升5.6%、平均提升4.2%，16个测试配置中有15个达到最优效果；仅用10%训练数据即可达到平层CoT全量数据的准确率水平。

最值得记住的结论：中间推理文本本身不足以带来最优增益，有效建模早期局部结论对后续决策的支撑关系才能进一步提升SFT的监督效率。
