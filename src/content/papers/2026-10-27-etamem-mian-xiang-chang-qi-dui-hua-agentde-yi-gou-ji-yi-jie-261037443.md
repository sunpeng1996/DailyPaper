---
title: 'ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational
  Agents'
title_zh: ETAMem：面向长期对话Agent的异构记忆解耦与对齐框架
authors:
- Xinying Qian
- Ying Zhang
- Yu Zhao
- Xubo Liu
- Baohang Zhou
- Jeff Z. Pan
affiliations:
- Nankai University
- Tiangong University
- The University of Edinburgh
arxiv_id: '2610.37443'
url: https://arxiv.org/abs/2610.37443
pdf_url: https://arxiv.org/pdf/2610.37443
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent长期记忆 · 多视角异构存储
tags:
- Long-term Memory
- Conversational Agent
- Heterogeneous Memory
- Entropy-based Routing
- Multi-view Memory
one_liner: 提出事件/情感/时间三视角异构记忆框架，提升长期对话Agent记忆检索精度与效率
practical_value: '- 电商/导购Agent的用户记忆系统可直接复用三视角拆分思路：将用户交互数据拆分为事实（浏览/购买行为）、情感（好恶评价）、时间三类，分别用通用语义编码器、情感编码器编码，比统一语义存储的召回准确率提升5%以上

  - 检索层可落地熵驱动路由逻辑：无需人工预设不同记忆视图的检索权重，根据查询的相似度分布熵自适应分配预算，对偏好查询、事件查询、时序查询自动适配，比平均分配预算效果提升显著

  - 生产环境降本可复用动态维护机制：用原子记忆单元（AMU）拆分+懒更新节点摘要+自适应阈值校准的组合方案，记忆构建的LLM token消耗比主流时序树记忆方案低60%+

  - 长会话场景可加召回不足fallback逻辑：当检索到的记忆证据不足时， fallback回对应时段的原始会话文本，可补全AMU提取过程中丢失的细节，避免错误回答'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长期对话Agent记忆系统存在两大痛点：一是信息纠缠，粗粒度存储单元混合事实、情感、时序等异构信息，召回噪声高；二是组织错配，仅基于语义相似度的存储结构忽略不同信息的关联逻辑，情感偏好、时序关联类信息易分散，导致多跳、时序查询准确率低，无法支撑长期个性化交互需求。
### 方法关键点
- 异构信息解析：将对话拆分为独立语义的原子记忆单元（AMU），用轻量情感分类器标注极性，中性单元归事实类，正负向单元归情感类
- 三视角分层存储：事件视图用语义相似度聚类组织中性AMU，情感视图用专属情感编码器组织正负向AMU，时间视图按会话/日/周/月固定层级索引全量AMU
- 动态维护机制：事件/情感视图采用自适应阈值执行插入、分裂、合并操作，节点摘要懒更新降低LLM调用成本，阈值用EMA平滑避免波动
- 熵驱动检索：计算查询在各视图下相似度分布的归一化熵，熵越低（检索信号越明确）的视图分配越高检索预算，单视图内用语义+BM25混合得分做分层beam search，召回不足时fallback回原始会话补全细节
### 关键结果
在LoCoMo、LongMemEval-S两个公开长期记忆基准上，对比TiMem、Mem0、MAGMA等SOTA基线：LoCoMo整体准确率84.68%，相对最优基线提升12.46%；LongMemEval-S整体准确率83.00%，相对最优基线提升7.96%；记忆构建token消耗比TiMem低67.92%，推理成本与主流方案持平。
### 核心结论
异构信息分类存储+查询自适应跨视图检索，是比单一结构记忆更适合长期个性化交互的设计思路。
