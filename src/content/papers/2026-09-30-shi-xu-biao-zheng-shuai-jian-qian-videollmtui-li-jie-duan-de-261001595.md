---
title: 'Before It Fades: Reinforcing Temporal Representations at Inference Time in
  VideoLLMs'
title_zh: 时序表征衰减前：VideoLLM推理阶段的时序表征增强方法
authors:
- Youngwoo Shin
- Yusung Ro
- Minseo Kim
- Junmo Kim
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
arxiv_id: '2610.01595'
url: https://arxiv.org/abs/2610.01595
pdf_url: https://arxiv.org/pdf/2610.01595
published: '2026-09-30'
collected: '2026-10-03'
category: Multimodal
direction: VideoLLM时序推理 · 无训练推理优化
tags:
- VideoLLM
- Temporal Reasoning
- Inference Optimization
- Zero Training
- Representation Learning
one_liner: 无训练时序激活注入方法TAI，缓解VideoLLM时序信息从中间层向输出层衰减的问题
practical_value: '- 针对序列类任务（如用户行为序列、多轮对话时序）中LLM表征逐层衰减问题，可参考TAI思路，在推理阶段提取中间层高价值特征按衰减权重回注，无需训练即可提升任务效果

  - 对于时序敏感的推荐/Agent任务（如用户行为路径推理、多步骤商品导购归因），可复用「计算正反序输入的层间表征差定位关键信息层」的方法，快速定位模型性能瓶颈

  - 无训练的推理优化方案可直接部署在现有服务中，不会带来额外训练成本，适合算力有限、迭代快的业务场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
VideoLLM普遍存在时序推理短板，将视频帧顺序反转后，模型对时序问题的预测结果往往不变，经分析发现中间层提取的时序表征会向输出层逐层衰减，无法传递到最终预测环节。

### 方法关键点
定义层间时序发散向量τ_l衡量正反序输入的层间表征差异，跟踪τ_l幅值发现时序信息在中间层达到峰值后逐层衰减；无需训练的时序激活注入（TAI）方法，对每个输入提取峰值层的τ_l，按实测衰减系数回注到后续所有层。

### 关键结果
在3种主流VideoLLM、4个时序推理基准上稳定提升时序推理效果，对非时序任务的负面影响可忽略，无额外训练成本。
