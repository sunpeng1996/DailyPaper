---
title: Decision Models as Retrieval Gates Against Injection and Pollution
title_zh: 用决策模型作为检索门防御RAG的prompt注入与内容污染
authors:
- Mahdi Ghadamyari
- Reza Habibi
affiliations:
- Google
- University of California, Santa Cruz
arxiv_id: '2611.08325'
url: https://arxiv.org/abs/2611.08325
pdf_url: https://arxiv.org/pdf/2611.08325
published: '2026-11-05'
collected: '2026-11-06'
category: RAG
direction: RAG安全 · 检索段注入与污染防护
tags:
- RAG
- prompt injection
- decision model
- retrieval filtering
- content pollution
one_liner: 用开源4B决策模型做RAG检索过滤门，成本为大模型法官1/10，大幅降低攻击成功率
practical_value: '- 电商RAG导购/商品问答、Agent工具调用场景可直接复用该架构，在召回与生成层间加Kev-4B决策门，过滤第三方UGC、网页内容中的恶意注入、引流内容，单段落latency仅76ms，成本为70B大模型法官的1/10，对线上吞吐影响极低

  - 处理HTML来源的召回内容时直接喂原始HTML给决策模型，相比喂纯文本AUROC提升7个点，无需做复杂的HTML解析、隐藏内容剔除等预处理，降低开发成本

  - 面对内容污染风险高的场景（如UGC内容池、开放网页检索），将过滤门放在召回排序前的全候选池阶段，不要仅过滤topN召回结果，避免过滤后有效内容不足导致回答质量暴跌

  - 可复用三层决策逻辑：高风险内容直接丢弃、中风险触发强制引文生成prompt、低风险正常放行，阈值可根据业务可接受的误杀率灵活调整，如误杀要求高设阈值0.5，攻击防控优先级高设阈值0.35'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统依赖开放网络、UGC等非受控召回内容，易被植入prompt注入指令、AI生成的虚假误导内容，传统的文本清洗、Unicode标准化、引文提示等防护方案仅能将攻击成功率从27.9%降至13.6%，残留大量可见注入、字符混淆类攻击，而通用大模型作为检测法官成本过高，难以落地线上高吞吐场景。
### 方法关键点
- 采用开源4B参数决策模型Kev作为检索门，无需微调，单次推理同时输出3个分类得分：是否包含面向AI的指令、是否为误导性填充内容、是否与query相关，无生成过程，推理效率极高
- 决策逻辑：高风险得分直接丢弃段落，中风险触发强制每句带引文的生成prompt，低风险正常放行
- 输入优先采用原始HTML而非提取后的纯文本，保留更多隐藏注入的结构特征
- 内容污染场景下将过滤门放在召回候选池排序前，而非仅过滤topN召回结果，避免过滤后有效内容不足
### 关键实验结果
- 注入测试集：1000条论坛类网页query，覆盖9种注入隐藏载体、4类混淆改写注入
- 污染测试集：200条MS MARCO query，候选池2/3为AI生成虚假点击bait内容
- 核心数字：传统防护方案叠加Kev门后，攻击成功率从13.6%降至5.7%，误杀率仅2.2%，clean query响应率从85.6%微升至86.2%；污染场景下候选池前置过滤将虚假内容曝光率降至0.5%，回答准确率保持83%（无防护仅28%）；Kev单段落推理latency 76ms，成本仅为70B大模型法官的1/10。
> 最值得记住的一句话：小参数量专用决策模型做检索段分类任务的性价比远高于通用大模型法官，足以覆盖绝大多数业务场景的RAG安全需求。
