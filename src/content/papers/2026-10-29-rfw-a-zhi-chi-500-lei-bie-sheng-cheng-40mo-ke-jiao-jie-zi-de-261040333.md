---
title: 'RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories'
title_zh: RFW-A：支持500+类别生成40万可铰接资产的智能体生成框架
authors:
- Yuanbo Lyu
- Changjian Pan
- Saining Zhang
- Yi Yang
- Peishuo Li
- Zhiheng Li
- Jialu Liu
- Junhao Chen
- Jiawei Weng
- Yupeng Gao
affiliations:
- Alibaba Group
- Tsinghua University
- Peking University
- Nanyang Technological University
- The Hong Kong University of Science and Technology
arxiv_id: '2610.40333'
url: https://arxiv.org/abs/2610.40333
pdf_url: https://arxiv.org/pdf/2610.40333
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: Agent 程序化资产生成范式优化
tags:
- Agent
- Procedural Generation
- Asset Generation
- Program Synthesis
- Embodied AI
one_liner: 结合Agent合成与程序化生成范式，低成本构建超40万500+类别的高可用可铰接资产库
practical_value: '- 大规模同品类内容生成场景（如电商3D商品资产、品类化文案批量生成）可复用「同品类逻辑抽象+Agent生成可复用生成器+批量执行」范式，大幅降低LLM
  API调用成本

  - 可迁移成本摊销思路：将Agent推理成本分摊到同品类大量生成样本上，对比单样本调用Agent的方案，单样本生成成本可降低96%以上

  - 批量内容生成的有效性校验可参考「跨配置/状态采样测试+Agent自动迭代修正」方案，无需人工介入即可保障生成内容的合格率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高质量可铰接资产是具身感知、仿真、操作任务的核心基础，传统人工标注、单样本Agent合成方案分别存在人力成本高、LLM调用成本重复浪费的问题，无法支撑大规模资产构建需求。

### 方法
基于同类别资产共享构建逻辑的核心观察，结合Agent合成与程序化生成的互补优势：由Agent将同品类资产的构建逻辑抽象为分类别的可复用生成器，通过跨配置、跨运动状态的采样测试迭代修正生成器；验证通过后的生成器可直接批量生成同品类多样化资产，无需额外LLM调用。

### 结果
单品类生成器平均开发成本为$10.62，生成200个资产时单资产成本摊销至$0.05，较单样本Agent合成基线的$1.24成本降低96%；已构建覆盖500+类别、超40万可直接用于仿真的高有效性资产库，用该数据集训练的模型在关节估计任务、零样本真实场景迁移任务上均实现性能提升。
