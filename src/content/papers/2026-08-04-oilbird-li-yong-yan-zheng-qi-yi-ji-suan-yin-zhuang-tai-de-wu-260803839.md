---
title: 'Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already
  Computes'
title_zh: Oilbird：利用验证器已计算隐状态的无训练投机解码方法
authors:
- Tao Jin
- Phuong Minh Nguyen
- Zhenzhu Yan
- Teeradaj Racharak
- Naoya Inoue
affiliations:
- Japan Advanced Institute of Science and Technology
- Tohoku University
arxiv_id: '2608.03839'
url: https://arxiv.org/abs/2608.03839
pdf_url: https://arxiv.org/pdf/2608.03839
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM推理优化 · 无训练投机解码
tags:
- Speculative Decoding
- Training-free
- Inference Acceleration
- Tool Calling
- Semantic Retrieval
one_liner: 新增基于验证器已计算隐状态的语义检索分支，融合现有词法投机解码树，无训练提升工具调用场景推理速度
practical_value: '- 对于电商客服Agent、工具调用类Agent服务，可直接复用该无训练Speculative Decoding方案，在不修改模型输出的前提下提升推理速度，工具调用场景最多可达4.4倍加速，比训练类方案EAGLE-3快一倍以上，无额外训练成本

  - 现有已落地的无训练Speculative Decoding系统（如基于后缀匹配的方案）可低侵入接入该语义分支，不需要额外增加节点预算，即可提升24%~29%的接受token长度，改造代价极低

  - 对于重复度高的生成场景（如电商商品文案批量生成、订单通知生成），可借鉴「同一存储双索引（词法+语义隐状态）+ 树结构合并」的设计，避免重复计算，进一步提升生成吞吐'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有无训练Speculative Decoding依赖精确后缀匹配，在工具调用这类重复结构多但局部参数（如ID、名称）不同的场景下，大量已存在的正确候选因为局部token不同无法匹配，在工具调用密集的API-Bank基准上，最强精确匹配方案漏匹配的案例中约一半是寻址问题而非覆盖问题，浪费了已有计算资源，亟需无额外训练成本的优化方案。

### 方法关键点
- 存储设计：同一份历史生成token池，同时维护两套索引：一套是原有的词法后缀索引，另一套是验证器每步已计算的、模型约85%层位置的隐状态余弦索引，隐状态直接从验证前向传播中拷贝，无额外计算开销
- 检索逻辑：先运行词法检索得到基础链，仅在词法匹配非空时触发语义检索，取top8相似度≥0.8的隐状态对应候选，根据相似度动态决定拷贝长度，相似度越高拷贝越长
- 树合并策略：语义候选链从树根开始和已有的词法树合并，相同前缀的节点共享不重复创建，仅占用固定16/60的树节点预算，不提升验证开销，验证逻辑完全不变保证输出无损

### 关键实验
测试覆盖10个基准，重点验证API-Bank、ToolAlpaca、tau-bench零售三个高重复场景，基线对比GOOSE、SuffixDecoding、EAGLE-3等主流方案。在API-Bank工具调用场景下，Llama-3.1-8B上达到4.4×自回归解码速度，比最强无训练基线高13%，比训练类基线EAGLE-3高116%；嵌入到3个已有无训练Speculative Decoding系统中，相同池和节点预算下接受长度提升24%~29%。

**最值得记住的一句话**：无训练Speculative Decoding的核心瓶颈在寻址而非覆盖，利用验证过程中已经产生的免费隐状态做语义检索，能以极低代价解决精确匹配的盲区。
