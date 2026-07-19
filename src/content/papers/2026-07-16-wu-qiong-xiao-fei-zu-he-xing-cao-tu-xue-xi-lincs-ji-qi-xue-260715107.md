---
title: Learning in Infinitesimal Non-Compositional Sketches
title_zh: 《无穷小非组合性草图学习（LINCS）：机器学习范畴论新框架》
authors:
- Sridhar Mahadevan
affiliations:
- Adobe Research
- University of Massachusetts, Amherst
arxiv_id: '2607.15107'
url: https://arxiv.org/abs/2607.15107
pdf_url: https://arxiv.org/pdf/2607.15107
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 机器学习范畴论基础理论研究
tags:
- Categorical-ML
- Theoretical-ML
- Compositionality
- Tangent-Category
- Coalgebra
one_liner: 推出基于范畴论的LINCS框架，将机器学习形式化为非组合性修复的不动点搜索问题
practical_value: '- 本文为纯机器学习理论研究，暂无已验证的落地方法，当前业务可借鉴价值极低

  - 后续若发布推荐/LLM场景下的配套实验结论，可参考其微扰下非组合性缺陷的度量思路评估模型鲁棒性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有机器学习框架普遍依赖损失标量化、向量空间等强假设，缺乏对非组合性（模型输出违反结构约束）的统一定义与修复范式。
### 方法关键点
1. 基于范畴论的LINCS框架将机器学习问题建模为带交换条件、极限/余极限锥的草图，将非组合性定义为通用因子分解失败，而非预测值与真值的算术误差；
2. 引入正切函子计算无穷小微扰下的非组合性缺陷（INC），迭代正切提升生成多层因子分解问题塔；
3. 机器学习被形式化为寻找连续正切展开后稳定的共代数不动点，基于Aczel–Mendler定理证明满足集类实现条件时最终INC共代数必然存在。
### 关键结果
目前暂无公开落地实验结果，深度学习、LLM、强化学习场景下的实验验证正在推进，相关结论将在配套论文中发布。
