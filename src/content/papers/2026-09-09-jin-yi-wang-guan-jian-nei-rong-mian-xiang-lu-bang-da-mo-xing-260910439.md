---
title: 'Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs'
title_zh: 仅遗忘关键内容：面向鲁棒大模型的层选择性遗忘框架FOM-UL
authors:
- Ravi Ranjan
- Olivera Kotevska
- Agoritsa Polyzou
affiliations:
- Florida International University
- Oak Ridge National Laboratory
arxiv_id: '2609.10439'
url: https://arxiv.org/abs/2609.10439
pdf_url: https://arxiv.org/pdf/2609.10439
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: LLM机器遗忘 · 量化鲁棒性优化
tags:
- LLM Unlearning
- Transformer Layer Selection
- Quantization Robustness
- Privacy Compliance
- Parameter Efficient Tuning
one_liner: 通过梯度比值筛选高遗忘影响低保留损伤的Transformer层定向更新，实现抗量化的鲁棒LLM机器遗忘
practical_value: '- 业务侧需移除LLM（导购Agent、文案生成、生成式推荐）训练的敏感/侵权/违规内容时，可复用该层选择策略，基于遗忘/保留集梯度比值筛选更新层，替代全模型微调，降低算力消耗的同时减少对通用业务能力的损伤

  - 低比特量化部署的业务LLM做内容删除时，优先采用集中式层更新而非弥散的全局更新，避免量化rounding抵消小参数更新导致遗忘内容复现的问题

  - 可将梯度显著性筛选思路迁移到推荐排序模型更新场景，比如需要下架特定违规商品/商家相关的排序记忆时，仅更新对该类样本影响最大的模型层，降低全局更新带来的全量效果波动'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM机器遗忘方法多采用全局或固定范围参数更新，不仅易损伤模型通用能力，还会在部署时的低比特量化场景下出现遗忘内容复现的问题，同时全量更新算力成本极高，无法满足合规层面「被遗忘权」的快速响应需求。
### 方法关键点
- 提出层显著性得分`Sig(ℓ)`，等于每层在遗忘集上的梯度L2范数除以保留集上的梯度L2范数，筛选出对遗忘目标影响大、对保留内容影响小的层，仅更新这些层的参数，其余层完全冻结
- 三层损失联合优化：梯度上升最大化遗忘集损失、最大化遗忘集输出与原模型分布的KL散度，梯度下降最小化保留集损失，平衡遗忘效果与能力保留
- 迭代层扩展机制：初始仅更新得分最高的k层，若遗忘效果不达标则逐步增加更新层，避免过度更新损伤效用
### 关键结果
在TOFU、KnowUnDo、MUSE三个标准遗忘基准上对比GA、NPO、SURE、LUNAR等7个SOTA基线，FOM-UL残留记忆降低15%+，隐私泄露风险降低40%，保留集效用接近原模型；4/8比特量化场景下遗忘内容复现率比基线低60%，对抗prompt攻击下的内容泄露率仅11.6%，比最优基线低近30%；7B规模模型训练仅需8GB显存，耗时20分钟，远低于全量更新的4小时。
> 最值得记住：集中式定向更新比弥散的全局更新更适配工业界量化部署、低资源的LLM遗忘需求
