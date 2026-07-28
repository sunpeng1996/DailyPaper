---
title: 'A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens,
  Bit-Exact, Forever'
title_zh: 冻结12B模型基于验证内存实现零生成Token、100%准确输出，优于前沿大模型
authors:
- Sietse Schelpe
affiliations:
- Corbenic AI
arxiv_id: '2607.23806'
url: https://arxiv.org/abs/2607.23806
pdf_url: https://arxiv.org/pdf/2607.23806
published: '2026-07-25'
collected: '2026-07-28'
category: LLM
direction: LLM推理优化 · 验证内存复用
tags:
- Frozen-LLM
- Verified-Memory
- Zero-Generation-Token
- Deterministic-Inference
- Exact-Addressing
one_liner: 冻结12B模型搭配前置验证的持久化内存，对已解决问题家族实现零生成Token、确定性100%准确的低延迟输出
practical_value: '- 电商场景下高频重复的结构化计算（如满减规则匹配、商品价格核算、用户权益校验）可参考「一次验证+永久复用」架构，替换当前每次请求调用LLM重复计算的流程，单问题家族仅17-34次请求即可收回验证成本，后续零Token开销

  - Agent技能库可放弃传统向量相似度检索，改用精确寻址+前置验证的存储层，避免94%+的错误检索率，同时实现技能复用的零生成Token开销

  - 对需要审计、合规的广告推荐场景（如文案合规校验、敏感内容识别规则），可复用这套bit-exact确定性输出的设计，满足监管可追溯要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM能力提升依赖重训，GPU成本高昂、模型迭代后行为需重新审计、输出天然非确定，且对已解决的重复问题每次查询都要支付全量生成Token成本；现有RAG、KV缓存、Agent技能库等方案均无法同时满足精确寻址、预验证、零生成Token复用的要求，大量重复推理场景浪费严重。
### 方法关键点
- 模型全程冻结无权重更新，能力增长完全来自独立的持久化验证内存层，所有存入内存的解法都经过不依赖答案密钥的独立验证环节，不合格内容直接拦截
- 内存存储参数化的验证方法而非固定答案，支持同问题家族下全新参数实例的计算，也支持多存储项的跨域组合推理
- 采用精确内容寻址而非近似向量检索，寻址延迟达微秒级，零碰撞
### 关键结果
- 覆盖9类算法/数学问题的180个全新测试实例，4款不同架构12-14B模型（含MoE）全部达到180/180准确率，零生成Token，单次回答延迟仅6-23ms，能耗36mWh
- 4500条存储项场景下，近似向量检索错误率达94.3%，精确寻址零错误
- 单张46GB GPU支持600万Token可移动上下文窗口，显存占用仅增长263MB，远高于vLLM的3万Token上限
- 单问题家族的一次性验证成本摊销阈值仅17-34次查询，之后的所有访问均为纯收益
### 核心结论
对可验证的重复工作，一次验证、永久复用的架构在成本、延迟、确定性上远优于每次重新生成的前沿模型调用模式
