---
title: 'Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space
  Reweighting'
title_zh: Loom：基于嵌入空间重加权的自由文本诊断共识生成框架
authors:
- Ron Begleiter
- Katya Egert Berg
- Gilad Saban
- Gil Shabat
affiliations:
- NVIDIA
arxiv_id: '2609.02649'
url: https://arxiv.org/abs/2609.02649
pdf_url: https://arxiv.org/pdf/2609.02649
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: 根因分析Agent · LLM共识优化
tags:
- RCA
- LLM Consensus
- Embedding Reweighting
- Inference Optimization
- Weak Supervision
one_liner: 提出仅需单次LLM调用的生成式共识框架，在根因分析任务上实现26~33倍推理提速并匹配SOTA精度
practical_value: '- 多信号聚合场景可复用嵌入空间迭代质心重加权方法，替代多轮LLM辩论/投票方案，大幅降本提速，可直接迁移到电商用户评论多维度归因、广告投放效果异常诊断等场景

  - 可将领域专家知识预编译为可执行的模板化规则（类似Diagnostic Strands），再用轻量LLM做信息合成，比端到端Agent幻觉率更低、可解释性更强，适合电商合规性要求高的故障排查、客诉根因分析场景

  - 共识阶段完成冲突消解后，下游合成任务可使用8B级小参数LLM，精度损失极小，适合本地化部署、低延迟要求的业务场景，比如实时流量异常告警的根因生成'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工业场景下多源噪声文本信号的可靠共识聚合是NLP落地的核心痛点，传统弱监督仅能处理离散标签，而端到端LLM Agent存在上下文限制、幻觉累积、推理延迟过高等问题，尤其根因分析（RCA）这类高可靠性、低延迟要求的场景，现有方案难以兼顾精度、效率与可解释性。

### 方法关键点
- 模块化Diagnostic Strands设计：将领域专家知识/历史故障经验预编译为程序型启发式规则，触发时输出填充了实体、时序、指标的模板化假设，不触发则弃权，避免runtime无边界搜索
- 迭代嵌入质心重加权算法：将所有触发的假设映射到连续嵌入空间，先基于规则文档相似度做冗余去重，再以专家预设权重初始化，交替更新质心与规则权重，语义匹配度高的共识性假设权重更高，全程仅需毫秒级耗时
- 轻量LLM合成：仅将重加权排序后的Top-K假设输入单次LLM调用，严格约束LLM仅做信息整合，禁止新增事实，大幅降低幻觉风险

### 关键结果
在OpenRCA基准的4个数据集上对比SOTA RCA Agent基线，Loom在Bank、Market-2数据集上匹配基线精度，仅在Market-1、Telecom上略有差距；单incident仅需1次LLM调用，平均耗时22s，相对基线的567s实现26倍提速，改用Llama-3.1-8B作为合成器时提速可达33倍，精度仅下降3.7个百分点。

最值得记住的一句话：对于规则覆盖度足够的工业垂直场景，将冲突消解前置到确定的数学空间，再用LLM做轻量合成，远比端到端迭代Agent更适合落地。
