---
title: 'ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding'
title_zh: ChainFlow：面向投机解码的少步隐空间流匹配方法
authors:
- Selim Aktas
- Yusuf Erdem Erdem
- Ahmed Zeer
- Himmet Toprak Kesgin
- Muzaffer Kaan Yuce
- Mehmet Fatih Amasyali
affiliations:
- Koç University
- Yıldız Technical University
arxiv_id: '2611.08669'
url: https://arxiv.org/abs/2611.08669
pdf_url: https://arxiv.org/pdf/2611.08669
published: '2026-11-05'
collected: '2026-11-09'
category: LLM
direction: LLM推理优化 · 投机解码加速
tags:
- Speculative Decoding
- Flow Matching
- LLM Inference
- Latent Space
- VAE
one_liner: 首个基于目标LLM隐状态的流匹配投机解码器，同参数下比EAGLE-3快39%、比DFlash快11%
practical_value: '- 低并发高实时性LLM场景（如电商推荐理由生成、搜索query改写、Agent工具调用）可直接复用8×4紧凑型树模式，单batch下推理速度最高提2倍，大幅降低
  latency

  - 跨境多语业务（如多语客服、商品翻译）可复用小比例旧域数据重放的迁移方案，不用全量重训就能适配新语言，同时保留旧语言90%以上加速效果

  - 高并发LLM服务可新增并发阈值开关：并发数≤4时启用ChainFlow，高于阈值自动切回普通自回归解码，平衡 throughput 和 latency'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有投机解码两类范式均存在短板：自回归Drafter逐token生成，drafting成本随草稿长度线性增长，占推理总耗时20%-40%；并行扩散类Drafter一次出多token，但忽略token间依赖，接受率低，跨语言/跨域适配性差。LLM推理成本是电商、Agent场景落地的核心瓶颈，尤其是长生成、多语言、低并发高实时性请求场景，亟需更高性价比的加速方案。
### 方法关键点
- 对目标LLM的输出隐状态做VAE压缩，流匹配网络仅在低维隐空间做短距离传输，1-2步欧拉步即可生成8个位置的隐状态，drafting成本几乎不随目标模型尺寸增长
- 新增轻量Markov头+路径头，在流匹配输出后补全token间依赖，无需二次运行流网络
- 支持链/树两种输出模式，紧凑型8×4树一次生成32个候选，一次并行验证即可覆盖多条生成路径，提升接受长度
- 多语言适配时混合20%旧域数据重放，避免灾难性遗忘，无需全量重训即可适配新语言
### 关键结果
基于Qwen3.5 4B/9B/27B系列模型测试，对比同参数EAGLE-3、DFlash baseline：单batch下8×4树模式平均比EAGLE-3快39%、比DFlash快11%；27B参数下平均加速2.12倍，数学推理域最高达3.23倍；适配土耳其语后加速比仍达1.81-2.25倍，远高于baseline跨域性能。
> 核心结论：投机解码的本质是基于目标模型已有的隐状态轨迹做短距离传输，而非从零生成草稿，流匹配对这类短路径预测的效率远高于自回归/扩散范式
