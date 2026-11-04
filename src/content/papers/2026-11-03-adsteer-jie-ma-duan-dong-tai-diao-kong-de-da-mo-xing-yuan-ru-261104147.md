---
title: 'AdSteer: Native Advertising in Large Language Model Generation'
title_zh: AdSteer：解码端动态调控的大模型原生广告植入框架
authors:
- Shuhang Lin
- Chuhao Zhou
- Zhenyu Wang
- Xiao Lin
- Changsheng Wang
- Saibo Geng
- Dimitris N. Metaxas
affiliations:
- Rutgers University
- Nanyang Technological University
- UIUC
- Michigan State University
- EPFL
arxiv_id: '2611.04147'
url: https://arxiv.org/abs/2611.04147
pdf_url: https://arxiv.org/pdf/2611.04147
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · LLM原生广告植入
tags:
- Native Advertising
- Constrained Decoding
- Logit Steering
- LLM Monetization
- Controllable Generation
one_liner: 基于冻结LLM解码端token概率动态调控，自然植入原生广告，兼顾体验与效率
practical_value: '- 解码端logit软约束steering的思路可直接复用在电商智能客服、生成式导购场景，无需微调LLM即可自然植入商品推荐，避免生硬插入的体验损失，同时比多轮改写方案省20%+推理token成本

  - AdAnchor绑定广告与用户意图短语的设计可迁移到广告召回阶段，解决短query与广告描述的语义gap，大幅提升召回相关性，尤其适配搜索、AI导购等强意图场景

  - 四状态FSM+轻量SteerHead的受控生成框架可复用在指定关键词植入、合规内容管控等场景，只需替换AdTrie的关键词库即可上线，单step新增延迟<1ms，几乎无推理overhead

  - 分类头粒度选择结论可直接落地：开放对话场景用通用SteerHead，强商业意图的搜索/导购场景用细分类目专属头，平衡效果和训练成本'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM规模化部署推理成本高，现有原生广告植入方案存在明显缺陷：prompt级注入生硬、多轮改写推理成本高、微调灵活性差无法适配广告库存快速更新，难以平衡用户体验、投放效率和商业收益，亟需轻量可落地的LLM原生广告方案。

### 方法关键点
- 四阶段pipeline：AnchorRetrieval通过预定义的意图短语锚点匹配广告，解决短query与广告描述的语义gap；AdTrie构造广告关键词前缀树，实现token级匹配追踪；四状态FSM控制广告植入的触发、激活、退出时机；轻量SteerHead动态调控每步的转向强度和衰减系数，通过修改token logit实现软约束生成，全程冻结LLM backbone。
- 采用MoE思路构建CategorySteerBank，包含通用头和类目专属头，根据query所属类目路由调用，适配不同垂类的植入逻辑，无额外推理延迟。
- 两阶段训练：先在全类目数据上预训练通用头，再基于通用权重微调类目专属头；奖励函数同时覆盖广告命中、生成自然度、原分布保真度三个维度，通过奖励加权回归训练SteerHead。

### 关键实验
在GEM-Bench的三个场景（人文对话、通用聊天、商业搜索）上评测，对比prompt注入、后置插入、多轮改写、微调四类基线：整体得分平均比最强基线高14.1%，总token消耗比改写类方法低22.5%；商业搜索场景下自然度得分最高提升45.3%，信任度得分最高提升130%。

### 核心结论
LLM原生广告不需要在用户体验和商业变现之间做强制tradeoff，解码端轻量软约束控制可以实现广告的自然植入，综合表现优于现有所有方案。
