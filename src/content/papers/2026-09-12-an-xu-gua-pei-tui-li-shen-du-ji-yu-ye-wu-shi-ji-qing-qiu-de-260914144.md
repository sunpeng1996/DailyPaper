---
title: 'One Size Does Not Fit All: Setting Inference Depth from the Questions a Deployment
  Actually Asks'
title_zh: 按需适配推理深度：基于业务实际请求的LLM早退出优化
authors:
- Jerry Kaplan
affiliations:
- Stanford University
arxiv_id: '2609.14144'
url: https://arxiv.org/abs/2609.14144
pdf_url: https://arxiv.org/pdf/2609.14144
published: '2026-09-12'
collected: '2026-09-15'
category: LLM
direction: LLM推理优化 · 早退出阈值校准
tags:
- Early Exit
- Inference Optimization
- LLM Deployment
- Edge LLM
- Evaluation Metric
one_liner: 无需修改模型、无标注即可针对特定部署校准早退出阈值实现推理加速，揭示token级保真度评估的缺陷
practical_value: '- 电商垂类场景（客服回复、商品属性抽取、营销文案生成等）可直接复用该无标注校准流程：采集60+业务真实Prompt跑全模型得到输出，再基于业务可接受的保真度校准早退出阈值，无需修改模型即可获得1.1x~1.6x的推理速度提升，降低部署成本

  - 端侧购物Agent/本地推荐类应用优先在7B/8B参数级模型上落地该方案，置信度校验成本仅占全栈算力的8%左右，远低于0.5B小模型的38%，收益更显著；exit深度直接选满足保真度要求的最浅层即可

  - 垂类LLM服务的效果评估不能仅依赖token级保真度、困惑度这类通用指标，必须增加业务任务级校验（比如属性抽取的字段准确率、活动规则问答的答案正确率），避免出现指标好看但业务效果严重下降的问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Transformer生成每token都需跑完所有层，算力浪费严重；通用早退出方案采用全局统一阈值，没有利用特定部署场景的请求分布特性，实际收益受限；同时现有token级保真度等评估指标未考虑任务正确性，容易误导优化方向。
### 方法关键点
- 完全不修改预训练模型，仅在中间层附加轻量readout（1.5B模型仅3MB），将中间层隐状态投影到输出层坐标空间，无需人工标注，直接用全模型自身的输出作为标签拟合readout
- 仅针对部署场景的真实流量校准早退出置信度阈值即可获得最大收益，readout权重、exit深度无需分场景定制，单个通用readout即可覆盖多类业务场景
- 推理时若中间层输出的置信度超过校准阈值则直接输出，否则跑完全部层，缺失的KV cache采用现有投影方法补全
### 关键实验
覆盖7类垂类语料（算术题、Python补全、信息抽取、客服回复、中英文解释等），在3款主流开源模型（Qwen2.5-1.5B/7B、Llama3.1-8B）上测试：
1. 仅校准阈值即可将早退出率最高提升59个百分点，1.5B模型在算术题场景半层退出率达96%，7B模型推理速度最高提升1.38倍，Llama 8B最高提升1.59倍
2. 中文场景的早退出收益最低，对阈值要求最严格，是全局阈值的主要约束项
3. token级保真度存在严重缺陷：算术题场景下token级保真度达0.87的配置，答案正确率仅20%，而全模型正确率为100%
### 核心结论
所有垂类部署场景都可以通过无标注的阈值校准挖掘早退出的额外收益，永远不要用全局统一阈值做垂场景的早退出配置，同时要警惕token级指标掩盖的任务正确性损失
