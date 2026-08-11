---
title: 'Give the Long-tail More SPACE: Promoting Provider Fairness in Next POI Recommendation'
title_zh: SPACE：面向下一个POI推荐长尾供给方公平性的模型无关框架
authors:
- Anran Zhang
- Jiaqi Jiang
- jiahui Jin
- Yuhan Zhao
affiliations:
- School of Computer Science and Engineering, Southeast University
- Department of Computer Science, Hong Kong Baptist University
arxiv_id: '2608.07998'
url: https://arxiv.org/abs/2608.07998
pdf_url: https://arxiv.org/pdf/2608.07998
published: '2026-08-08'
collected: '2026-08-11'
category: RecSys
direction: 推荐系统公平性 · 长尾POI曝光优化
tags:
- Fairness
- Long-tail Recommendation
- POI Recommendation
- User Embedding Generation
- Model-Agnostic
one_liner: 通过约束感知的虚拟用户生成，在不损失精度的前提下提升POI推荐长尾商家曝光
practical_value: '- 本地生活/到店类推荐场景可复用双约束（用户出行成本/商家供给容量）设计，避免为追求公平性生成不可达/过载的无效推荐，损害用户及商家体验

  - 长尾/冷启场景可借鉴约束引导的虚拟用户生成方案，基于用户分群+非平衡最优运输分配配额生成训练样本，无需修改原有召回排序架构即可落地

  - 多利益相关方推荐场景可复用训练侧增强思路，相比重排序类公平性方案无线上推理开销，额外训练成本仅增加不到3%，适合工业级部署'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
下一个POI推荐是本地生活服务的核心模块，但主流模型普遍存在曝光马太效应，80%长尾线下商家获得的流量远低于头部。现有公平性方法直接套用会存在两个核心缺陷：一是用户有物理出行约束，推送距离过远的不可达POI会严重损失用户体验；二是线下POI有服务容量上限，过度曝光长尾会导致商家承接过载，反而降低供需匹配效率。
### 方法关键点
- **社区推断**：基于用户偏好+出行约束特征做软聚类，划分用户社区，确保同社区用户的出行预算、活动规律一致；
- **配额分配**：基于非平衡最优运输（UOT）为每个长尾POI分配虚拟用户配额，严格对齐POI的历史最大接待量上限，同时优先分配给和POI匹配度高的用户社区；
- **虚拟用户生成**：基于约束引导的潜扩散模型，以POI特征+社区原型为初始化锚点生成符合真实用户分布的embedding，生成的<虚拟用户,长尾POI>对直接加入原有训练集，无需修改下游推荐模型架构。
### 关键实验结果
在NYC、TKY、CA三个真实POI数据集上测试，覆盖FPMC、LSTPM、GETNext等5类主流POI推荐backbone：
1. 公平性指标最高提升94.11%，长尾POI曝光、覆盖率均显著提升；
2. 推荐精度无损失，最高提升54.85%，解决了公平性-精度的权衡矛盾；
3. 训练开销仅增加不到3%，无线上推理额外成本。
### 核心结论
物理场景下的供给方公平性不能只看统计指标，必须同时对齐用户的执行约束和商家的供给约束，才能实现真实的供需匹配效率提升
