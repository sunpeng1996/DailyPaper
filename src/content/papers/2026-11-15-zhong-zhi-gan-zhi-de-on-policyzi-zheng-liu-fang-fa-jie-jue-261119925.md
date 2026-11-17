---
title: 'Learning When to Continue and When to Stop: Termination-Aware OPSD'
title_zh: 终止感知的On-Policy自蒸馏方法：解决推理终止不匹配问题
authors:
- Chaoqun He
- Wannian Yi
- Changyi Sun
- Chaojun Xiao
- Lijie Wen
affiliations:
- Tsinghua University
arxiv_id: '2611.19925'
url: https://arxiv.org/abs/2611.19925
pdf_url: https://arxiv.org/pdf/2611.19925
published: '2026-11-15'
collected: '2026-11-17'
category: Training
direction: LLM蒸馏训练 · 终止行为优化
tags:
- OPSD
- Knowledge Distillation
- LLM Training
- Reasoning
- EOS Alignment
one_liner: 为On-Policy自蒸馏新增两类终止相关辅助损失，同时缓解过早终止与重复过生成问题
practical_value: '- 电商导购/客服Agent场景可复用Stop/Continue Distillation思路：将词典拆分为终止/续接两类，对齐老师模型的终止概率，仅增加轻量训练损失即可降低多轮推理过早终止的问题，无需修改推理逻辑。

  - 商品文案/推荐理由生成场景可复用Repetition-Aware Unlikelihood Training方案：提前从基线模型的失败输出中挖掘重复片段作为负样本，训练时针对性惩罚重复续接行为，无需推理时重复检测，延迟更低、生成稳定性更高。

  - 业务侧小模型做领域推理增强（如凑单计算、营销规则推理）可直接采用TA-OPSD框架：无需额外大模型教师，仅增加6.66%的训练开销，即可同时提升推理准确率与生成稳定性，性价比远高于原始OPSD、GRPO等方案。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
On-Policy Self-Distillation（OPSD）是低开销LLM推理增强范式，无需额外大模型教师，仅用带特权信息（如参考答案）的同参数冻结模型做教师，在学生生成的轨迹上做蒸馏，适配业务侧小模型迭代需求。但现有OPSD存在严重的终止不匹配问题：要么推理未完成就过早终止，要么推理停滞之后反复生成重复内容直到打满长度上限，原始token级蒸馏损失无法有效对齐师生的EOS决策，甚至训练过程中师生的EOS概率差会持续扩大。

### 方法关键点
- 新增**Stop/Continue Distillation**辅助损失：将词典划分为终止token集和续接token集，聚合两类的概率质量，用KL散度直接对齐师生的二分类终止决策，缓解过早终止问题。
- 新增**Repetition-Aware Unlikelihood Training**辅助损失：从基线模型的失败生成轨迹中挖掘出现≥3次的重复片段作为负样本，针对性惩罚学生在对应前缀下生成这些重复续接的概率，缓解重复过生成问题。
- 总损失为原始OPSD损失加两个加权辅助损失，权重通过初始梯度范数自动校准，无需额外调参，仅增加6.66%的训练token开销。

### 关键实验
在Qwen3 1.7B/4B/8B三个尺度模型上，用OpenThoughts数据集训练，在AIME24/25、AMC23三个数学推理基准上测试：相比原始OPSD，平均准确率分别提升4.84、3.73、1.32个百分点；过早终止错误占比从12.78%降到3.06%，长度打满的过生成比例从7.55%降到4.77%，优于SFT、GRPO、Stable-OPD等所有基线。

最值得记住的一句话：自蒸馏训练不仅要对齐token级生成内容，还要显式监督「什么时候继续、什么时候停止」的高层决策，才能同时提升推理准确率和生成稳定性。
