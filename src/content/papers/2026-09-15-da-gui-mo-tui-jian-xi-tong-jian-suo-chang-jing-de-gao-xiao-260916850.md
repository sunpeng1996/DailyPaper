---
title: Efficient Swing Computation for Retrieval in Large-Scale Recommender Systems
title_zh: 大规模推荐系统检索场景的高效Swing相似度计算方法
authors:
- Runhao Jiang
- Renchi Yang
affiliations:
- Hong Kong Baptist University
arxiv_id: '2609.16850'
url: https://arxiv.org/abs/2609.16850
pdf_url: https://arxiv.org/pdf/2609.16850
published: '2026-09-15'
collected: '2026-09-16'
category: RecSys
direction: 推荐系统召回 · 高效Swing相似度计算
tags:
- Swing
- i2i Retrieval
- Collaborative Filtering
- Approximation Algorithm
- Top-K Query
one_liner: 提出带理论误差保证的自适应Swing算法ASC与K-ASC，实现数倍至数个量级的计算加速
practical_value: '- 可直接复用QFilter++优化用户交互集合的交运算，仅需交集基数的场景最高可获得3倍加速，避免重复计算开销

  - 落地Swing计算时可参考自适应选型思路：低热度商品用USS、高热度商品用GNS，替代传统的用户截断 heuristic，既保证精度又降低计算成本

  - Top-K相似商品召回场景可复用K-ASC的过滤-精修范式：先用少量采样预算生成候选集，仅对边界候选做分数精修，大幅降低采样开销且精度几乎无损

  - 论文开源了工业级C++实现，可直接迁移到现有i2i召回的Swing离线/在线计算链路，无需修改业务逻辑即可降低资源消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Swing是工业界i2i召回的核心相似度算法，广泛应用于阿里、快手、Shopee等平台的推荐、广告、搜索场景，但现有Swing计算方案存在明显缺陷：精确计算的时间复杂度与商品交互用户数成平方关系，热门商品计算成本极高；常用的用户截断 heuristic 会损失精度，无法适配百亿级交互的大规模推荐场景。
### 方法关键点
- 优化QFilter得到QFilter++，集合交集基数计算速度最高提升3倍，无需实例化完整交集
- 提出两个带(ε,λ)理论误差保证的随机估计算法：GNS分组重复采样的用户对避免重复交运算；USS采样用户交互子集规避大集合交运算开销
- 构建ASC算法，通过成本模型自适应为不同度数的商品选择GNS/USS，兼顾两者效率优势
- 针对Top-K查询场景优化出K-ASC，采用过滤-精修范式：先用10%采样预算生成Top-K+κ候选集，通过伯恩斯坦界识别边界候选，剩余预算仅精修边界候选的Swing分数
### 关键结果
在8个真实数据集（含百亿边的MAG、Yambda数据集）上对比7种基线：相同精度下ASC比基线快1~2个数量级；K-ASC在MAG数据集上Top100查询精度达99.9%，耗时仅1.5ms，比Exact方法（8.5秒）提速超5600倍，比截断Swing精度高15%+，耗时仅为其1/10。
### 核心结论
工业级Swing计算的核心优化思路是「算力自适应分配」：针对不同热度商品选最优算法，Top-K场景仅在有不确定性的边界候选上投入算力，而非全局均匀分配。
