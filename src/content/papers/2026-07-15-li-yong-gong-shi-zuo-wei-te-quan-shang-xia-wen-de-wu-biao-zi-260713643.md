---
title: Consensus as Privileged Context for Label-Free Self-Distillation
title_zh: 利用共识作为特权上下文的无标签自蒸馏框架CANON
authors:
- John Gkountouras
- Josip Jukić
- Ivan Titov
affiliations:
- University of Amsterdam
- University of Edinburgh
arxiv_id: '2607.13643'
url: https://arxiv.org/abs/2607.13643
pdf_url: https://arxiv.org/pdf/2607.13643
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 大模型无标签训练 · 自蒸馏
tags:
- Self-Distillation
- Label-Free Training
- Consensus
- Reasoning
- LoRA
- Privileged Context
one_liner: 提出无标签自蒸馏框架CANON，将模型自生成的多数共识转为稠密token级监督，算力仅为无标签RL的1/7且性能更优
practical_value: '- 业务中无标注数据充足的场景（如用户query理解、商品属性推理、规则类Agent问答），可复用CANON的无标签训练思路：采样多输出取共识后做token级自蒸馏，无需标注即可提升小模型性能，节省标注成本

  - 无需RL复杂迭代流程，仅需1次生成+单epoch微调即可拿到收益，算力仅为无标签RL的1/7，适合业务端快速迭代垂直领域小模型

  - 可复用共识质量判断规则：先统计base模型单样本pass@1与多数投票准确率的gap，gap越大的场景该方法收益越高，饱和场景无需浪费算力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有无标签提升LLM推理性能的方案普遍对共识信号利用不充分：自一致性投票仅在推理阶段生效，基于共识的RL、偏好优化等训练方法仅将共识压缩为标量奖励、过滤规则或偏好对，浪费了共识解中的大量结构化信息，且RL类方法需要多轮生成迭代，算力开销极高；而效果更优的特权上下文自蒸馏依赖金标数据，无法在无标注场景落地。

### 方法关键点
- 对每个无标注prompt，采样N条rollout，提取多数答案，从命中该答案的rollout中选择平均token对数似然最高的作为共识解
- 取模型初始状态的冻结快照作为教师，将共识解作为特权上下文输入教师，教师对所有学生rollout输出逐token的next-token分布
- 学生通过LoRA微调，训练目标为最小化自身逐token分布与教师分布的JSD，仅需1次生成+单epoch训练，梯度不回传教师

### 关键结果
在AMC、AIME、GPQA、MATH500等数学/科学推理基准上测试：
- 直推场景下，CANON较base模型pass@1最高提升12个百分点，比无标签RL方法高6个百分点，算力仅为后者的1/7，性能接近金标特权上下文蒸馏
- 归纳场景下，在混合无标签数据集训练的CANON，迁移到未见过的测试集时性能与金标训练方法持平
- 收益不只是分布锐化：训练后模型可解决之前32次采样均未命中的问题，多数投票准确率同步提升2~3个百分点

**最值得记住的一句话**：在有可提取明确答案的场景下，小模型自身的多数共识几乎可替代金标作为自蒸馏的特权上下文，以极低算力拿到接近有监督训练的收益
