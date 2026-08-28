---
title: 'TTPO: Test-Time Policy Optimization'
title_zh: TTPO：无标注场景下的测试时策略优化方法
authors:
- Aozhe Wang
- Zhengxi Lu
- Jianze Wang
- Shangke Lv
- Ying Liu
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Hua Yang
- Qianglong Chen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2608.27448'
url: https://arxiv.org/abs/2608.27448
pdf_url: https://arxiv.org/pdf/2608.27448
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: LLM无标注测试时训练·策略优化
tags:
- Test-Time Training
- Policy Optimization
- OPSD
- GRPO
- LLM Reasoning
- Pseudo Label
one_liner: 提出不对称双分支的无标注测试时训练策略，在数学推理任务上性能追平有监督OPSD
practical_value: '- 可借鉴不对称正负样本处理逻辑，在推荐/广告的无标注在线调优场景，对和多数用户行为一致的样本做知识蒸馏，不一致的做负向惩罚，大幅降低伪标签错误的扩散影响

  - token级选择技巧可直接复用：蒸馏时给高熵、高师生散度的token加权重，负样本惩罚时只过滤高置信错误的token，提升在线调优的梯度效率，减少无效计算和噪声干扰

  - 无标注自进化思路可迁移到电商Agent的推理能力优化：用多数投票生成伪标签在用户咨询、售后决策等任务上做闭环迭代，无需人工标注即可持续提升Agent的复杂任务处理准确率

  - 固定50/50正负样本采样比例的技巧，可用于在线训练的梯度稳定，避免正负样本动态失衡导致的训练波动，降低在线调优的不稳定风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM后训练方法（RL、OPSD）高度依赖标注数据，无法适配无标注测试时训练（TTT）场景；基于多数投票的伪标签方案在高难度任务上错误率可达85%，错误伪标签会误导每一个token的蒸馏，导致训练失效。
### 方法关键点
- 不对称双分支设计：基于多数投票划分正负样本，正样本（匹配伪标签）用OPSD做密集token级蒸馏，负样本（不匹配伪标签）用GRPO做序列级惩罚，利用「即使伪标签错误，79%的负样本仍是真错误」的特性，将伪标签错误的影响范围限制在少量正样本中
- token级优化：蒸馏分支通过学生熵、师生散度的Soft-OR权重降权已收敛token，聚焦高价值学习位置；RL分支仅惩罚高置信错误token，避免误伤局部正确的推理步骤
- 训练时固定50/50正负样本比例，加权平衡两个分支的损失梯度，提升训练稳定性
### 关键结果
- 无标注TTPO在5个竞赛级数学推理基准上性能追平甚至超过有监督OPSD：Qwen3-1.7B/4B/8B平均准确率分别达40.1%/58.6%/62.6%，优于有监督OPSD的39.7%/58.4%/61.7%
- 纯TTT场景下，Qwen3-1.7B准确率从38.0%提升至45.2%；关闭思考模式时，不同规模模型的准确率增益达25.2%~36.4%，是有监督OPSD增益的数倍
- 跨任务泛化性强，在单个基准上训练可同步提升另外两个基准的性能，无过拟合问题
> 最值得记住的一句话：即使伪标签错误率高达85%，只要利用正负样本的不对称特性做差异化处理，无标注自训练依然可以达到甚至超过有监督训练的效果
