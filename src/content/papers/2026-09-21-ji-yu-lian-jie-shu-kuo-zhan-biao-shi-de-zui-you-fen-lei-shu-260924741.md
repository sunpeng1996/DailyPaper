---
title: An Exact Junction-Tree Extended Formulation for Optimal Classification Trees
title_zh: 基于联结树扩展表示的最优分类树精确求解框架
authors:
- Jiancheng TU
- WenqiFan
affiliations:
- Department of Computing, The Hong Kong Polytechnic University
- Department of Management and Marketing, The Hong Kong Polytechnic University
arxiv_id: '2609.24741'
url: https://arxiv.org/abs/2609.24741
pdf_url: https://arxiv.org/pdf/2609.24741
published: '2026-09-21'
collected: '2026-09-22'
category: Training
direction: 最优分类树 · 精确训练求解
tags:
- Optimal Classification Tree
- Linear Programming
- Junction Tree
- Column Generation
- Message Passing
one_liner: 提出基于联结树的最优分类树精确线性规划表示，配套两种求解方法，速度较SOTA快一个数量级
practical_value: '- 推荐系统可解释召回/排序的规则树优化场景，可复用联结树剪枝+子树并行优化思路，降低全局最优规则树的求解耗时

  - 高可解释性要求的广告准入/电商风控决策场景，可直接套用该框架生成全局最优分类树，平衡决策效果与可解释性要求

  - 分类模型精确训练场景，可复用列生成+消息传递的组合求解策略，替代传统贪心/混合整数规划方法，提升最优解验证效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统分类树（如CART）采用贪心构造，上游分支决策会限制下游效果，无法获得全局最优解；现有最优分类树的混合整数规划求解方法收敛慢，相同计算预算下常无法验证最优性。
### 方法关键点
1. 采用联结树表示二元特征的限深分类树，构造整值线性规划（LP）表示，支持递归子树优化
2. 提出精确约简策略，在保留最优值和最优树可恢复性的前提下压缩模型规模
3. 配套两种求解方法：列生成求解受限整值LP结合全域边界验证最优性；消息传递递归合并最优子树代价，子树任务可独立并行计算
### 关键结果
1. 精确约简大幅降低联结树表示的模型规模
2. 相同计算预算下，该LP框架可验证更多混合整数规划方法无法确认最优性的实例
3. 列生成+消息传递方法比现有SOTA最优分类树精确方法的几何平均runtime降低一个数量级
