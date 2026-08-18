---
title: Architecture-Dependent Causal Transfer of Activation States Across Large Language
  Models
title_zh: 大语言模型跨架构激活状态的因果迁移特性研究
authors:
- Fernando Cardenas Piepereit
affiliations:
- Velez-Malaga, Spain
arxiv_id: '2608.16347'
url: https://arxiv.org/abs/2608.16347
pdf_url: https://arxiv.org/pdf/2608.16347
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: LLM 跨模型激活状态迁移
tags:
- Activation State Transfer
- Representational Alignment
- Causal Intervention
- Cross-LLM Communication
- Mutual k-NN
one_liner: 验证仅同架构族大模型可通过学习投影实现有限的激活状态因果迁移
practical_value: '- 多Agent系统通信优化：同架构族小模型可通过学习MLP投影做激活级通信，替代自然语言中转，降低token成本和latency，适合电商导购多端Agent协同场景

  - 跨模型迁移工程Trick：计算跨模型表征对齐优先用mutual k-NN而非CKA/Procrustes，避免高幅值激活outliers干扰结果；激活注入时避开位置0的attention
  sink，选择多token占位符的最后位置注入，防止破坏注意力机制

  - 跨模型迁移效果预判：不要仅靠隐藏层表征对齐度判断迁移可行性，需做端到端生成级验证，不同规模/量化方式的模型即使表征对齐度高，也可能无法实现因果迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多AI系统交互依赖自然语言中转，存在编解码开销、token成本高、latency大的问题，若能直接交换内部激活状态可大幅降低overhead，但跨独立训练的不同架构LLM的激活迁移可行性尚未得到因果层面验证。

### 方法关键点
- 选择4款架构异构开源LLM：3款因果解码器架构（Qwen2-0.5B、Phi-3-mini、Mistral-7B）+1款编码解码器架构（FLAN-T5-base），覆盖不同厂商、参数量与注意力机制
- 三层递进验证：1）表征相似度分析，对比CKA、Procrustes、mutual k-NN三种对齐指标，设置随机初始化模型作为null baseline；2）训练MLP投影网络映射源模型隐藏态到目标模型空间，用top-1检索准确率评估投影效果；3）端到端因果注入实验，将投影后的激活注入目标模型中间层，对比负对照组验证生成层面的因果效应
- 工程优化：平均池化时排除因果模型的位置0激活（attention sink），激活注入采用逐层前向而非复用KV cache，避免张量维度错误

### 关键结果
- 表征对齐层面：因果解码器之间的中间层对齐度远高于与编码器架构的对齐度，mutual k-NN对激活outlier鲁棒性最优，训练后模型对齐度是随机初始化的3~6倍
- 投影检索层面：3组因果解码器对的top-1检索准确率达45%~50%，远高于5%的随机水平；FLAN-T5组仅为5%，和随机水平相当
- 端到端因果迁移层面：仅Qwen2-0.5B→Phi-3-mini组通过显著性检验，真实注入的检索准确率23.3%，负对照组为0%，p=0.047；其余两组指向Mistral-7B的迁移无显著效果，即使其投影检索准确率达50%

### 核心结论
LLM跨模型激活因果迁移仅在同架构族下有限可行，隐藏层表征对齐度无法直接预测生成层面的迁移效果
