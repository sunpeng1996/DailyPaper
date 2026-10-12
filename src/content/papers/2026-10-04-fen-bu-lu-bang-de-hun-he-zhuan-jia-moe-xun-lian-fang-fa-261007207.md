---
title: Distributionally Robust Mixture-of-Experts Training
title_zh: 分布鲁棒的混合专家（MoE）训练方法
authors:
- Xin Teng
- Muxiao Li
- Hongyi Wen
affiliations:
- New York University
- Center for Data Science, NYU Shanghai
arxiv_id: '2610.07207'
url: https://arxiv.org/abs/2610.07207
pdf_url: https://arxiv.org/pdf/2610.07207
published: '2026-10-04'
collected: '2026-10-12'
category: Training
direction: MoE训练 · 分布鲁棒优化
tags:
- MoE
- Distributionally Robust Optimization
- Pretraining
- Load Balancing
- Routing Robustness
one_liner: 提出即插即用的DRMoET训练目标，无需改动MoE路由与架构，显著提升鲁棒性与下游表现
practical_value: '- 采用MoE架构的生成式推荐/LLM推理服务可直接引入DRMoET作为补充训练目标，无需改动现有路由逻辑，仅需极小计算开销即可降低非最优路由的损失，提升长尾/分布偏移场景下的推荐/生成效果

  - 激活加权的损失归因trick可直接复用：结合路由概率和专家输出激活范数分配损失权重，相比纯路由概率归因能更准确反映专家对最终结果的贡献，提升训练效率

  - 长尾用户/商品场景的推荐系统训练可借鉴将MoE专家作为内生鲁棒分组的思路，替代预定义的用户/商品分层，自适应提升最差分组表现，无需额外标注'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE训练仅关注负载均衡，未解决路由不完美时token被分配给训练不充分的非最优专家导致的损失陡增问题；负载均衡辅助损失还可能和任务目标冲突，损害专家专业化特性。

### 方法关键点
- 将每层的每个专家作为内生鲁棒分组，通过分布鲁棒优化最小化层内最差专家的归因损失，无需改动路由规则与模型架构，即插即用
- 采用激活加权的损失归因：结合路由概率与专家输出激活的L2范数分配损失权重，同时使用stop-gradient避免归因系数干扰训练
- 维护EMA平滑的专家损失，用熵正则化的softmax更新每层的专家权重，最终对损失重加权后反向传播，仅增加极小计算开销

### 关键结果
在746M、10.3B两个规模的FLAME-MoE上验证：10.3B参数+67B训练token配置下，7个下游任务平均得分从0.6625提升至0.6767，相比无辅助损失的基线高3.36个百分点；专家损失标准差降低8.58%，强制非最优路由场景下的额外损失降低4.3%，同时专家-域的互信息提升12.9%，未损害专业化。

> 最值得记住的结论：MoE稀疏缩放的核心指标不只是负载均衡，路由鲁棒性才是提升容量可靠性的关键
