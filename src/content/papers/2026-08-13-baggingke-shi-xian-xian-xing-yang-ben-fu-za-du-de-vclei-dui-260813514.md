---
title: Bagging Robustly Learns VC Classes with Linear Sample Complexity
title_zh: Bagging可实现线性样本复杂度的VC类对抗鲁棒学习
authors:
- Omar Montasser
affiliations:
- Yale University
arxiv_id: '2608.13514'
url: https://arxiv.org/abs/2608.13514
pdf_url: https://arxiv.org/pdf/2608.13514
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 对抗鲁棒学习 · VC理论分析
tags:
- Adversarial Robustness
- VC Theory
- Bagging
- RERM
- Sample Complexity
one_liner: 证明Bagging结合RERM的算法可实现VC类线性样本复杂度的对抗鲁棒学习并给出匹配下界
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有VC类对抗鲁棒学习的样本复杂度上界为指数级，采样开销过高，缺乏理论可证的高效实现路径。

### 方法关键点
组合经典Bagging（bootstrap聚合）与鲁棒经验风险最小化（RERM），在$O(d^\star)$个独立bootstrap样本上分别求解RERM，最终输出多模型的多数投票预测结果，其中$d^\star$为对偶VC维。

### 关键结果数字
1. 证明VC类对抗鲁棒学习的样本复杂度仅与VC维$d$线性相关，较2019年的原有上界实现指数级优化；
2. 给出匹配的理论下界：该oracle模型下任意学习器均需至少$\Omega(d^\star)$次RERM调用，即便训练样本量无限也无法降低该调用次数下限。
