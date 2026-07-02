---
title: Amplifying Membership Signal Through Chained Regeneration
title_zh: 通过链式再生增强成员推断信号
authors:
- Wojciech Łapacz
- Stanisław Pawlak
affiliations:
- Warsaw University of Technology
arxiv_id: '2606.31991'
url: https://arxiv.org/abs/2606.31991
pdf_url: https://arxiv.org/pdf/2606.31991
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 大模型隐私审计 · 成员推断
tags:
- Membership Inference Attack
- Dataset Inference
- Generative Model
- Privacy Auditing
- Chained Generation
one_liner: 无需影子模型的模型无关框架MADreMIA，通过链式迭代生成强化成员推断与数据集推理信号
practical_value: '- 生成式推荐/广告模型训练数据版权合规审计时，可复用链式迭代再生思路，无需训练影子模型就能低成本判断授权数据是否被误用

  - 排查大模型训练集数据泄露风险时，可利用记忆样本迭代再生时一致性更高、退化更慢的特征，提升低FPR场景下的检测准确率

  - 跨模态生成推荐系统的隐私合规校验，可直接适配该模型无关框架，覆盖文本、图像、音频多模态内容的成员校验'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
生成模型普遍存在训练数据记忆特性，隐私审计、版权核验、基准污染检测等场景需要高效的成员推断（MIA）与数据集推理（DI）能力，但现有one-shot方法信号弱、跨模态敏感性差，且依赖对大模型极不友好的影子模型训练。
### 方法关键点
模型无关的MADreMIA框架无需训练影子模型，通过多模态链式迭代生成（每轮输出作为下一轮输入）的轨迹提取固有信号，利用训练集记忆样本迭代再生时一致性更高、退化更慢的特征强化低FPR场景下的成员证据。
### 关键结果
在自回归模型、扩散模型、大语言模型上均取得优于现有one-shot方法的检测表现，低FPR下性能提升显著，同时在音频模型上验证了初步适配可行性。
