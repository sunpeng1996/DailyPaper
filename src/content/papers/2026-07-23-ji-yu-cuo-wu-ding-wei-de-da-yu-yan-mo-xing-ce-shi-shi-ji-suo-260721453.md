---
title: Test-Time Scaling via Error Localization
title_zh: 基于错误定位的大语言模型测试时计算缩放方法
authors:
- Rajiv Shailesh Chitale
- Rahul Madhavan
- Taneesh Gupta
- Deepanway Ghosal
- Aravindan Raghuveer
affiliations:
- Google DeepMind
arxiv_id: '2607.21453'
url: https://arxiv.org/abs/2607.21453
pdf_url: https://arxiv.org/pdf/2607.21453
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM推理 · 测试时计算优化
tags:
- Test-Time Scaling
- Error Localization
- Token-Level Credit Assignment
- LLM Reasoning
- Inference Optimization
one_liner: 无需梯度更新，通过token级错误定位复用推理前缀，大幅提升LLM测试时推理效率
practical_value: '- 电商导购/客服Agent处理复杂用户问题时，复用TTEL错误定位逻辑，对失败回答无需全量重生成，仅修正错误片段即可，可降低40%+推理token成本，同时保留上下文一致性

  - 生成式推荐场景（如推荐理由生成、商品文案生成）中，结合规则校验的错误反馈（如价格/属性错误）定位错误token位置，仅重生成错误段落，提升生成效率和内容合规性

  - 工程上可直接复用「真实反馈vs null反馈概率差过滤」的错误定位方案，无需额外训练PRM或微调模型，可快速适配现有LLM推理链路，零训练成本落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM测试时缩放方案（独立采样、多轮迭代修正等）均存在明显效率缺陷：独立采样完全丢弃失败轨迹的有效推理内容，冗余度极高；多轮修正将轨迹专属反馈当作全局修正信号，常重复同类错误或上下文膨胀。尤其在代码、数学这类长推理链场景，单步错误就会导致全轨迹失效，现有方案的计算浪费问题尤为突出。
### 方法关键点
- 错误定位：对失败轨迹分别计算三类上下文下的token生成概率：原生成上下文、带真实反馈的上下文、带无意义null反馈的上下文，通过「（原概率-反馈上下文概率）-（原概率-null上下文概率）」得到过滤后的错误 spike，消除上下文本身带来的概率偏移，精准定位错误token位置
- 搜索策略：定位到错误点后，截断保留错误点之前的有效前缀，仅从错误位置重新生成；若未检测到有效错误信号，才从头重启生成，最大化复用已生成的有效推理内容
- 无训练依赖：整个过程仅用预训练LLM自身的概率输出，无需梯度更新、额外训练奖励模型或微调，适配任意支持log-prob输出的LLM
### 关键实验
在LiveCodeBench代码基准、AIME-2025/HMMT-2025数学竞赛基准上测试，对比基线为独立采样、多轮修正、递归自聚合RSA。核心结果：Qwen3-8B在LiveCodeBench上pass@64达71.0%，仅消耗360.4k生成token，比独立采样的735.0k减少近一半；AIME-2025上pass@16达82.0%，全算力区间的Pareto frontier均优于所有基线。
### 核心结论
测试时优化不需要全量重试，通过LLM自身对反馈前后的概率差异就能定位局部错误，复用有效内容的效率收益远高于重新生成全量轨迹。
