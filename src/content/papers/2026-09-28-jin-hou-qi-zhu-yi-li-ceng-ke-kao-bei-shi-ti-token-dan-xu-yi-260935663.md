---
title: Late Attention Layers Alone Can Copy Entity Tokens, but Not Without Attending
  to Their Context
title_zh: 仅后期注意力层可拷贝实体Token，但需依赖上下文注意力引导
authors:
- Muyu He
- Yuchen Liu
- Ran Tao
- Li Zhang
affiliations:
- Independent
- University of Pennsylvania
- Drexel University
arxiv_id: '2609.35663'
url: https://arxiv.org/abs/2609.35663
pdf_url: https://arxiv.org/pdf/2609.35663
published: '2026-09-28'
collected: '2026-09-30'
category: LLM
direction: LLM可解释性 · 实体拷贝注意力机制
tags:
- Entity Copying
- Interpretability
- Attention Mechanism
- Transformer
- LLM
one_liner: 提出两种可解释性方法，揭示LLM实体拷贝依赖后期层与上下文注意力的机制
practical_value: '- 做电商RAG导购、订单查询类Agent时，可在prompt中为需要精确输出的实体（如商品SKU、订单号、优惠券码）添加1-2个强相关事实描述，提升精确拷贝准确率，避免输出错误码值

  - 优化LLM推理服务时，针对实体拷贝占比高的场景（如搜索Query改写、用户指令实体抽取），可针对性保留后半段注意力层的KV cache，裁剪前半层冗余缓存，降低显存占用

  - 做prompt工程时，若任务要求严格匹配prompt中的实体（如生成广告文案需精确保留品牌名、商品名），避免使用与实体弱相关的无关上下文，防止干扰注意力引导，降低精确输出率'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
实体拷贝是LLM从prompt中提取信息、完成下游任务的基础能力，现有研究仅聚焦单个注意力头的拷贝功能，未明确不同深度层的分工，也未厘清上下文token对实体拷贝的影响机制，无法为模型优化、prompt设计提供可落地的指导。
### 方法关键点
- 设计genie-in-a-bottle方法：将实体信息访问限制在固定滑动层窗口内，精准量化不同层对实体拷贝的贡献，避免跨窗口信息泄露干扰
- 设计attention lobotomy方法：softmax后清零指定token间的注意力权重，精准隔离单条注意力路径的因果影响，不改变其余注意力分布
- 基于Qwen3-8B-Base开展实验，覆盖5类实体拷贝prompt模板、100个单/双token实体，以精确拷贝成功率、通用拷贝成功率为核心评估指标
### 关键实验结果
- 仅模型后半段2组独立注意力层（L20附近+最末段）对实体拷贝是必要且充分的，前半层仅通过定位实体位置间接贡献，无直接提取作用
- 切断上下文token对实体的注意力后，精确拷贝成功率平均下降47%，仅能输出实体对应概念（如输出George代替Orwell），无法匹配原token
- 仅当上下文描述与实体事实一致且强关联时，上下文才会存储实体信息，否则仅起到注意力引导作用
### 核心结论
LLM的精确实体拷贝不是仅靠解码位置对实体的注意力就能完成的，必须依赖上下文token对实体的注意力引导，且核心计算集中在模型后半段的特定层
