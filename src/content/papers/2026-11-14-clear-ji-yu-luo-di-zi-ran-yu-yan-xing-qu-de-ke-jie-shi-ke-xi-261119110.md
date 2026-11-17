---
title: 'CLEAR: Legible and Steerable Recommendation via Grounded Natural-Language
  Interests'
title_zh: CLEAR：基于落地自然语言兴趣的可解释可调控推荐系统
authors:
- Qi Guo
- Reza Mirghaderi
- Iordanis Fostiropoulos
- David Fan
- Yuchen Liu
- Shiliang Tang
- Lukasz Korycki
- Golnaz Ghasemiesfeh
- Xinzhu Bei
- Sasha Vorontsov
affiliations:
- Meta
arxiv_id: '2611.19110'
url: https://arxiv.org/abs/2611.19110
pdf_url: https://arxiv.org/pdf/2611.19110
published: '2026-11-14'
collected: '2026-11-17'
category: RecSys
direction: 可控可解释推荐 · 自然语言兴趣层
tags:
- Controllable Recommendation
- Natural Language User Profile
- LLM4Rec
- Deployed System
- User Modeling
one_liner: Meta推出搭载可编辑自然语言兴趣层的可控可解释推荐系统，已落地Instagram与Facebook
practical_value: '- 可复用「自然语言兴趣层统一读写路径」设计：用户显式编辑的兴趣优先级高于模型推断结果，直接打通检索、排序、归因、曝光控制全链路，避免用户修改不生效的问题，适合电商个性化推荐的用户可控功能开发

  - 落地层面可参考「新增兴趣冷启动三板斧」：兴趣触发的候选召回贡献13.7pp响应率提升、预留顶部坑位贡献11.1pp、排序加权贡献8.7pp，三者叠加可快速响应用户新增兴趣诉求，适配短视频/电商Feed的实时调控需求

  - 效率优化方案可直接复用：兴趣增量更新而非全量重生成降低35%算力开销，全局共享兴趣归一化标注减少98%的重复标注请求，适合大规模生产环境降本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统的用户偏好表征是隐式黑盒，用户无法查看、修改系统推断的兴趣，单点反馈也无法保证偏好修正的持久性，亟需同时具备可解释性（用户能看懂兴趣推断结果）和可调控性（用户修改能真实影响后续推荐结果）的工业级系统设计，且要能兼容现有推荐链路，无需完全替换原有排序模型。

### 方法关键点
- 构建可编辑自然语言兴趣层：LLM从用户近期行为生成候选兴趣，经行为接地（反向匹配用户历史交互事件验证）后展示给用户，用户显式添加/屏蔽的兴趣优先级高于模型推断结果，持久存储不被后续推断覆盖
- 统一兴趣身份打通全链路：每个归一化后的兴趣作为检索地址，同时支持lexical检索、行为触发的i2i检索、Embedding ANN检索、生成式检索，召回的候选和原有推荐池合并后排序
- 闭环曝光调控：实时统计每个兴趣的曝光量，过高则降低权重，过低则补充候选，避免单兴趣刷屏，用户对调控推荐的交互回流到基础推荐模型训练数据

### 关键实验
用户直接评测显示88.5%的展示兴趣被判定为准确；离线兴趣生成任务上，定制3B模型F1@10达0.3967，优于Gemini 2.5 Pro的0.3633和旧版生成器的0.1911，推理成本仅为Gemini 2.5 Pro的1/216。线上生产实验中，用户新增兴趣的当日响应率达79.6%，82.6%的用户的显式兴趣内容占推荐量的5%以上，独立多模态裁判判定87.2%的兴趣匹配曝光内容是相关的。

### 核心结论
可控推荐的核心不是暴露推荐系统的全部内部状态，而是提供可编辑的权威兴趣层，让用户修改能真实落地到全推荐链路，同时不需要重训基础模型。
