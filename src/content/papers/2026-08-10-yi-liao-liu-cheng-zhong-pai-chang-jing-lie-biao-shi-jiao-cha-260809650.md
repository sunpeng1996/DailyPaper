---
title: 'Listwise Cross-Encoder Fine-Tuning vs. Agentic Instruction Tuning for LLM
  Rerankers: A Systematic Study in Medical Procedure Reranking'
title_zh: 医疗流程重排场景列表式交叉编码器微调与智能体调优LLM重排器对比研究
authors:
- Matan Fainzilber
- Shlomit Plavner
affiliations:
- Healthee
arxiv_id: '2608.09650'
url: https://arxiv.org/abs/2608.09650
pdf_url: https://arxiv.org/pdf/2608.09650
published: '2026-08-10'
collected: '2026-08-11'
category: RecSys
direction: 重排系统 · 范式对比与落地优化
tags:
- Cross-Encoder
- Listwise Learning to Rank
- Reranking
- Agentic Prompt Optimization
- LLM Reranker
one_liner: 系统对比两类重排范式，证实109M列表式微调交叉编码器效果优于37倍参数量的4B LLM重排器
practical_value: '- 成本/延迟敏感的生产重排场景优先选择小参数量领域适配交叉编码器做listwise微调，效果优于大参数量LLM重排器，可直接复用在电商搜索/广告重排场景，大幅降低
  serving 成本

  - 缺标注数据时可采用「LLM生成多样化query+LLM排序标注+Top3质量过滤」流水线构造领域重排数据集，覆盖长尾意图，适合电商新品/冷门类目的重排数据搭建

  - 用LLM做重排基线时可复用agentic prompt优化闭环，基于badcase迭代生成候选prompt，无需手动调优，适合临时小流量实验的快速基线搭建

  - 交叉编码器微调优先选ListNet/LambdaLoss，冻结策略最多冻embedding层，冻结超过6层会带来明显效果下降，可直接复用这套配置到通用领域重排任务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
医疗保险查询场景存在用户口语表达与临床术语的巨大语义鸿沟，重排效果直接影响理赔正确性与用户体验；当前大模型重排器推理成本高、延迟大，而小参数量交叉编码器此前多采用pointwise/pairwise损失，未直接优化整列表排序质量，亟需系统性对比两类重排范式的落地价值。

### 方法关键点
- 数据：双阶段LLM合成数据集，基于708个保险服务生成2647条覆盖3类意图的用户查询，再用GPT-4o做相关性排序，过滤保留目标项在前3的样本，专家验证Top3准确率达92%+
- 交叉编码器方案：选取MedCPT、MiniLM两个backbone，对比LambdaLoss、ListNet、PListMLE三种listwise损失，测试全参数训练、冻embedding、冻前6层三种冻结策略
- LLM重排器方案：基于Qwen3-Reranker-4B，采用GPT-4驱动的智能体迭代优化prompt，通过good/bad case生成候选prompt，验证择优迭代直到收敛

### 关键实验
在263条 held-out 测试集上，最优方案为109M参数量的MedCPT+ListNet全参数训练，NDCG@3达0.961，比prompt优化后的4B Qwen3重排器高2.6pp，Spearman相关系数高13.3pp，参数量仅为后者的1/37，可直接跑在CPU上。

### 核心结论
在领域明确、成本/延迟约束强的生产重排场景，小参数量领域适配模型做listwise微调的投入产出比远高于大参数通用LLM重排器
