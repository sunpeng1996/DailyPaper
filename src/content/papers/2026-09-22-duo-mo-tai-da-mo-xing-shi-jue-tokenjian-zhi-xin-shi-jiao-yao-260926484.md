---
title: 'From Token Importance to Conditional Removability: Rethinking Visual Token
  Pruning in Multimodal Large Language Models'
title_zh: 多模态大模型视觉Token剪枝新视角：从重要性评估到条件可移除性判断
authors:
- Shengli He
- Yongchao Liang
- Roumeng He
- Junjie Zeng
- Jiyuan He
- Xin Fang
- Can Wu
- Li Zheng
affiliations:
- Guizhou University
- Shanghai Ocean University
arxiv_id: '2609.26484'
url: https://arxiv.org/abs/2609.26484
pdf_url: https://arxiv.org/pdf/2609.26484
published: '2026-09-22'
collected: '2026-09-23'
category: Multimodal
direction: 多模态大模型 · 无训练视觉Token剪枝优化
tags:
- MLLM
- Token Pruning
- Efficient Inference
- Training-free
- Multimodal
one_liner: 提出无训练两阶段视觉Token剪枝框架CoRePrune，兼顾深度与删除上下文实现更优精度-时延平衡
practical_value: '- 做图文/短视频多模态商品理解、多模态推荐的业务，可直接复用CoRePrune的两阶段剪枝逻辑，在不重训MLLM的前提下降低高分辨率商品图、多帧短视频的推理prefill时延，减少服务成本

  - 剪枝评估思路可迁移：将基于删除扰动的条件可移除性评估方法，用到搜索推荐场景的长用户行为序列Token剪枝、智能Agent历史对话KV cache压缩上，提升大模型推荐/Agent的推理效率

  - 渐进式剪枝trick可复用：对长序列输入不要在输入层一次性剪枝，随着表征深度递进刷新剪枝评估指标，平衡剪枝效率和信息保留率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
多模态大模型处理高分辨率图、多帧视频时会生成上千个视觉Token，导致prefill阶段注意力计算开销激增，现有无训练剪枝方法仅基于Token重要性静态筛选，忽略了剪枝深度、删除集合上下文对移除后扰动的影响，容易丢失关键信息导致性能掉点。

### 方法关键点
- 构建条件可移除性评估框架：将剪枝决策从「筛选低重要性Token」转为「评估删除操作对下游的扰动幅度」，明确扰动同时受表征深度、当前删除集合两个条件影响
- 两阶段无训练剪枝逻辑CoRePrune：第一阶段渐进式感知扰动剪枝，在视觉编码器多个深度层刷新删除扰动得分，逐层完成剪枝；第二阶段集合条件优化，在跨模态交互后基于当前虚拟删除集合重新评估候选Token的恢复收益，通过反向贪心筛选最终保留Token
- 低开销工程实现：通过增量更新删除集合统计量、批量反向贪心筛选的方式，将剪枝额外开销控制在毫秒级

### 关键实验
在Qwen3.5、LLaVA系列、InternVL3.5等5个MLLM backbone的图像、高分辨率图、视频任务上，对比DivPrune、CDPruner等SOTA剪枝方法：Qwen3.5上仅保留128个视觉Token时，可保留90.3%的稠密模型性能，同时prefill时间降低51.0%；激进压缩场景下（如InternVL3.5仅保留64个Token），比SOTA基线性能高出14.3个百分点。

### 核心结论
Token重要性不等同于可移除性，剪枝决策必须同时考虑删除的深度位置和已删除集合的上下文影响
