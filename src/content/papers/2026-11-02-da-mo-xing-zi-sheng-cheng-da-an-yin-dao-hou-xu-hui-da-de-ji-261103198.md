---
title: Written Once, Read Differently How Language Models Own Answers Steer Their
  Next Ones
title_zh: 大模型自生成答案引导后续回答的机制与低代价干预方法
authors:
- Marcus Armstrong
affiliations:
- University of Houston
arxiv_id: '2611.03198'
url: https://arxiv.org/abs/2611.03198
pdf_url: https://arxiv.org/pdf/2611.03198
published: '2026-11-02'
collected: '2026-11-03'
category: LLM
direction: 大模型可解释性 · 行为干预
tags:
- self-commitment
- representation_engineering
- activation_steering
- attention_sink
- interpretability
one_liner: 揭示大模型自我承诺效应的统一写入方向与可变读取电路，实现低代价消除该效应
practical_value: '- 做多轮电商导购Agent/推荐场景的LLM应答时，可通过ablation跨主题共享的承诺方向，降低前序回答对后续商品/问题判断的偏差，保留attention
  sink时PPL损失仅≤1.3%

  - 多轮Agent架构选型时，不要直接迁移小模型的电路级优化结论到7B以上大模型：规模越大，承诺效应的读取电路越分散，前10个注意力头承载的耦合占比从100%降至28%-40%

  - 用LLM做A/B测评、用户调研模拟时，注意不同模型、system prompt、训练方式会改变自承诺的读取逻辑甚至反转符号，需提前做场景适配校验

  - 基于representation engineering做模型行为调控时，优先选择跨主题共享的隐层方向做干预，普适性更强、边际成本更低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型广泛应用于多轮对话、Agent决策、自动测评场景，前序自生成输出会系统性倾斜后续不同问题的判断结果，导致错误传播、结论依赖对话顺序，现有研究未明确该自承诺效应的跨模型通用机制，也缺乏低代价的消除方案。

### 方法关键点
- 构造覆盖4个领域120个实体的3600组二元问题对测试集，固定模型首个回答为Yes/No，度量第二个回答的对数几率偏移量（耦合度）
- 从残差流提取每个问题的承诺方向，识别跨主题共享的统一隐层方向g，通过direction ablation、注意力头归因定位读写电路
- 设计消融时保留attention sink的优化方案，平衡效应消除效果与通用能力损失

### 关键结果
- 22款0.5B-72B开源模型中，问题承诺方向的余弦相似度与耦合度的Spearman相关系数达0.43-0.85，ablation共享方向g后最多仅残留17%的耦合效应
- 指令微调后14%-96%的问题会反向读取承诺方向，部分模型仅修改system prompt即可反转读取符号
- 保留attention sink的消融方案下，18/19的指令微调模型PPL上升≤1.3%，MMLU精度波动≤±3.5个点，16款模型保留90%以上的独立回答准确率

### 核心结论
大模型的特定行为可能存在稳定的隐层写入方向，但读取电路会随模型规模、训练方式、prompt动态变化，小模型的机制研究结论不能直接迁移到大模型。
