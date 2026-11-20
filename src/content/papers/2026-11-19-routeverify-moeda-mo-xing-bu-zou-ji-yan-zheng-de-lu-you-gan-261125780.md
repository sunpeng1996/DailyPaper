---
title: 'RouteVerify: Routing Interventions for Step-Level Verification in Mixture-of-Experts
  Models'
title_zh: RouteVerify：MoE大模型步骤级验证的路由干预机制研究
authors:
- Yucheng Du
- Ryan A. Rossi
- Xiyang Hu
affiliations:
- University of Southern California
- Adobe Research
- Arizona State University
arxiv_id: '2611.25780'
url: https://arxiv.org/abs/2611.25780
pdf_url: https://arxiv.org/pdf/2611.25780
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: MoE大模型 · 路由干预与可解释性
tags:
- MoE
- activation patching
- step verification
- interpretability
- routing
one_liner: 通过受控激活替换实验揭示MoE路由可读取正确性信号但干预效果很少匹配供体步骤正确性
practical_value: '- 电商/Agent场景用MoE做推理、生成推荐时，可复用路由logit探针快速识别推理步骤正确性，AUROC最高达0.88，无需修改模型即可轻量上线

  - 做MoE模型行为调控时，优先选择post-MoE残差作为干预位点，单层干预下残差替换效果始终优于路由/MoE输出替换（36组对比全占优）

  - 基于MoE做内容合规、商品描述校验等步骤级验证场景时，不要仅依据路由信号的可解释性就用路由干预调整结果，其输出变化很少和供体正确性挂钩，可控性差

  - 若必须用路由做干预，优先选择跨全路由层+推理分歧点附近token窗口的组合方案，干预效果远优于单层单token路由替换'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
过往研究观察到MoE路由状态可区分正确与错误推理步骤，行业普遍默认修改路由即可控制步骤级验证结果，但该因果关联从未经过严格验证，明确路由干预的效果边界对MoE的可解释性优化、推理行为调控有重要落地价值。
### 方法关键点
- 设计RouteVerify受控激活替换框架，对比三类干预接口：router logits、MoE输出、post-MoE残差状态，变量控制替换的层范围、token位置
- 定义两个独立量化指标：T衡量配对激活替换下的验证margin变化幅度，D衡量固定接收方时不同正确性供体的margin差异，严格区分干预效果大小与正确性依赖度
- 覆盖9个主流开源MoE checkpoint（Qwen3、Gemma4、OLMoE等），基于PRMBench步骤级推理验证数据集完成对照实验
### 关键结果
- 路由logit的out-of-fold探针可有效区分正确/错误推理步骤，8个checkpoint的AUROC达0.80~0.88
- 单层干预下，残差替换的效果始终优于路由/MoE输出替换（36组对比全部占优）；跨全路由层替换路由logits可显著提升干预效果，9个checkpoint的效果均超过范数匹配的随机替换对照组
- 路由干预的效果很少依赖供体正确性：单层路由干预下9个checkpoint的D均不显著，全层路由干预下仅1个checkpoint的D显著为正；而残差干预下8/9的checkpoint的D显著为正
### 核心结论
MoE路由能读取正确性信号不代表干预路由就能按照正确性方向改变模型输出，干预效果的大小和正确性依赖度是两个完全独立的指标，完全取决于干预接口、层覆盖范围和token位置选择
