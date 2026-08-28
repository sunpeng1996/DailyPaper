---
title: 'Prediction of Prediction (PoP): Inter-Layer Activation Fusion for Single-Pass
  Hallucination Detection in Large Language Models'
title_zh: PoP：基于层间激活融合的大模型单步幻觉检测方法
authors:
- Himal Badu
arxiv_id: '2608.27165'
url: https://arxiv.org/abs/2608.27165
pdf_url: https://arxiv.org/pdf/2608.27165
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: 大模型可靠性 · 低开销幻觉检测
tags:
- Hallucination Detection
- Hidden State
- Low-Latency Inference
- Transformer
- Uncertainty Estimation
one_liner: 通过单轮前向传播融合Transformer层间激活实现低开销大模型事实幻觉检测
practical_value: '- 业务使用开源LLM做商品文案生成、导购Agent、智能客服时，可直接接入PoP做幻觉检测，仅增加<1.2% latency几乎不影响吞吐量，无需额外多轮生成开销

  - 可复用层间激活融合思路，做生成式推荐的候选item/query质量校验，预判生成内容的语义正确性，避免给用户推送错误关联的商品或信息

  - 实时响应场景（如搜索Query改写、实时push文案生成）可使用其在线预警能力，在错误内容生成1-2个token时就触发拦截，节省下游推理成本，避免错误内容触达用户

  - 闭源LLM业务场景无法获取隐状态时，可借鉴相邻层表示漂移的统计思路，适配到可获取的输出logit特征上做轻量风险校验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM在电商导购、智能客服、文案生成等高风险业务场景容易生成事实错误内容，现有幻觉检测方案要么依赖多轮生成/外部校验带来数倍latency和资源开销，要么仅用输出层logit或单层隐状态容易误判（过置信错误内容漏检、风格化正确内容误杀），急需低开销、高精度的单步检测方案。
### 方法关键点
- 仅在单轮前向传播时通过钩子抓取Transformer各层隐状态，无需修改模型权重或额外生成步骤
- 计算相邻归一化隐状态的余弦距离作为层转移不确定性特征，结合可学习深度权重聚合
- 用轻量跨层注意力融合全层隐状态，拼接转移特征、时序漂移特征后通过2层MLP输出token级幻觉概率，再经Platt校准得到序列级风险分
- 检测头总参数量仅1.4M左右，额外计算开销极低
### 关键结果
在TruthfulQA、HaluEval 2.0、FaithDial三个基准测试，对比logit熵、静态隐层探针、语义熵（K=5）、外部NLI校验等baseline：
- Llama-3-8B上TruthfulQA AUROC达75.5%，比最优单层探针高9.4pp，仅比多轮语义熵低0.7pp但latency低400%
- 额外开销仅0.3ms/token、18.4MB显存，推理latency增幅<1.2%
- 跨模型迁移AUROC降幅<3.5pp，抗风格、温度扰动的性能降幅<2.4pp
- token级检测精度71.8%、召回68.4%，可在错误生成后1.2个token内触发预警
### 核心结论
层间表示的动态转移特征比单层静态隐状态或输出logit包含更可靠的事实正确性信号，可在几乎不影响推理效率的前提下实现幻觉检测
