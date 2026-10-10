---
title: Controlled Acquisition and Abstention in Three-Channel Score Conflicts
title_zh: 三通道分数冲突下的受控信息获取与弃权决策
authors:
- Mengzhe Geng
affiliations:
- National Research Council Canada
arxiv_id: '2610.10808'
url: https://arxiv.org/abs/2610.10808
pdf_url: https://arxiv.org/pdf/2610.10808
published: '2026-10-07'
collected: '2026-10-10'
category: Multimodal
direction: 多模态融合决策 · 成本收益权衡
tags:
- Multimodal Fusion
- Decision Policy
- Cost-Benefit Tradeoff
- Threshold Policy
- Uncertainty Estimation
one_liner: 提出多模态三通道分数冲突场景的阈值决策策略，平衡信息获取成本、弃权惩罚与决策效用
practical_value: '- 多模态召回/排序场景下，可复用阈值决策逻辑，在多源特征分数冲突时，权衡补全特征的成本、弃权（推兜底内容）的惩罚与决策准确率的平衡

  - 预算受限的推荐场景（如实时性要求高、算力预算有限），低预算下可参考用pair uncertainty做特征选择，比随机/不补充特征的策略效用更高

  - 低容错业务（如电商广告合规审核），如果不允许弃权输出兜底结果，可优先用多源分数多数投票策略获得更高效用'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态（音/视/文）融合场景下，现有直接输出决策的模型无法解决两个核心问题：是否值得付出成本获取缺失的第三模态信息、是否应该在信息不足时弃权避免错误，且不同场景下弃权、信息获取、错误输出的成本差异极大，仅靠准确率无法衡量决策优劣。
### 方法关键点
构建受控三分数冲突基准，设计阈值决策策略，可基于观测到的两个模态分数，决策是请求第三模态、直接输出结果还是弃权，可适配不同场景的reward规则。
### 关键结果
合成数据集上，阈值策略准确率达0.789±0.006、效用0.481±0.014，远超三分数多数投票基线的0.626±0.008、0.252±0.016；10%/25%预算下，训练得到的价值选择器比无查询/随机策略效用更高，全预算且不允许弃权时多数投票策略效用更优。
