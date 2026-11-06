---
title: 'From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional
  Hallucinations?'
title_zh: 面向文本与Agent场景的多维度幻觉检测基准HALUCHECK
authors:
- Hanyu Qiu
- Ze Liu
- Zhe Zhao
- Kuang Xiong
- Blaze Chen
- Zhenxiang Yan
- Renfen Hu
affiliations:
- Beijing Normal University
- Tencent AI Lab
arxiv_id: '2611.08231'
url: https://arxiv.org/abs/2611.08231
pdf_url: https://arxiv.org/pdf/2611.08231
published: '2026-11-05'
collected: '2026-11-06'
category: Eval
direction: 幻觉检测评测 · 文本与Agent双场景
tags:
- Hallucination Detection
- Benchmark
- Agent
- LLM Evaluation
- Factuality
- Faithfulness
one_liner: 发布42k中英双语多粒度幻觉检测基准，覆盖文本事实与Agent轨迹两类幻觉
practical_value: '- 电商/推荐场景下LLM生成的商品文案、营销内容、智能客服回复的幻觉检测，可复用HALUCHECK的三类文本扰动策略（属性错配、数值偏移、细节虚构）构造自测数据集，快速验证内部幻觉检测能力

  - 开发电商导购Agent、任务型Agent的团队，可直接复用HaluAgent的三类幻觉标注体系（规划、工具调用、感知）搭建轨迹质检流程，快速定位Agent执行错误的根因节点

  - 幻觉检测模型优化可复用三个验证有效的提效方向：开启显式Thinking链路提升细粒度定位准确率、接入Web Search/RAG降低事实类幻觉漏判、用少量标注数据做LoRA微调适配特定场景幻觉模式'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM已广泛应用于内容生成、信息检索、Agent任务执行等场景，低概率幻觉在规模化落地时仍会引发法律纠纷、虚假信息传播、Agent错误执行等高风险后果，现有幻觉检测基准零散、覆盖场景单一，缺乏细粒度定位、修正、根因追溯的标注支撑，尤其缺失中文场景和Agent轨迹类幻觉的标准化评测能力。
### 方法关键点
- 构建总规模42k+的中英双语HALUCHECK基准，分为HaluText（事实类幻觉，含真实扰动的HALUREAL、虚构实体的HALUFAKE子集）和HaluAgent（Agent轨迹忠实度幻觉）两大模块
- 标注覆盖样本级检测标签、文本幻觉的span位置与修正值、Agent幻觉的最早根因步骤，扰动程度分明显、中等、细微三级，贴合真实业务中幻觉的发生特点
- 设计支持Uncertain选项的评测指标，对不确定回答赋值0.5分，平衡检测准确率与风险保守性，更符合业务落地的安全需求
### 关键结果
在14款主流LLM上评测：文本事实幻觉检测最高准确率84%，但span定位F1、修正率均显著低于检测准确率；Agent场景幻觉检测最高准确率仅72.36%，根因步骤定位准确率不足60%；开启Thinking、接入Web Search、LoRA微调分别可带来5%-15%的性能提升，但均无法完全解决幻觉检测问题。

值得记住的结论：当前LLM的幻觉检测能力仍存在明显短板，尤其Agent场景的细粒度幻觉定位与根因追溯远未达到大规模业务可用水平。
