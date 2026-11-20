---
title: 'CACO: Coverage-Aware Coordinated Optimization for Continuous Generative Retrieval'
title_zh: CACO：面向连续生成式检索的覆盖度感知协同优化框架
authors:
- Pan Zhang
- Nan Zhuang
- Yongkang Zhang
- Kun Xú
- Zhongtao Jiang
- Zhiwei Wang
- Kun Xǔ
- Youhuan Li
affiliations:
- 湖南大学
- 华中农业大学
arxiv_id: '2611.25738'
url: https://arxiv.org/abs/2611.25738
pdf_url: https://arxiv.org/pdf/2611.25738
published: '2026-11-19'
collected: '2026-11-20'
category: GenRec
direction: 生成式检索 · 召回覆盖度优化
tags:
- Generative Retrieval
- Flow Matching
- Self-supervised Post-training
- Recall Optimization
- Coverage Optimization
one_liner: 为冻结的生成式检索backbone提供轻量后训练优化，固定预算下提升召回、降低查询结果重叠
practical_value: '- 可复用轻量后训练思路：现有生成式/多兴趣召回模型无需全量重训，新增仅0.6M参数的查询协调网络，仅增加0.5%-3%推理延迟即可获得10%+的召回收益

  - 可复用无标注覆盖度优化目标：用base模型采样的reference query检索频次作为相关性代理，无需新增标注数据，适配召回场景冷启动/无标注优化需求

  - 工程上可落地不可导问题解决方案：通过切线空间对偶扰动+反事实单query替换计算边际覆盖增益，绕开ANN检索不可导的技术难点

  - 业务侧可复用预算分配逻辑：固定总检索预算下，将query数放大、单query召回数缩小（如40*10替代20*20）搭配CACO可进一步降低ANN检索耗时、提升覆盖度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于flow matching、diffusion的连续生成式检索，通过采样多query并行ANN召回提升覆盖度，但现有方法仅优化分布多样性、单兴趣区分度，未考虑集合级检索几何特性：多query采样的ANN邻域高度重叠，固定预算下大量检索槽浪费在重复物品，召回上限低；同时离散top-K检索、单目标监督也阻碍端到端覆盖度优化。

### 方法关键点
1. 无监督覆盖度目标构造：从冻结base模型采样大量reference query，统计各item的检索频次作为相关性代理，加权计算查询集合的覆盖度得分，重复召回的物品不新增得分
2. 协同查询调整网络：引入用户历史交叉注意力+query间双向自注意力+相对方向门控，通过切线空间投影+球面收缩更新query，保证初始query的相关性不下降
3. 无偏梯度估计：训练时对每个query加切向对偶扰动，用反事实单query替换计算每个query的边际覆盖增益，绕开ANN不可导问题，实现端到端训练

### 关键结果
在8个公开基准、1个24分区工业流数据集、6个冻结backbone（含flow matching、diffusion类）上测试：Recall@100最高提升23.7%，Recall@400最高提升23.9%；多query结果的pairwise Jaccard重叠降低53.3%-64.9%，推理延迟仅增加0.5%-3.0%；直接适配所有连续生成式召回backbone，无需修改原有模型结构。

**最值得记住的一句话**：固定检索预算下，优化多query的互补覆盖度比单纯提升单query相关性、单兴趣区分度能带来更高的召回增益。
