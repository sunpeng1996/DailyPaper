---
title: 'Better Rankers, Worse Retrievers: The Hidden Cost of RL Post-Training in Generative
  Recommendation'
title_zh: 生成式推荐RL后训练的隐性代价：排序能力提升但召回下降
authors:
- Yuheng Chen
- Fan Zhang
- Yixuan Xu
- Chao Yang
- Yang Xiang
- Can Yang
affiliations:
- The Hong Kong University of Science and Technology
- Trip.com Group
arxiv_id: '2611.22838'
url: https://arxiv.org/abs/2611.22838
pdf_url: https://arxiv.org/pdf/2611.22838
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式推荐 · RL后训练优化
tags:
- GenRec
- RL
- GRPO
- Semantic ID
- Recall
- Post-training
one_liner: 发现生成式推荐RL后训练的召回损失问题，提出外滚出锚定方法同时保top精度与召回
practical_value: '- RL后训练的评估不能仅测NDCG@10、hit@10等小K指标，必须按实际部署的召回截断位（如K=100/500/1000）测试召回，避免上线后候选池覆盖不足

  - 采用GRPO做生成式推荐RL训练时，可直接复用out-of-rollout anchoring技巧，仅需新增1项与SFT模型在滚出外样本的KL散度损失，几乎无额外成本即可修复召回损失，同时保留top精度收益

  - RL负采样不要仅使用模型自身top候选作为负例，这类候选多为未标注正例（相似用户的消费选择），易导致合理结果被频繁惩罚，可搭配随机负例降低误伤，或引入多正例标注优化奖励函数

  - 若生成式推荐在业务中作为召回层输出数百上千候选给下游排序，优先保证大K召回，可直接用锚定优化后的GRPO替代原生GRPO，无需调整原有RL训练流程'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐标准训练流程为SFT后接RL（多为GRPO），业界普遍仅报告top10以内精度收益，但实际部署中模型多作为召回层输出数百到上千候选给下游排序，RL对大K召回的影响长期被忽略，大量工业实践出现RL后召回下降的零散问题，缺乏系统研究与解决方案。
### 方法关键点
- 定位召回损失根源：RL训练仅将日志单条next item作为正例，滚出采样的其他高置信候选被当作负例惩罚，而这类候选多为相似用户的正例，惩罚累积后导致其在相似用户候选列表中排名下降，最终大K召回降低
- 提出out-of-rollout anchoring：在原生GRPO损失基础上新增约束项，对每条prompt采样若干滚出外物品，约束其在当前模型与SFT模型中的相对排序一致，不干涉滚出内的RL更新
### 关键实验
在5个亚马逊公开数据集上测试，基线为原生GRPO与SFT模型：
1. 原生GRPO在Office数据集上NDCG@10从11.59%提升至12.55%，但hit@50从25.73%降至24.22%，hit@500从52.84%降至47.69%，22%的SFT top500候选被挤出
2. 加锚定的GRPO NDCG@10达12.64%（与原生GRPO无显著差异），hit@50恢复至26.27%，hit@500恢复至52.14%，基本回到SFT召回水平
3. 方法在全量5个数据集上均有效，适配GRPO、REINFORCE++等多种RL配置

> 最值得记住：生成式推荐RL后训练评估必须匹配实际部署的截断深度，错误惩罚高置信候选是召回损失的核心原因
