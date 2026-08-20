---
title: 'Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck'
title_zh: 真实场景下的测试时缩放：性能瓶颈并非探索而是利用
authors:
- Davide Romano
- Kanak Raj
- Jerrod Parker
- Daniele Giofrè
affiliations:
- Thomson Reuters
arxiv_id: '2608.18931'
url: https://arxiv.org/abs/2608.18931
pdf_url: https://arxiv.org/pdf/2608.18931
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: LLM测试时缩放 · 探索利用拆分
tags:
- Test-time Scaling
- Reward Model
- Open-ended Generation
- Exploitation
- Exploration
- Fusion
one_liner: 首次在多领域开放生成任务上对比5类测试时缩放方法，证明利用而非探索是性能瓶颈
practical_value: '- 做生成式推荐/Agent回复/商品文案优化时，优先测试多候选Fusion方案，而非基于RM的Best-of-N选择，当前通用RM和生成结果的相关度仅~0.12，Best-of-N几乎无收益

  - 投入测试时缩放（TTS）资源前，先在业务小样本上测RM和真实标注的Spearman相关系数ρv，ρv直接等于Best-of-N的headroom capture，低于0.3就不要投预算做RM选优

  - 不要用树搜索类TTS方法做开放生成类任务（如商品文案、客服回复、营销话术），PRM引导的剪枝会导致多样性坍缩，性能反而不如单样本基线

  - 做LLM自我优化时，迭代精炼（SR）方案仅在特定专业文档生成任务有效，大部分开放场景迭代会导致性能下降，优先用一次多候选融合'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Test-time scaling（TTS）方法在数学、代码等可明确验证的任务上收益显著，但相关研究几乎都在验证逻辑简单的场景下开展，真实场景下的开放生成任务（如法律咨询、医疗建议、商品文案、营销话术）没有唯一正确答案，Reward Model（RM）难以可靠排序候选，TTS的真实表现与性能瓶颈始终缺乏系统验证。

### 方法关键点
- 统一将TTS的token预算拆分为探索（生成候选）和利用（选优/融合/精炼）两个环节，定义headroom capture指标衡量利用环节的效率
- 计算归一化对比5类主流TTS方法：Best-of-N（BoN）、Beam Search、Particle Filter、Sequential Refinement（SR）、Fusion
- 提出偏差校正的oracle质量估计方法，消除评分噪声对候选池最优质量估计的系统性高估

### 关键结果
在法律、医疗、金融、通用对话、创意写作5个开放生成基准上对齐token预算测试，覆盖Qwen3.5、OLMo3等多个模型：
- 现有SOTA RM与真实质量的Spearman相关度仅~0.12，BoN仅能捕获~15%的候选池质量提升空间，几乎无实际收益
- Fusion是唯一在所有基准上稳定优于单样本基线的方法，也仅能捕获~40%的可用提升空间
- 树搜索类方法因PRM引导的多样性坍缩，性能普遍低于单样本基线，SR仅在1/5基准上有真实收益，其余场景反而退化

测试时缩放的瓶颈从来不是生成不出足够好的候选，而是无法从候选池里选出/融合出最优结果。
