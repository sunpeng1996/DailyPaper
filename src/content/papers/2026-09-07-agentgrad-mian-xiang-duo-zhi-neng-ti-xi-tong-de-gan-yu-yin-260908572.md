---
title: 'AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems'
title_zh: AgentGrad：面向多智能体系统的干预引导式Prompt优化框架
authors:
- Jaewon Chu
- Jinwoo Seo
- Jaewon Cho
- Jeehye Na
- Yunyang Xiong
- Youngdae Kim
- Hyunwoo J. Kim
affiliations:
- Korea University
- KAIST
- Meta AI
- UNIST
arxiv_id: '2609.08572'
url: https://arxiv.org/abs/2609.08572
pdf_url: https://arxiv.org/pdf/2609.08572
published: '2026-09-07'
collected: '2026-09-10'
category: MultiAgent
direction: 多智能体系统 · Prompt自动优化
tags:
- Multi-Agent
- Prompt Optimization
- Textual Gradient
- Intervention
- LLM
one_liner: 通过顺序干预定位故障智能体+语义梯度抽象实现多智能体Prompt高效优化，性能SOTA且提速2.5倍
practical_value: '- 电商多Agent链路（意图理解+召回+文案生成等）的Prompt优化可复用反向顺序干预策略，快速定位故障Agent，避免全链路盲目调优，大幅降低优化成本

  - 文本梯度聚合阶段无需随机拼接梯度，可按语义聚类生成通用梯度，避免不同故障模式的信号冲突，提升优化后Prompt的泛化性

  - Prompt迭代可优先处理覆盖故障样本多的梯度，先解决共性问题再处理个例，能进一步提升优化效率

  '
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动多智能体系统（MAS）的性能高度依赖各Agent的Prompt设计，传统文本梯度类Prompt优化方法存在两大核心痛点：梯度提取阶段无法定位真正导致系统故障的Agent，也缺乏Agent级别的细粒度监督信号；梯度聚合阶段随机拼接不同故障模式的梯度，导致更新方向混乱、优化后Prompt泛化性差，且整体迭代成本极高。

### 方法关键点
- **顺序干预定位故障Agent**：对失败样本按执行顺序反向逐个给Agent注入引导hint，验证单个Agent修正后能否解决故障，锁定目标Agent，同时将干预后的正确输出作为Agent级伪标签，生成细粒度文本梯度
- **语义文本梯度抽象**：将同一Agent的样本级梯度按语义聚类为小批量，每个簇抽象为一条通用梯度，避免不同故障模式的信号混合；聚类大小采用循环调度，兼顾共性规则与个性化修正
- **梯度更新校验**：按簇覆盖的样本数从大到小更新Prompt，先在对应簇样本上验证生效，再通过验证集校验泛化性后才正式更新

### 关键实验
在HotpotQA、HoVer、IFBench、PUPA、MATH共5个MAS基准上测试，对比MIPROv2、TextGrad、GEPA三大SOTA基线：使用GPT-5-mini时平均比无优化基线高11.76个百分点，比次优GEPA平均高2.52个百分点，整体优化耗时平均比次快基线低2.5倍；使用开源Qwen3-8B时同样实现SOTA，平均比无优化基线高9.67个百分点；优化后的Prompt跨同领域未见过的基准也表现最优。

最值得记住的一句话：多智能体Prompt优化的核心是把故障归因做准，针对性的细粒度更新远好于全链路无差别调优，既能提效果还能降成本
