---
title: 'Equal Ranking Quality, Different Decisions: Training Order-Consistent LLM
  Scorers'
title_zh: 相同排序质量不同决策：训练序一致的LLM打分器
authors:
- Markus Frohmann
- Mahdiyar Alavi
- Elizabeth Lingg
- Navid Rekabsaz
affiliations:
- Thomson Reuters Labs
- University of Toronto
- Vector Institute
arxiv_id: '2608.26762'
url: https://arxiv.org/abs/2608.26762
pdf_url: https://arxiv.org/pdf/2608.26762
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 排序优化 · LLM打分器序一致性训练
tags:
- Reranker
- LLM
- Order-Consistency
- SFT
- Evaluation
one_liner: 提出OC-SFT微调方法，不损失排序质量的前提下大幅降低LLM打分器的顺序敏感性
practical_value: '- 做LLM reranker选型时，除nDCG等排序指标外，必须新增决策稳定性指标（如阈值保留集重叠率、下游结果翻转率），否则相同排序质量的模型线上输出差异可达30%以上，严重影响用户体验

  - 可直接复用OC-SFT训练范式，在现有SFT损失基础上增加同候选不同排列的得分方差惩罚项，仅需LoRA微调，无需修改推理逻辑，无额外推理成本

  - 若当前使用推理端多排列平均方案解决顺序敏感问题，替换为OC-SFT训练的单排列模型即可达到相同稳定性，推理成本直接降低80%以上，适配高QPS的电商搜索/推荐场景

  - 无需在prompt端尝试轮询分区、logit校准等优化，这类方案仅能小幅提升排序质量，对决策稳定性无 measurable 提升'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM reranker、奖励模型、多文档QA打分器均采用多候选同prompt的批量打分模式，得分高度依赖候选排列顺序，但工业界选型仅关注nDCG等排序质量指标，忽略决策一致性：相同nDCG的模型，下游阈值筛选的候选集、QA输出、偏好训练对的重合度可能低至0.66，严重影响线上业务稳定性。推理端多排列平均方案会数倍提升耗时，prompt端的轮询分区、logit校准等优化无法解决决策层面的顺序敏感问题，亟需低成本的训练层解决方案。

### 方法关键点
- 提出**OC-SFT**（序一致性监督微调），损失由两部分组成：① 单排列下的排序拟合损失（与普通SFT一致）；② 同一候选在不同排列下的得分方差惩罚项，强制拉齐同一候选在不同排列下的打分结果，仅需2个排列视图即可生效
- 采用固定答案骨架的打分读出方式，直接提取每个候选对应位置的grade期望作为连续得分，无需生成文本，得分跨实例可比较，支持阈值筛选
- 支持自蒸馏训练，无需外部教师模型，仅需LoRA微调即可，不改变推理逻辑

### 关键实验
在18个段落排序、3个多文档QA、5个响应排序数据集上对比单顺序SFT、顺序平均蒸馏、DebiasFirst、排列增强、推理端10次排列平均（BSC）等方案：
- 排序质量基本持平（nDCG@10差距<0.01）的前提下，OC-SFT的保留集Jaccard重叠率从单顺序SFT的0.656提升至0.835，QA答案翻转率从0.177降至0.125，响应排序偏好对翻转率从0.869降至0.661，所有决策稳定性指标最优
- OC-SFT单排列的稳定性超过10次排列平均的BSC效果，推理成本仅为后者的1/10

### 核心结论
LLM打分器的选型不能仅看排序质量指标，必须同时评估下游实际决策的一致性，相同排序质量的模型决策重合度差异可超过20%
