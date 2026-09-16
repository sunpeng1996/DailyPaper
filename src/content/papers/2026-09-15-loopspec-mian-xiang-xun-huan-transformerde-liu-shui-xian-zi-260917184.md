---
title: 'LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers'
title_zh: LoopSpec：面向循环Transformer的流水线自投机解码框架
authors:
- SangLyul Cho
- Langqing Cui
- Sehoon Kim
- Dongsu Han
- Insu Han
affiliations:
- Seoul National University
- KAIST
arxiv_id: '2609.17184'
url: https://arxiv.org/abs/2609.17184
pdf_url: https://arxiv.org/pdf/2609.17184
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM推理 · 自投机解码优化
tags:
- Looped Transformers
- Self-Speculative Decoding
- Inference Acceleration
- KV Cache
- SGLang
one_liner: 免训练的自投机解码框架，为Looped Transformers带来最高6.83倍无损推理加速
practical_value: '- 业务中若采用Looped Transformer做Agent工具调用、推荐文案生成、Query改写等在线推理场景，可直接复用该免训练框架，无需修改模型结构即可获得数倍推理提速，降低部署成本

  - 双候选残差投机+门控分支裁剪的设计可迁移到其他大模型推理场景，无需额外训练小草稿模型，避免草稿与目标模型分布不匹配的问题，适合资源受限的端侧/在线服务部署

  - 按分支复用KV缓存索引、预生成不同批大小CUDA Graph的工程trick，可直接复用到多分支投机解码的工程实现中，降低GPU kernel调度和缓存管理开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped Transformers通过循环复用共享Transformer块实现了小参数量下媲美大深度标准Transformer的性能，尤其适合端侧、低资源部署场景，但推理时每次循环都需要重复访存拉取相同权重，受内存带宽瓶颈限制，解码延迟远高于同参数量的标准Transformer；传统投机解码需要额外训练专用草稿模型，存在训练成本高、草稿与目标模型分布偏移、占用额外显存的问题。
### 方法关键点
- 完全免训练，无需修改模型结构，直接利用Looped Transformer不同循环深度的中间隐状态生成草稿token，无需额外草稿模型
- 流水线并行调度：前序token未完成全循环深度验证时，即可用浅层循环输出的草稿启动后续token的计算，不同分支的循环计算批量执行，最大化硬件利用率
- 双候选+门控优化：新增深层循环输出的残差第二候选作为fallback，仅当深浅层对第一候选的置信度不一致时才生成第二分支，避免分支数指数爆炸
- 理论推导得到最优双候选深度的闭式解，与实测最优配置高度匹配
### 关键结果
在Ouro（循环深度4）、Raven（循环深度32）两个Looped Transformer系列共7个checkpoint上测试，覆盖数学推理、通用推理、代码生成三类基准，相比标准自回归解码最高实现6.83×无损加速，比需要训练的DFlash投机解码方案最高快1.7×。
**最值得记住的一句话**：利用模型自身的中间计算结果做自投机解码，是实现免训练、无分布偏移的大模型推理加速的高性价比方向。
