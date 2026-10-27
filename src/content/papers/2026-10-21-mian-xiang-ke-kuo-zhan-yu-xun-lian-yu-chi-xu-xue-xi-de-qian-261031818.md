---
title: Nested Sparsity for Scalable Pretraining and Continual Learning
title_zh: 面向可扩展预训练与持续学习的嵌套稀疏Transformer NESTOR
authors:
- Tianzhe Chu
- Druv Pai
- Yi Ma
affiliations:
- University of Hong Kong
- UC Berkeley
arxiv_id: '2610.31818'
url: https://arxiv.org/abs/2610.31818
pdf_url: https://arxiv.org/pdf/2610.31818
published: '2026-10-21'
collected: '2026-10-27'
category: LLM
direction: LLM架构优化 · 嵌套稀疏MoE
tags:
- MoE
- Sparse Attention
- Continual Learning
- Pretraining
- Transformer
one_liner: 提出嵌套稀疏架构NESTOR，同等计算下优于传统MoE，适配持续学习与长上下文
practical_value: '- 垂直域MoE LLM优化：做电商推荐文案生成、用户语义理解的垂域大模型时，可复用分层路由设计，先按语义粗路由到注意力列再细路由到专家，同等计算下预训练效率提升10%+，跨域微调遗忘率降低3%

  - 长上下文序列建模优化：处理电商商品长文本、用户全生命周期行为序列的LLM可参考随深度递增激活列数的设计，32k+长上下文扩展效率比传统MoE提升30%以上

  - 多域持续学习优化：多域电商/广告垂域LLM持续微调时，可参考NESTOR路由冻结策略，仅更新激活列对应参数，无需重放旧数据即可降低旧域效果衰减'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统MoE Transformer仅在MLP层实现稀疏计算，注意力层参数全局共享，长上下文下计算占比极高，且持续预训练时易出现旧域灾难性遗忘；现有稀疏注意力方法仅优化注意力映射，未与MoE稀疏性分层联动，无法同时提升预训练效率、长上下文适配性与持续学习能力。

### 方法关键点
- 核心设计嵌套稀疏机制：将条件计算拓展到注意力层，每个block先通过列路由将token分配到Kc个独立注意力列，每个列仅处理被路由到的token子序列，同时实现注意力参数稀疏与注意力映射稀疏
- 分层路由联动：列路由结果在block内M层共享，每个列内部自带MoE专家层，token在激活列内再路由到Ke个专家，稀疏性嵌套叠加，架构可兼容退化为标准MoE或dense Transformer
- 工程优化：随网络深度递增激活列数（从底层3列到顶层全列激活），采用无辅助损失的路由负载均衡策略，搭配注意力残差连接提升训练稳定性

### 关键结果
在DCLM数据集上训练100M~1B active参数模型，对比标准MoE、dense Transformer基线：
1. 预训练阶段：同等参数规模下，NESTOR计算效率是MoE的1.13~1.29倍，是dense模型的3.1~4.1倍，规模越大优势无衰减
2. 域适应持续预训练：无旧数据重放时，NESTOR新域适配效果与MoE相当，旧域遗忘率比MoE低3%，比dense模型低21%
3. 长上下文扩展：从4k扩展到64k上下文时，同等FLOPs下NESTOR的优势随上下文长度增长，比MoE最多降低0.06 nat困惑度

最值得记住的一句话：将条件计算从MoE层拓展到注意力层并实现分层嵌套联动，是同时提升大模型预训练效率、长上下文能力与持续学习性能的高性价比方向
