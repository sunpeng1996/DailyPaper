---
title: 'PACE: Primitive-Aware Code Evolution for Automated Algorithm Design'
title_zh: PACE：面向自动化算法设计的基元感知代码演化框架
authors:
- Zhuoliang Xie
- Ruihao Zheng
- Xiang Xu
- Genghui Li
- Zhengkun Wang
affiliations:
- Southern University of Science and Technology
- Shenzhen University
arxiv_id: '2608.07395'
url: https://arxiv.org/abs/2608.07395
pdf_url: https://arxiv.org/pdf/2608.07395
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM 自动化算法代码演化优化
tags:
- Automated Algorithm Design
- Code Evolution
- LLM
- Thompson Sampling
- Code Reuse
one_liner: 通过可执行算法基元解耦代码逻辑，实现LLM自动化算法设计时优质组件跨程序留存复用
practical_value: '- 做推荐/广告策略迭代时，可复用EAP思路将常用排序逻辑、召回规则拆为可独立评估的原子基元，避免全策略迭代时优质局部逻辑被丢弃

  - 可借鉴基于父级相对性能提升的Thompson采样方法，给不同策略基元做优先级排序，无需额外构造离线评估数据集即可快速筛选优质组件

  - 构建Agent工具库时可参考动态EAP池设计，自动留存高价值工具代码片段，实现跨Agent任务的工具逻辑复用'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM驱动的自动化算法设计以完整程序为最小演化单元，优质局部代码逻辑随劣化的整体程序被丢弃，且难以单独评估单个算法组件的贡献，迭代效率低。
### 方法关键点
1. 提出可执行算法基元（EAP），将代码局部逻辑从完整程序中解耦为可独立留存的持久化单元，维护动态EAP池实现跨程序的代码级迁移；
2. 设计基元感知的演化算子，从结构上保证EAP的留存与跨程序复用；
3. 采用基于父代相对性能提升的Thompson采样引导EAP选择，无需额外评估数据集即可高效筛选优质基元。
### 关键结果
在4个自动化算法设计任务上验证，PACE既能发现性能有竞争力的算法，还能从结构上留存高价值算法组件，避免优质逻辑丢失。
