---
title: 'LOCI: A Locator-Critic with Refinement Loop'
title_zh: LOCI：带迭代优化回路的定位器-验证器多智能体框架
authors:
- Walid Bousselham
- Mathilde Caron
- Arsha Nagrani
- Cordelia Schmid
affiliations:
- Google DeepMind
arxiv_id: '2608.30959'
url: https://arxiv.org/abs/2608.30959
pdf_url: https://arxiv.org/pdf/2608.30959
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: 多智能体协作 · 视觉推理优化
tags:
- MultiAgent
- Training-Free
- VLM
- VisualReasoning
- Actor-Critic
one_liner: 训练免的定位-验证解耦多智能体框架，大幅提升VLM复杂视觉推理表现
practical_value: '- 电商商品智能QA、合规审核等细粒度视觉理解场景，可直接复用Locator-Critic解耦架构：Locator负责裁剪商品图关键区域，Critic仅基于图像+问题做验证，不接收Locator的文本推理，避免认知偏差，显著降低看错商品细节的错误率

  - 高价值场景可启用多Locator并行探索，通过增加搜索多样性提升准确率，配合动态早停策略（简单样本3轮内结束）平衡效果与推理成本，适合大促客服兜底、违规商品召回等业务

  - 全流程训练免，仅通过prompt区分两个Agent角色，无需微调基础VLM，可快速适配新业务场景，大幅降低落地成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有VLM在复杂视觉推理任务上表现差，核心瓶颈不是推理能力，而是无法准确定位图像中关键细节；且单模型同时做证据定位和验证会出现认知固化，容易基于错误的视觉感知生成看似合理的错误结论，限制了VLM在电商QA、内容审核等需要高准确率视觉理解场景的落地。

### 方法关键点
- 训练免框架，同一个基础VLM通过不同prompt拆分为两个独立Agent：Locator负责生成Python代码裁剪图像区域，收集回答所需的视觉证据；Critic仅接收裁剪后的图像和原始问题，不接触Locator的文本推理，判断证据是否足够回答问题，不足则给出明确优化反馈。
- 两个Agent形成迭代优化回路，直到Critic判定证据足够，再由Locator输出最终答案。
- 支持多Locator并行拓展：多个Locator同时独立探索图像区域，Critic统一评估所有裁剪结果，提升搜索多样性，避免单个Locator陷入局部错误。

### 关键结果
在V*、HR-Bench、VisualProbe-Hard三个复杂视觉推理基准上，开源模型Qwen3-VL分别提升12.1、5.8、11.2个点，闭源模型Gemini 2.5 Pro分别提升8.9、4.3、4.8个点，显著超过SOTA。Ablation显示Critic不接收Locator文本推理是核心设计，去掉该约束性能下降2个点以上；8个并行Locator的版本在V*基准上准确率达到96.0%，比单Locator高3.3个点。

### 最值得记住的一句话
感知类任务的核心瓶颈往往不是推理能力，而是精准定位证据的能力，解耦探索和验证环节、避免验证模块被生成模块的推理误导，是提升系统鲁棒性的关键。
