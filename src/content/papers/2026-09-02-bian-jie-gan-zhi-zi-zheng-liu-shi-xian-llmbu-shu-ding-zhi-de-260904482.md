---
title: Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety
  Refusal
title_zh: 边界感知自蒸馏：实现LLM部署定制化的可控安全拒绝
authors:
- Alejo López-Ávila
- Iker García-Ferrero
- Jezabel Garcia
- Antonio Tiene
- Román Orús
affiliations:
- Multiverse Computing
arxiv_id: '2609.04482'
url: https://arxiv.org/abs/2609.04482
pdf_url: https://arxiv.org/pdf/2609.04482
published: '2026-09-02'
collected: '2026-09-09'
category: LLM
direction: LLM安全对齐 · 定制化拒绝边界
tags:
- LLM Safety
- Self-Distillation
- LoRA
- Alignment
- Over-Refusal
one_liner: 提出覆盖修复+边界对数据的自蒸馏框架，实现LLM部署定制化安全对齐，显著降低过度拒绝率
practical_value: '- 垂类Agent（电商客服、内容导购）可复用窄边界对齐范式：无需全量拦截敏感主题，通过构建领域内「需拦截请求/需回答请求」边界对数据微调LoRA，精准控制拦截范围，既规避合规风险，又不影响正常用户请求响应

  - 训练数据补全trick：自生成训练数据时可采用多级重试+通用模板补全策略，解决单次生成漏覆盖难例的问题，提升边缘case的处理效果

  - 过度拒绝优化方案：生成式推荐/客服场景的过度拒绝问题，可通过加入「表面敏感但实际合法」的FakeHarm类样本做前向KL正则，同时用本模型生成的合规回答替换外部数据集，可将过度拒绝率降低60%以上，且对安全效果影响极小'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM安全对齐普遍采用粗粒度主题级拦截，无法满足部署定制化需求：例如政务服务Agent需要拒绝政治操纵类请求，但必须正常回答选举事实类问题，现有方案要么全量拦截整个敏感主题，要么出现大量过度拒绝合法请求的问题；同时自生成安全训练数据存在19.88%的难例覆盖率缺口，边界效果缺乏有效评估手段。
### 方法关键点
- 提出窄边界安全对齐范式：无需拦截完整主题，仅拦截主题内指定有害子集，保留良性子集的回答能力
- 数据覆盖修复：通过Escalate多级重试+Graft通用拒绝补全策略，将自生成拒绝数据的覆盖率缺口从19.88%降至0.20%
- 边界感知数据构造：生成语义高度相近的有害-良性边界对，搭配表面敏感实际合法的FakeHarm样本；训练时有害样本用交叉熵，良性样本用和基线模型的前向KL正则，精准控制拒绝边界
- 双维度评估体系：同时评估有害内容拒绝率和良性内容过度拒绝率，避免只追求安全指标牺牲可用性
### 关键结果
基于Qwen3-8B+LoRA训练，政治领域目标有害请求拒绝率从9.47%提升至84.75%，跨领域有害内容平均响应率从26.26%降至0.14%；使用本模型生成的合规数据替换外部数据集，XSTest过度拒绝率从15.20%降至5.20%；加入边界对数据后，边界处良性样本过度拒绝率从32.94%降至4.16%，仅带来4.16%的有害样本拒绝率损失。
> 核心结论：安全对齐不能仅追求单一有害拒绝率，数据组合直接决定安全与可用性的trade-off，必须同时评估拒绝边界两侧的表现。
