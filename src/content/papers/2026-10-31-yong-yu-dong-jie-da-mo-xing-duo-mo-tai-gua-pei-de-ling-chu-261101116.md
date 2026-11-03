---
title: Zero-Gated Cross-Attention
title_zh: 用于冻结大模型多模态适配的零初始化门控交叉注意力机制
authors:
- Basavaraj R M
- Manav Verma
affiliations:
- Independent Researcher
- HRS Group
arxiv_id: '2611.01116'
url: https://arxiv.org/abs/2611.01116
pdf_url: https://arxiv.org/pdf/2611.01116
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: LLM多模态适配 · 门控交叉注意力设计
tags:
- Cross-Attention
- Multimodal LLM
- Parameter Efficient Tuning
- Frozen LLM
- Gating Mechanism
one_liner: 提出零初始化门控交叉注意力桥IGCA，消除冻结LLM多模态注入的初始化扰动，提升训练效果
practical_value: '- 做多模态生成式推荐（如融合商品图/视频/用户语音输入的推荐）时，可复用IGCA的零初始化门控设计，避免跨模态信息注入破坏预训练LLM的分布，减少前期训练步数的浪费

  - 做冻结大模型的参数高效适配时，可引入该可学习标量门控机制，明确归因效果提升是来自跨模态对齐还是初始化扰动恢复，降低架构迭代的验证成本

  - 做电商Agent的多模态感知模块接入时，可参考IGCA的低侵入式设计，仅训练适配器和门控参数，无需改动大模型主干，大幅降低功能迭代的试错成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有冻结LLM的多模态注入方案采用随机初始化的交叉注意力适配器，训练初始阶段就会引入非零扰动，将LLM中间表示带离预训练分布：一方面破坏预训练模型原生能力，前期梯度需优先修复扰动，浪费训练算力；另一方面无法明确后续效果提升是来自跨模态对齐还是扰动恢复，归因困难，难以验证架构迭代的真实收益。
### 方法关键点
- 提出Inductively Gated Cross-Attention（IGCA），在交叉注意力输出与残差连接之间加入可学习标量门控α，α初始化为0，利用`tanh(0)=0`的性质保证训练初始时刻交叉注意力模块完全不生效，模型输出与原生冻结LLM完全一致
- 训练时仅更新IGCA的Q/K/V投影矩阵与门控α参数，LLM主干完全冻结，适配成本低
- 可作为多模态证据注入的核心接口，集成到Agent多阶段接地pipeline中
### 关键结果
在Falcon-40B的6个decoder层插入IGCA，共404亿可训练适配器参数，训练59500步后：
- 训练loss从3.9403降至0.0007
- 留出集最佳checkpoint loss为2.2201，较无门控基线的4.3469降低48.9%
- 平均留出集loss从4.3423降至2.2498，最佳checkpoint平均门控值仅0.0713，验证模块会渐进式启用跨模态能力
### 核心结论
冻结大模型跨模态适配的核心矛盾是「注入新信息」与「保留预训练分布」的平衡，零初始化门控是实现该平衡的低成本可落地方案
