---
title: Studying quantization trade-offs for efficient inference deployment in machine
  translation
title_zh: 面向机器翻译高效推理部署的量化策略权衡研究
authors:
- Jim Zhao
- Sohir Maskey
- Koen Oostermeijer
- Douglas Orr
- Teryn Jones
affiliations:
- University of Basel
- Aleph Alpha Research
- Graphcore
arxiv_id: '2607.29397'
url: https://arxiv.org/abs/2607.29397
pdf_url: https://arxiv.org/pdf/2607.29397
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: 大模型推理 · 量化与分块策略优化
tags:
- Quantization
- LLM Inference
- Machine Translation
- vLLM
- Post-training Quantization
one_liner: 在A100/H100上验证机器翻译模型量化+分块最优部署策略，指出段级评测的长上下文质量盲区
practical_value: '- 部署≥9B的LLM时，A100优先选W8A8量化、H100优先选W4A8量化，可在几乎无损前提下提升吞吐量，适合电商智能客服、商品文案生成等大流量场景

  - 处理长文本（如商品详情翻译、用户长会话理解）时，优先采用200-400 token的分块策略，可同时兼顾推理效率与内容质量，降低资源开销

  - 上线量化模型前不能仅做短样本评测，必须补充长上下文业务场景的效果验证，避免出现量化后长文本生成质量骤降、内容遗漏等问题

  - 对于<2B的小模型不建议做W8A8量化，会引入额外计算overhead反而降低推理效率，适合直接用BF16部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM部署普遍采用量化降低显存占用、提升推理效率，但现有研究多孤立评测量化的精度损失或token级性能，未结合真实服务场景下的长文档处理、并发负载等因素，也忽略了量化策略与分块策略的协同影响；传统段级机器翻译评测无法反映长上下文下的量化质量损失，难以指导实际部署。

### 方法关键点
- 选取EuroLLM（1.7B/9B/22B）、Hy-MT2（1.8B/7B）两类翻译模型，测试W4A16、W8A8、W4A8三种量化方案，在A100/H100上基于vLLM做近生产环境的推理性能评测
- 引入WMT24++文档级翻译评测集，构建不同阈值的文档分块策略，同时对比段级与文档级的量化质量差异
- 分别做离线基准测试（固定序列长度、batch size）与闭环在线测试（模拟1-500并发用户、1200token长文档），综合评估latency、吞吐量、翻译质量的trade-off

### 关键结果数字
- 9B及以上模型量化收益显著：A100上W8A8、H100上W4A8可在相同延迟下提升吞吐量，22B模型量化后可节省20-30GB显存，大幅提升高并发下的调度效率
- 200-400token分块为最优区间：与量化策略结合后，可在大部分部署场景下提升latency-throughput帕累托表现
- 段级评测严重低估长上下文量化损失：EuroLLM-9B的W8A8量化在段级评测中xCOMET仅下降5.3%，但在800token长块场景下chrF++评分骤降48.1%，出现内容遗漏、拒绝回答等故障
- <2B小模型量化无收益甚至负收益：W8A8在1.7B模型上引入的动态激活量化overhead会导致throughput低于BF16基线

**最值得记住的一句话**：量化策略不能孤立选型，必须结合硬件、模型大小、业务负载、分块策略联合优化，且必须经过真实长文本业务场景的效果验证
