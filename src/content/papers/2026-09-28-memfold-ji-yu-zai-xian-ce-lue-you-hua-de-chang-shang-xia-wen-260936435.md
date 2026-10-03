---
title: 'MemFold: Learning Compact Soft Memory for Long-Context Personalization via
  On-Policy Optimization'
title_zh: MemFold：基于在线策略优化的长上下文个性化紧凑软记忆框架
authors:
- Jingxuan Wu
- Yuzhe Yang
- Yiqiao Huang
- Chengzhi Liu
- Qingni Wang
- Chengxuan Qian
- Shutong Wu
- Jiawei Zhang
- Xin Eric Wang
affiliations:
- University of California, Santa Barbara
- University of North Carolina at Chapel Hill
- Harvard University
- University of Wisconsin–Madison
arxiv_id: '2609.36435'
url: https://arxiv.org/abs/2609.36435
pdf_url: https://arxiv.org/pdf/2609.36435
published: '2026-09-28'
collected: '2026-10-03'
category: Agent
direction: Agent 长时软记忆优化 · 策略蒸馏
tags:
- LongContext
- Personalization
- SoftMemory
- OnPolicyTraining
- KnowledgeDistillation
one_liner: 提出固定预算软记忆优化框架，通过在线策略蒸馏提升长上下文个性化性能
practical_value: '- 可复用置信度门控在线蒸馏范式训练业务中的用户记忆压缩模块：用全上下文冻结模型对学生的实际采样响应重打分，不需要标注参考序列，可直接用于电商导购Agent、个性化推荐的用户长历史压缩场景，减少偏好违背类错误

  - 软记忆预算无需盲目扩容：实验显示128~256个软向量即可达到最优效果，扩容到512反而精度下降，且推理成本随预算变化小于1%，业务中可直接取256作为默认配置平衡效果与开销

  - 长上下文个性化训练优先组合GRPO序列级任务奖励+token级蒸馏信号：GRPO贡献70%以上的性能收益，蒸馏补充细粒度信号，该范式可直接迁移到个性化文案生成、用户偏好动态建模等推荐/广告场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长上下文个性化记忆方案分为两类：全量保留文本会导致输入长度随交互历史线性增长，推理成本不可控；压缩为固定尺寸潜向量的方案，训练时仅优化文本重构或参考答案对齐，未针对模型实际生成的响应做优化，容易出现用户偏好违背、过期信息误用等问题，超长历史场景下性能衰减尤为严重。

### 方法关键点
- 记忆架构：先基于用户全量历史和当前Query生成查询相关的结构化文本记忆，再通过Perceiver风格压缩器映射为固定K个连续软向量，推理时仅需读取K个向量，输入长度与历史长度无关
- 训练范式：仅用单个LoRA适配层，基于学生自身采样的响应做优化，结合两个互补信号：① GRPO序列级任务奖励，衡量响应是否符合任务要求；② 置信度门控在线蒸馏，冻结的全上下文教师模型重打分学生生成的token，仅强化教师置信度更高的学生采样token，避免教师低精度信号干扰
- 推理侧：仅保留学生模型和压缩器，无额外开销，记忆生成与读取复用同一个适配层

### 关键结果
在3款Qwen系列骨干上测试，对比GRPO、OPSD、AutoCompressor、MemGen等基线：
- PersonaMem-128K任务上精度最高达94.4%，较次优基线高出15.9个百分点，优势随历史长度扩大
- 跨域迁移无需目标域训练，在PrefEval、LongMemEval上精度较基线平均提升10%以上
- 样本效率比GRPO高40%，相同精度下所需学生采样rollout数量更少

> 最值得记住的一句话：记忆压缩的优化目标不应该是文本重构准确率，而应该是压缩后的记忆能否支撑下游任务生成符合预期的输出，脱离下游任务的记忆优化没有实际业务价值。
