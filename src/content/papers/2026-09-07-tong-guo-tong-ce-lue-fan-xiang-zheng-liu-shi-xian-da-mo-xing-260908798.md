---
title: Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation
title_zh: 通过同策略反向蒸馏实现大模型弱到强泛化
authors:
- Youngrok Park
- Sangmin Bae
- Hojung Jung
- Jongwoo Ko
- Yunseon Choi
- Young Jin Kim
- Pashmina Cameron
- Aaron Courville
- Se-Young Yun
affiliations:
- KAIST AI
- Microsoft
- University of Toronto
- Mila
- Université de Montréal
arxiv_id: '2609.08798'
url: https://arxiv.org/abs/2609.08798
pdf_url: https://arxiv.org/pdf/2609.08798
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: 大模型训练 · 弱到强泛化 知识蒸馏
tags:
- Knowledge-Distillation
- Weak-to-Strong
- On-Policy
- RLVR
- Policy-Gradient
one_liner: 提出同策略反向蒸馏OPRD，利用弱教师策略偏移加速学生训练并突破教师性能上限
practical_value: '- 做LLM4Rec/Agent的小模型蒸馏到大模型场景时，可用OPRD替代传统OPD，避免被小教师能力上限锁死，同时提升33%+训练样本效率

  - 多垂类电商推荐小模型合并为统一大模型时，OPRD的梯度投影放大机制可减少跨任务冲突，最终性能可超过所有单领域教师

  - 基于GRPO的推荐排序RL优化场景，可引入旧版本上线模型的策略偏移作为梯度放大方向，降低训练步数，加快迭代上线

  - 工程上OPRD仅增加小模型前向和梯度投影操作，开销仅比GRPO高12%左右，可低成本接入现有RL训练流水线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统知识蒸馏将弱教师输出作为直接优化目标，会给学生模型强加能力天花板，而从头训练大模型的算力成本极高；在跨代模型迁移、多领域小模型合并两类落地场景中，亟需既能复用小模型已训练收益，又不限制大模型最终性能上限的蒸馏方法。

### 方法关键点
- 计算弱教师相对于其预训练参考策略的policy shift，仅取单位方向向量，不直接匹配教师的最终输出分布
- 对学生基于RLVR的policy gradient做分解，仅放大与教师shift方向对齐的分量，正交分量保持不变，完整保留原优化目标的stationary points
- 负对齐分量（学生梯度与教师方向相反）采用warmup策略，前期优先复用教师经验，后期支持学生突破教师能力限制
- 原生适配单教师跨代迁移、多教师领域合并两种场景，无需修改训练数据和Reward定义

### 关键实验
在数学推理、逻辑推理任务上验证：单教师4B→8B跨代迁移场景，比GRPO少33%~67%更新步数达到教师性能，早期checkpoint最高提升22.7pp，最终平均性能超过最优基准10.8pp；多教师4个4B垂类小模型合并为8B大模型场景，比Mix-RL少55%更新步数达到教师水平，最终性能超过所有单领域specialist 14.12pp；强到弱蒸馏场景同样超过OPD基准最高29.2pp。

最值得记住的一句话：蒸馏的核心是复用教师的优化方向而非直接模仿教师输出，才能既降低训练成本又不被教师能力上限束缚。
