---
title: Topology-Masked Unified Backbone for Joint Feature Interaction and Multi-Domain
  Sequence Modeling
title_zh: 面向联合特征交互与多域序列建模的拓扑掩码统一骨干网络
authors:
- Zhihao Zhu
- Dezheng Han
- Jikang Xia
- Shuaishuai Guo
affiliations:
- Shandong University
- Tsinghua University
arxiv_id: '2608.27005'
url: https://arxiv.org/abs/2608.27005
pdf_url: https://arxiv.org/pdf/2608.27005
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 推荐排序 · 多域统一建模
tags:
- CVR-Prediction
- Multi-Domain-Rec
- Unified-Backbone
- Attention-Mask
- Sequence-Modeling
one_liner: 提出MaskRec架构，用拓扑掩码注意力统一建模特征交互与多域序列依赖
practical_value: '- 多源异构信息统一建模时，可直接复用TopoMask思路：根据业务先验按信息角色/域手动定义注意力连通性，比如允许同域行为序列内部交互、阻断无关域直接交互，既减少噪声又降低attention计算量

  - 多域推荐/广告排序场景可前置DualQ模块：先做用户侧与候选侧的双向交叉注意力生成基础交互query，再通过FiLM调制生成域感知query，提前注入用户-候选交互信号，可稳定带来千级AUC提升

  - 异构特征处理不要盲目压缩：dense特征按语义（统计类/连续类）拆分做token化，稀疏ID补充频率桶特征，均可带来明确的效果提升

  - 多域序列建模可引入可学习记忆token作为聚合节点：16个全局+4个域级的配置性价比最高，无需额外设计复杂聚合层即可完成多源信息汇总'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业CVR预测需同时建模异构特征交互与多域用户行为序列依赖，现有方案要么用分离模块限制跨源深度交互，要么无约束统一架构忽略信息源结构差异，易引入噪声、性能上限低。
### 方法关键点
- 所有输入统一token化：异构特征、多域行为序列、上下文、全局/域级可学习记忆token、增强query token均映射到同一嵌入空间
- 设计TopoMask结构化注意力掩码：按token角色和域关联显式控制注意力连通性，同类型/同域token允许交互、无关域交互阻断、全局记忆token可访问全量信息，在同一注意力流程内完成结构化建模
- 前置DualQ双路交互query模块：先做用户侧与候选侧的双向交叉注意力，再通过FiLM调制生成域感知增强query，提前注入用户-候选交互信号
- 仅取全局记忆、域记忆、增强query的表征拼接，输入MLP头预测CVR
### 关键结果
在腾讯广告算法大赛数据集上，对比HyFormer风格官方基线，Val AUC从0.8318提升至0.8413，Test AUC从0.8249提升至0.8346；消融实验显示，移除DualQ会导致Test AUC下降0.001，将dense特征压缩为单个token会导致Test AUC下降近0.01，16个全局+4个域级的记忆token配置性能仅比最优32/8配置低0.0001，性价比极高。
### 核心启示
统一多源建模的核心不是无差别全连接交互，而是在统一空间内基于业务先验做结构化信息路由，兼顾效率与效果。
