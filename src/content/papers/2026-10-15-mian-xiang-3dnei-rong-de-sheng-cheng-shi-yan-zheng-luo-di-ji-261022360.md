---
title: Grounding Generative Verification in 3D Content
title_zh: 面向3D内容的生成式验证落地技术研究
authors:
- Shuanglin Li
- Jiaying Lin
- Shuquan Ye
affiliations:
- Southeast University
- Shenzhen Loop Area Institute
- The Hong Kong University of Science and Technology
arxiv_id: '2610.22360'
url: https://arxiv.org/abs/2610.22360
pdf_url: https://arxiv.org/pdf/2610.22360
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态大模型 · 3D内容生成验证
tags:
- MLLM
- 3D Generation
- Verification Benchmark
- Multimodal Reasoning
- Data Pipeline
one_liner: 提出3D内容验证基准、可扩展训练数据流水线与验证驱动的生成优化框架
practical_value: '- 验证反馈+递归迭代的优化思路可直接复用在生成式推荐场景，比如商品3D素材、营销文案生成的合规性校验与迭代修正，降低错误内容曝光率

  - 多视角事实抽取+反事实标注的流水线可迁移至多模态电商内容训练数据构造，尤其是3D商品展示素材的高质量标注，降低人工成本

  - 候选池择优的验证范式可用于GenRec的生成结果粗筛，大幅提升生成物品/内容的事实准确率，减少幻觉'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型与3D生成技术仅关注视觉保真度，缺乏基于3D证据的任务特异性正确性校验能力，无法定位输出不符合要求的原因并迭代优化。
### 方法关键点
1. 构建覆盖10类任务的3DVerifierBench基准，评估模型的验证决策、拒识解释、规格与候选变更响应能力
2. 提出可扩展训练数据流水线，融合多视角事实抽取、可控3D编辑、原生标注，生成14126条带矛盾解释和关联反事实的训练样本
3. 探索验证反馈在3D生成中的落地路径：候选择优、递归迭代优化
### 关键结果
- 最强基线GPT-6 Astra与人类验证性能差距达21.6个百分点
- 16候选池的oracle选择可将事实完全准确率从26.7%提升至90.0%
- 人类引导的递归优化可100%满足全部7项要求，远优于Oracle@8仅满足3项的水平
