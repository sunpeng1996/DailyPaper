---
title: 'TRACER: Balancing Stability-Plasticity-Cognitivity Trilemma for LLM Enhanced
  Continual Recommendation'
title_zh: TRACER：平衡LLM增强持续推荐的稳定性-可塑性-认知性三元困境
authors:
- WooJoo Kim
- HyunSik Yoo
- JunYoung Kim
- JaeHyung Lim
- SeongKu Kang
- HwanJo Yu
affiliations:
- Pohang University of Science and Technology
- University of Illinois Urbana-Champaign
- Korea University
arxiv_id: '2608.16075'
url: https://arxiv.org/abs/2608.16075
pdf_url: https://arxiv.org/pdf/2608.16075
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: LLM增强持续推荐 · SPC三元困境平衡
tags:
- Continual Recommendation
- LLM Enhancer
- SPC Trilemma
- TRACER
- LightGCN
one_liner: 提出TRACER框架解决LLM增强持续推荐的SPC三元困境，性能超SOTA最多14.38%
practical_value: '- 可直接复用LLM增强推荐三阶段整合范式：在训练目标对齐、新实体初始化、推理语义融合三个阶段分别优化，避免盲目叠加语义特征导致的效果失衡

  - 新实体冷启动可直接采用Procrustes投影技巧：将新用户/商品的语义embedding正交对齐历史ID embedding空间，无需额外训练即可大幅降低新实体适配成本，适合电商大促新品/新商家上线场景

  - 梯度选择性语义对齐trick可迁移到兴趣快速变化场景：仅在语义梯度与推荐任务梯度同向时启用语义对齐损失，反向时关闭，既注入语义知识又不干扰用户兴趣迁移的学习，适配直播/短视频推荐场景

  - 语义特征注入可采用LoRA+置信门控方案：语义adapter用LoRA限制更新空间+置信度门控动态调整注入强度，避免语义主导预测导致的历史遗忘，同时降低内存开销，适合线上实时更新的推荐流'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
持续推荐（CR）需要从流式交互中捕捉用户动态兴趣，但长期受交互稀疏限制，LLM语义增强可有效缓解稀疏问题，但现有方案直接融合语义特征会触发稳定性（保留历史偏好）-可塑性（适配兴趣迁移）-认知性（利用LLM通用语义知识）三元困境（SPC Trilemma）：盲目注入通用语义先验要么导致历史偏好遗忘，要么阻碍兴趣迁移学习，要么过度依赖通用语义忽略个性化信号，现有方案均未系统解决该冲突。
### 方法关键点
1. 先验证三类LLM enhancer的固有偏置：训练目标加语义对齐的Guidance类偏稳定性、新实体用语义embedding初始化的Initialization类偏可塑性、推理时融合语义特征的Utilization类偏认知性，三者简单叠加会放大认知性偏置，完全打破SPC平衡。
2. 针对性设计三个消解偏置的模块：
- Procrustes投影（PP）：将语义子空间正交旋转对齐历史ID embedding的协作子空间，再加局部校准，解决初始化类的拓扑错位问题，保留可塑性同时降低对稳定性的破坏
- 置信门控冷凝（CC）：用门控网络动态计算语义特征的注入置信度，语义adapter采用LoRA限制更新空间，解决推理类的语义主导问题，保留认知性同时不破坏稳定性与可塑性
- 语义同步（SS）：计算语义梯度与推荐任务梯度的余弦相似度，仅同向时启用语义对齐损失，反向时对旧实体采用历史embedding正则，解决指导类的语义锚定过强问题，保留稳定性同时不破坏可塑性
### 关键结果
在5个真实数据集（Amazon Home/CDs/Movies/Electronics + Yelp）上对比20个基线（纯ID持续推荐方案+4类LLM enhancer），TRACER的NDCG@20最高超出SOTA 14.38%，同时在稳定性（BWT）、可塑性（TRG）、认知性（SRT）三个维度均达最优，内存开销接近纯ID模型，对LLM编码器选择、超参数的鲁棒性极强。
> 最值得记住：LLM语义增强推荐不是简单叠加语义特征，需根据语义知识在训练、初始化、推理三个阶段的作用偏置针对性消解冲突，才能兼顾历史保留、兴趣适配、语义认知三者平衡。
